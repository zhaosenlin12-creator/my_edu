---
type: web_source
source_url: "https://vibe-hub.org/border-radius"
title: "圆角 BorderRadius"
language: zh
category: "border-radius"
fetched_at: 2026-07-27T10:03:58+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←分割线阴影→

# 圆角BorderRadius

你可能会说

把卡片的尖角磨圆一点，看着柔和些。

**圆角是通过 border-radius 把元素直角改为圆弧的 CSS 样式**·卡片、按钮和头像常用 border-radius 控制四个角的弧度；正方形设为 50% 可得到圆形，长条设为很大的值可得到胶囊形。项目里应建立少量可复用的圆角档位，避免任意混用数值；圆角会影响观感，但“越圆越亲和”只是设计经验。

### 什么时候用

- 相同角色的元素**圆角规则一致**；[卡片 **Card**](/card)、[输入框 **Input**](/input) 角色不同，不必强行使用同一数值

  输入控件：control token内容容器：surface token
- [头像 **Avatar**](/avatar) 可用 **border-radius: 50%**：正方形会形成正圆

  林正方形 + 50% = 正圆头像
- [标签 **Tag**](/tag) 或胶囊按钮的**圆角至少达到高度的一半**；足够大的固定值是实现手段，不是语义规则

  胶囊标签胶囊按钮
- 圆角可**分档管理**：档位数量和数值由组件尺寸、密度与品牌系统决定

  小档中档大档

### 什么时候不用

- **无语义地混用多种圆角**，会削弱组件之间的一致性
- 给长方形写 50%：得到的是**椭圆不是胶囊**
- 容器有圆角但**子内容仍超出边界**：需要裁切时使用 overflow: hidden
- 四角使用**无规则的不同半径**，会让轮廓缺乏一致性

组成结构 · Anatomy

内容

1圆角半径Radius角的圆弧大小，四个角可分别设

2边框Border圆角沿着边框的弧线走

3内容Content默认不被圆角裁剪，除非 overflow: hidden

常见变体 · Variants

较小半径Small

希望保留较清楚边缘感时；按组件尺寸选择

中等半径Medium

需要在边缘感和柔和轮廓间平衡时

较大半径Large

需要更明显圆弧时；先检查内容空间和嵌套关系

圆形Circle

正方形头像、状态点或圆形图标容器

胶囊Pill

长条标签或按钮需要两端完整圆弧时

典型使用场景

卡片与面板

border-radius: 12px

**消息通知**

**深色模式**

圆形头像

![](/assets/avatar-fox.png)50% 正圆

**小狐狸** · 2 小时前

这篇圆角教程太好懂了，已收藏！

胶囊标签

![](/assets/photo-cat.png)

**前端入门训练营**

热卖
上新

＋ 关注

**border-radius: 999px** 是让此示例达到胶囊轮廓的 CSS 写法，不是所有组件的固定值

输入框与按钮

同角色沿用同一圆角 token

搜索

border-radius
box-shadow
flex 布局

延伸阅读 · 权威出处

[border-radius 属性MDN ↗](https://developer.mozilla.org/en-US/docs/Web/CSS/border-radius)
