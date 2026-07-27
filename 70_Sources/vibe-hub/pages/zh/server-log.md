---
type: web_source
source_url: "https://vibe-hub.org/server-log"
title: "服务端日志 Server Logs"
language: zh
category: "server-log"
fetched_at: 2026-07-27T10:04:25+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←ServerlessSEO→

# 服务端日志Server Logs

你可能会说

线上报错了，我想知道服务器那边到底发生了什么，去哪看？

**记录后端运行时发生了什么，主要用来查找失败原因**·例如，用户提交订单时出现 500 错误；如果记录了关键步骤，日志可以帮助判断问题发生在数据库连接还是权限检查。日志要保留时间和必要线索，但不能记录密码、Token、Cookie 或完整个人资料。

先知道

[后端 **Backend**](/backend)[终端命令行 **Terminal**](/terminal)

12:08:31 **POST /api/orders** req\_8fa2INFO order created · 201 · 184msuser=u\_23 · order=o\_91

### 什么时候用

- 记录时间、级别、请求 id、动作、结果和耗时

  一条可定位的日志

  12:08:31 **INFO** req\_8fa2POST /api/orders · **201** · 184ms
- 错误日志保留堆栈和必要上下文，用户响应保持简洁

  用户和开发者看到不同层次

  页面提示**暂时无法保存，请重试**服务端日志**DB timeout · stack trace**
- 部署后先复现一次，再按时间或 request id 搜索日志

  用 request id 串起一次请求

  **req\_8fa2** · request received**req\_8fa2** · payment checked**req\_8fa2** · order created
- 对错误率、延迟和关键失败设置监控与告警

  从单条日志上升到监控

  过去 5 分钟**错误率 8.2%**告警**已通知值班人员**

### 什么时候不用

- 打印密码、Token、Cookie 或整份用户资料

  日志中不能记录敏感信息

  password=**123456**token=**eyJhbGciOi••••**cookie=**session=••••**
- 只写“出错了”：没有动作、对象和错误原因

  这条日志无法帮助排错

  16:42:09 **ERROR 出错了***缺少请求、动作、对象和原因*
- 用日志代替错误处理：打印后仍假装请求成功

  打印错误后仍返回成功

  数据库失败→console.error→200 OK

  日志不能代替重试、回滚或失败响应
- 线上开启海量调试日志又从不清理，成本和噪音一起涨

  调试日志淹没真正的问题

  每天**1,280 万行 DEBUG**真正错误**3 行，被噪音盖住**

组成结构 · Anatomy

12:08:31 · INFOreq\_8fa2order created · 184ms

1时间与级别Time & Level说明何时发生、是普通信息、警告还是错误

2请求编号Request ID把同一次请求产生的多行日志串在一起，方便跨步骤追踪

3事件与上下文Event记录动作、结果、耗时和必要标识，但不写密码、Token 或完整个人资料

常见变体 · Variants

INFOINFO

请求完成 · 201

记录正常的关键业务动作

WARNWARN

重试第 2 次

暂未失败，但需要关注

ERRORERROR

数据库连接失败

请求失败，需要定位和告警

典型使用场景

Vercel Function Logs

函数日志**查看一次请求发生了什么**

12:08:31 INFO req\_8fa2POST /api/ordersorder created · 201 · 184ms

按 request id 追踪请求

请求追踪**用同一个 request id 串起多步**

req\_8fa2 · request receivedreq\_8fa2 · payment checkedreq\_8fa2 · order savedreq\_8fa2 · response 201

查看 500 错误堆栈

500 错误**用户看到简短提示，日志保留细节**

页面**暂时无法保存，请重试**日志**DB timeout · stack line 42**

监控错误率与响应耗时

运行监控**从日志汇总错误率和耗时**

请求量**12.4k**P95 延迟**820ms**错误率**8.2%**告警**已通知**
