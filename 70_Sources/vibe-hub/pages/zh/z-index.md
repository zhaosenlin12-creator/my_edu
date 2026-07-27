---
type: web_source
source_url: "https://vibe-hub.org/z-index"
title: "层级 Z-Index"
language: zh
category: "z-index"
fetched_at: 2026-07-27T10:04:01+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←网格布局吸顶→

# 层级Z-Index

你可能会说

那个弹窗被别的内容挡住了，让它显示在最上面。

**决定互相重叠的页面元素谁显示在上面**·例如，下拉菜单被横幅挡住时，要同时检查菜单和横幅所在的父级；只把 z-index 改成 99999，也可能仍然无效。项目里应使用少量固定层级，避免数字越堆越乱。

先知道

[定位 **Position**](/position)

z: 1
z: 2
z: 3

### 什么时候用

- [弹窗 **Modal**](/modal) 盖遮罩、遮罩盖页面：**三层各司其职**

  确认删除这个项目？

  取消确认删除
- **吸顶导航**：滚动内容从它底下过

  导航 · z-index: 100
- [下拉菜单 **Dropdown**](/dropdown)、[文字提示 **Tooltip**](/tooltip) **浮在卡片上**不被盖住

  全部状态全部状态进行中
- 为内容、吸顶、浮层和弹窗建立少量统一层级

  内容 1吸顶 100浮层 1000弹窗 10000

### 什么时候不用

- 没先确认**定位、flex/grid 子项和层叠上下文**，只改数字通常没用

  z-index: 99 但没设 position
- 仅靠增大 z-index 数值解决遮挡：层级规则会失去可维护性

  z-index: 9999z-index: 99999z-index: 999999
- 指望子元素 z-index 9999 **翻出父级**：层级逃不出父级的上下文

  父级 z-index: 1子级 9999z-index: 2
- 用 z-index 解决**调一下 DOM 顺序就行**的问题

  代码中较早出现的内容用 z-index 强行改变遮盖顺序若视觉顺序应与文档顺序一致，应先调整 DOM 结构

组成结构 · Anatomy

z-index: 1z-index: 2大的在上面

1下层元素Bottomz-index 较小，被压在下面

2上层元素Topz-index 较大，盖在上面

3层级值Z-Index用于定位元素，以及 flex/grid 子项的层叠数值；还要看它所在的层叠上下文

常见变体 · Variants

内容叠放1 ~ 10

12

卡片角标、头像轻微叠压

吸顶导航100

100

固定栏压住滚动内容

浮层1000

页面1000

下拉、气泡、文字提示

弹窗遮罩10000

10000

示例档位：让模态层高于普通页面浮层

典型使用场景

弹窗盖过页面

页面 z-index: 1

遮罩 z-index: 1000

弹窗 z-index: 1001
**确认退出登录？**

取消退出

吸顶导航

**文档中心**
指南
API
z-index: 100

同一层叠规则里，导航层级高于滚动内容

下拉菜单浮层

**任务列表**
进行中 ▾

z-index: 1000

全部

进行中 ✓

已完成

下拉浮在卡片上面，不被盖住也不被裁

右下角悬浮按钮

＋
z-index: 10

延伸阅读 · 权威出处

[z-index 属性MDN ↗](https://developer.mozilla.org/en-US/docs/Web/CSS/z-index)[层叠上下文MDN ↗](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_positioned_layout/Stacking_context)
