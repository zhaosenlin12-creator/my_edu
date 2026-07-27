---
type: web_source
source_url: "https://vibe-hub.org/streaming-response"
title: "流式响应 Streaming Response"
language: zh
category: "streaming-response"
fetched_at: 2026-07-27T10:04:30+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←结构化输出无状态请求→

# 流式响应Streaming Response

你可能会说

别让我干等，像打字机一样一个字一个字往外蹦。

**流式响应是服务器把生成结果分成连续片段发送、界面逐段显示的传输方式**·例如，聊天回答会像打字一样逐段出现。首段更早可见不代表整份回答更早完成，总时长仍受后续生成和传输影响。

先知道

[HTTP](/http)[Token](/token)

也常被叫作*Streaming**流式输出*

延伸阅读 · 权威出处

[流式响应指南OpenAI ↗](https://developers.openai.com/api/docs/guides/streaming-responses)
