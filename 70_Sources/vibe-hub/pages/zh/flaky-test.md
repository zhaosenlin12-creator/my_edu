---
type: web_source
source_url: "https://vibe-hub.org/flaky-test"
title: "不稳定测试 Flaky Test"
language: zh
category: "flaky-test"
fetched_at: 2026-07-27T10:04:18+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←测试数据与 Fixture验收标准→

# 不稳定测试Flaky Test

你可能会说

同一个 commit 的测试一会儿过一会儿不过，别只点重试，查清是时序还是共享数据。

**不稳定测试是在代码未改变时仍会时而通过、时而失败的测试。**·例如 CI 中的页面测试偶发超时，或并行用例抢同一个账号导致结果交替。重试可以帮助确认现象和收集证据，但不能当作修复；稳定失败通常更像真实缺陷或固定配置错误。

先知道

[测试用例 **Test Case**](/test-case)

也常被叫作*Flaky Test**不稳定用例**间歇性失败测试*

延伸阅读 · 权威出处

[ISTQB GlossaryISTQB ↗](https://glossary.istqb.org/)[Playwright 测试与 FixturePlaywright ↗](https://playwright.dev/docs/intro)
