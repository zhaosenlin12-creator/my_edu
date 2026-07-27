---
type: timeline
status: active
domain: ai,codex,sessions
audience: self
updated_at: 2026-07-27
tags: codex,timeline,history
---

# Codex 会话时间线

> 从 `codex-session-digest.json` 提炼出来的会话脉络。按主题分组,方便回顾。

## 总览

- 会话总数:**92**
- 主题维度:**60** 项
- 仓库维度:**6** 个
- 工具维度:**60** 个

## 高频主题(用户首条消息词频)

- `the` · 116
- `image` · 103
- `png` · 91
- `users` · 74
- `administrator` · 74
- `temp` · 65
- `codex` · 63
- `for` · 61
- `user` · 57
- `appdata` · 54
- `local` · 54
- `name` · 51
- `files` · 50
- `request` · 49
- `git` · 49
- `mentioned` · 48
- `path` · 34
- `https` · 30
- `ppt` · 29
- `ran` · 27

## 高频仓库

- `zhaosenlin12-creator/Scrapling.git` · 3
- `zhaosenlin12-creator/senlin_website.git` · 2
- `zhaosenlin12-creator/world_website.git` · 2
- `zhaosenlin12-creator/gaokao_design.git` · 2
- `zhaosenlin12-creator/MotionSites-Prompts.git` · 2
- `zhaosenlin12-creator/img2threejs.git` · 2

## 高频工具 / 关键词(模型回复)

- `the` · 102
- `and` · 37
- `let` · 35
- `ppt` · 29
- `powershell` · 22
- `hero` · 21
- `godot` · 21
- `skill` · 19
- `exe` · 18
- `vite` · 17
- `png` · 15
- `npm` · 15
- `image` · 15
- `check` · 14
- `with` · 14
- `docs` · 14
- `https` · 14
- `kaifa` · 13
- `css` · 13
- `windows` · 13

## 关键会话样本


## 按主题归类

### 教学 / 教案 / Python / Ursina
- 关键词:`kaifa_boot` · 23
- 关键词:`kaifa` · 11

### Web / 项目代码
- 仓库:`zhaosenlin12-creator/Scrapling.git` · 3
- 仓库:`zhaosenlin12-creator/senlin_website.git` · 2
- 仓库:`zhaosenlin12-creator/world_website.git` · 2
- 仓库:`zhaosenlin12-creator/gaokao_design.git` · 2
- 仓库:`zhaosenlin12-creator/MotionSites-Prompts.git` · 2
- 关键词:`zhaosenlin12-creator` · 18

### AI 工具 / Vibe Coding
- 关键词:`codex` · 63
- 关键词:`skill` · 9

### Godot / 3D / 游戏
- 仓库:`zhaosenlin12-creator/img2threejs.git` · 2

### 抓取 / Scrapling / firecrawl
- 仓库:`zhaosenlin12-creator/Scrapling.git` · 3
- 关键词:`firecrawl` · 21
- 关键词:`firecrawl_src` · 16

### 知识库 / Obsidian
- 关键词:`kaifa_boot` · 23

## 看相关

- [[60_Assets/codex-session-digest.json]] · 原始数据
- [[60_Assets/codex-session-summary.md]] · 会话摘要
- [[50_AI/codex]] · Codex 工具卡

## 怎么更新

```bash
python 60_Assets/build_knowledge_index.py  # 重新生成 digest
python 90_Scripts/generate_timeline.py   # 生成这份时间线
```