# AGENTS.md

> **AI Agent 必读** — 这是这座知识库的使用说明书。每次会话开始，AI 必须先读完这份文件，再读取 [[brain/North Star]] 和最近一篇 [[daily/]]，然后再回应用户。

## 0. 库主是谁

- **机构**：乐启享（教育机构）
- **个人品牌**：愈见森林（抖音）/ 森林（教学身份）
- **个人站**：<https://senlin-c1n.pages.dev/>
- **年度核心目标**：
  1. 教学产品化（7 天训练营可规模化）
  2. 抖音涨到 10000 粉
- **详细画像**：见 [[10_Profile/我是谁]] [[10_Profile/我在哪]] [[10_Profile/我要去哪]] [[10_Profile/能力地图]]

## 1. 知识库结构

```
00_Home/          入口、指南、本周最重要
10_Profile/       身份 / 定位 / 能力
20_Projects/      进行中的项目
30_Teaching/      教学产品、课程、学员
40_Content/       自媒体内容、直播
50_AI/            AI 学习路线、技能
60_Assets/        Dossier（事实/推断/待确认三段式）+ 本地资料
70_Sources/       外站抓取（vibe-hub 等）+ 原始数据
80_Canvas/        Obsidian Canvas 可视化
90_Archive/       归档
90_Scripts/       Python 脚本（audit 等）
```

详细结构看 [[README]]。

## 2. AI 必须遵守的规则

### 风格
- 中文为主，技术词保留英文
- 不用「评分 X 年教学经验」「拥有 X 项技能」这种抽象话
- 每句话都要可追溯到 dossier 或具体文件
- 生产级别，不是开发文案

### 三段式 Dossier（重要）
每个核心实体（机构、人、项目、课程）的 dossier 必须分三段：
- **事实**：可直接引用的来源（文件名 / URL / 日期）
- **推断**：基于事实的合理推断，标「推断」前缀
- **待确认**：未知或需要求证的，标「待确认」

### 不要做的事
- 不要给学员做「专业级」评价（「资深」「大牛」之类）
- 不要编造 GitHub commit 数、粉丝数、收入
- 不要把推断当作事实陈述

## 3. 会话生命周期

### 启动必读
1. 这份 AGENTS.md
2. [[brain/North Star]]
3. 最新一篇 [[daily/]] 笔记

### 关闭前必做（如果今天产生了新信息）
- 在 `daily/YYYY-MM-DD.md` 追加一段「今日决策」「今日待办」
- 涉及长期决策 → 在 `decisions/YYYY-MM-DD-title.md` 创建 ADR
- 涉及人物 → 在 `people/name.md` 更新
- 涉及项目状态变化 → 更新 `20_Projects/xxx.md` 的 status 字段

### 找东西的方式
- **目录走读**：用 [[MOCs]] 里的索引笔记
- **Dataview 查询**：用 `*.base` 文件（项目看板、能力地图、决策时间线）
- **搜索**：Obsidian 全局搜索（Ctrl+Shift+F），或 PowerShell `rg`
- **AI 检索**：告诉 agent 「去 70_Sources 找 XX」或「在 20_Projects 里找跟 XX 相关的项目」

## 4. 常用任务速查

| 任务 | 看哪里 |
|------|--------|
| 库主是谁 / 在哪 / 去哪 | `10_Profile/` |
| 当前进行项目 | `20_Projects/` |
| 教学产品怎么定价 | `30_Teaching/` |
| 抖音选题 / 直播复盘 | `40_Content/` |
| 学 AI 怎么学 | `50_AI/` |
| 关键人物 / 机构 / 站点 详细资料 | `60_Assets/dossiers/` |
| 外站学习资料（vibe-hub 等） | `70_Sources/` |
| 最近做了什么 | `daily/` 最新 7 天 |
| 关键决策 | `decisions/` |
| 运行脚本 / 自动化 | `90_Scripts/` |

## 5. 关键工具与命令

### 启动本地 vibe-hub 镜像
```
start-server.bat
```
双击 `C:\my_know\70_Sources\vibe-hub\start-server.bat`，浏览器自动开 `http://localhost:8765/`。

### 跑 audit
```
python C:\my_know\90_Scripts\audit_dossiers.py
```

### 抓取新站
```
python C:\Users\Administrator\.codex\skills\website-knowledge-crawler\scripts\mirror_site.py <url> <out>
```

### 更新知识库索引
```
python C:\my_know\90_Scripts\build_knowledge_index.py
```

## 6. 跟库主对话时的语气

- 实务、直接、不绕弯子
- 用「你」不用「您」
- 简短句子，长篇用结构（短段落 + 偶尔列表）
- 不带表情、不用 emoji 除非库主先用了
- 不主动称赞，避免拍马屁

## 7. 升级这份文件

库主的生活方式 / 目标 / 偏好变化时，更新这份文件 + `brain/North Star.md`，让 AI 永远拿到最新的画像。