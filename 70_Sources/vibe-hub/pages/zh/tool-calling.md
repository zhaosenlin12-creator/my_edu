---
type: web_source
source_url: "https://vibe-hub.org/tool-calling"
title: "工具调用 Tool Calling"
language: zh
category: "tool-calling"
fetched_at: 2026-07-27T10:04:32+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←Sub-agentReAct→

# 工具调用Tool Calling

你可能会说

AI 光会说不会做，怎么让它真的去查数据库、发请求？

**工具调用是模型请求产品执行指定工具并提供参数的输出方式**·例如，模型可请求查询日历，产品检查权限和参数后才实际读取日程，再把真实结果交回模型。删除、发送等操作仍须检查范围并确认。

先知道

[结构化输出 **Structured Output**](/structured-output)[API](/api)

也常被叫作*Function Calling**函数调用*

延伸阅读 · 权威出处

[工具调用指南OpenAI ↗](https://developers.openai.com/api/docs/guides/function-calling)
