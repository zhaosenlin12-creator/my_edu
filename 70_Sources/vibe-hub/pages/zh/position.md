---
type: web_source
source_url: "https://vibe-hub.org/position"
title: "定位 Position"
language: zh
category: "position"
fetched_at: 2026-07-27T10:04:09+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←吸顶居中→

# 定位Position

你可能会说

把这个小图标固定在卡片右上角，别的内容怎么排都不影响。

**定位是通过 CSS position 和偏移量决定元素是否脱离文档流及其参照位置的布局规则**·卡片角标常让父元素 relative、子元素 absolute；悬浮工具栏可用 fixed，滚动后固定的表头可用 sticky。普通内容优先使用正常布局；absolute、fixed 的参照物会受包含块等规则影响，元素偏位时应检查父级而不是不断加偏移值。

NEW
✓ 卡片写了 relative，角标贴在卡片右上角

NEW
✕ 卡片未建立定位上下文，角标相对外层容器定位

### 什么时候用

- 在相对定位的卡片中放置绝对定位的角标

  3
- **右下角悬浮按钮**：fixed 钉在视口，滚动也不动

  ＋
- **吸顶导航、筛选栏**：sticky 滚到点才吸住，见 sticky

  筛选栏 · sticky 吸顶
- 让下拉菜单和文字提示贴着触发元素出现

  全部状态全部状态进行中

### 什么时候不用

- 绝对定位找错参照父级，元素会偏离预期位置

  角标飞到角落卡片没写 relative，absolute 参照了 body
- 元素还是 static 就写 z-index：**普通块级元素上的 z-index 通常不参与排序**，但 flex/grid 子项是例外；还要检查层叠上下文

  z-index: 99 但没设 position
- 拿 **fixed 当吸顶**用：脱离文档流，不是盖住内容就是要手动补占位

  fixed 栏
- 整页依赖**absolute 固定坐标**：内容变长时容易错位

  top:6 left:8top:18 left:62top:42 left:28全写死坐标，内容一变长全错位

组成结构 · Anatomy

角标top: 0 · right: 0z-index: 1 压得住内容

1包含块Containing Blockabsolute 常由最近的定位祖先确定包含块；transform、contain 等也可能建立包含块，找不到时参照初始包含块，不要笼统称 body

2定位元素Positioned Elementposition 不是 static 的那个，才能用偏移量

3偏移量Offsetstop / right / bottom / left，决定离参照物各边多远

4层叠Stackingz-index 可用于定位元素和 flex/grid 子项；先比较所在的层叠上下文，再比较数值

常见变体 · Variants

默认Static

static

默认就是它，跟着文档流排队

相对自己Relative

relative

微调位置，或给子元素当锚点

相对祖先Absolute

3

角标浮层，相对最近的定位祖先

钉在视口Fixed

＋

悬浮按钮、固钉操作，滚动不跟走

到点吸住Sticky

top: 0

表头、导航滚到设定位置才吸住

典型使用场景

卡片右上角角标

![](/assets/avatar-fox.png)

设计小分队

新版首页的稿子传上来了

10:24
3

![](/assets/avatar-robot.png)

Vibe 助手

你的页面已经部署好了

09:50

右下角悬浮按钮

＋

吸顶导航

**Vibe 图鉴**
组件
概念
练习

下拉与气泡浮层

**成员列表**
角色：全部 ▾

![](/assets/avatar-fox.png)小狸管理员

![](/assets/avatar-robot.png)阿机访客

全部角色 ✓

管理员

编辑者

延伸阅读 · 权威出处

[position 属性MDN ↗](https://developer.mozilla.org/en-US/docs/Web/CSS/position)
