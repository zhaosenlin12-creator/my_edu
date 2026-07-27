---
type: web_source
source_url: "https://vibe-hub.org/padding"
title: "内边距 Padding"
language: zh
category: "padding"
fetched_at: 2026-07-27T10:03:59+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←外边距弹性布局→

# 内边距Padding

你可能会说

字都顶到盒子边上了，让内容和边框之间留点空。

**内边距是元素内容与边框之间的留白，用来让文字或图标不紧贴组件边缘**·按钮文字四周、输入框内容与边框之间的空间通常用 padding 设置，它会带着元素的背景色并计入元素的可见尺寸。需要把组件彼此拉开时用margin；不要用外边距假装按钮内部留白，否则点击区域不会跟着变大。

先知道

[间距 **Space**](/space)

内容

### 什么时候用

- [卡片 **Card**](/card) 内容与边框之间保留一致的**内部间距**
- [按钮 **Button**](/button) 的 padding 会影响**可点击区域**与文字周围的空间

  过小合适
- [输入框 **Input**](/input) 文字不贴边：左右 padding 要结合字号、控件高度和触控目标测试

  间距过小保留内边距
- 容器内**统一留白**：一处 padding 管住所有内容

### 什么时候不用

- 与外部元素之间的距离使用 margin

  margin ↔ 拉开外部距离padding ↔ 增加内部留白**内容**
- padding 过小会让**内容紧贴边框**，降低可读性和点击准确性
- 不要用 padding 模拟文字行距，行距应由 line-height 控制

  第一行第二行
- padding 过大导致**内容可用空间不足**，比例失衡

组成结构 · Anatomy

内容

1边框Borderpadding 的外边界

2内边距Padding带着元素背景色的留白区

3内容Content被 padding 护在中间的内容

常见变体 · Variants

均匀16px

*内容*

卡片、面板的默认留白

按钮式8px 16px

*按钮*

横向比纵向多，按钮、标签常用

非对称Asymmetric

*卡片*

某一侧要更多呼吸感时

典型使用场景

卡片内容留白

padding: 16px

本周访问量

48,210

▲ 较上周 +8.2%

按钮点击区域

保存

✕ 点击区域只有一丁点

保存

✓ padding: 10px 26px，好按

输入框文字留白

✕ padding 太小，内容紧贴边框

✓ 左右 14px，文字不贴边

弹窗内容留白

padding: 20px
**开启消息通知？**

有新评论时第一时间提醒你。

稍后开启

延伸阅读 · 权威出处

[padding 属性MDN ↗](https://developer.mozilla.org/en-US/docs/Web/CSS/padding)
