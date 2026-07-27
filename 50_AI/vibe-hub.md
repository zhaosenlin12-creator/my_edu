---
type: ai
status: active
domain: ai,reference
audience: self,student,teacher
source: https://vibe-hub.org
local: "[[70_Sources/vibe-hub]]"
pages: 484(zh 242 + en 242)
updated_at: 2026-07-27
tags: ai,vibe-hub,reference
---

# VibeHub 离线资料

> [vibe-hub.org](https://vibe-hub.org) 的**全站离线镜像**。484 页(中文 242 + 英文 242),AI 编程大白话学习资料。

## 一句话

VibeHub 是**用大白话讲 AI 编程概念**的资料站。我用 firecrawl 全站抓取下来,本地可以直接读。**我的 AI 入门 + 抖音脚本参考都从这里取材**。

## 资料规模

- 总页数:**484 页**
- 中文:242 页
- 英文:242 页
- 抓取方式:`firecrawl` 全站爬取
- 抓取脚本:`[[50_AI/_skills/website-knowledge-crawler]]`
- 位置:`[[70_Sources/vibe-hub/]]`

## 内容分布

```mermaid
graph TB
  V[VibeHub] --> T[技术 topics]
  V --> C[组件 components]
  V --> P[提示词 prompts]
  V --> S[风格 styles]
  V --> A[Agent / RAG]

  T --> T1[AI / Backend / Design / Git / Product / Technology]
  C --> C1[Button / Card / Modal / Table / Tree 等]
  P --> P1[Vibe Coding 入门 / Prompt 模式]
  S --> S1[Minimal / Swiss / Notion / Y2K 等]
  A --> A1[Sub-agent / Agent Loop / Tool Calling]
```

## 我怎么用它

| 用途 | 怎么用 |
|---|---|
| **学新概念** | Agent / RAG / Tool Calling 等从 `topics/ai.md` 读起 |
| **写抖音脚本** | 找"普通人能 8 秒看懂"的钩子 |
| **选 UI 组件** | `components/` 找参考 |
| **选视觉风格** | `styles/` 找方向 |
| **写 prompt** | `vibe-coding.md` + `system-prompt.md` |

## 高频使用的页

- `topics/ai.md` · AI 术语大全
- `agent-loop.md` / `sub-agent.md` · Agent 设计
- `tool-calling.md` · 工具调用
- `vibe-coding.md` · Vibe Coding 是什么
- `token-cost.md` · Token 成本治理
- `system-prompt.md` · 系统提示词

## 抓取流程

```mermaid
sequenceDiagram
  participant Me
  participant Codex
  participant Firecrawl
  participant Vault

  Me->>Codex: 我要爬 vibe-hub.org
  Codex->>Firecrawl: 用 website-knowledge-crawler skill
  Firecrawl->>Vault: 484 页 markdown 进 70_Sources/vibe-hub/
  Me->>Vault: Obsidian 全文搜索
```

## 注意事项

- **不进 GitHub**(`.gitignore` 已配置)
- **不修改原文**(留作可检索资料库)
- **本地路径**:`[[70_Sources/vibe-hub/README]]`

## 看相关

- [[50_AI/_skills/website-knowledge-crawler]] · 抓取 skill
- [[70_Sources/vibe-hub/]] · 484 页离线
- [[70_Sources/index]] · 资料总入口