---
type: web_source
source_url: "https://vibe-hub.org/integration-test"
title: "集成测试 Integration Test"
language: zh
category: "integration-test"
fetched_at: 2026-07-27T10:04:16+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←单元测试端到端测试→

# 集成测试Integration Test

你可能会说

别只测函数，确认下单接口真的能把订单写进测试数据库，再把结果读回来。

**集成测试是验证多个模块、服务或依赖之间能否按约定正确协作的测试。**·例如提交订单后，接口应把正确字段写进测试数据库，并返回前端能够识别的结果。它能发现字段名、序列化和依赖连接问题；若从浏览器入口走完整用户流程，则属于范围更大的端到端测试。

先知道

[单元测试 **Unit Test**](/unit-test)[API](/api)

也常被叫作*Integration Test**集成测*

延伸阅读 · 权威出处

[ISTQB GlossaryISTQB ↗](https://glossary.istqb.org/)
