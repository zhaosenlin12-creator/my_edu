# VibeHub 本地学习捕获

- 来源：https://vibe-hub.org/
- Sitemap：https://vibe-hub.org/sitemap.xml
- 抓取日期：2026-07-27
- 抓取引擎：Scrapling（默认；本地无需 API key）
- 抓取结果：484 项（中文 242 + 英文 242），失败 0

## 三种使用方式

### 1. 在 Obsidian 里检索（推荐日常）

- 在 `pages/` 里按目录走读；中文在 `zh/`，英文在 `en/`
- 用 Excel 打开 `index.csv`，按语言、分类、标题筛选
- 想找主题归类时打开 `zh/topics/` 或 `en/topics/`（AI、Backend、Design、Git、Product、Technology 六个分类索引页）

### 2. 在浏览器里像原站一样预览（推荐体验）

`site/` 是完整镜像（HTML + CSS + JS + 图片），启动本地服务器即可在浏览器看到与 vibe-hub.org 一致的页面、交互和样式：

```powershell
python -m http.server 8765 --directory C:\my_know\70_Sources\vibe-hub\site
```

然后浏览器打开 <http://localhost:8765/>。中文站走 `/`，英文站走 `/en/`。

> 第一次启动镜像耗时 3-5 分钟，484 页 + 532 资源。后续若要刷新：
> ```powershell
> python C:\Users\Administrator\.codex\skills\website-knowledge-crawler\scripts\mirror_site.py `
>     https://vibe-hub.org C:\my_know\70_Sources\vibe-hub\site --workers 6
> ```

### 3. 让 Codex 检索（推荐 AI 辅助）

每个 `pages/**/*.md` 都是清洁的 Markdown，前置 `type / source_url / title / language / category / engine / fetched_at`。在 Codex 里直接说「去 70_Sources/vibe-hub 找 XX」即可索引检索。

## 学习路线

按 [[50_AI/AI编程学习路线]] 的顺序走，不建议从头读到尾。先做分类页的通读，再按需钻单点术语。

## 抓取与同步

- 抓取 skill：`website-knowledge-crawler`（位于 `~/.codex/skills/website-knowledge-crawler/`）
- 默认引擎：Scrapling（本地、无需 API key）
- 备选引擎：Firecrawl（需要 `FIRECRAWL_API_KEY` 与 `FIRECRAWL_API_URL` 环境变量）
- 全量更新（Markdown）：

  ```powershell
  python C:\Users\Administrator\.codex\skills\website-knowledge-crawler\scripts\crawl_site.py `
      https://vibe-hub.org C:\my_know\70_Sources\vibe-hub `
      --workers 4 --delay 0.15 --engine scrapling
  ```

- 全量镜像（HTML）：

  ```powershell
  python C:\Users\Administrator\.codex\skills\website-knowledge-crawler\scripts\mirror_site.py `
      https://vibe-hub.org C:\my_know\70_Sources\vibe-hub\site --workers 6
  ```

- 难爬站点可用 auto 引擎自动回退到 Firecrawl。

- `pages/` 已纳入 git，可在 GitHub 仓库看到完整捕获内容。`site/` 因体积较大不进 git，本地按需生成。