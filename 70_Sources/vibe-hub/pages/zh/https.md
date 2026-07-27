---
type: web_source
source_url: "https://vibe-hub.org/https"
title: "HTTPS"
language: zh
category: "https"
fetched_at: 2026-07-27T10:04:11+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←HTTPCDN→

# HTTPS

你可能会说

浏览器说我的网站“不安全”，地址栏那个小锁怎么弄出来？

**地址栏里以 https:// 开头、用于保护设备与网站之间数据的加密连接**·例如，用户登录时，HTTPS 会降低密码在传输途中被同一网络中的其他人读取或篡改的风险。它只保护连接，不代表网站内容、公司身份或交易一定可信。

先知道

[HTTP](/http)[域名 **Domain**](/domain)

也常被叫作*安全连接**HTTPS 连接*

🔒 https://vibeui.dev 加密连接

⚠️ http://old-site.com 不安全

浏览器界面会因版本而异；关键是确认连接与证书状态

### 什么时候用

- 上线**默认开 HTTPS**：许多托管平台可自动申请和续期证书，仍要检查域名绑定、续期状态与重定向

  强制 HTTPS

  证书平台自动签发（Let's Encrypt）
- 小锁表示**到该域名的连接受 TLS 保护**；它不评价网站内容、经营者或交易安全

  🔒vibeui.dev

  加密连接，并校验证书是否匹配当前域名
- 页面是 https，里面的**图片、脚本也要 https** 引入

  <img src="https://cdn.vibeui.dev/a.png">
- 涉及**登录、支付**的页面，https 是底线

  🔒••••••••

  密码在加密通道里传输

### 什么时候不用

- 公开网站仍使用 **HTTP**：传输未受 TLS 保护，浏览器也可能显示不安全提示

  不安全http://old-site.com

  浏览器会提示连接未加密，用户无法确认传输是否受保护
- https 页面里引 **http 资源**：浏览器会拦截许多主动混合内容，其他资源也可能被升级或警告；应统一使用 HTTPS

  <img src="http://…">
- **证书过期未续期**：浏览器会显示警告，并可能阻止用户继续访问

  证书已过期 14 天
- 看到「不是私密连接」**还继续输密码**：密码可能被窃取

  ⚠ 您的连接不是私密连接

  仍然继续前往（不安全）

组成结构 · Anatomy

🔒 https://vibeui.dev**证书**Let's Encrypt有效期至 2026-10

1连接状态Connection Status浏览器对当前 TLS 连接与证书的状态提示，不是对网站信誉的背书

2证书Certificate证书将域名公钥绑定到签发信息；常见 DV 证书只验证域名控制权，自动签发也需要正确配置

3加密通道EncryptionTLS 用加密和完整性校验保护传输；终端设备或网站本身仍可能有风险

常见变体 · Variants

DV 证书Domain Validated

🔒 vibeui.dev DV

只验证域名，托管平台免费自动签

OV / EV 证书Organization Validated

🔒 bank.example OV

额外验证企业身份，银行政务常用

典型使用场景

地址栏小锁与证书

🔒
vibeui.dev

连接是安全的

你与此网站之间传输的信息已加密

颁发给vibeui.dev

颁发者Let's Encrypt

有效期至2026-10-18

托管平台自动开 HTTPS

**域名 vibeui.dev**
HTTPS 已启用

SSL 证书
Let's Encrypt · 自动续期

强制 HTTPS

下次自动续期
2026-09-18

http 站点的警告页

⚠️

您的连接不是私密连接

攻击者可能会试图从 old-site.com 窃取您的信息  
（例如密码、通讯内容或信用卡信息）

返回安全页面
仍然继续（不安全）

混合内容被拦截

🔒
vibeui.dev

Console

✕ Mixed Content: 此页面通过 HTTPS 加载，

但请求了不安全的图片 http://img.old.com/a.png，

该请求已被阻止。

→ 把图片地址改成 https:// 即可

延伸阅读 · 权威出处

[HTTPS 词汇表MDN ↗](https://developer.mozilla.org/en-US/docs/Glossary/HTTPS)[为什么 HTTPS 很重要web.dev ↗](https://web.dev/articles/why-https-matters)
