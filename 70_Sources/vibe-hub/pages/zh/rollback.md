---
type: web_source
source_url: "https://vibe-hub.org/rollback"
title: "回滚 Rollback"
language: zh
category: "rollback"
fetched_at: 2026-07-27T10:04:19+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←监控功能开关→

# 回滚Rollback

你可能会说

新版本让预订失败率升高，先切回上一版，并确认版本号和错误率真的恢复。

**回滚是把系统或配置恢复到先前已知可用状态，以停止新版本造成的影响。**·例如 v2 上线后错误率明显上升，可以把流量切回 v1，再检查线上版本和关键指标是否恢复。修好代码后发布 v3 属于向前修复；关闭功能开关也不一定改变部署版本。

先知道

[部署上线 **Deployment**](/deployment)[监控 **Monitoring**](/monitoring)

也常被叫作*Rollback**版本回滚**回退*

延伸阅读 · 权威出处

[Kubernetes Deployment 回滚Kubernetes ↗](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#rolling-back-a-deployment)
