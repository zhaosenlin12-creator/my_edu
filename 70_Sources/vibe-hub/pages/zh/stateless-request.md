---
type: web_source
source_url: "https://vibe-hub.org/stateless-request"
title: "无状态请求 Stateless Request"
language: zh
category: "stateless-request"
fetched_at: 2026-07-27T10:04:30+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←流式响应结构化输出→

# 无状态请求Stateless Request

你可能会说

AI 其实记不住我？每次都要把背景重新讲一遍？

**无状态请求是每次向模型提问时，都要重新带上它这次需要知道的背景。**·例如你只发送“把第二条改短”，却没有同时带上前面的三条标题，模型就不知道“第二条”指什么。聊天记录可以由产品保存，但不会因为界面还看得到就自动进入这次请求。

先知道

[API](/api)[HTTP](/http)

也常被叫作*无状态 API*

延伸阅读 · 权威出处

[管理对话状态OpenAI ↗](https://developers.openai.com/api/docs/guides/conversation-state)
