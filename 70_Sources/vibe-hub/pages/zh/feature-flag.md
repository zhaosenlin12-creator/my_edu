---
type: web_source
source_url: "https://vibe-hub.org/feature-flag"
title: "功能开关 Feature Flag"
language: zh
category: "feature-flag"
fetched_at: 2026-07-27T10:04:18+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←回滚Serverless→

# 功能开关Feature Flag

你可能会说

新行程编辑器先只给内部同事看，出问题时不用重新部署就能立刻关闭。

**功能开关是运行时按配置或用户条件启用、停用代码路径的机制。**·例如同一版本已经包含新编辑器，但开关只让内部账号进入新路径，其他用户继续看到旧页面。它把代码部署与功能开放分开；长期不用的开关仍要清理，也不能代替版本回滚和数据恢复。

先知道

[部署上线 **Deployment**](/deployment)[状态 **State**](/state)

也常被叫作*Feature Flag**Feature Toggle**功能旗标**特性开关*

延伸阅读 · 权威出处

[功能开关简介OpenFeature ↗](https://openfeature.dev/docs/reference/intro/)
