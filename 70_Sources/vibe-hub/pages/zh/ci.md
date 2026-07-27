---
type: web_source
source_url: "https://vibe-hub.org/ci"
title: "持续集成 CI"
language: zh
category: "ci"
fetched_at: 2026-07-27T10:04:18+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←构建代码规范检查→

# 持续集成CI

你可能会说

每次提 PR 都自动跑构建、Lint 和测试，失败就先别合进主分支。

**持续集成是频繁合入变更并自动构建、测试，以尽早发现集成问题的做法。**·例如推送分支后，流水线自动安装依赖、执行 Lint、单元测试和构建，并把结果显示在 PR 上。CI 提供合入前后的快速反馈，但检查通过不等于版本已经发布到生产。

先知道

[Git](/git)[构建 **Build**](/build)[单元测试 **Unit Test**](/unit-test)

也常被叫作*CI**Continuous Integration**持续集成*

延伸阅读 · 权威出处

[持续集成GitHub Actions ↗](https://docs.github.com/en/actions/get-started/continuous-integration)
