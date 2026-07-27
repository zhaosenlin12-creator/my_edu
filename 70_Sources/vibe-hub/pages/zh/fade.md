---
type: web_source
source_url: "https://vibe-hub.org/fade"
title: "渐入渐出 Fade In / Out"
language: zh
category: "fade"
fetched_at: 2026-07-27T10:04:07+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←弹性过渡→

# 渐入渐出Fade In / Out

你可能会说

切换内容的时候，让旧的淡出、新的淡入。

**渐入渐出是一种通过改变透明度让内容出现或离开的基础动效**·提示框、卡片或弹窗进入和退出时可用 opacity 的淡入淡出，视觉负担较低。它仍要配合正确的阅读顺序、点击和最终隐藏状态；如果需要表达内容来自哪个方向或层级，滑动或缩放可能更清楚。

先知道

[透明度 **Opacity**](/opacity)[过渡 **Transition**](/transition)

分帧示意：opacity 0 → 1，同时轻轻上移

### 什么时候用

- 让弹窗或卡片以渐入配合轻微位移出现
- **退场可比入场更短**：是否更快及具体时长要按任务、距离与减少动态效果设置验证

  入场较缓退场较快
- **内容切换交叉淡化**：[标签页 **Tabs**](/tabs)、轮播旧出新进，视线不断

  旧的淡出，新的淡入
- **优先考虑 opacity 和 transform**：它们通常能避免布局变化，仍应按实际性能验证

  opacitytransform

### 什么时候不用

- **层级变化只用 fade**：菜单可能缺少来源线索，需要时结合缩放或位移表达方向

  全部状态全部状态进行中菜单只原地淡入，缺少来源与方向线索
- fade 时长与任务不匹配：**过长会拖慢操作感，过短又可能看不清变化**；不要套固定毫秒数

  fade时长过长

  淡入过慢会延迟内容可用感
- 透明度为 0 时仍可能挡住点击，要同时处理交互状态

  opacity: 0 了还占位，挡住下面的点击
- **所有变化都只用 fade**：会削弱缩放、滑页等交互原本的层级与方向信息

  弹窗 fade缩放 fade滑页 fade

组成结构 · Anatomy

transform: translateY(8px)animation-duration: .2s

1透明度Opacity从 0 到 1，控制元素由透明变为可见

2轻微位移Offset入场配上移几像素，更自然

3时长Duration按内容距离、任务紧迫度与减少动态效果偏好设定，不存在通用固定毫秒数

常见变体 · Variants

纯淡入Pure Fade

遮罩与占位内容安静出现

淡入上移Fade In Up

卡片弹窗入场，最自然

交叉淡化Cross Fade

轮播与 Tab 内容切换

典型使用场景

弹窗与遮罩入场

新建项目

取消创建

遮罩与弹窗同步淡入，并用轻微位移表达进入方向

提示出现与消失

✓ 保存成功
入场 fade-in，时长按任务调整

✓ 保存成功
退场 fade-out，可采用更快节奏

Tab 内容切换

简介
评论 12
相关文章

![](/assets/avatar-fox.png)**新消息**：通过短暂入场动效提示列表新增了一项

旧内容（残影）淡出、新内容淡入，交叉淡化不打断视线

页面内容初次呈现

fade-in  
300ms  
→

![](/assets/cover-mountain.png)

周末徒步路线

阅读约 4 分钟

首屏内容整体淡入 + 轻微上移，不闪不跳

延伸阅读 · 权威出处

[opacity 属性MDN ↗](https://developer.mozilla.org/en-US/docs/Web/CSS/opacity)
