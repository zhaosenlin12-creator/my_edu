---
type: adr
status: accepted
date: 2026-07-28
tags: [decision, vibe-hub, mirror]
---

# ADR · vibe-hub 镜像策略：pages 进 git，site 本地

## 上下文

把 vibe-hub.org 全站本地化有两种思路：

1. **纯静态 HTML 镜像**（HTML + CSS + JS + 资源）：完整、像原站，但要下载 40+ MB
2. **纯 Markdown 抓取**（清洗后的文本）：小、可 grep、可被 AI 检索，但失去视觉

库主明确要求「像原站打开一样」，所以两个都要。

问题是：哪个进 git？

## 决定

- **`pages/`（Markdown）**：进 git。每个 md 带 frontmatter（`type / source_url / title / language / category / engine / fetched_at`），484 个文件约 3 MB，可被 AI / Obsidian 检索。
- **`site/`（HTML 镜像）**：本地按需生成。不进 git（太大），双击 `start-server.bat` 跑 `python -m http.server` 预览。
- **共享元数据**：`index.csv`（484 条记录）、`failures.csv`、`README.md` 都进 git。

## 影响

### 好的

- git 体积可控（pages + index.csv 共约 3 MB）
- 库主在 Obsidian 里能直接读 md，但要看视觉就启本地 server
- `site/` 出问题可以随时重抓（mirror_site.py 是确定性的）
- 仓库可移植：clone 后没有 `site/` 也不影响内容检索

### 成本

- 库主需要知道有「两个入口」（Obsidian 读 md / 本地浏览器看 HTML）
- 每次 vibe-hub 更新需要重抓（双轨：crawl_site.py + mirror_site.py）

### 后续动作

- [ ] 写一个 `refresh-vibe-hub.bat` 一键跑双轨抓取
- [ ] 给 `site/` 出一个 devcontainer 配置方便其他机器跑
- [ ] 镜像脚本加 `--site-icon` 选项让品牌色更准

## 引用

- [[../70_Sources/vibe-hub/README]]
- [[../AGENTS]]（操作手册里写了启动方式）