---
type: web_source
source_url: "https://vibe-hub.org/select"
title: "选择器 Select"
language: zh
category: "select"
fetched_at: 2026-07-27T10:03:47+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←评分自动完成→

# 选择器Select

你可能会说

选项有几十个，全摆出来太占地方，收起来点一下再挑。

**选择器是从固定选项列表中选择一个或多个值的表单控件**·城市、部门等选项较多且不适合平铺时可收进选择器。只有少量选项时 [单选框 **Radio**](/radio) 更直观；允许用户自定义内容时应使用输入框或 [自动完成 **AutoComplete**](/auto-complete)。

也常被叫作*下拉选择框**Select Box*

全部状态

全部状态*✓*
进行中*✓*
已完成*✓*
已过期*✓*

容易混淆？这样区分

选择器Select**≠**[下拉菜单 **Dropdown**](/dropdown)

[选择器 **Select**](/select) 用来选择一个表单值；[下拉菜单 **Dropdown**](/dropdown) 展开的是操作或导航，例如重命名、导出和删除。

选择器Select**≠**[自动完成 **AutoComplete**](/auto-complete)

[选择器 **Select**](/select) 只能从固定选项中选择；[自动完成 **AutoComplete**](/auto-complete) 会随着输入给出建议，是否允许填写自定义内容要另外说明。

### 什么时候用

- **值来自一组固定选项**：状态、分类、优先级

  全部状态

  全部状态进行中已完成已过期
- **选项较多、平铺不便**：收进下拉列表

  选择城市

  北京上海广州深圳杭州…
- **列表页的筛选条件**：几个选择器排一排，即选即筛

  全部状态全部分类最近更新
- **选项文案比较长**：模板、文件这类带描述的选项

  选择模板

  AI 产品需求文档模板（含评审 checklist）用户调研报告模板

### 什么时候不用

- **选项较少且需要直接比较**：使用 [单选框 **Radio**](/radio) 平铺展示

  全部进行中已完成
- 需要**选择多个选项**：使用 [复选框 **Checkbox**](/checkbox) 或多选选择器

  前端后端设计
- **选项有上下级**，如省市区、类目：使用 [级联选择器 **Cascader**](/cascader)

  省 / 市 / 区广东省深圳市南山区
- 允许用户**输入新值**：使用 [自动完成 **AutoComplete**](/auto-complete) 或支持创建的选择器

  自定义标签

  前端后端➕ 创建“自定义标签”

组成结构 · Anatomy

全部状态进行中全部状态*✓*

1触发框Trigger平时收起来的样子，显示当前选中值

2选中文案Selected Label告诉用户现在选的是什么

3下拉箭头Caret表示内容可以展开，图标可随展开状态变化

4下拉面板Dropdown显示所有选项的浮层，可以搜索和分组

5选项Option悬停高亮，选中项带对勾

常见变体 · Variants

基础单选Default

全部状态

全部状态*✓*
进行中*✓*

选项固定、只选一个时的默认形态

多选Multiple

前端后端

选项偏多又要同时选好几个时用

可搜索Searchable

🔍深圳

深圳上海

选项较多时，可通过输入定位目标选项

可清空Clearable

进行中*✕*

筛选条件可选时，允许用户恢复为未选择状态

禁用Disabled

全部状态

条件不满足时暂时禁用，防止误选

典型使用场景

任务状态筛选

**任务列表**
进行中

官网首页改版进行中

支付流程走查进行中

埋点方案评审待开始

注册时选城市

所在城市

广东 · 深圳

广东 · 深圳*✓*
广东 · 广州
浙江 · 杭州

切换语言 / 时区

**界面语言**选择界面显示的语言简体中文

**时区**影响日程和提醒的显示时间UTC+8 北京

报表维度切换

**访问量趋势**
按周

W26W27W28W29W30W31

延伸阅读 · 权威出处

[<select>：HTML 选择元素MDN ↗](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)[Listbox 列表框模式WAI-ARIA APG ↗](https://www.w3.org/WAI/ARIA/apg/patterns/listbox/)
