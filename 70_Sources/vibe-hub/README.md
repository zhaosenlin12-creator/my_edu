# VibeHub 本地学习捕获

- 来源：https://vibe-hub.org/
- Sitemap：https://vibe-hub.org/sitemap.xml
- 抓取日期：2026-07-27
- 成功抓取：484 项（中文 242 + 英文 242）
- 失败：0

## 在 Obsidian 里检索

- 在 `70_Sources/vibe-hub/pages` 里按目录走读；中文在 `zh/`，英文在 `en/`
- 用 Excel 打开 `index.csv`，按语言、分类、标题筛选
- 想找主题归类时打开 `zh/topics/` 或 `en/topics/`（AI、Backend、Design、Git、Product、Technology 六个分类索引页）

## 学习路线

按 [[50_AI/AI编程学习路线]] 的顺序走，不建议从头读到尾。先做分类页的通读，再按需钻单点术语。

## 抓取与同步

- 抓取脚本：`C:\Users\Administrator\.codex\skills\website-knowledge-crawler\scripts\crawl_site.py`
- 默认引擎：Scrapling（本地、无需 API key）
- 备选引擎：Firecrawl（需要 `FIRECRAWL_API_KEY` 环境变量）
- 全量更新：`python crawl_site.py https://vibe-hub.org C:\my_know\70_Sources\vibe-hub --workers 4 --delay 0.15`
- `pages/` 已纳入 git，可在云端仓库看到完整捕获内容