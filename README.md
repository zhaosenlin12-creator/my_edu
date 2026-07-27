# 森林个人知识库

> 一个面向开发、教学、直播、自媒体与 AI 协作的 Obsidian Vault。目标不是收藏信息，而是持续回答：我是谁、我在哪、我要去哪。

## 从这里开始
1. [[10_Profile/我是谁]]：身份、角色、价值主张
2. [[10_Profile/我在哪]]：当前项目、教学、内容和卡点
3. [[10_Profile/我要去哪]]：90 天、1 年、3 年目标
4. [[10_Profile/能力地图]]：已验证能力、在补能力和边界
5. [[00_Home/本周最重要的事]]：把方向落到本周动作

## 目录
- `00_Home`：本周焦点、模板和 MOC 总索引
- `10_Profile`：个人画像、能力证据与目标
- `20_Projects`：GitHub 和本地项目卡
- `30_Teaching`：课程、教案和学员作品
- `40_Content`：抖音、直播、栏目和复盘
- `50_AI`：工具卡、工作流和学习路线
- `60_Assets`：本地与在线资产索引
- `70_Sources`：外部学习资料及来源说明
- `80_Canvas`：能力与关系可视图
- `90_Archive`：停止维护的历史内容

## 快速检索
- Obsidian 全文搜索：`Ctrl+Shift+F`
- 按主题浏览：`00_Home/MOCs/`
- 查项目：[[20_Projects/index]]
- 查课程：[[30_Teaching/index]]
- 查内容：[[40_Content/index]]
- 查 AI：[[50_AI/index]]
- 查外部资料：[[70_Sources/index]]
- 命令行：`rg -n "关键词" C:\my_know`

核心笔记统一使用 properties：`type`、`status`、`domain`、`audience`、`repo`、`url`、`summary`、`next_action`、`updated_at`。

## 记录原则
- 事实、推断、待确认分开写
- 宣称“会”必须链接到项目、课程、内容或数据证据
- 每张卡都要有下一步，不建没有用途的收藏夹
- 外部原文与自己的理解分开存放
- Token、密码、合同、学生隐私永不进入仓库

## VibeHub 离线学习库
`70_Sources/vibe-hub` 已从 <https://vibe-hub.org/> 的 sitemap 抓取 484 个允许页面，中文和英文各 242 页。

- 本地全文：`70_Sources/vibe-hub/pages/`
- 表格索引：`70_Sources/vibe-hub/index.csv`
- 学习路线：[[50_AI/AI编程学习路线]]
- 原始页面仅保留本地，不推送到公开 GitHub
- 抓取 Skill：`C:\Users\Administrator\.codex\skills\website-knowledge-crawler`

## 四位徒弟入门
协作和建库规则见 [[CONTRIBUTING]]。每位徒弟复制这套骨架后，必须重写自己的“三问”和能力地图，不照抄森林的个人结论。

## GitHub 同步
- 本地 Vault：`C:\my_know`
- 远端：<https://github.com/zhaosenlin12-creator/my_edu>
- 开始工作：`git pull --rebase`
- 提交检查：`git status` 与 `git diff --check`
- 同步：`git add -A && git commit -m "docs: update knowledge base" && git push`

## 推荐 Obsidian 插件
Dataview、Templater、Excalidraw、Tag Wrangler、Obsidian Git。插件不是知识库成立的前提，先把核心工作流跑通再安装。
