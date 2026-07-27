---
type: web_source
source_url: "https://vibe-hub.org/json"
title: "JSON"
language: zh
category: "json"
fetched_at: 2026-07-27T10:04:11+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←APICORS→

# JSON

你可能会说

AI 返回给我的那种大括号套小括号的数据，怎么读、怎么写？

**软件之间传递结构化数据时常用的文本格式**·例如，天气服务可以用 JSON 返回城市、温度和天气状态，App 再读取这些字段显示出来。JSON 能包含对象、列表、文字、数字和真假值，收到后仍要检查字段是否符合预期。

先知道

[HTTP](/http)

也常被叫作*JSON 数据**JavaScript Object Notation*

```
{
  "name": "按钮 Button",
  "price": 0,
  "free": true,
  "tags": ["通用", "表单"]
}
```

### 什么时候用

- 拿到 api 返回**先整体看结构**，再决定取哪层

  { "data": { "list": [ … ] } }先确认整体结构，再按层级读取字段
- 数组是**有序值列表**，常可循环渲染成 [列表 **List**](/list)；先确认每项结构是否一致

  [{…}"文本"42]

  有序 JSON 值列表；是否同构要看接口约定
- 嵌套就**一层层往里取**：data.user.name

  data→user→name

  嵌套字段需要按层级读取
- 压缩后的内容难以阅读时，可用**可信的格式化工具**增加缩进；敏感数据不要粘贴到未知网站

  {"a":1,"b":[2,3]}→格式化

### 什么时候不用

- 键名**忘加双引号**：JS 行，JSON 不行

  { name: "小林" }键名缺少双引号，无法按 JSON 解析
- 最后一项后面**多一个逗号**：解析直接报错

  [ "a", "b", ]JSON 不允许最后一项后保留尾随逗号
- 用**单引号**包字符串：JSON 只认双引号

  { 'name': '小林' }JSON 的键和字符串必须使用双引号
- 按 JavaScript 对象的写法加入**注释**：标准 JSON 不支持注释

  { // 注释 "a": 1 }JSON 不支持注释

组成结构 · Anatomy

```
{
  "tags": ["通用", "表单"]
}
```

1对象Object一对花括号包起来的整体，描述「一个东西」

2键Key冒号左边的名字，必须双引号

3数组Array方括号包起来的有序列表，渲染 [列表 **List**](/list) 就靠它

4值Value冒号右边的内容：字符串、数字、布尔、对象、数组

常见变体 · Variants

对象Object

{ "name": "按钮", "price": 0 }

花括号包键值对，描述一个东西

数组Array

[ "通用", "表单", "反馈" ]

方括号包列表，顺序有意义

嵌套Nested

{ "user": { "roles": […] } }

对象套数组，真实数据都这样

典型使用场景

Network 面板看返回

HeadersPreviewResponse

▾ **data**: {…}  
▾ **list**: [3]  
▾ **0**: {name: "按钮 Button", price: 0}  
▾ **1**: {name: "输入框 Input", price: 0}  
▸ **2**: {…}  
**total**: 42

Preview 帮你把 JSON 排成可折叠的树

编辑器里的 data.json

data.json

{

"site": "Vibe 图鉴",

"stats": {

"components": 48,

"online": true

},

"tags": ["通用", "表单"]

}

JSON 校验报错

1  {

2    "name": "按钮",

3    "tags": ["通用",],

4  }

✕ 第 3 行：数组最后一项后面多了逗号

终端 jq 美化输出

$ curl -s https://api.vibeui.dev/user/1 | jq

{

"id": 1,

"name": "林小狐",

"roles": [

"admin",

"editor"

]

}

# jq 将压缩 JSON 格式化为带缩进的结构

延伸阅读 · 权威出处

[使用 JSON 数据MDN ↗](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/JSON)
