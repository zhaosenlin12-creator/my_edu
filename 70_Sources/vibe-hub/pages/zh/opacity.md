---
type: web_source
source_url: "https://vibe-hub.org/opacity"
title: "透明度 Opacity"
language: zh
category: "opacity"
fetched_at: 2026-07-27T10:04:01+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←阴影渐变→

# 透明度Opacity

你可能会说

这张图太抢戏了，把它调得半透明一点。

**透明度是通过 opacity 同时降低元素及其全部子内容可见程度的 CSS 属性**·淡入提示框或弱化非当前内容时可设置 opacity。只想让背景半透明应改用 rgba；opacity: 0 的元素仍可能占位置或被点击，隐藏交互还需处理焦点。

100%50%15%

### 什么时候用

- **禁用态变淡**：[按钮 **Button**](/button)、[输入框 **Input**](/input) 不可用降到 0.4 左右

  可用禁用
- **悬停反馈**：次要图标平时 0.5，悬停恢复 1

  ✎→✎
- **半透明遮罩**：[弹窗 **Modal**](/modal) 背后压暗但隐约可见

  弹窗
- **淡入淡出**：配 transition 是最常用的动效

### 什么时候不用

- 只需让**背景透明**时使用 rgba；opacity 会同时降低内容透明度

  opacity .4rgba .4
- 正文透明度过低会降低**文字对比度**，影响阅读

  正文透明度过低，文字对比度不足。
- 不要把 opacity: 0 当成移除元素，它仍会占位并可能响应点击

  这里有个 opacity: 0 的按钮，还点得到
- **多层半透明元素叠加**会改变最终颜色和对比度，应检查合成结果

  多层透明度会叠加，实际颜色更难预测

组成结构 · Anatomy

opacity: 0.45背景透出来

1下层背景Backdrop透过来看见的东西

2半透明元素Elementopacity 小于 1，整体变淡

3透出效果See-through透明度越低，背景透得越多

常见变体 · Variants

禁用0.4

禁用

不可点的按钮、输入框

悬停0.8

悬停

次要图标平时淡一点

遮罩0.5

遮罩

弹窗背后压暗页面

完全隐藏0

0

占位做淡入动画时使用

典型使用场景

禁用按钮

opacity: 0.4 = 禁用
邮箱

取消
提交

悬停反馈

**设计规范.md**
✎
⧉
★

次要图标平时 opacity 0.45，悬停的那个恢复 1

弹窗半透明遮罩

遮罩 rgba(.32)，背景隐约可见

✓ 保存成功

淡入淡出动画

已复制链接
→
已复制链接
→
已复制链接
transition: opacity .2s，淡入

延伸阅读 · 权威出处

[opacity 属性MDN ↗](https://developer.mozilla.org/en-US/docs/Web/CSS/opacity)
