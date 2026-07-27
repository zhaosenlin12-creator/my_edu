---
type: web_source
source_url: "https://vibe-hub.org/overflow"
title: "内容溢出 Overflow"
language: zh
category: "overflow"
fetched_at: 2026-07-27T10:04:12+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←盒模型间距→

# 内容溢出Overflow

你可能会说

这张卡片的内容底部被遮住了，帮我检查是不是纵向溢出，别让按钮被裁掉。

**Overflow 是内容超过容器可用空间时，浏览器决定如何显示、裁切或滚动的规则。**·例如卡片设置固定高度后，较长内容可能越过底边；若祖先使用 `overflow: hidden`，底部说明和按钮会直接消失。Overflow 可以发生在横向或纵向，它处理“放不下以后怎么办”，不是用来掩盖本应重新排版的布局问题。

先知道

[盒模型 **Box Model**](/box-model)

也常被叫作*CSS Overflow*

延伸阅读 · 权威出处

[overflowMDN ↗](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
