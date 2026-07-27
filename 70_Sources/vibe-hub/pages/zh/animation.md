---
type: web_source
source_url: "https://vibe-hub.org/animation"
title: "动画 Animation"
language: zh
category: "animation"
fetched_at: 2026-07-27T10:04:06+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←过渡缓动→

# 动画Animation

你可能会说

让这个图标一直循环动，比如轻轻上下浮动。

**动画是一种用 @keyframes 定义多个阶段，并控制其播放方式的 CSS 动效**·加载指示、分步入场等连续变化可用 animation；简单的悬停和选中反馈通常用transition就够了。循环和大幅移动容易干扰阅读，必须尊重 prefers-reduced-motion；结束后是否停在最后一帧也应由实际界面状态决定。

先知道

[过渡 **Transition**](/transition)

0%50%100%@keyframes 定义节点，浏览器补齐中间

### 什么时候用

- **加载类循环**：[进度条 **Progress**](/progress)、[骨架屏 **Skeleton**](/skeleton) 的呼吸与转动

  加载中，请稍候…
- **关键帧编排**：把一段完整动作拆成节点，浏览器补齐中间

  0%50%100%
- **入场编排**：多个元素用 delay 依次出场，有节奏感

  123
- 状态切换用transition，自主播放的多阶段动作再用动画

  悬停变色transition

  加载呼吸animation

### 什么时候不用

- **过度使用循环动画**：会分散注意力并影响阅读
- 简单悬停效果不必使用关键帧，过渡就能完成

  悬停变色@keyframes

  简单 hover 可使用 transition
- 未设置 **fill-mode: forwards**：动画结束后会回到初始帧

  ↩
- 响应 prefers-reduced-motion，减少用户不需要的动画

  减弱动态效果

  应响应用户的减弱动态效果偏好

组成结构 · Anatomy

*0%**100%*2sease-in-outinfinite ⟳

1关键帧Keyframes动作的节点，中间帧由浏览器补齐

2时长Duration完整播一遍要多久

3速度曲线Timing每一帧之间的快慢，见缓动

4播放次数Iteration1 次入场，infinite 循环

常见变体 · Variants

一次性Once

入场编排，播完停在末帧

无限循环Infinite

⟳

加载、呼吸等持续状态

交替往返Alternate

↔

摆动闪烁这类往复动作

典型使用场景

骨架屏呼吸循环

@keyframes 呼吸：透明度 0.4 ↔ 1 循环，告诉用户“正在加载”

加载指示器旋转

![](/assets/avatar-robot.png)

AI 助手

正在生成回复，大约需要 5 秒…

animation: rotate 0.8s infinite，一直转到数据回来

页面入场编排

访问量

12,480

▲ 8.2%

新用户

326

▲ 3.1%

转化率

4.6%

▼ 0.4%

animation-delay: 0msanimation-delay: 100msanimation-delay: 200ms

animation-delay 依次入场，页面有节奏地“亮”起来

一次性强调闪烁

![](/assets/avatar-fox.png)

**新回复** 已加入列表，并通过短暂入场动效标出变化

新

![](/assets/avatar-robot.png)

**机器人助理** 赞了你的文章

1 小时前

背景高亮闪一次
→
→
停在末帧，不循环

延伸阅读 · 权威出处

[animation 属性MDN ↗](https://developer.mozilla.org/en-US/docs/Web/CSS/animation)
