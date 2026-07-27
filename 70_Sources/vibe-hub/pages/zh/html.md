---
type: web_source
source_url: "https://vibe-hub.org/html"
title: "HTML"
language: zh
category: "html"
fetched_at: 2026-07-27T10:04:14+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←Markdown前端→

# HTML

你可能会说

AI 写出来的代码里一堆 < > 和英文单词，这些东西是干嘛的？

**HTML 是用标签描述网页内容结构、供浏览器渲染页面的标记语言**·它用标签标出标题、段落、图片、链接和按钮。例如，产品页面的内容层级由 HTML 组织；视觉样式通常交给 CSS，复杂交互需要 JavaScript。

也常被叫作*HTML 页面结构**超文本标记语言*

<html>
<head> *元信息*
<body>
<h1> *标题*
<p> *段落*
<a> *链接*

→

**小狸的主页**
我喜欢爬山和拍照。
看我的相册 →

### 什么时候用

- 把标题、图片和章节组织成清楚的网页结构

  一份给人看的项目报告清楚的标题、重点、图片和章节  
  让读者快速扫到真正关心的内容HTML 把内容变成阅读体验
- **制作可直接分享的页面**：官网、落地页、图文文章和报告，发一个网址就能在浏览器打开

  🔒 report.example.com/launch

  **新品发布报告**打开网页
- **加入图片、链接和交互**：页面可以跳转、填写表单、播放媒体或触发操作

  ▶ 视频↗ 链接填写表单

  页面可提供媒体、链接和表单等交互元素
- 把 Markdown 内容转成需要正式呈现的网页

  # 发布计划  
  - 本周上线→**发布计划**· 本周上线

### 什么时候不用

- 标签打开后没有正确关闭，容易破坏后续结构

  <div> 卡片  
  后续内容可能仍处于该元素内…缺少 </div> 会使 DOM 结构与预期不一致
- 标签交叉嵌套，浏览器难以得到预期结构

  <b><i>文字</b></i>
- 不要把页面正文放进文档元数据区域（head）；正常可见内容应组织在 body 中

  <head> 欢迎来到我的网站结构无效，浏览器可能按容错规则把内容移到 body
- 不要用文字处理软件另存 HTML，以免破坏标签结构

  Windex.html → 另存为 .docx

  DOCX 不是 HTML；浏览器不会将其作为网页结构解析

组成结构 · Anatomy

<a href="https://vibe.guide">点我看看</a>

1开始标签Opening Tag尖括号加标签名，告诉浏览器「这里开始」

2属性Attribute写在开始标签里的附加信息，如链接地址、图片路径

3内容Content两对尖括号之间的部分，改文案只动这里

4结束标签Closing Tag多一个斜杠，告诉浏览器「到这里结束」

常见变体 · Variants

div 通用容器div

<div> … </div>

没有更合适的语义标签时，用它组织内容和布局

h1~h3 与 pHeadings & p

<h1> <p>

标题和段落，文章的骨架

a 与 imgLink & Image

<a> <img>

a 跳网址，img 贴图片

button 与 inputButton & Input

<button> <input>

页面上能点能填的交互件

典型使用场景

AI 给你的 index.html

帮我做一个个人主页

好的，这是你的 index.html：

<h1>小狸的主页</h1>
<p>我喜欢爬山和拍照。</p>
<a href="/photos">看我的相册</a>

浏览器「查看源代码」

view-source:https://my-first-page.vercel.app

1  <h1>小狸的主页</h1>  
2  <p>我喜欢爬山和拍照。</p>  
3  <a href="/photos">看我的相册</a>

DevTools 检查元素

**小狸的主页**

我喜欢爬山和拍照。

看我的相册 →

<h1>…</h1>  
<p>…</p>  
<a>…</a>

常见标签速认小抄

常见标签速认

**<div>** 通用容器

**<p>** 段落

**<a>** 链接

**<img>** 图片

**<button>** 按钮

**<input>** 输入框

延伸阅读 · 权威出处

[用 HTML 组织内容MDN ↗](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content)[HTML：超文本标记语言MDN ↗](https://developer.mozilla.org/en-US/docs/Web/HTML)
