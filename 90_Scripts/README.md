# 90_Scripts 工具脚本

这些脚本是 Obsidian Vault 的“执行层”，能直接在 PowerShell 中运行，把零散的笔记变成可重复的工作流。每个脚本都是单文件、无外部网络依赖的 Python 3.10+ 命令。

## 抖音选题草稿
读取 `20_Projects` / `30_Teaching` / `40_Content` 的卡片，加上 VibeHub 本地术语，生成今天的抖音草稿卡。

```powershell
python C:\my_know\90_Scripts\douyin_topic_picker.py --out C:\my_know\40_Content\draft-2026-07-28.md
```

## 直播复盘
把一场直播的关键数据写入 `40_Content/live/<日期>.md` 并追加到 `60_Assets/live-summary.csv`。

```powershell
python C:\my_know\90_Scripts\live_recap.py --date 2026-07-28 --title "Vibe Coding 30 分钟能做啥" --peaks 120 --new-followers 18 --conversions 3 --qa "作业点评, 1v1 试听" --failure "卡顿 5 分钟" --improvement "开播前测速"
```

## 知识卡索引
扫一遍 Vault 里的所有 Markdown，生成 `60_Assets/knowledge-index.csv`，便于在 Excel 里按 type / domain / status 过滤。

```powershell
python C:\my_know\90_Scripts\build_knowledge_index.py
```

## 代码审查
在指定仓库的 `git diff --cached` 上跑一遍密钥、敏感路径和隐私字段扫描，输出报告到 `40_Content/code-review-<仓库>.md`。

```powershell
python C:\my_know\90_Scripts\code_review.py --repo C:\kaifa\game-google
```

## 课程计划
根据课程名、年级、节数、目标和交付物生成一节可用的课程计划 Markdown。

```powershell
python C:\my_know\90_Scripts\course_planner.py --name "Vibe Coding 入门 6 课时" --grade "四年级" --lessons 6 --goals "理解 prompt" "跑通一个网页" --deliverables "可发布网页"
```

## 与 Codex 的边界
- Codex 负责解释需求、生成文档、修改代码
- 脚本负责数据落盘、检索、复盘、文件归档
- 结果出错时，先看脚本输出，再回到 Codex 排查逻辑
