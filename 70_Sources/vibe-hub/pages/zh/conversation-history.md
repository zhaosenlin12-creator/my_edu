---
type: web_source
source_url: "https://vibe-hub.org/conversation-history"
title: "对话历史 Conversation History"
language: zh
category: "conversation-history"
fetched_at: 2026-07-27T10:04:31+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←系统提示词上下文工程→

# 对话历史Conversation History

你可能会说

为什么每次提问，都要把之前聊的一起发给它？

**对话历史是产品保存并在后续请求中重新提供给模型的先前消息记录**·例如，用户说“把第二条改短”时，产品带回原来的三个标题，模型才能确定所指内容。聊天越长越占空间，界面可见的旧消息不代表本次一定全部发送。

先知道

[上下文窗口 **Context Window**](/context-window)

也常被叫作*聊天记录**消息历史*

延伸阅读 · 权威出处

[管理对话状态OpenAI ↗](https://developers.openai.com/api/docs/guides/conversation-state)
