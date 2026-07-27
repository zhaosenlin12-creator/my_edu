---
type: web_source
source_url: "https://vibe-hub.org/card-grid-layout"
title: "卡片网格布局 Card Grid"
language: zh
category: "card-grid-layout"
fetched_at: 2026-07-27T10:04:09+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←文档三栏布局居中窄栏布局→

# 卡片网格布局Card Grid

你可能会说

内容做成一排排卡片，宽了多放几列，窄了自动换行。

**卡片网格布局是一种用规则行列排列同类卡片，并随可用宽度换行的页面结构**·作品、商品和模板列表可将每个项目做成结构相近的[卡片 **Card**](/card)，再用 Grid 自动排布。列数和最小卡片宽度要按标题、图片和操作仍能显示来决定；内容差异很大时，不必强求所有卡片完全等高。

先知道

[卡片 **Card**](/card)[网格布局 **Grid**](/grid)

### 什么时候用

- **卡片结构一致**：相同信息放在相同位置，便于快速比较，见 [卡片 **Card**](/card)

  **无线耳机**¥ 299

  **机械键盘**¥ 199
- 使用 Grid 的自动列宽，让卡片随容器换行
- **间距统一**：gap 一处管所有格距，见 [间距 **Space**](/space)
- **同行高度拉齐**：卡片一样高，墙面才整齐

### 什么时候不用

- 列数写死 repeat(4, 1fr)，**窄屏直接溢出**
- 未控制卡片高度：**网格行高不齐**
- 每张卡片结构不同：**列表扫描效率降低**
- 格距**缺少统一规则**：使用一处 gap 管理

  ✎★⬇⋯

组成结构 · Anatomy

卡片

1网格容器Containerdisplay: grid，定义列和间距

2卡片Card结构一致的成员，同构才好扫读

3网格间距Gap格子之间的缝，一处声明全管

常见变体 · Variants

自适应列AutoFill

卡片有合理最小宽度、列数需要随容器变化时

固定两列Two Cols

卡片内容多，需要大预览

固定三列Three Cols

内容宽度稳定的后台列表

典型使用场景

作品集展示

![](/assets/cover-mountain.png)

山野露营 App

UI 设计 · 2025

![](/assets/cover-workspace.png)

效率工具官网

网页设计 · 2025

![](/assets/photo-cat.png)

宠物社区小程序

产品设计 · 2024

商品列表

🎧

降噪耳机 Pro

**¥ 899**已售 2.3 万

⌨️

机械键盘 87 键

**¥ 349**已售 8,600

💡

智能护眼台灯

**¥ 199**包邮

模板市场

SaaS 落地页

Landing · 免费使用

活动报名页

Event · 免费使用

博客主题

Blog · ¥ 29使用

图片素材墙

筛选

![](/assets/slide-summer.png)![](/assets/slide-city.png)![](/assets/slide-forest.png)![](/assets/cover-mountain.png)

「夏日」相关素材 12,408 张 · 按热度排序

延伸阅读 · 权威出处

[卡片：UI 组件定义NN/g ↗](https://www.nngroup.com/articles/cards-component/)[CSS 网格布局中的自动放置MDN ↗](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout/Auto-placement_in_grid_layout)
