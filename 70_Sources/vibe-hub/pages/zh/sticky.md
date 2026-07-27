---
type: web_source
source_url: "https://vibe-hub.org/sticky"
title: "吸顶 Sticky"
language: zh
category: "sticky"
fetched_at: 2026-07-27T10:04:08+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←层级定位→

# 吸顶Sticky

你可能会说

往下滚的时候，让导航栏一直钉在页面顶部。

**吸顶是一种让元素先按正常位置排列、滚动到指定边界后暂时固定显示的 CSS 定位方式**·position: sticky 让元素平时留在文档流，滚到 top 或 bottom 等阈值后暂时吸附。它受最近滚动祖先和包含块边界限制；祖先的 overflow 可能改变它跟随的滚动容器，容器没有足够滚动距离时也看不到效果。使用时还要设置相应偏移值。

先知道

[定位 **Position**](/position)

🔥 热门组件

按钮 Button

输入框 Input

卡片 Card

🧭 页面导航

导航菜单 Menu

分页 Pagination

面包屑 Breadcrumb

↕ 滚动试试：分组标题会吸在顶部接力

### 什么时候用

- [表格 **Table**](/table) **长表格表头**：滚到底也知道每列是什么

  任务　　状态登录页改版　进行中支付流程　已完成
- **列表分组标题**：通讯录字母、日期分组依次接力

  A阿凯B白老师
- **筛选栏、navbar**：滚到顶部才吸住

  筛选栏 · sticky 吸顶
- 在需要吸附的轴上设置偏移，例如 **top: 0**；没有对应偏移时不会进入吸附状态

  position: sticky; top: 0;

### 什么时候不用

- 祖先有 **overflow**：它可能成为 sticky 的滚动容器并限制可吸附范围；先检查实际滚动容器与高度

  祖先：overflow: hidden可能限制 sticky 的滚动范围检查祖先 overflow、滚动容器和可滚动高度
- 用 **fixed 模拟吸顶**：元素脱离文档流，可能遮挡内容或需要补位

  fixed 栏
- 吸顶元素**没有背景色**：滚动内容可能与其叠加

  透明背景的吸顶标题
- **同时吸附多层控件**：导航、筛选和表头可能持续占用视口，应测试剩余内容区域是否足够

  吸顶导航吸顶筛选吸顶表头

组成结构 · Anatomy

分组标题 · stickytop: 0在文档流里占位，不遮别人

1滚动容器Scroll Containersticky 相对最近的滚动祖先吸附

2吸顶元素Sticky Element写上 position: sticky 的那个元素

3吸附阈值top / bottom滚到距边缘多远时吸住，不写就不生效

4文档流占位In Flow吸住后原来的位置还留着，内容不被遮挡

常见变体 · Variants

吸顶Sticky Top

top: 0

表头、导航滚到顶就吸住

吸底Sticky Bottom

bottom: 0

底部操作栏滚到底才贴住

分组接力Group Headers

AB

通讯录字母、日期分组标题

典型使用场景

长表格吸顶表头

任务负责人状态

登录页改版林小hu进行中

支付流程走查阿凯已完成

设计规范 v2 归档白老师未开始

通讯录字母分组

A

![](/assets/avatar-fox.png)阿凯前端

![](/assets/avatar-robot.png)阿May运营

B

![](/assets/avatar-fox.png)白老师设计

吸顶筛选栏与导航

近地铁
可做饭

![](/assets/cover-mountain.png)

**山居民宿 · 云顶**

大理 · 古城东门 · ¥688/晚

![](/assets/slide-forest.png)

**林间木屋 · 溪谷**

莫干山 · 庾村 · ¥520/晚

底部吸底操作栏

![](/assets/slide-summer.png)

**夏日海边明信片套装 ×1**

¥ 39.00

![](/assets/photo-cat.png)

**猫咪摄影集《窗台上的光》 ×1**

¥ 128.00

![](/assets/slide-city.png)

**城市漫步地图 · 广州 ×2**

¥ 58.00

合计 **¥ 283.00**
去结算 (4)

延伸阅读 · 权威出处

[position 属性MDN ↗](https://developer.mozilla.org/en-US/docs/Web/CSS/position)[吸顶表头：5 种改进方法NN/g ↗](https://www.nngroup.com/articles/sticky-headers/)
