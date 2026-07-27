---
type: web_source
source_url: "https://vibe-hub.org/response-speed"
title: "TTFT / TPS"
language: zh
category: "response-speed"
fetched_at: 2026-07-27T10:04:31+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←速率限制Token 用量与成本→

# TTFT / TPS

你可能会说

为什么有的 AI 半天才出第一个字，有的秒回？

**TTFT 与 TPS 是分别衡量模型首段响应等待时间和后续生成速度的指标**·TTFT 是从发送请求到收到第一个输出 Token 的时间，TPS 表示开始生成后每秒产生的 Token 数。TTFT 短不代表整段回答很快，输出长度也会影响总时长。

先知道

[流式响应 **Streaming Response**](/streaming-response)[Token](/token)

也常被叫作*TTFT 与 TPS**TTFT & TPS**首 Token 延迟**每秒 Token 数*

延伸阅读 · 权威出处

[延迟优化指南OpenAI ↗](https://developers.openai.com/api/docs/guides/latency-optimization)
