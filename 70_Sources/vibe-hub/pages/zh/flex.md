---
type: web_source
source_url: "https://vibe-hub.org/flex"
title: "弹性布局 Flex"
language: zh
category: "flex"
fetched_at: 2026-07-27T10:03:59+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←内边距网格布局→

# 弹性布局Flex

你可能会说

把这几个按钮排成一行，间距均匀，还能垂直居中。

**弹性布局是一种用 Flexbox 沿一条主轴排列和对齐直接子元素的 CSS 布局方式**·导航链接横排、按钮组居中或图标与文字并排时，可在父元素上设置 display: flex。justify-content 控制主轴分布，align-items 控制交叉轴对齐；它适合一行或一列的关系，需要同时规划多行和多列时应先考虑grid。

先知道

[间距 **Space**](/space)

### 什么时候用

- **导航横排**：菜单项、工具栏、按钮组排一行

  首页组件术语
- **竖向堆叠**：[表单 **Form**](/form) 字段、列表项用 column

  姓名邮箱flex-direction: column 改为垂直排列
- **水平垂直居中**：登录区、空状态等单一内容可在明确尺寸的容器中居中

  登录主轴与交叉轴都设为 center
- **两端对齐**：标题靠左、操作靠右用 space-between

  项目动态查看全部

### 什么时候不用

- 用 **float + clearfix** 构建常规一维排列：需要额外清除浮动，Flex 通常更清晰

  左浮动右浮动
- **多行多列对齐**的卡片墙通常使用 grid

  需要同时控制行列关系时，Grid 通常更直接
- 子元素宽度全写死还不换行，**直接溢出容器**

  固定宽度且禁止换行时，子元素可能溢出容器
- 未设置 flex-wrap: wrap：内容变多时会被压缩或溢出

  标签一标签二标签三标签四标签五标签六

组成结构 · Anatomy

项目主轴 →交叉轴 ↓

1弹性容器Container写上 display: flex 的那个父元素

2弹性项目Item容器里的直接子元素

3主轴Main Axis项目的排列方向，justify-content 管它

4交叉轴Cross Axis和主轴垂直，align-items 管它

常见变体 · Variants

横排Row

默认主轴为水平方向；内容需要沿同一行流动时选择

竖排Column

主轴改为垂直方向；内容顺序应自上而下时选择

居中Center

在容器尺寸明确时，把两条轴上的剩余空间分配到内容两侧

两端对齐SpaceBetween

把主轴剩余空间放到项目之间；适合两端需要贴边的排列

典型使用场景

导航栏横排

display: flex，一排横着站

![](/assets/logo.svg)**Vibe 图鉴**
组件
术语
场景

![](/assets/avatar-robot.png)

logo、链接、头像都交给 flex 横排对齐

表单字段竖排

flex-direction: column

昵称
邮箱
保存资料

标题与操作分居两端

justify-content: space-between

**项目动态**
查看全部 →

![](/assets/avatar-fox.png)小狐狸 更新了「首页改版」
10:24

内容垂直居中

align-items + justify-content: center

![](/assets/empty-box.png)

暂无消息，内容在两条轴上居中

延伸阅读 · 权威出处

[Flexbox 弹性布局MDN ↗](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Flexbox)[Flexbox 完整指南CSS-Tricks ↗](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
