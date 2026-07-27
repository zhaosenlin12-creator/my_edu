---
type: web_source
source_url: "https://vibe-hub.org/selection"
title: "选中高亮 Selection"
language: zh
category: "selection"
fetched_at: 2026-07-27T10:04:08+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←鼠标指针悬停→

# 选中高亮Selection

你可能会说

用户划选文字时的底色，想换成品牌色。

**选中高亮是用户拖选网页文字后，浏览器为选区显示的前景色和背景色**·可用 ::selection 为文章或说明文字设置选区颜色，并在不同主题下检查对比度。它可以适度使用品牌色，但不能影响文字辨认；user-select: none 只适合拖拽手柄等确实不应被选中的元素，正文和说明通常应允许复制。

默认色

拖选一段文字，中间这段就是选中高亮，底色由浏览器决定。

品牌色

拖选一段文字，中间这段就是选中高亮，和品牌色呼应。

### 什么时候用

- 没有品牌化需求时，浏览器默认选中样式通常已经清楚可见

  拖选一段文字，这一段被选中了，颜色由浏览器和系统决定。
- 换成**品牌色**呼应：可在合适的作用域用 ::selection 定义；全局规则会影响所有可选文本，先确认范围

  同一段话，选中色换成品牌色，先确认对比度与作用范围。
- 定制时**保证对比度**：深底配白字，浅底配深字

  深底白字 ✓浅底深字 ✓
- 拖拽手柄等纯交互元素可加 **user-select: none**：防误选

  保存user-select: none

### 什么时候不用

- 选中色**对比度过低**：用户难以识别选中内容

  这段话中有一部分被选中，但状态不明显。
- 拖动按钮等**纯操作元素时意外选中文字**：可在明确范围内防止误选

  按钮文字被选中拖动点击区域时意外选中了按钮文字
- 一个页面使用**多种选中色**：会削弱选中状态的一致性

  选区选区选区
- 给**正文**设置 user-select: none，会阻止用户选中和复制内容

  正文设置了 user-select: none，用户无法选中并复制需要的内容。

组成结构 · Anatomy

前面这段没选中，这段被拖选，后面也没选中

1普通文本Text没被选中的部分，保持原样

2选区Selection鼠标拖选覆盖的那一段范围

3高亮底色Background::selection 的 background

4高亮文字色Color::selection 的 color，和底色对比要够

常见变体 · Variants

默认Default

选中高亮

没有品牌化需求时保留浏览器默认样式

品牌色Brand

选中高亮

低成本呼应品牌色的精致感

防误选NoSelect

拖拽手柄 · user-select: none

确实不应被选中的拖拽手柄或纯交互装饰

典型使用场景

文章正文选中复制

把提示词写好的三个习惯

写提示词时，先说明目标，再补充必要背景。模型只能依据当前提供的信息响应，因此关键约束也要明确写出。

📋 复制

代码片段选中

1.card {

2  border-radius: 12px;

3  padding: 16px;

4}

按钮拖拽防误选

保存草稿
✕ 拖动时意外选中按钮文字

保存草稿
✓ user-select: none 防误选

品牌官网的文本选中

MUSEON STUDIO

让好想法被世界看见

用 ::selection 统一设置选区配色

延伸阅读 · 权威出处

[::selection 伪元素MDN ↗](https://developer.mozilla.org/en-US/docs/Web/CSS/::selection)[user-select 属性MDN ↗](https://developer.mozilla.org/en-US/docs/Web/CSS/user-select)
