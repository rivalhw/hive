#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Download posts from a specified Hive account via JSON-RPC API.

Supports:
    - All posts including community posts (uses get_discussions_by_author_before_date)
    - Incremental mode: skips posts already downloaded in previous runs
    - Filtering by date range
    - Saving as Markdown organized by account/year/month/day
    - Rate limiting to avoid 429 errors

Usage example:
    python download_hive_posts.py --account steemit
    python download_hive_posts.py --account alice --start-date 2023-01-01 --end-date 2023-12-31
    python download_hive_posts.py --account alice --no-resume   # re-download everything
"""

import argparse
import json
import os
import re
import sys
import threading
import time
from datetime import datetime, timezone
from typing import Optional, Set

import requests
from requests.adapters import HTTPAdapter, Retry

DEFAULT_API = "https://api.hive.blog"
REQUEST_TIMEOUT = 30
CACHE_FILENAME = ".downloaded_permlinks"
PAGE_SIZE = 20  # max for get_discussions_by_author_before_date

_thread_local = threading.local()


# ---------------------------------------------------------------------------
# Rate limiter — token bucket, shared across all threads
# ---------------------------------------------------------------------------

class _RateLimiter:
    def __init__(self, rate: float):
        self._rate = rate
        self._tokens = rate
        self._lock = threading.Lock()
        self._last = time.monotonic()

    def acquire(self):
        while True:
            with self._lock:
                now = time.monotonic()
                self._tokens = min(
                    self._rate,
                    self._tokens + (now - self._last) * self._rate,
                )
                self._last = now
                if self._tokens >= 1.0:
                    self._tokens -= 1.0
                    return
            time.sleep(0.05)


_rate_limiter: Optional[_RateLimiter] = None


# ---------------------------------------------------------------------------
# HTTP session (per-thread, connection pooling + retry)
# ---------------------------------------------------------------------------

def _make_session() -> requests.Session:
    session = requests.Session()
    retry = Retry(
        total=4,
        backoff_factor=1.0,
        status_forcelist=[500, 502, 503, 504],
        allowed_methods=["POST"],
    )
    adapter = HTTPAdapter(pool_connections=4, pool_maxsize=16, max_retries=retry)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session


def _get_session() -> requests.Session:
    if not hasattr(_thread_local, "session"):
        _thread_local.session = _make_session()
    return _thread_local.session


# ---------------------------------------------------------------------------
# JSON-RPC
# ---------------------------------------------------------------------------

def rpc_call(api_url: str, method: str, params=None):
    payload = {"jsonrpc": "2.0", "method": method, "params": params or [], "id": 1}
    backoff = 2.0
    for attempt in range(5):
        if _rate_limiter is not None:
            _rate_limiter.acquire()
        try:
            resp = _get_session().post(
                api_url,
                json=payload,
                headers={"Content-Type": "application/json"},
                timeout=REQUEST_TIMEOUT,
            )
        except requests.RequestException as exc:
            if attempt == 4:
                raise RuntimeError(f"Network error calling {method}: {exc}") from exc
            time.sleep(backoff)
            backoff *= 2
            continue

        if resp.status_code == 429:
            wait = float(resp.headers.get("Retry-After", backoff))
            time.sleep(wait)
            backoff = min(backoff * 2, 30.0)
            continue

        try:
            resp.raise_for_status()
            data = resp.json()
        except requests.RequestException as exc:
            if attempt == 4:
                raise RuntimeError(f"Network error calling {method}: {exc}") from exc
            time.sleep(backoff)
            backoff *= 2
            continue

        if "error" in data:
            raise RuntimeError(f"API error in {method}: {data['error']}")

        return data.get("result")

    raise RuntimeError(f"Exhausted retries for {method}")


def get_discussions_by_author_before_date(
    api_url: str, account: str, start_permlink: str, before_date: str, limit: int
):
    return rpc_call(
        api_url,
        "condenser_api.get_discussions_by_author_before_date",
        [account, start_permlink, before_date, limit],
    )


# ---------------------------------------------------------------------------
# Incremental download cache
# ---------------------------------------------------------------------------

class DownloadCache:
    def __init__(self, cache_path: str):
        self._path = cache_path
        self._lock = threading.Lock()
        self._permlinks: Set[str] = set()
        self._load()

    def _load(self):
        if os.path.exists(self._path):
            with open(self._path, "r", encoding="utf-8") as f:
                for line in f:
                    pl = line.strip()
                    if pl:
                        self._permlinks.add(pl)

    def __contains__(self, permlink: str) -> bool:
        return permlink in self._permlinks

    def __len__(self) -> int:
        return len(self._permlinks)

    def add(self, permlink: str):
        with self._lock:
            if permlink not in self._permlinks:
                self._permlinks.add(permlink)
                with open(self._path, "a", encoding="utf-8") as f:
                    f.write(permlink + "\n")

    @classmethod
    def empty(cls, cache_path: str) -> "DownloadCache":
        obj = object.__new__(cls)
        obj._path = cache_path
        obj._lock = threading.Lock()
        obj._permlinks = set()
        return obj


# ---------------------------------------------------------------------------
# File helpers
# ---------------------------------------------------------------------------

def sanitize_filename(name: str) -> str:
    return re.sub(r'[\\/:*?"<>|]', "_", name)


def save_post(post: dict, base_output_dir: str, account: str) -> str:
    created_str = post.get("created", "")
    try:
        created_dt = datetime.fromisoformat(created_str.replace("Z", "+00:00"))
    except ValueError:
        created_dt = datetime.now(timezone.utc)

    output_dir = os.path.join(
        base_output_dir,
        account,
        f"{created_dt.year:04d}",
        f"{created_dt.month:02d}",
        f"{created_dt.day:02d}",
    )
    os.makedirs(output_dir, exist_ok=True)

    title = post.get("title", "").strip() or "untitled"
    base_name = sanitize_filename(title)
    path = os.path.join(output_dir, f"{base_name}.md")

    counter = 1
    stem = path[:-3]
    while os.path.exists(path):
        path = f"{stem}_{counter}.md"
        counter += 1

    meta_raw = post.get("json_metadata", {})
    if isinstance(meta_raw, str):
        try:
            meta_raw = json.loads(meta_raw)
        except (json.JSONDecodeError, ValueError):
            pass
    meta = json.dumps(meta_raw, ensure_ascii=False, indent=2)

    content = (
        f"# {post.get('title', '')}\n\n"
        f"**Author:** @{post['author']}  \n"
        f"**Permlink:** {post['permlink']}  \n"
        f"**Created:** {post['created']}  \n"
        f"**Category:** {post.get('category', '')}  \n"
        f"**Tags:** {meta}\n\n"
        f"---\n\n"
        f"{post.get('body', '')}\n"
    )
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    return path


# ---------------------------------------------------------------------------
# Core: paginate and save all posts
# ---------------------------------------------------------------------------

def fetch_and_save_all(
    api_url: str,
    account: str,
    base_output_dir: str,
    start_dt: Optional[datetime],
    end_dt: Optional[datetime],
    cache: DownloadCache,
    no_resume: bool,
    debug: bool,
):
    """
    Paginate through all posts using get_discussions_by_author_before_date.
    This API returns full post content (no separate get_content needed) and
    includes community posts, unlike get_blog_entries.
    """
    before_date = "2099-12-31T23:59:59"
    start_permlink = ""
    is_first_page = True

    downloaded = skipped_cache = skipped_date = errors = 0
    page_num = 0

    while True:
        try:
            posts = get_discussions_by_author_before_date(
                api_url, account, start_permlink, before_date, PAGE_SIZE
            )
        except RuntimeError as exc:
            print(f"ERROR fetching page: {exc}", file=sys.stderr)
            break

        if not posts:
            break

        # The first item on page 2+ is the last item from the previous page — skip it.
        batch = posts if is_first_page else posts[1:]
        is_first_page = False
        page_num += 1

        if not batch:
            break

        if debug:
            p = batch[0]
            print(f"  [debug] page {page_num} first: {p.get('created')} /{p.get('permlink')}")

        for post in batch:
            permlink = post.get("permlink", "")

            if not no_resume and permlink in cache:
                skipped_cache += 1
                continue

            created_str = post.get("created", "")
            try:
                created_dt = datetime.fromisoformat(created_str.replace("Z", "+00:00"))
            except ValueError:
                created_dt = None

            if created_dt:
                if start_dt and created_dt < start_dt:
                    skipped_date += 1
                    continue
                if end_dt and created_dt > end_dt:
                    skipped_date += 1
                    continue

            try:
                path = save_post(post, base_output_dir, account)
                cache.add(permlink)
                downloaded += 1
                print(f"[{downloaded}] {path}")
            except OSError as exc:
                errors += 1
                print(f"ERROR saving {account}/{permlink}: {exc}", file=sys.stderr)

        date_range = f"{posts[-1].get('created', '?')} → {posts[0].get('created', '?')}"
        print(f"  page {page_num}: {len(posts)} posts ({date_range})")

        if len(posts) < PAGE_SIZE:
            break

        last = posts[-1]
        start_permlink = last["permlink"]
        before_date = last["created"]

    return downloaded, skipped_cache, skipped_date, errors


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args():
    parser = argparse.ArgumentParser(
        description="Download Hive account posts via JSON-RPC API"
    )
    parser.add_argument(
        "--api",
        default=DEFAULT_API,
        help=f"Hive API node URL (default: {DEFAULT_API})",
    )
    parser.add_argument(
        "--account",
        required=True,
        help="Hive account name whose posts will be downloaded",
    )
    parser.add_argument(
        "--start-date",
        help="Only download posts created on or after this date (YYYY-MM-DD)",
    )
    parser.add_argument(
        "--end-date",
        help="Only download posts created on or before this date (YYYY-MM-DD)",
    )
    parser.add_argument(
        "--output",
        default="./posts",
        help="Output directory for downloaded posts (default: ./posts)",
    )
    parser.add_argument(
        "--rps",
        type=float,
        default=3.0,
        help="Max API requests per second (default: 3)",
    )
    parser.add_argument(
        "--no-resume",
        action="store_true",
        help="Ignore the download cache and re-download all posts",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Print extra info for troubleshooting",
    )
    return parser.parse_args()


def main():
    global _rate_limiter

    args = parse_args()
    _rate_limiter = _RateLimiter(args.rps)

    api_url = args.api.rstrip("/")
    account = args.account.strip().lstrip("@").lower()
    output_dir = os.path.abspath(args.output)

    start_dt: Optional[datetime] = None
    end_dt: Optional[datetime] = None
    if args.start_date:
        start_dt = datetime.strptime(args.start_date, "%Y-%m-%d").replace(
            tzinfo=timezone.utc
        )
    if args.end_date:
        end_dt = datetime.strptime(args.end_date, "%Y-%m-%d").replace(
            hour=23, minute=59, second=59, tzinfo=timezone.utc
        )

    account_dir = os.path.join(output_dir, account)
    os.makedirs(account_dir, exist_ok=True)
    cache_path = os.path.join(account_dir, CACHE_FILENAME)

    cache = DownloadCache.empty(cache_path) if args.no_resume else DownloadCache(cache_path)

    print(f"API node    : {api_url}")
    print(f"Account     : {account}")
    print(f"Rate limit  : {args.rps} req/s")
    if start_dt:
        print(f"Start date  : {start_dt.date()}")
    if end_dt:
        print(f"End date    : {end_dt.date()}")
    print(f"Output dir  : {output_dir}")
    if args.no_resume:
        print("Resume mode : off (--no-resume)")
    else:
        print(f"Cached posts: {len(cache)} already downloaded")
    print("-" * 40)

    downloaded, skipped_cache, skipped_date, errors = fetch_and_save_all(
        api_url, account, output_dir, start_dt, end_dt, cache, args.no_resume, args.debug
    )

    print("-" * 40)
    print(f"Downloaded      : {downloaded}")
    if skipped_cache:
        print(f"Already had     : {skipped_cache}")
    if skipped_date:
        print(f"Skipped by date : {skipped_date}")
    if errors:
        print(f"Errors          : {errors}")


if __name__ == "__main__":
    main()
