---
type: web_source
source_url: "https://vibe-hub.org/smoke-test"
title: "冒烟测试 Smoke Test"
language: zh
category: "smoke-test"
fetched_at: 2026-07-27T10:04:17+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←端到端测试回归测试→

# 冒烟测试Smoke Test

你可能会说

新版本刚部署，先用几分钟检查首页、登录和预订入口，坏一个就先别继续。

**冒烟测试是新构建后用少量关键检查判断系统是否基本可用、值得继续深测。**·例如先打开首页、完成一次登录并检查核心接口健康；任一关键入口失败就阻断后续测试。它追求广而浅的快速判断，不是完整回归测试，也不应把所有用例都塞进来。

先知道

[构建 **Build**](/build)[测试用例 **Test Case**](/test-case)

也常被叫作*Smoke Test**冒烟检查**Build Verification Test**BVT*

延伸阅读 · 权威出处

[ISTQB GlossaryISTQB ↗](https://glossary.istqb.org/)
