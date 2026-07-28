---
type: adr
status: accepted
date: 2026-07-28
tags: [decision, knowledge-base, ai-memory]
---

# ADR · 升级知识库到「专业级 AI 记忆库」

## 上下文

知识库原本只有 `00_Home` / `10_Profile` / `20_Projects` 等 11 个目录，缺少：

- AI 操作手册（每次跟 agent 都要重新解释自己是谁）
- 长期目标锚点（散在 `我是谁 / 我要去哪` 两个文件）
- 每日会话记录（只有一个 `codex-session-timeline.md`）
- 决策日志（决定散在各处，没法回溯）

研究 GitHub 上 3 个最火的 Obsidian 知识库项目：
- **breferrari/obsidian-mind**（4k star）— 给 AI 编程 agent 持久记忆
- **eugeniughelbur/obsidian-second-brain**（3.6k star）— Karpathy LLM Wiki 模式
- **kepano/kepano-obsidian**（4.2k star）— 自下而上组织哲学

obsidian-mind 的「三层记忆」模型正中需求：
- 长期：身份 / 目标 / 原则（`brain/`）
- 中期：当前项目 / 待办 / 最近决策（`20_Projects/` + `decisions/`）
- 短期：最近 7-30 天的活动（`daily/`）

## 决定

按 obsidian-mind 模型改造知识库：

1. 添加 `AGENTS.md` / `CLAUDE.md` 在 vault 根目录
2. 添加 `brain/North Star.md` 锚点文件
3. 添加 `daily/` 目录 + 模板
4. 添加 `decisions/` 目录 + ADR 模板
5. 添加 `.codex/hooks/` 会话开/关自动化
6. 添加 Obsidian Bases `.base` 文件（项目看板 / 能力查询 / 决策时间线 / 每日笔记）

## 影响

### 好的

- agent 启动后不需要重新解释库主是谁
- 长效决策可追溯，避免「上次为什么这么做」
- 每日记录可生成周报 / 月报
- 后续徒弟可以基于这套结构搭自己的

### 成本

- 每次会话结束要花 5 分钟更新 `daily/`
- 重要决策要写 ADR，不能跳过
- 多了一层需要维护的「仪式」

### 后续动作

- [ ] 每个徒弟拿到一份 AGENTS.md 模板，自己填空
- [ ] 季度复盘时把当季 ADR 整理到月度总结
- [ ] 半年后评估这套系统是否真的节省时间

## 引用

- 参考：https://github.com/breferrari/obsidian-mind
- 参考：https://github.com/eugeniughelbur/obsidian-second-brain
- 相关：[[../AGENTS]] [[North Star]]