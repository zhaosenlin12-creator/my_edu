---
type: web_source
source_url: "https://vibe-hub.org/auto-complete"
title: "自动完成 AutoComplete"
language: zh
category: "auto-complete"
fetched_at: 2026-07-27T10:03:48+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←选择器级联选择器→

# 自动完成AutoComplete

你可能会说

输入前几个字，下面自动猜我要写什么，点一下就补全。

**自动完成是在用户输入时显示匹配建议、帮助更快完成输入的表单控件**·填写地址、联系人或标签时可从建议中点选，也可继续输入。最终能否提交未匹配内容取决于业务规则；只接受固定选项时要限制为选择建议，或改用 [选择器 **Select**](/select)，并处理无匹配和加载失败。

先知道

[输入框 **Input**](/input)[选择器 **Select**](/select)

也常被叫作*自动补全**输入建议*

**vibe** coding 入门指南
**vibe**-ui-guide 组件图鉴
**vibe** 设计规范文档

容易混淆？这样区分

自动完成AutoComplete**≠**[选择器 **Select**](/select)

[自动完成 **AutoComplete**](/auto-complete) 会根据输入内容给出建议；[选择器 **Select**](/select) 不需要输入，只能从固定列表中选择。

自动完成AutoComplete**≠**组合框（Combobox）

组合框（Combobox）是“输入框加弹出选项”的完整控件；自动完成（AutoComplete）更强调输入后自动出现匹配建议的行为，两者在很多组件库里会被混用。

### 什么时候用

- **搜索框联想**：输入关键词，实时给出候选

  vibe

  **vibe** coding 入门**vibe**-ui-guide**vibe** 设计规范
- **固定后缀补全**：邮箱、网址这类「半自由」输入；提交时仍按业务规则校验

  oil-oil@

  oil-oil@**gmail.com**oil-oil@**qq.com**oil-oil@**163.com**
- **历史记录快速重选**：最近搜过、用过的直接点

  *🔍 搜索组件…*

  最近搜索日期选择器表单校验
- **命令面板**：输入指令名快速执行操作

  ⌘ 新建

  ➕ 新建项目📄 新建文档📁 新建文件夹

### 什么时候不用

- **选项是固定枚举**：使用 [选择器 **Select**](/select)，或限制组合框只能选择建议

  全部状态

  全部状态进行中已完成已过期
- **数据有层级关系**：使用 [级联选择器 **Cascader**](/cascader) 逐级选择

  省 / 市 / 区广东省深圳市南山区
- **选项较少且需要直接比较**：使用 [单选框 **Radio**](/radio) 平铺展示

  全部进行中已完成
- **业务只接受已有数据**，却允许未匹配内容提交

  城市深圳s

  错误值仍能提交，会影响后续统计

组成结构 · Anatomy

**vibe** coding 入门指南vibe-ui-guide 组件图鉴

1输入框Input用户打字的地方，和普通输入框一样

2建议面板Suggestion Panel跟随输入实时刷新候选

3建议项Suggestion一条候选，键盘上下可选

4高亮片段Matched Text命中的关键词加亮，说明为什么推荐它

常见变体 · Variants

搜索联想Search Suggest

**vibe** coding 入门**vibe**-ui-guide

搜索框里边打字边给候选词

邮箱后缀Email Suffix

oil-oil@**gmail.com**oil-oil@**qq.com**

邮箱、网址这类半固定格式的输入

历史记录History

🕘 日期选择器🕘 表单校验

让用户一次点击重选最近搜过的内容

分组建议Grouped

组件**按钮** Button文档**按钮**设计规范

候选来自不同类型时，按类型分组以便识别

典型使用场景

全局搜索框

**Vibe 图鉴**
🔔

**按钮** Button · 组件
**按钮**设计规范 · 文档
单选**按钮** Radio · 组件

登录邮箱输入

登录账号

oil-oil@**gmail.com**
oil-oil@**qq.com**

地址联想

收货地址

深圳市**南山**区科技园南区 R2-B 栋
深圳市**南山**区蛇口海上世界 C 区
广州市**南山**街道 12 号

命令面板

⌘ 新建

➕ 新建项目
📄 新建文档

延伸阅读 · 权威出处

[Combobox 组合框模式WAI-ARIA APG ↗](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/)
