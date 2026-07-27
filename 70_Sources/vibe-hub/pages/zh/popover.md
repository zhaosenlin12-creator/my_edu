---
type: web_source
source_url: "https://vibe-hub.org/popover"
title: "气泡卡片 Popover"
language: zh
category: "popover"
fetched_at: 2026-07-27T10:03:55+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←气泡确认框文字提示→

# 气泡卡片Popover

你可能会说

点一下头像，旁边浮出一张小卡片显示资料。

**气泡卡片是贴近触发元素展开、可承载补充信息和少量操作的浮层组件**·点击成员头像可展开其资料、链接和少量操作。只有一句简短解释时使用[文字提示 **Tooltip**](/tooltip)更合适；触屏设备不能只依赖悬停。

先知道

[按钮 **Button**](/button)

林

oil-oil

产品经理 · 深圳

查看主页 →

林

### 什么时候用

- **点头像看人**：用户信息卡，带主页入口

  **oil-oil**

  查看主页 →林
- **轻量筛选面板**：几个勾选项就地展开

  **筛选状态**进行中已完成▼
- **说明 + 操作链接**：快捷键、帮助入口

  **快捷键**⌘S 保存 · ⌘P 发布查看全部 →⌘
- **通知 / 设置小面板**：比 Tooltip 丰富，比弹窗轻

  **通知设置**
  管理偏好 →🔔

### 什么时候不用

- 只有一句简短说明：使用 [文字提示 **Tooltip**](/tooltip)

  设置⚙
- 内容接近半页：使用 [弹窗 **Modal**](/modal) 或 [抽屉 **Drawer**](/drawer)

  **帮助中心**查看全部 24 篇 →？
- 需要用户确认操作：使用 [气泡确认框 **Popconfirm**](/popconfirm)

  ⚠ 确认删除这条记录？

  取消确定

  删除
- 全局性公告：使用 [警告提示 **Alert**](/alert) 固定在页面中

  📢 本周六 02:00-04:00 系统维护，期间暂不可用

组成结构 · Anatomy

通知设置

管理偏好 →

🔔

1气泡卡片Popover就地展开的容器，箭头指向触发源

2标题Title可选，说清这张卡片是什么

3内容区Content列表、说明、链接，比 Tooltip 自由

4触发元素Trigger通过点击或悬停展开，例如头像

常见变体 · Variants

用户卡片User Card

林

oil-oil

产品经理

点击头像或姓名查看身份信息

筛选面板Filter

筛选状态

☑ 进行中

☐ 已完成

几个筛选项就地展开，不占页面位置

说明带链接With Link

快捷键

⌘S 保存 · ⌘P 发布

查看全部 →

解释一句话不够，还要给个入口

典型使用场景

头像用户卡片

**项目协作台**
🔔
![](/assets/avatar-fox.png)

![](/assets/avatar-fox.png)

林小hu

产品经理 · 深圳

查看主页 →

表头筛选

名称负责人状态 ▾

筛选状态

☑ 进行中
☐ 已完成
☐ 已归档

快捷键说明

✎⬇⌘

快捷键

⌘S 保存 · ⌘P 发布

查看全部 →

通知设置面板

**消息中心**
🔔

通知设置

新评论提醒

系统公告

延伸阅读 · 权威出处

[Popover APIMDN ↗](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API)
