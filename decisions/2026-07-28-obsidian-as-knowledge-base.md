---
type: adr
status: accepted
date: 2026-07-28
tags: [decision, tool, knowledge-base]
---

# ADR · 选用 Obsidian 作为知识库底座

## 上下文

个人 / 团队知识库有多个候选：

| 工具 | 优势 | 劣势 |
|------|------|------|
| **Obsidian** | 本地 Markdown、双链、插件生态、Vault-as-folder | 同步需自己解决 |
| Notion | 多人协作强、database 视图 | 月费、依赖网络、数据锁定 |
| Logseq | 大纲式、隐私好 | UI 学习曲线、插件少 |
| Apple Notes | 系统集成、移动端好 | 弱结构化、无版本控制 |
| VSCode + Markdown | 全键盘工作流 | 无可视化、无双链 |

## 决定

**Obsidian** 作为知识库底座。

理由：
1. **本地 Markdown** = 数据自主，git 同步，与 AI 工具天然兼容
2. **双链** + **Graph View** = 知识网络化
3. **插件生态**（Bases、Dataview、Templater、Excalidraw）覆盖大部分需求
4. **Vault-as-folder** = 可以直接用 `rg` / `python` / `codex` 操作
5. **免费** 个人版，4 个徒弟也能各自搭

## 影响

### 好的

- 数据完全自主（纯文件夹 + md）
- 与 GitHub / Codex / Python 工具链无缝
- 库主可以用任何编辑器直接读写

### 成本

- 移动端体验比 Notion / Apple Notes 差
- 多人实时协作不行（但 4 个徒弟是各自独立的 vault）
- 需要自己解决备份（git 够用）

### 后续动作

- [ ] 把 Obsidian Bases 配成熟（这次会话里会做）
- [ ] 给 4 个徒弟每人出一份「Obsidian vault 起步包」（基于本 vault 的 AGENTS.md 模板）
- [ ] 评估是否需要 Obsidian Sync / Git 同步方案

## 引用

- [[../AGENTS]]
- [Obsidian 官网](https://obsidian.md)