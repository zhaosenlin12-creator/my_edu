---
type: web_source
source_url: "https://vibe-hub.org/transition"
title: "过渡 Transition"
language: zh
category: "transition"
fetched_at: 2026-07-27T10:04:08+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←渐入渐出动画→

# 过渡Transition

你可能会说

按钮变色太突兀了，能不能慢慢变过去？

**过渡是一种让 CSS 属性从一个状态平滑变化到另一个状态的动效方式**·按钮悬停变色、开关滑块移动等只有起点和终点的变化适合 transition。应明确变化属性、时长和easing；不要默认写 transition: all，宽高等可能触发布局计算的属性也要谨慎，并为减少动态效果的用户降低非必要运动。

先知道

[悬停 **Hover**](/hover)[按下 **Active**](/active)

悬停我← 真的会变（transition）

分帧示意：颜色一格一格变过去，而不是瞬间跳变

### 什么时候用

- 让按钮和链接的悬停颜色平滑变化

  保存→保存
- 明确写出变化属性、时长和easing

  transition-property: backgroundtransition-duration: .25stransition-timing-function: ease-out
- **按距离与任务设时长**：短反馈通常更快，较大的空间移动可能更久；不要套用固定时长

  短反馈按距离测试较大位移
- 优先过渡 transform 和opacity等流畅属性

### 什么时候不用

- 不要默认使用 transition: all，以免无关属性也产生动画

  transition: all连 width、padding 的意外变化也被动画
- 时长与任务不匹配：**过长会拖慢反馈，过短会掩盖变化**；按内容、距离和减少动态效果偏好验证

  hover

  变色过渡过长，会让反馈显得迟缓
- 未设置 transition：颜色会**直接切换**，缺少状态变化反馈

  ⚡
- 谨慎过渡宽高，位移和缩放优先使用 transform

  →

  过渡 width/height 会触发重排，卡

组成结构 · Anatomy

*默认**→**悬停*transition-property: backgroundtransition-duration: .25stransition-timing-function: ease-out

1状态变化Trigger悬停、选中等状态切换，是过渡的起点

2过渡属性Property明确列出需要过渡的属性，避免用 all 意外影响其他变化

3时长Duration变化持续多久；按距离、任务和减少动态效果偏好测试

4缓动Easing速度曲线，决定渐变的气质

常见变体 · Variants

颜色过渡Color

→

悬停变色、选中态切换

变换过渡Transform

浮起

浮起滑入用 transform，性能最好

透明度过渡Opacity

淡入淡出的入场与退场

典型使用场景

按钮悬停变色

写下你的想法…

取消

发布
🖱️

→

`transition: background .25s ease`

开关拨动滑移

新消息提醒

每周精选邮件

深色模式

滑块通过 transform 平移；左侧残影表示运动轨迹

卡片悬停浮起

![](/assets/cover-workspace.png)

官网改版

昨天更新

![](/assets/cover-mountain.png)

徒步相册

2 小时前

🖱️

![](/assets/slide-forest.png)

团建报名

3 天前

悬停时用 transform 与阴影提供过渡反馈，移开后平滑回落

弹窗淡入淡出

确认退出登录？

未保存的草稿会自动保留。

取消退出

弹窗与遮罩 opacity

以 opacity 平滑过渡

延伸阅读 · 权威出处

[transition 属性MDN ↗](https://developer.mozilla.org/en-US/docs/Web/CSS/transition)
