---
type: web_source
source_url: "https://vibe-hub.org/route"
title: "路由与端点 Route & Endpoint"
language: zh
category: "route"
fetched_at: 2026-07-27T10:04:22+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←后端框架后端→

# 路由与端点Route & Endpoint

你可能会说

用户访问不同的网址，怎么让不同的代码来接管？

**决定一种请求进入后端后，应该交给哪段代码处理**·例如，GET /api/posts 会交给读取文章列表的代码，POST /api/posts 会交给创建文章的代码。端点就是外部可以请求的具体入口，每一条都要说明输入、成功和失败结果。

先知道

[后端 **Backend**](/backend)[HTTP](/http)[API](/api)

**GET**`/api/posts`→ 列表处理

**POST**`/api/posts`→ 创建处理

**GET**`/api/posts/:id`→ 详情处理

方法和路径一起决定进哪段代码

### 什么时候用

- 用**方法 + 名词路径**表达意图：GET /users、POST /users

  方法说明动作，路径说明对象

  读取用户**GET /users**创建用户**POST /users**
- 把路径参数、查询参数和请求体分清楚

  三种参数放在不同位置

  路径**/users/42**查询**?tab=orders**请求体**{ "name": "小林" }**
- 每条端点写清输入、成功响应、错误状态和权限要求

  一条端点要写清四件事

  输入**email**成功**201**失败**400 / 409**权限**需登录**
- 先用浏览器 Network、curl 或 API 工具单独验证端点

  先单独验证接口

  curl -X POST /api/orders**201 Created**{ "orderId": "o\_42" }

### 什么时候不用

- 不要把所有功能放进一个含义不清的通用端点

  一个端点包办一切

  POST /api/doEverything{ "action": "maybe-save-or-delete" }

  端点名称无法清楚表达其读取、修改或删除行为
- 读取数据却用 POST、删除数据却用 GET：会偏离 HTTP 语义，也可能影响缓存和安全预期

  方法和动作相反

  删除**GET /delete/42**读取**POST /getUser**
- 只设计成功响应：参数缺失、冲突和服务失败时也应返回约定的状态与错误信息

  只设计成功分支

  200 成功→500 失败→缺少恢复提示

  参数缺失和服务失败也应有明确响应
- 把密码、令牌等敏感信息放在 URL 查询参数里：它们可能进入浏览历史和访问日志

  敏感信息出现在网址里

  GET /report?**api\_key=sk-live-••••***浏览历史 · 访问日志 · 分享截图*

组成结构 · Anatomy

GET/api/posts?page=2

1方法MethodGET 读取、POST 创建、PATCH 修改、DELETE 删除

2路径Path资源地址，最好使用名词并保持复数规则一致

3查询参数Query用于筛选、搜索、排序和分页，不应该包含密码或令牌

典型使用场景

GET /api/posts 取列表

文章列表**GET /api/posts**

请求参数**?page=2&tag=design**
*→*
响应**200 · 20 篇文章**

POST /api/login 提交登录

提交登录**POST /api/login**

邮箱**oil@example.com**密码**••••••••**登录

请求体携带账号信息，成功后建立会话

GET /api/users/:id 取详情

用户详情**GET /api/users/:id**

路径参数**id = u\_23**姓名**林小狐**角色**editor**

DELETE /api/tasks/:id 删除任务

删除任务**DELETE /api/tasks/:id**

任务**整理首页文案**删除后**按产品策略处理**

确认删除

先确认，再请求 DELETE /api/tasks/t\_42

延伸阅读 · 权威出处

[HTTP 请求方法MDN ↗](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)[HTTP 概述MDN ↗](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview)
