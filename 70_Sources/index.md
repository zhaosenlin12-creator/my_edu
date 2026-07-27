---
type: moc
status: active
domain: sources,ai
audience: self,apprentice
updated_at: 2026-07-27
tags: sources,learning
---

# 外部学习资料

> 外部资料保留来源与抓取日期；原文是参考，不等于自己的知识。自己的理解要写回课程、项目或方法卡。

## VibeHub AI 编程术语库
- 在线来源：<https://vibe-hub.org/>
- 本地说明：[[70_Sources/vibe-hub/README]]
- CSV 检索表：`70_Sources/vibe-hub/index.csv`
- 离线页面：`70_Sources/vibe-hub/pages/zh/` 与 `pages/en/`
- 学习路径：[[50_AI/AI编程学习路线]]

## 如何搜索
- Obsidian：`Ctrl+Shift+F` 搜术语或大白话描述
- 表格：用 Excel 打开 `index.csv`，按语言、类别、标题过滤
- Codex：要求在 `70_Sources/vibe-hub/pages/zh` 中检索并引用源文件
- 命令行：`rg -n "关键词" 70_Sources/vibe-hub/pages/zh`

## 版权与更新
- 484 页离线镜像仅用于个人学习和课堂备课，不在公开 GitHub 仓库发布
- GitHub 同步索引、来源说明和自己的学习路线
- 更新时重新运行 `website-knowledge-crawler` Skill，并比较 sitemap 数量
