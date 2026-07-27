---
type: web_source
source_url: "https://vibe-hub.org/grid"
title: "网格布局 Grid"
language: zh
category: "grid"
fetched_at: 2026-07-27T10:04:00+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←弹性布局层级→

# 网格布局Grid

你可能会说

这些卡片排成整齐的格子，屏幕窄了自动变成两列。

**网格布局是一种用 CSS Grid 同时定义行和列，再把子元素放入二维格子的布局方式**·商品或模板列表需要随屏幕宽度自动换列时，可在父元素上定义 grid，再用 repeat(auto-fit, minmax(200px, 1fr)) 作为起点。最小宽度必须按标题、图片和操作仍能看清来调整；只有一条轴的简单排列用flex往往更直接。

先知道

[间距 **Space**](/space)

### 什么时候用

- **卡片墙等分多列**：repeat(3, 1fr) 可定义三列等宽轨道
- **自适应列数**：auto-fill 配合 minmax，可按容器宽度和内容最小宽度换列
- **页面骨架**：用列轨道明确侧栏与主要内容的宽度关系
- **使用 gap 管理格距**，避免逐个给网格项设置 margin

### 什么时候不用

- 只排**一行或一列**时，flex 通常更简单

  需要同时控制行列关系时，Grid 通常更直接
- 手写 **width: 33.33%** 建栅格：调整间距时需要额外计算

  33.33%33.33%33.33%
- 固定列数与列宽可能在**窄屏发生溢出**，应按内容与断点调整或使用自适应列
- 逐项使用 margin 制造格距，会增加**边缘项目的单独处理**

组成结构 · Anatomy

格子

1网格容器Container写上 display: grid 的父元素

2轨道Track定义出来的每一行、每一列

3单元格Cell行和列交叉出的格子

4网格间距Gap格子之间的缝，一行声明全管

常见变体 · Variants

等分列Repeat

卡片墙每列一样宽

自适应AutoFill

宽度变了列数自动增减

带间距Gap

使用 gap 统一管理行列间距

页面骨架TwoColumns

侧栏 + 内容这类整体框架

典型使用场景

图片卡片墙

repeat(3, 1fr) 三列等分

![](/assets/cover-mountain.png)

**山野徒步**

1.2k 收藏

![](/assets/cover-workspace.png)

**桌面美学**

856 收藏

![](/assets/photo-cat.png)

**猫咪日常**

2.4k 收藏

响应式商品列表

auto-fill + minmax，按可用宽度调整列数

![](/assets/slide-summer.png)

**夏日帆布包**

¥ 89

![](/assets/slide-city.png)

**城市明信片**

¥ 19

![](/assets/slide-forest.png)

**森林香薰**

¥ 129

仪表盘格子

grid-template-columns: 2fr 1fr

**访问趋势**

注册用户

**8,921**

转化率

**4.6%**

页面整体骨架

grid-template-columns: 120px 1fr

**控制台**

概览

项目

设置

**项目概览**

延伸阅读 · 权威出处

[CSS Grid 网格布局MDN ↗](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Grids)[CSS Grid 布局完整指南CSS-Tricks ↗](https://css-tricks.com/snippets/css/complete-guide-grid/)
