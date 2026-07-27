# VibeHub 本地学习捕获

- 来源：https://vibe-hub.org/
- Sitemap：https://vibe-hub.org/sitemap.xml
- 抓取日期：2026-07-27
- 成功抓取：484 项（中文 242 + 英文 242）
- 失败：0
- 引擎：Scrapling（默认；本地无需 API key）

## 在 Obsidian 里检索

- 在 `70_Sources/vibe-hub/pages` 里按目录走读；中文在 `zh/`，英文在 `en/`
- 用 Excel 打开 `index.csv`，按语言、分类、标题筛选
- 想找主题归类时打开 `zh/topics/` 或 `en/topics/`（AI、Backend、Design、Git、Product、Technology 六个分类索引页）

## 学习路线

按 [[50_AI/AI编程学习路线]] 的顺序走，不建议从头读到尾。先做分类页的通读，再按需钻单点术语。

## 抓取与同步

- 抓取 skill：`website-knowledge-crawler`（位于 `~/.codex/skills/`）
- 默认引擎：Scrapling（本地、无需 API key）
- 备选引擎：Firecrawl（需要 `FIRECRAWL_API_KEY` 与 `FIRECRAWL_API_URL` 环境变量）
- 全量更新（本地重抓）：

  ```powershell
  python C:\Users\Administrator\.codex\skills\website-knowledge-crawler\scripts\crawl_site.py `
      https://vibe-hub.org C:\my_know\70_Sources\vibe-hub `
      --workers 4 --delay 0.15 --engine scrapling
  ```

- 难爬站点可用 auto 引擎自动回退：

  ```powershell
  python ... --engine auto
  ```

- `pages/` 已纳入 git，可在 GitHub 仓库看到完整捕获内容。