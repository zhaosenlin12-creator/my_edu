---
type: web_source
source_url: "https://vibe-hub.org/cd"
title: "持续交付 / 持续部署 CD"
language: zh
category: "cd"
fetched_at: 2026-07-27T10:04:17+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←部署上线预发布环境→

# 持续交付 / 持续部署CD

你可能会说

把 CI 通过的版本继续送到测试环境；生产上线保留人工批准，并把两种 CD 写清楚。

**CD 是让通过验证的版本持续处于可发布状态，或自动发布到目标环境的交付方式。**·持续交付通常把候选版本准备好，由人决定何时发布；持续部署则在门禁通过后自动进入生产。两者都接在 CI 之后，区别首先要看生产前是否保留人工批准。

先知道

[持续集成 **CI**](/ci)[部署上线 **Deployment**](/deployment)

也常被叫作*CD**Continuous Delivery**Continuous Deployment**持续交付**持续部署**CI/CD*

延伸阅读 · 权威出处

[持续部署GitHub Actions ↗](https://docs.github.com/en/actions/get-started/continuous-deployment)
