---
type: web_source
source_url: "https://vibe-hub.org/url"
title: "URL"
language: zh
category: "url"
fetched_at: 2026-07-27T10:04:10+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←DNSHTTP→

# URL

你可能会说

地址栏里那一长串是什么？我想让每个页面都有自己固定的地址。

**浏览器地址栏和链接里，用来找到具体页面或文件的地址**·例如，https://vibe-hub.org/api 指向 VibeHub 的 API 词条页；站内的相对 URL 可以只写 /api，它会从当前网站继续定位。URL 还可以带筛选条件或页内位置，分享前要检查其中是否含有 Token、密码或个人信息。

先知道

[域名 **Domain**](/domain)

也常被叫作*网址**网页地址*

https://vibeui.dev/components/button?tab=demo#anatomy

协议域名路径参数锚点

### 什么时候用

- 分享时**复制完整链接**，别人打开就是同一页

  https://vibe-ui.dev/x/8fk2复制

  复制成功
- 用 **path** 表达页面位置：/components/button 一看就懂

  vibeui.dev/components/button路径定位站点中的资源或页面
- 搜索、筛选条件放 **query**：链接可分享、可复现

  /search?q=按钮&sort=hot查询参数随链接保存筛选或页面状态
- 长文档用 **#hash 锚点**，打开直接滚到那一节

  /button#anatomy片段标识可定位到页面中的指定位置

### 什么时候不用

- 随手转发带有**登录令牌或密钥的链接**：收到链接的人可能获得你的访问权限

  ?token=sk-live-8f2k…链接可能进入历史、日志和转发记录，不应包含密钥
- 拼 URL 时**中文和空格不编码**：链接断成一截一截

  /search?q=我的 页面空格等字符需要按 URL 规则编码
- 分享时**只复制域名丢了 path**：对方通常只会打开站点首页

  vibeui.dev
- 把数据塞在 **# 后面传给后端**：片段标识不会随 HTTP 请求发给服务器

  /pay#amount=999# 后面的内容不会发给服务器

组成结构 · Anatomy

https://vibeui.dev/components/button?tab=demo#anatomy

1协议Protocolhttps://，送信方式；现在是 https 的天下

2域名Domain寄到哪个小区，见 domain；靠 dns 翻译成 IP

3路径Path小区里哪栋哪室：/components/button 就是某个页面

4查询参数Query? 后面 key=value 的留言条，& 连接多条，会发给服务器

5锚点Hash# 后面的页内定位，只在浏览器里生效，不发给服务器

常见变体 · Variants

绝对地址Absolute URL

https://vibeui.dev/components/button

包含协议和域名，适合外部分享或跨站引用

相对路径Relative Path

/components/button

站内跳转，换域名也不用改

锚点链接Anchor Link

#anatomy

只定位到当前页的某一节

典型使用场景

地址栏里的完整网址

🔒
https://**vibeui.dev**/components/button

按钮与基础样式

按钮 Button

页面上最重要的动作，交给按钮

主要按钮次要按钮

搜索结果页的参数

🔍
按钮

vibeui.dev/search?q=按钮&cat=通用

找到 3 个相关条目

**按钮 Button**

提交表单、触发动作、确认危险操作…

**开关 Switch**

状态立即生效的开关…

分享弹窗复制链接

分享这个条目

https://vibeui.dev/components/button#anatomy

生成海报
复制链接

✓ 已复制到剪贴板

文档页锚点定位

本页目录

什么时候用

场景

组成结构

变体

/components/button#anatomy

**组成结构 · Anatomy**

延伸阅读 · 权威出处

[什么是 URL？MDN ↗](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_URL)
