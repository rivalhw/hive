# Hive Posts Downloader

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

一个简单易用的 Python 工具，用于从 [Hive](https://hive.io/) 区块链平台下载指定账户的博客文章。

## ✨ 功能特性

- 📥 **批量下载** - 自动下载指定 Hive 账户的所有原创文章（排除转发内容）
- 📅 **日期过滤** - 支持按日期范围筛选帖子
- 📁 **智能组织** - 自动按 `账户/年/月/日` 的层级结构保存
- 📝 **Markdown 格式** - 将帖子内容保存为 Markdown 文件，便于阅读和备份
- ⚡ **多线程加速** - 支持并发下载，提高抓取效率
- 🔄 **自动重试** - 网络错误时自动重试，确保数据完整性

## 🚀 安装

### 环境要求

- Python 3.8 或更高版本

### 安装依赖

```bash
# 克隆仓库
git clone https://github.com/rivalhw/hive.git
cd hive-posts-downloader

# 安装依赖
pip install requests
```

## 📖 使用方法

### 基本用法

```bash
python download_hive_posts.py --account steemit
```

### 完整参数说明

```bash
python download_hive_posts.py \
  --account steemit \
  --api https://api.hive.blog \
  --output ./posts \
  --start-date 2023-01-01 \
  --end-date 2023-12-31 \
  --workers 8 \
  --delay 0.2
```

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--account` | **(必填)** Hive 账户名 | - |
| `--api` | Hive API 节点 URL | `https://api.hive.blog` |
| `--output` | 输出目录路径 | `./posts` |
| `--start-date` | 起始日期 (格式: YYYY-MM-DD) | - |
| `--end-date` | 结束日期 (格式: YYYY-MM-DD) | - |
| `--workers` | 并发下载线程数 | `8` |
| `--delay` | API 请求间隔（秒） | `0.2` |

### 使用示例

#### 下载特定用户的所有文章

```bash
python download_hive_posts.py --account alice
```

#### 下载特定日期范围内的文章

```bash
python download_hive_posts.py --account bob --start-date 2023-01-01 --end-date 2023-06-30
```

#### 使用自定义 API 节点和输出目录

```bash
python download_hive_posts.py --account charlie --api https://api.openhive.network --output ~/hive_backup
```

#### 降低并发数以避免 API 限制

```bash
python download_hive_posts.py --account dave --workers 4 --delay 0.5
```

## 📂 输出结构

下载的文章将按以下目录结构保存：

```
output/
└── {account}/
    └── {YYYY}/
        └── {MM}/
            └── {DD}/
                └── {Post Title}.md
```

### 示例

```
posts/
└── steemit/
    └── 2023/
        └── 12/
            └── 25/
                └── Merry Christmas.md
                └── Holiday Updates.md
```

### 文件格式

每个 Markdown 文件包含以下元数据：

```markdown
# 文章标题

**Author:** @username  
**Permlink:** post-permlink  
**Created:** 2023-12-25T10:30:00  
**Category:** blog  
**Tags:** {"tags": ["hive", "blogging"]}

---

文章内容正文...
```

## 🌐 可用的 Hive API 节点

- `https://api.hive.blog` (默认)
- `https://api.openhive.network`
- `https://rpc.ausbit.dev`
- `https://hived.emre.sh`

## ⚙️ 工作原理

1. **获取文章列表** - 使用 `condenser_api.get_blog_entries` 获取账户的所有博客条目
2. **过滤转发** - 自动识别并排除转发（reblog）内容，只保留原创文章
3. **并行下载** - 使用多线程并发获取每篇文章的完整内容
4. **日期筛选** - 根据用户指定的日期范围过滤文章
5. **保存文件** - 将文章内容保存为 Markdown 格式，并按日期层级组织

## 🛠️ 开发计划

- [ ] 支持导出为 JSON 格式
- [ ] 支持下载评论/回复
- [ ] 支持图片批量下载
- [ ] 添加进度条显示
- [ ] 支持增量更新（仅下载新文章）

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request

## 📝 许可证

本项目采用 [MIT](LICENSE) 许可证开源。

## 🙏 致谢

- [Hive](https://hive.io/) - 去中心化的社交媒体区块链平台
- [Hive API 文档](https://developers.hive.io/) - 开发者文档

---

> 💡 **提示**: 如果下载大量文章，建议适当增加 `--delay` 参数，以免对 API 节点造成过大压力。
