---
type: web_source
source_url: "https://vibe-hub.org/focus"
title: "聚焦 Focus"
language: zh
category: "focus"
fetched_at: 2026-07-27T10:04:06+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←按下拖拽→

# 聚焦Focus

你可能会说

Tab 键切换的时候看不出当前停在哪，能不能给个明显的框？

**聚焦是当前会接收键盘输入或操作的元素所处的交互状态**·按 Tab 键浏览链接和按钮、点击输入框时都会看到 focus；清楚的描边能告诉键盘用户下一次按键会作用在哪里。若替换浏览器默认 outline，必须提供同样明显且对比度足够的焦点样式，不能只在鼠标点击时保留。

用 Tab 聚焦
使用 Tab 键依次导航，比较有无可见焦点指示的差异

### 什么时候用

- [输入框 **Input**](/input) 可用**边框与外圈**清楚显示当前聚焦状态

  *🔍 搜索你感兴趣的内容…*
- **焦点指示要明显**：与背景有足够对比并保持可见面积；具体宽度按组件和可访问性要求验证

  保存
- **Tab 顺序合理**：[表单 **Form**](/form) 从上到下、从左到右，符合阅读顺序

  ① 姓名② 邮箱③ 电话
- 自定义复选框和选择器也要支持键盘聚焦

  自定义复选框

### 什么时候不用

- 使用 **outline: none**却未提供替代焦点样式：键盘用户无法定位焦点

  outline: none
- **焦点描边对比度不足**：用户难以区分聚焦状态

  保存
- 用 **div 模拟按钮**：若未补全语义和键盘交互，Tab 与读屏用户无法正常操作

  <div onclick>
- **tabindex 顺序不合理**：焦点移动顺序会偏离阅读和操作流程

  ② 姓名① 邮箱③ 电话

组成结构 · Anatomy

输入中…描边 2px+Tab → 下一个

1焦点元素Target当前拿到焦点的那个控件

2焦点描边Focus Ring告诉所有人“焦点在这儿”

3焦点顺序Tab OrderTab 键的行进路线，默认按 DOM 顺序

常见变体 · Variants

描边Outline

按钮

浏览器默认焦点样式已经清楚可见时

光晕Ring

输入框

品牌色外发光，更现代

背景高亮Background

菜单项

列表、菜单项聚焦时用

典型使用场景

键盘 Tab 浏览表单

完善资料

`Tab ⇥` 将焦点移动到下一个可聚焦元素

输入框聚焦输入

![](/assets/avatar-fox.png)

这个配色方案不错

聚焦输入：描边与外圈共同标出当前输入位置

屏幕阅读器导航

推送通知

🔊 画外音：「推送通知，开关，已打开」

快捷键直达搜索框

🔍
主题切换
`⌘K`

切换为深色模式

主题与外观设置

延伸阅读 · 权威出处

[:focus-visible 伪类MDN ↗](https://developer.mozilla.org/en-US/docs/Web/CSS/:focus-visible)[理解成功标准 2.4.7：焦点可见WCAG ↗](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html)
