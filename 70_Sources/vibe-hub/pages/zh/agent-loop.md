---
type: web_source
source_url: "https://vibe-hub.org/agent-loop"
title: "Agent 循环 Agent Loop"
language: zh
category: "agent-loop"
fetched_at: 2026-07-27T10:04:32+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←ReActAI Agent→

# Agent 循环Agent Loop

你可能会说

AI 干到一半就停了，能不能让它自己接着干，拿不准的再来问我？

**产品反复调用模型和工具，并控制继续、确认或停止的运行机制。**·例如修复页面按钮时，产品把读取、修改和检查结果一轮轮交给模型，并在检查通过、达到次数上限或需要你确认时停止。它负责控制任务怎样运行，不能只看模型说“完成了”。

先知道

[ReAct](/react-pattern)[无状态请求 **Stateless Request**](/stateless-request)

也常被叫作*Agentic Loop**智能体循环*

延伸阅读 · 权威出处

[可信 Agent 如何规划、行动、观察并继续Anthropic ↗](https://www.anthropic.com/research/trustworthy-agents)[运行 AgentOpenAI ↗](https://developers.openai.com/api/docs/guides/agents/running-agents)
