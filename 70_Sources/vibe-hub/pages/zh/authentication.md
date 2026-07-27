---
type: web_source
source_url: "https://vibe-hub.org/authentication"
title: "身份认证 Authentication"
language: zh
category: "authentication"
fetched_at: 2026-07-27T10:04:23+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←权限控制权限控制→

# 身份认证Authentication

你可能会说

怎么证明“你是你”？我要加登录功能。

**身份认证是验证用户所声明身份的机制**·用户用密码、验证码或第三方身份结果证明身份；验证通过后，应用通常另用 Cookie 携带 session ID，或让客户端携带 Token 延续登录状态。密码不能明文保存；登录后仍要由authorization判断用户能做什么。

先知道

[路由与端点 **Route & Endpoint**](/route)[数据库 **Database**](/database)[环境变量 **Env Var**](/env-var)

也常被叫作*登录认证*

邮箱**you@example.com**
密码**••••••••**
登录

证明身份*→*服务端核对*→*登录态

### 什么时候用

- 优先采用成熟身份服务或框架方案，不自己发明密码系统

  成熟方案提供常见认证能力

  密码 / 验证码→身份服务→安全会话
- 在 HTTPS 下为登录 Cookie 设置 Secure、HttpOnly，并按跨站需求选择 SameSite

  登录 Cookie 的常见保护

  HttpOnly**脚本不可读**Secure**只走 HTTPS**SameSite**限制跨站携带**
- 登录失败使用模糊提示，避免泄露账号是否存在

  失败提示不泄露账号状态

  不推荐**该邮箱不存在**
  *→*
  推荐**账号或密码错误**
- 退出登录时让服务端会话或令牌真正失效

  退出要让凭证真正失效

  会话有效→服务端撤销→再次请求 401

### 什么时候不用

- 数据库明文保存密码：一旦数据泄露，受影响记录的密码会直接暴露

  密码不能明文入库

  email: oil@example.compassword: **123456**

  数据库泄露后，明文存储的密码会直接暴露
- 把 JWT 当加密保险箱：内容通常只是编码，仍可能被读到

  JWT 内容通常可以解码查看

  header.payload.signaturepayload: { "email": "oil@example.com" }

  不要在里面放密码、令牌等敏感信息
- 只在前端 localStorage 里写 isLoggedIn=true

  改本地变量不能证明身份

  控制台修改**isLoggedIn = true**
  *→*
  服务端检查**没有有效会话 · 401**
- 登录接口没有限速：容易被批量猜密码

  缺少限速的登录接口

  1 分钟**10,000 次尝试**结果**可持续猜密码**

组成结构 · Anatomy

身份凭证*→*服务端验证*→*登录状态

1身份凭证Credential密码、一次性验证码或第三方平台返回的身份结果

2验证Verification服务端核对凭证、限速并处理失败，不相信前端自己宣布登录成功

3登录状态Session用安全 Cookie 或受保护 Token 让后续请求能证明是同一位用户

常见变体 · Variants

Cookie SessionCookie Session

`Set-Cookie: session=…`

传统网站常见，浏览器自动携带 Cookie

TokenBearer Token

`Authorization: Bearer …`

移动端或独立 API 常见

第三方登录OAuth Login

Continue with GitHub

把身份验证交给成熟平台

典型使用场景

邮箱密码登录

邮箱密码**验证成功后建立登录状态**

邮箱**oil@example.com**密码**••••••••**登录

Session**✓ 已建立**

短信或邮箱验证码

一次性验证码**验证码只在短时间内有效**

6 位验证码**482 913**

剩余时间**04:32**尝试次数**1 / 5**

验证

使用 GitHub / Google 登录

第三方登录**把身份验证交给成熟平台**

使用 GitHub 继续使用 Google 继续

平台返回身份结果，本站再建立自己的会话

退出与登录过期

退出与过期**会话失效后需重新认证**

点击退出→服务端撤销 Session→受保护请求 → 401

延伸阅读 · 权威出处

[HTTP 认证MDN ↗](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication)[登录表单最佳实践web.dev ↗](https://web.dev/articles/sign-in-form-best-practices)[身份认证安全清单OWASP ↗](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)[密码存储安全清单OWASP ↗](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
