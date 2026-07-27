---
type: web_source
source_url: "https://vibe-hub.org/cors"
title: "CORS"
language: zh
category: "cors"
fetched_at: 2026-07-27T10:04:12+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←JSON数据校验→

# CORS

你可能会说

网页请求接口被浏览器拦住了，帮我检查是不是 CORS 配置没有允许这个站点。

**CORS 是浏览器要求服务器明确同意后，网页才能跨源读取响应的安全机制。**·例如网页从 `app.example.com` 请求 `api.example.com`，服务器要在响应中允许这个网页来源，浏览器才把数据交给脚本。它保护的是浏览器里的跨源读取；接口能否被调用、用户是否有权限，仍要由服务器验证。

先知道

[HTTP](/http)[API](/api)

也常被叫作*跨源资源共享**跨域资源共享**Cross-Origin Resource Sharing*

延伸阅读 · 权威出处

[跨源资源共享（CORS）MDN ↗](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS)
