---
type: web_source
source_url: "https://vibe-hub.org/input"
title: "输入框 Input"
language: zh
category: "input"
fetched_at: 2026-07-27T10:03:45+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←表单标签多行文本域→

# 输入框Input

你可能会说

页面上要有个填邮箱的地方。

**输入框是让用户填写账号、搜索词等短文本的表单控件**·账号、昵称和搜索词通常放在输入框中。字段名称要始终可见，格式错误要在附近说明；需要输入多行说明时应使用多行文本域。

也常被叫作*文本输入框**单行输入框*

邮箱用于接收登录通知，不会公开

邀请码邀请码不存在，请检查后重试

容易混淆？这样区分

输入框Input**≠**搜索输入框

搜索输入框是用途明确的输入框（Input），通常还带提交、清除或搜索建议；普通输入框可以填写姓名、邮箱等各种单行内容。

输入框Input**≠**[自动完成 **AutoComplete**](/auto-complete)

[输入框 **Input**](/input) 只负责接收文字；[自动完成 **AutoComplete**](/auto-complete) 会根据已经输入的内容给出可选建议。

### 什么时候用

- **登录、注册**：账号密码这类短文本

  oil-oil••••••••

  登录
- **搜索**：输入简短关键词查找内容

  *🔍 搜索你感兴趣的内容…*
- **表单收集信息**：姓名、邮箱逐行填

  姓名林小hu

  邮箱*you@example.com*
- **起名字、改标题**：精确的短文本编辑

  标题2026 年产品规划 v3

### 什么时候不用

- 需要填写**多行连续内容**：使用 [多行文本域 **Textarea**](/textarea)

  这个组件的交互设计得很细致……
- 必须从**固定选项**中选择：使用 [选择器 **Select**](/select)

  状态进行中
- 将 **placeholder 当作标签**：输入后字段用途不再可见

  *姓名*输入后“姓名”两个字就消失了
- 用输入框展示只读内容，让用户误以为可以修改

  版本v2.4.0

  用户以为可以改，其实不能

组成结构 · Anatomy

邮箱

用于接收登录通知

1标签Label说明这里需要填写什么

2输入框本体Input聚焦时高亮描边，错误时变红

3辅助说明Help Text补充格式要求或错误原因

常见变体 · Variants

默认Default

绝大多数一行文本输入的通用形态

密码Password

密码、密钥等需要遮挡的内容

带前缀图标With Icon

*🔍*

搜索等场景，用图标暗示要填什么

错误状态Error

校验不通过时，红框配上出错原因

禁用Disabled

这一项暂时不允许用户修改

典型使用场景

登录注册表单

注册账号

注 册

已有账号？直接登录

顶部搜索框

**图鉴**
首页组件课程
*🔍*
![](/assets/avatar-fox.png)

个人信息设置

个人信息

头像![](/assets/avatar-fox.png)更换

昵称

邮箱

保存修改

重命名弹窗

📄

📄

重命名文件

取消确定

延伸阅读 · 权威出处

[<input> 输入元素MDN ↗](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input)[帮助用户在表单中输入数据web.dev ↗](https://web.dev/learn/forms/form-fields)
