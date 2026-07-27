---
type: web_source
source_url: "https://vibe-hub.org/http"
title: "HTTP"
language: zh
category: "http"
fetched_at: 2026-07-27T10:04:11+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←URLHTTPS→

# HTTP

你可能会说

我就想知道，点一下按钮，浏览器和服务器之间到底发生了什么。

**浏览器或 App 向服务器提出请求、再接收结果时遵守的通信规则**·例如，用户在资料页修改昵称并点击保存后，页面会通过 HTTP 发出请求，服务器再返回成功、失败和具体内容。开发者可以在浏览器的 Network 面板里看到这次通信。

先知道

[URL](/url)

也常被叫作*HTTP 请求**超文本传输协议*

GET —— 获取资源  
GET /api/components HTTP/1.1  
Host: api.vibeui.dev

POST —— 交数据  
POST /api/login HTTP/1.1  
Content-Type: application/json{ "email": "you@example.com", "pwd": "••••••" }

### 什么时候用

- 地址栏回车、普通链接导航通常发 **GET**：接口通常把它设计为读取，不应借此改变业务状态

  🔒vibeui.dev/components

  GET地址栏回车就是 GET
- [表单 **Form**](/form) 默认会发 **GET**；配置 method="post" 才发 POST。登录、注册等操作常按接口约定把数据放在请求体里

  you@example.com••••••••

  登录POST
- 调 api 出问题，先开 **Network 面板**看请求长什么样

  NetworkFetch/XHR

  GET/api/list200

  POST/api/save200
- 可按常见约定用 **PUT / PATCH / DELETE** 表达更新或删除；也有接口因兼容性或动作语义使用 POST，先遵循接口契约

  GETPOSTPUTDELETE

### 什么时候不用

- 用 **GET 传密码**：明文留在浏览器历史和服务器日志里

  /login?pwd=123456密码进了浏览器历史和服务器日志
- 给 **GET 依赖请求体**：规范没有为它定义通用语义，许多实现会忽略或拒绝；把参数按接口约定放进 URL

  GET/api/list

  GET 请求体没有通用语义，不应依赖服务端怎样处理它
- 下单按钮**只靠前端防重复点击**：网络重试和并发仍可能重复到达；服务端要按幂等键、订单号或唯一约束保证同一操作只生效一次

  POST/api/order ×3

  重复请求可能创建多笔订单；服务端也要用幂等键或唯一约束兜底
- 接口报错时先检查实际请求，不要直接猜测前端问题

  未检查实际请求，就按假设修改接口格式

组成结构 · Anatomy

POST /api/login HTTP/1.1  
Host: api.vibeui.dev  
Content-Type: application/json{ "email": "you@example.com", "pwd": "••••••" }

1请求方法Method这封信想干嘛：GET 拿、POST 交、PUT 改、DELETE 删

2请求地址URL寄给谁，见 url；路径加参数

3请求头Headers信封上的附加说明：内容类型、身份凭证、来源

4请求体Body可选的数据载体，常见于 POST、PUT、PATCH 等请求；内容格式由 Content-Type 和接口约定决定

常见变体 · Variants

GETGET

GET /api/list?page=1

获取资源，并按接口约定在 URL 中传查询参数

POSTPOST

POST /api/login

交数据，内容放在请求体里

PUT / PATCHPUT & PATCH

PUT /api/items/42

更新已有数据，覆盖或局部改

DELETEDELETE

DELETE /api/items/7

删除数据时用，请慎重

典型使用场景

地址栏回车发 GET

🔒
vibeui.dev/components
⏎

Network · 1 个请求

components
GET
200
document

登录表单发 POST

登录 Vibe

登录中…

点击瞬间 → POST /api/login

Network 面板看请求

Network
Fetch/XHR

list?page=1GET20064 ms

savePOST200120 ms

items/42PUT20098 ms

items/7DELETE20475 ms

curl 手动发请求

$ curl -X POST https://api.vibeui.dev/login \

-H "Content-Type: application/json" \

-d '{"email":"you@example.com","pwd":"123456"}'

{ "token": "eyJhbGciOi…" }

# 方法 -X、头 -H、体 -d，一封信的三要素

延伸阅读 · 权威出处

[HTTP 概述MDN ↗](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview)
