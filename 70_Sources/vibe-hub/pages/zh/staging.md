---
type: web_source
source_url: "https://vibe-hub.org/staging"
title: "预发布环境 Staging"
language: zh
category: "staging"
fetched_at: 2026-07-27T10:04:17+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←持续交付 / 持续部署监控→

# 预发布环境Staging

你可能会说

先把候选版本部署到和生产配置接近的预发布环境，用脱敏数据走完流程，别直接碰生产。

**预发布环境是在生产发布前，用接近生产的配置验证候选版本的独立环境。**·例如同一 commit 可先部署到 Staging，连接独立服务、测试支付和脱敏订单，再从预发布地址验收。Staging 属于测试环境，但不是所有本地、CI 临时环境或测试网址都叫 Staging。

先知道

[部署上线 **Deployment**](/deployment)[环境变量 **Env Var**](/env-var)

也常被叫作*Staging**Staging Environment**预发布环境**预生产环境**准生产环境*

延伸阅读 · 权威出处

[使用部署环境GitHub Actions ↗](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/control-deployments)
