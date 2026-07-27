---
type: web_source
source_url: "https://vibe-hub.org/color-picker"
title: "颜色选择器 ColorPicker"
language: zh
category: "color-picker"
fetched_at: 2026-07-27T10:03:49+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←表单表单标签→

# 颜色选择器ColorPicker

你可能会说

主题色想让用户自己挑，别写死。

**颜色选择器是让用户查看并选择颜色值的表单控件**·主题设置、图表标记和画板工具可用它选择颜色。除色盘外应显示可复制的色值；文字或图标仍必须满足足够对比度。

也常被叫作*色彩选择器*

HEX   #7257D8

容易混淆？这样区分

颜色选择器ColorPicker**≠**[选择器 **Select**](/select)

color-picker 会同时显示颜色预览和精确色值；[选择器 **Select**](/select) 只从固定的文字选项中选择一个值。

### 什么时候用

- **主题与品牌设置**：让用户选主色或强调色

  品牌色
- **画板和标注工具**：直接预览笔刷、填充或描边
- **图表系列颜色**：给每组数据一个可辨认的色彩

### 什么时候不用

- 只有两个明确选项时：使用色块按钮即可

  品牌色
- 只用颜色表达信息：同时提供文字或图标
- 未说明对比度要求，导致浅色文字难以阅读

组成结构 · Anatomy

#7257D8⌄

1颜色预览Swatch先让用户看见当前颜色

2颜色值Value提供可复制、可精确编辑的色值

3展开入口Trigger打开色盘或预设色列表

常见变体 · Variants

预设色Swatches

品牌只允许少量颜色时

完整色盘Palette

需要自由选择颜色时

带色值With value

#7257D8

设计或开发需要精确交接时

典型使用场景

品牌主题设置

**界面主题**

强调色#7257D8

白板笔刷颜色

**✎**

图表系列配色

延伸阅读 · 权威出处

[颜色类型输入框MDN ↗](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/color)
