---
type: web_source
source_url: "https://vibe-hub.org/margin"
title: "外边距 Margin"
language: zh
category: "margin"
fetched_at: 2026-07-27T10:03:59+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←间距内边距→

# 外边距Margin

你可能会说

这个块和旁边那个太贴了，把它们之间撑开一点。

**外边距是元素边框外的透明空间，用来控制它与周围元素之间的距离**·两张卡片之间或标题与正文之间可用 margin 留空。普通块级兄弟的上下 margin 在特定文档流中可能合并；Flex、Grid 子项不会这样合并，父容器的边框或内边距也会影响父子外边距合并。

先知道

[间距 **Space**](/space)

卡片 A24卡片 B

### 什么时候用

- **拉开模块间距**：卡片之间、段落与标题之间
- **水平居中**：定宽容器写 margin: 0 auto
- **统一只加一侧**：比如都用 margin-bottom，间距好维护
- **处理图标与文字的光学对齐**：先检查 line-height、图标画布和 flex 对齐，必要时再做局部微调

  ★收藏

### 什么时候不用

- 普通块级元素的垂直 margin 可能**发生外边距折叠**，结果不一定是两者相加

  块 A · margin-bottom: 20↕ 合并成 20（不是 32）块 B · margin-top: 12
- 内容与边框之间的留白使用 padding

  margin ↔ 拉开外部距离padding ↔ 增加内部留白**内容**
- 滥用**负 margin**调整布局：意图不清，后续维护困难

  负 margin 让元素与前一部分重叠
- 用**空 div 加 margin**制造间距：改用 [间距 **Space**](/space) 的间距体系

  仅用于制造间距的空 div

组成结构 · Anatomy

内容

1外边距Margin边框以外的透明间隔，用于拉开相邻元素

2边框Border元素的边界，出了它就是 margin 的地盘

3内边距Padding内容和边框之间，带着背景色

4内容Content文字、图片真正待的地方

常见变体 · Variants

四边相同16px

margin: 16px

四周都要均匀留空时用

单边margin-bottom

标题正文

段落、字段只向下留距离

水平居中0 auto

auto

定宽容器在页面里居中

负外边距Negative

封面图标题条

微调对齐或故意叠一点层次

典型使用场景

卡片之间的间隔

**本周订单**+12%

1,284

↕

margin-bottom: 16px

**最近动态**

小狐狸 评论了「首页改版」

段落与标题的距离

**v2.4 更新日志**

margin-top: 8px

新增深色模式与组件搜索，修复了 12 个已知问题。

margin-top: 24px，新章节离远一点

**v2.3 更新日志**

定宽容器水平居中

**登录账号**

定宽卡片写 **margin: 0 auto**，两侧自动均分剩余空间

图标与文字的光学对齐

★收藏

✕ 图标高出 2px，没对齐

★收藏

✓ margin-top: 2px 微调后对齐

延伸阅读 · 权威出处

[margin 属性MDN ↗](https://developer.mozilla.org/en-US/docs/Web/CSS/margin)[掌握 margin 塌陷MDN ↗](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_box_model/Mastering_margin_collapsing)
