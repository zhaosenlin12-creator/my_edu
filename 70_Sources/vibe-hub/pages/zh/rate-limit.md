---
type: web_source
source_url: "https://vibe-hub.org/rate-limit"
title: "速率限制 Rate Limit"
language: zh
category: "rate-limit"
fetched_at: 2026-07-27T10:04:32+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←Token 用量与成本TTFT / TPS→

# 速率限制Rate Limit

你可能会说

调用太频繁就报错，说什么超过限制，是怎么回事？

**速率限制是服务对一定时间内请求数、Token 数或并发任务数设置的上限**·达到限制后，请求可能排队、延迟或收到 429。具体上限会随服务、模型和账号而变化，处理时要分别看请求数、Token 数与并发任务数。

先知道

[API](/api)

也常被叫作*限流**请求频率限制*

延伸阅读 · 权威出处

[速率限制指南OpenAI ↗](https://developers.openai.com/api/docs/guides/rate-limits)[HTTP 429 与 Retry-AfterRFC 9110 ↗](https://www.rfc-editor.org/rfc/rfc9110.html#name-429-too-many-requests)
