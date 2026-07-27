---
type: web_source
source_url: "https://vibe-hub.org/centering"
title: "居中 Centering"
language: zh
category: "centering"
fetched_at: 2026-07-27T10:04:09+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←定位盒模型→

# 居中Centering

你可能会说

这个框帮我水平垂直都居中——怎么就那么难？

**居中是把文字、元素或一组内容在容器的水平、垂直或两条轴上对齐到中间的布局方式**·按钮组可用flex居中，网格单元可用grid的 place-items。文字和定宽块有各自做法；absolute 加 transform 适合浮层，不应作为普通内容的默认方案。

先知道

[弹性布局 **Flex**](/flex)[网格布局 **Grid**](/grid)

flex

grid

absolute

### 什么时候用

- 父容器使用 Flex 时，在两条轴上设置居中

  登录主轴与交叉轴都设为 center
- 父容器使用 Grid 时，可以用 place-items 居中
- **文字水平居中**：text-align: center，只管水平方向

  标题水平居中
- **定宽块级元素水平居中**：margin: 0 auto，见 margin

### 什么时候不用

- 为普通布局优先用 **flex 或 grid**：table/table-cell 仍可用于兼容旧实现或表格语义，不必一概否定
- 不要用多处 **margin 固定偏移**定位：容器宽度变化时会失准
- 绝对定位居中还要用 transform 修正元素自身尺寸

  只写 left/top: 50%，元素从中心往右下长
- 块级元素撑满宽度时，自动外边距看不出居中效果

  宽度没定死，margin: 0 auto 居不了中

组成结构 · Anatomy

元素主轴：justify-content: center交叉轴：align-items: center

1容器Container写上 display: flex 的父元素，居中都是它说了算

2居中元素Centered Item被放到正中间的那个子元素

3主轴对齐Justify Contentjustify-content: center，管主轴方向的居中

4交叉轴对齐Align Itemsalign-items: center，管交叉轴方向的居中

常见变体 · Variants

Flex 居中Flex

普通容器中最常用的居中方法

Grid 居中Grid

父元素已经是 grid 时最省字

绝对定位居中Absolute

老代码里常见，能认出来就行

典型使用场景

登录卡片放页面正中

登录 Vibe

登 录

空状态插图居中

![](/assets/empty-box.png)

暂无收藏

去逛逛，把喜欢的组件收藏起来

标题文字居中

新功能上线

像聊天一样写前端

描述你想要的效果，剩下的交给 AI

立即体验
查看演示 →

定宽容器水平居中

为什么居中这么难？

延伸阅读 · 权威出处

[CSS 居中完全指南CSS-Tricks ↗](https://css-tricks.com/centering-css-complete-guide/)
