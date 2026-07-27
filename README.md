---
type: readme
status: active
updated_at: 2026-07-27
tags: readme,entry
---

# 我的个人知识库 · 森林

> 这不是又一个“个人 PKM 模板”，是基于真实项目 / 抖音 / 直播 / 教学 / Codex 会话沉淀出来的可用系统。每张卡片都能跳到 [[60_Assets/dossiers]] 的真实档案。

## 怎么开始
1. 看 [[10_Profile/我是谁]] / [[10_Profile/我在哪]] / [[10_Profile/我要去哪]] / [[10_Profile/能力地图]] → 哲学三问 + 能力地图
2. 从 [[00_Home/MOCs/projects]] / [[00_Home/MOCs/teaching]] / [[00_Home/MOCs/content]] / [[00_Home/MOCs/ai_tools]] 四个入口挑一个
3. 想看“这件事到底有什么证据”→ 直接到 [[60_Assets/dossiers/]]
4. 想看我和 AI 的对话数据 → [[60_Assets/codex-session-digest.json]]

## 我是谁（在做什么）
- 森林（赵森林），湖北宜昌猇亭，乐启教育（乐启享）合伙人 / 副校长
- 项目：Web（Vite / Next.js / Express）/ 3D（Three / R3F / Phaser / Pyodide / Ursina）/ 业务系统 / 教学资产
- 内容：抖音“愈见森林”+ 直播六轮 SOP + 教学体系 18 单元
- AI：Codex + DeepSeek + 自托管脚本，92 个会话已落档

## 7 个核心 dossier（必看）
| dossier | 范围 | 文件大小 |
|---|---|---|
| [[60_Assets/dossiers/open_leqixiang]] | 乐其翔展览系统（Vite + React 19 + TS 5.9） | 5 KB |
| [[60_Assets/dossiers/python-adventure]] | Python 冒险岛（Next 16 + Phaser + Pyodide + FastAPI） | 6 KB |
| [[60_Assets/dossiers/senlin_website]] | 智创未来编程学院（Express + MySQL + AI 代理） | 5 KB |
| [[60_Assets/dossiers/world_website]] | 宇宙探索互动站（Next 14 + R3F 8 + three 0.169） | 4 KB |
| [[60_Assets/dossiers/douyin]] | 愈见森林（151 粉 → 1000 粉计划） | 7 KB |
| [[60_Assets/dossiers/live-streaming]] | 直播 6 轮 SOP（数据驱动版） | 7 KB |
| [[60_Assets/dossiers/teaching]] | 教学体系（18 分类 + 7 天创客营） | 7 KB |

## 数据资产
- 92 个 Codex 会话：[[60_Assets/codex-session-digest.json]] + [[60_Assets/codex-session-summary.md]]
- 32 个 GitHub 仓库：[[60_Assets/GitHub仓库总账]] + [[60_Assets/github-repositories.csv]]
- 本地 36 个目录 + 21 个 git 仓库：[[60_Assets/local-kaifa-directories.csv]] + [[60_Assets/local-git-repositories.csv]]
- 894 个教学目录：[[60_Assets/teaching-packages.csv]]（本机检索，不入 GitHub）
- 484 页 VibeHub 离线（[[70_Sources/vibe-hub/]]）：本地可读，不入 GitHub

## 仓库
- 本地 vault：`C:\my_know`
- 远程：`https://github.com/zhaosenlin12-creator/my_edu.git`
- HEAD：`37c22be`
- Obsidian 打开：`C:\kaifa_boot\Obsidian\Obsidian.exe -ArgumentList 'C:\my_know'`

## 工作流（每加一条都走一遍）
1. 先建 [[60_Assets/dossiers/<name>]] · 事实 / 推断 / 待确认 / 下一步
2. 再写 [[20_Projects/<name>]] / [[30_Teaching/<name>]] / [[40_Content/<name>]] · 引用 dossier
3. 必要时更新 [[10_Profile/能力地图]]（每条都能跳到 dossier）
4. 季度跑一次 `review-dossiers.py`（待建）

## 隐私 / 同步
- `.obsidian/workspace, cache, themes, plugins` 本地
- `70_Sources/vibe-hub/pages/` 大文件不入 GitHub
- `60_Assets/local-*.csv` 与 `teaching-packages.csv` 只本机检索
- `__pycache__/` 与 `.mp4 .mov .psd .zip .rar .7z` 不入

## 4 个徒弟
- 我（森林）把本知识库作为参考，让他们搭自己的，不要替他们制定目标