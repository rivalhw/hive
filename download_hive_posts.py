#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Download posts from a specified Hive account via JSON-RPC API.

Supports:
    - Downloading all original posts (excluding reblogs)
    - Filtering by date range
    - Saving as Markdown organized by account/year/month/day
    - Multi-threaded content fetching

Usage example:
    python download_hive_posts.py --account steemit --api https://api.hive.blog --output ./posts
    python download_hive_posts.py --account alice --api https://api.hive.blog --start-date 2023-01-01 --end-date 2023-12-31
"""

import argparse
import json
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone

import requests

DEFAULT_API = "https://api.hive.blog"
LIMIT = 500  # max allowed by condenser_api.get_blog_entries
REQUEST_TIMEOUT = 30


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
        "--workers",
        type=int,
        default=8,
        help="Number of threads for parallel downloading (default: 8)",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.2,
        help="Seconds to sleep between API calls for pagination (default: 0.2)",
    )
    return parser.parse_args()


def rpc_call(api_url: str, method: str, params=None):
    """Make a JSON-RPC call to the Hive API."""
    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params or [],
        "id": 1,
    }
    try:
        resp = requests.post(
            api_url,
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=REQUEST_TIMEOUT,
        )
        resp.raise_for_status()
        data = resp.json()
    except requests.RequestException as exc:
        raise RuntimeError(f"Network error calling {method}: {exc}") from exc

    if "error" in data:
        err = data["error"]
        raise RuntimeError(f"API error in {method}: {err}")

    return data.get("result")


def get_blog_entries(api_url: str, account: str, start_entry_id: int, limit: int = LIMIT):
    """Fetch a batch of blog entries for an account."""
    return rpc_call(
        api_url,
        "condenser_api.get_blog_entries",
        [account, start_entry_id, limit],
    )


def get_content(api_url: str, author: str, permlink: str):
    """Fetch full content of a single post/comment."""
    return rpc_call(api_url, "condenser_api.get_content", [author, permlink])


def sanitize_filename(name: str) -> str:
    """Remove characters unsafe for filenames."""
    return re.sub(r'[\\/:*?"<>|]', "_", name)


def save_post(post: dict, base_output_dir: str, account: str):
    """Persist a single post to disk under account/YYYY/MM/DD/."""
    created_str = post.get("created", "")
    try:
        created_dt = datetime.fromisoformat(created_str.replace("Z", "+00:00"))
    except ValueError:
        created_dt = datetime.now(timezone.utc)

    year = f"{created_dt.year:04d}"
    month = f"{created_dt.month:02d}"
    day = f"{created_dt.day:02d}"

    output_dir = os.path.join(base_output_dir, account, year, month, day)
    os.makedirs(output_dir, exist_ok=True)

    title = post.get("title", "").strip()
    if not title:
        title = "untitled"
    base_name = sanitize_filename(title)
    path = os.path.join(output_dir, f"{base_name}.md")

    # Handle duplicate titles in the same folder
    counter = 1
    base_path = path[:-3]
    while os.path.exists(path):
        path = f"{base_path}_{counter}.md"
        counter += 1

    meta = json.dumps(post.get("json_metadata", {}), ensure_ascii=False, indent=2)
    md = f"""# {post['title']}

**Author:** @{post['author']}  
**Permlink:** {post['permlink']}  
**Created:** {post['created']}  
**Category:** {post.get('category', '')}  
**Tags:** {meta}

---

{post['body']}
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(md)

    return path


def fetch_all_entries(api_url: str, account: str, delay: float):
    """Paginate through all blog entries and return a list of original post identifiers."""
    entries = []
    start_entry_id = 0
    errors = 0

    while True:
        try:
            batch = get_blog_entries(api_url, account, start_entry_id, LIMIT)
            errors = 0
        except RuntimeError as exc:
            print(f"ERROR fetching blog entries: {exc}", file=sys.stderr)
            errors += 1
            if errors > 5:
                print("Too many errors, aborting pagination.", file=sys.stderr)
                break
            time.sleep(delay * 3)
            continue

        if not batch:
            break

        for entry in batch:
            author = entry["author"]
            reblogged = entry.get("reblogged_on", "1970-01-01T00:00:00") != "1970-01-01T00:00:00"
            if reblogged or author != account:
                continue
            entries.append((author, entry["permlink"]))

        min_entry_id = min(entry["entry_id"] for entry in batch)
        start_entry_id = min_entry_id - 1
        if start_entry_id < 0:
            break
        time.sleep(delay)

    return entries


def download_worker(api_url, base_output_dir, account, author, permlink, start_dt, end_dt):
    """Worker function to fetch a single post and save it if it passes filters."""
    try:
        post = get_content(api_url, author, permlink)
    except RuntimeError as exc:
        return "error", f"ERROR fetching {author}/{permlink}: {exc}"

    if not post or not post.get("permlink"):
        return "error", f"WARNING empty content for {author}/{permlink}"

    created_str = post.get("created", "")
    try:
        created_dt = datetime.fromisoformat(created_str.replace("Z", "+00:00"))
    except ValueError:
        created_dt = None

    if created_dt:
        if start_dt and created_dt < start_dt:
            return "skip_date", None
        if end_dt and created_dt > end_dt:
            return "skip_date", None

    try:
        path = save_post(post, base_output_dir, account)
        return "saved", path
    except OSError as exc:
        return "error", f"ERROR saving {author}/{permlink}: {exc}"


def main():
    args = parse_args()

    api_url = args.api.rstrip("/")
    account = args.account.strip().lstrip("@").lower()
    output_dir = os.path.abspath(args.output)
    os.makedirs(output_dir, exist_ok=True)

    start_dt = None
    end_dt = None
    if args.start_date:
        start_dt = datetime.strptime(args.start_date, "%Y-%m-%d").replace(
            tzinfo=timezone.utc
        )
    if args.end_date:
        end_dt = datetime.strptime(args.end_date, "%Y-%m-%d").replace(
            hour=23, minute=59, second=59, tzinfo=timezone.utc
        )

    print(f"API node    : {api_url}")
    print(f"Account     : {account}")
    print(f"Workers     : {args.workers}")
    if start_dt:
        print(f"Start date  : {start_dt.date()}")
    if end_dt:
        print(f"End date    : {end_dt.date()}")
    print(f"Output dir  : {output_dir}")
    print("-" * 40)

    # Phase 1: collect all original post identifiers
    print("Fetching blog entry list...")
    entries = fetch_all_entries(api_url, account, args.delay)
    print(f"Found {len(entries)} original posts to process.")

    if not entries:
        print("No original posts found.")
        return

    # Phase 2: multi-threaded download
    downloaded = 0
    skipped_date = 0
    errors = 0

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        future_to_entry = {
            executor.submit(
                download_worker,
                api_url,
                output_dir,
                account,
                author,
                permlink,
                start_dt,
                end_dt,
            ): (author, permlink)
            for author, permlink in entries
        }

        for future in as_completed(future_to_entry):
            status, info = future.result()
            if status == "saved":
                downloaded += 1
                print(f"[{downloaded}] Saved {info}")
            elif status == "skip_date":
                skipped_date += 1
            elif status == "error":
                errors += 1
                print(info, file=sys.stderr)

    print("-" * 40)
    print(f"Downloaded : {downloaded}")
    print(f"Skipped by date : {skipped_date}")
    if errors:
        print(f"Errors     : {errors}")


if __name__ == "__main__":
    main()
