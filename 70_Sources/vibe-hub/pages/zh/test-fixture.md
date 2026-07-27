---
type: web_source
source_url: "https://vibe-hub.org/test-fixture"
title: "测试数据与 Fixture Test Data and Fixture"
language: zh
category: "test-fixture"
fetched_at: 2026-07-27T10:04:18+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←测试替身不稳定测试→

# 测试数据与 FixtureTest Data and Fixture

你可能会说

每次测试前都准备同一个用户和订单，跑完后清理掉，保证下一次还是同样的起点。

**测试数据是测试使用的输入与状态样本，Fixture 是复用这些准备和清理过程的机制。**·例如固定 JSON 保存用户和订单值，Fixture 在用例开始前创建它们、结束后删除或重置。数据回答“用什么值”，Fixture 回答“怎样准备和恢复环境”；它不负责替代外部服务的行为。

先知道

[测试用例 **Test Case**](/test-case)[数据库 **Database**](/database)

也常被叫作*Test Fixture**Fixture**测试夹具**测试数据*

延伸阅读 · 权威出处

[ISTQB GlossaryISTQB ↗](https://glossary.istqb.org/)[Playwright 测试与 FixturePlaywright ↗](https://playwright.dev/docs/intro)
