---
type: web_source
source_url: "https://vibe-hub.org/backend-framework"
title: "后端框架 Backend Framework"
language: zh
category: "backend-framework"
fetched_at: 2026-07-27T10:04:22+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←后端路由与端点→

# 后端框架Backend Framework

你可能会说

写后端有没有现成的架子，别让我从零搭。

**开发后端时使用的现成项目骨架，帮助组织请求、处理代码和错误**·例如，注册请求到来后，框架会把它交给注册功能的代码，并在出错时返回明确结果。框架不是一门新语言，应优先沿用项目已经选择的方案。

先知道

[后端 **Backend**](/backend)

入口**路由***GET /api/signup*
*→*
框架代办**公共处理***日志 · 身份 · 错误*
*→*
你写的业务**处理函数***创建账号*

框架给骨架；业务规则仍要你写清楚

### 什么时候用

- 优先使用项目已经选好的框架，遵循现有目录和写法

  先沿用项目结构

  *src/*├─ routes/orders.ts├─ services/payment.ts└─ app.ts

  新代码放进团队已经熟悉的位置
- 小项目选简单方案；团队大、规则多时再考虑更强约束

  规模决定约束

  小型 API**Express · 少量目录**多人项目**NestJS · 明确模块**
- 先读官方最小示例：一条 GET、一条 POST、一种错误处理

  先跑通官方最小示例

  GET /hello**200 OK**POST /items**201 Created**错误**400 Bad Request**
- 让 AI 说明代码放在哪个文件、由谁调用、如何验证

  让 AI 交代上下文

  放在哪**routes/orders.ts**谁调用**POST /api/orders**怎么验**npm test**

### 什么时候不用

- 把框架名字当能力：换框架不会自动解决业务设计问题

  框架不能替你决定业务

  换成 NestJS**✓ 目录更整齐**
  *→*
  退款规则**? 仍未定义**
- 一个项目同时混用多个后端框架，路由和配置各管一套

  一条请求穿过三套框架

  Next Route→Express→Fastify

  路由、插件和错误处理各管一套
- 不看版本就复制旧教程：配置和 API 很可能已经变化

  教程版本与项目版本不一致

  旧教程**Framework v3**
  *→*
  当前项目**Framework v5**

  先查当前版本的官方文档
- 只会运行模板却不理解请求入口、处理过程和响应出口，排错时会缺少判断依据

  模板能启动，但请求流程说不清

  请求从哪进？→谁处理？→响应从哪出？

组成结构 · Anatomy

①**路由入口***→*②**公共处理***→*③**业务处理**

1路由Route根据 HTTP 方法和路径，把请求交给对应处理函数

2公共处理Middleware在业务代码前后统一完成日志、身份、校验或错误转换

3处理函数Handler执行这条端点自己的业务规则，并返回明确响应

常见变体 · Variants

全栈框架Full-stack

Next.js · Nuxt

页面和后端放在一个项目里

轻量 API 框架Minimal API

Express · Fastify · Flask

快速搭几条清晰接口

带结构的框架Structured

NestJS · Django

模块和规则较多的团队项目

典型使用场景

Next.js Route Handler

Next.js Route Handler**页面与接口放在同一项目**

app/api/posts/route.tsexport async function GET() { return Response.json(posts)}

访问 GET /api/posts

Express 小型 API

Express API**用少量路由构建小服务**

app.get("/api/tasks", listTasks)app.post("/api/tasks", createTask)app.use(errorHandler)

FastAPI 数据接口

FastAPI**Schema 自动生成接口文档**

POST /items**创建商品**Request body**ItemSchema**Response**201**

Swagger 文档可直接调试

Django 内容管理后台

Django 后台**成熟内容项目的管理界面**

文章**1,284 条**作者**42 人**待审核**18 条**

框架自带模型、权限和管理后台

延伸阅读 · 权威出处

[服务端 Web 框架MDN ↗](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/First_steps/Web_frameworks)
