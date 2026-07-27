---
type: project
status: active
domain: knowledge,meta,workflow
audience: self
repo: zhaosenlin12-creator/my_edu
local_path: C:\my_know（git root）
remote: https://github.com/zhaosenlin12-creator/my_edu.git
updated_at: 2026-07-27
tags: obsidian,knowledge-base,dossier,meta,workflow
---

# my_edu · 个人知识库（本 vault 本身）

> 这是关于“知识库本身”的卡，不是某个外部项目。

## 一句话
**dossier 驱动的个人知识库**：用 Obsidian 做前端，本地 vault `C:\my_know`，git 推 `zhaosenlin12-creator/my_edu.git`，每张项目 / 内容 / 教学卡片都有真实档案背书。

## 状态
- 本地 vault：`C:\my_know`（head `37c22be`）
- 远程：`https://github.com/zhaosenlin12-creator/my_edu.git`
- 历史：从“模板填充版”升级到“dossier 驱动版”始于 2026-07-27

## 目录结构
```
C:\my_know\
├── 00_Home\                # 首页 / 模板 / MOC
├── 10_Profile\             # 我是谁 / 我在哪 / 我要去哪 / 能力地图
├── 20_Projects\            # 32 个项目卡
├── 30_Teaching\            # 教学体系卡
├── 40_Content\             # 抖音 / 直播 SOP
├── 50_AI\                  # 工具 + skill
├── 60_Assets\              # dossier / 数据 / Codex 会话
│   └── dossiers\           # 7 个核心档案（真实证据）
├── 70_Sources\             # VibeHub 离线（484 页）
├── 80_Canvas\              # 思维图 / 板书
├── 90_Archive\             # 已下架工具
└── 90_Scripts\             # Python 抓取 / 索引脚本
```

## dossier 体系（核心证据层）
- [[60_Assets/dossiers/open_leqixiang]] · 乐其翔展览系统
- [[60_Assets/dossiers/python-adventure]] · Python 冒险岛
- [[60_Assets/dossiers/senlin_website]] · 智创未来编程学院
- [[60_Assets/dossiers/world_website]] · 宇宙探索互动站
- [[60_Assets/dossiers/douyin]] · 愈见森林
- [[60_Assets/dossiers/live-streaming]] · 直播六轮 SOP
- [[60_Assets/dossiers/teaching]] · 教学体系

## 数据资产
- `60_Assets/codex-session-digest.json`（143 KB，92 个会话的主题 / 仓库 / 工具统计）
- `60_Assets/codex-session-summary.md`（105 KB，会话摘要）
- `60_Assets/github-repositories.csv`（7000 字节，32 个 GitHub 仓库）
- `60_Assets/local-kaifa-directories.csv`（2900 字节，本地目录）
- `60_Assets/teaching-packages.csv`（114 KB，894 个教学目录）
- `60_Assets/knowledge-index.csv`（16485 字节，全库索引）

## 工具脚本（C:\my_edu\90_Scripts\）
- `extract_codex_sessions.py`（6134 字节）· 提取 Codex 会话
- 还有 4 个 Python 脚本：douyin_topic_picker / live_recap / build_knowledge_index / code_review / course_planner

## 工作流
1. 新项目：先建 dossier（事实 / 推断 / 待确认），再写项目卡
2. 新课程：先写 dossier（适合对象 / 时长 / 资源 / 评估），再写课程卡
3. 新内容：先写 dossier（栏目 / SOP / 数据指标），再写内容卡
4. 新 AI 工具：先写 dossier（用途 / 风险 / 替代），再写工具卡

## 使用入口
- [[00_Home/快速使用指南]] · 第一次打开怎么用
- [[00_Home/MOCs/]] · 主题入口
- [[10_Profile/我是谁]] · 哲学三问起点

## 隐私 / 同步规则（.gitignore）
- `.obsidian/` workspace / cache / themes / plugins 全部本地
- `70_Sources/vibe-hub/pages/` 不进 GitHub（太大）
- `60_Assets/local-*.csv` 与 `teaching-packages.csv` 只本机检索
- `__pycache__/` / 大型媒体（.mp4 .mov .psd .zip .rar .7z）不进

## 下一步
- [ ] 把 index.md / 快速使用指南 / 最终验收 三页用 dossier 体系重写
- [ ] 把 README 顶部三个例子换成三个 dossier 入口
- [ ] 写一个 `review-dossiers.py` 季度脚本，自动校对 dossier 中的事实部分

## 关联
- [[60_Assets/dossiers/]]（所有 dossier 入口）
- [[20_Projects/index]]（32 个项目卡）
- [[30_Teaching/index]]
- [[40_Content/index]]
- [[50_AI/index]]