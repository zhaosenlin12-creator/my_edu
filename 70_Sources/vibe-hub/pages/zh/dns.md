---
type: web_source
source_url: "https://vibe-hub.org/dns"
title: "DNS"
language: zh
category: "dns"
fetched_at: 2026-07-27T10:04:10+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←域名URL→

# DNS

你可能会说

买了名字为什么还要“解析”？帮我把名字指到我的服务器上。

**互联网的地址簿，把域名查成浏览器能找到网站的地址**·例如，输入 vibe-hub.org 后，DNS 会先找到它对应的服务地址，浏览器才能连接。修改 DNS 后，旧地址可能仍被缓存一段时间，所以不同地区不一定同时更新。

先知道

[域名 **Domain**](/domain)

也常被叫作*DNS 解析**域名系统*

🌐浏览器查询  
vibeui.dev

→

📒DNS 解析器返回记录  
76.223.54.1

→

🖥️目标服务浏览器按记录  
建立连接

### 什么时候用

- 需要把名称指向 IPv4 地址时配置 **A 记录**

  A@76.223.54.1

  A 记录把名称指向 IPv4 地址
- 需要把一个名称指向另一个域名时配置 **CNAME**

  CNAMEwwwvibeui.dev

  CNAME 把一个名称指向另一个域名
- 改完解析先看**TTL 与现有缓存**，再从外部递归解析器复查；不同地点看到新记录的时间可能不同

  TTL 600缓存上限 10 分钟
- 网站无法访问时，先用 dig、nslookup 或在线工具**核对外部解析结果**

  $ dig vibeui.dev;; ANSWER: 76.223.54.1

### 什么时候不用

- 同一个名称配置 **CNAME 和其他数据记录**：标准 DNS 中 CNAME 不能与其他记录并存；托管商的 ALIAS/扁平化规则另看文档

  Awww → 76.223.54.1

  CNAMEwww → vibeui.dev

  同一名称的 CNAME 通常不能与 A 记录并存
- 旧缓存尚未到期时**反复修改记录**，不同解析器可能看到多套结果，会增加排查难度

  改成 A又改回多次变更

  缓存尚未到期时反复改动，会让排查难以对应到单一配置
- 计划切换服务前**没有提前调整 TTL 并等待旧缓存过期**：原记录可能继续被使用；稳定记录使用较长 TTL 本身并非错误

  TTL 86400最长缓存 1 天

  旧记录可能被缓存较久，变更后的收敛时间也会更长
- **记录值填写错误**：请求可能到达错误服务或无法访问，应复制核对并从外部复查

  A76.223.54.12

  地址填写错误会让请求到达错误服务或无法访问

组成结构 · Anatomy

🌐浏览器→📒DNS 服务器→A 记录  
vibeui.dev → IP→76.223.54.1

1递归解析器Resolver浏览器通常把查询交给递归解析器；它会查缓存，必要时向权威 DNS 查询

2权威 DNSAuthoritative DNS为域名保存正式记录的服务器；递归解析器从这里取得可缓存的答案

3解析记录Record你在控制台登记的那一行：A 记 IP，CNAME 记另一个域名

4IP 地址IP Address查到的门牌号，浏览器拿它去敲服务器的门

常见变体 · Variants

A 记录A Record

A @ → 76.223.54.1

域名指向 IPv4 地址，最常用

CNAMECNAME

CNAME www → vibeui.dev

域名指向另一个域名，托管常用

AAAAAAAA

AAAA @ → 2606:…:1

域名指向 IPv6 地址

TXTTXT

TXT @ → "verify=8f2k…"

验证域名所有权、配置邮箱时用

典型使用场景

DNS 控制台加记录

**DNS 解析 · vibeui.dev**
＋ 添加记录

类型主机记录记录值TTL

A@76.223.54.1600

CNAMEwwwvibeui.dev600

CNAMEblogvibeui.dev600

终端 dig 查解析

$ dig vibeui.dev

;; QUESTION SECTION:

;vibeui.dev.   IN  A

;; ANSWER SECTION:

vibeui.dev.  600  IN  A  76.223.54.1

;; Query time: 23 msec

修改解析等生效

修改解析记录

类型A

记录值

TTL
秒；较小 TTL 便于切换，但不清除已有缓存

保存，约 10 分钟生效

换服务器改指向

迁移到新服务器

旧：A @ → 76.223.54.1已停用

↓ 修改记录值

新：A @ → 76.223.105.8生效中

在旧记录缓存结束前，部分用户仍可能访问旧服务器；确认流量完成迁移后再关闭旧服务

延伸阅读 · 权威出处

[DNS 词汇表MDN ↗](https://developer.mozilla.org/en-US/docs/Glossary/DNS)
