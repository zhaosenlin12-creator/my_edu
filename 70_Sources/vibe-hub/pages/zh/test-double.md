---
type: web_source
source_url: "https://vibe-hub.org/test-double"
title: "测试替身 Test Double"
language: zh
category: "test-double"
fetched_at: 2026-07-27T10:04:17+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←测试覆盖率测试数据与 Fixture→

# 测试替身Test Double

你可能会说

单测别真的扣款，用一个可控的支付替身返回成功和超时，再检查订单模块怎么处理。

**测试替身是在测试中用可控对象代替真实依赖的做法，Mock 是其中一种常见形式。**·例如测试订单模块时，可让替身支付服务返回成功、拒绝或超时，并检查调用参数和处理结果。替身适合隔离慢或不稳定的外部依赖；要验证真实接口契约时仍需集成测试。

先知道

[单元测试 **Unit Test**](/unit-test)[API](/api)

也常被叫作*Test Double**Mock**测试替身**Stub**Fake**Spy*

延伸阅读 · 权威出处

[ISTQB GlossaryISTQB ↗](https://glossary.istqb.org/)[Jest Mock FunctionsJest ↗](https://jestjs.io/docs/mock-functions)
