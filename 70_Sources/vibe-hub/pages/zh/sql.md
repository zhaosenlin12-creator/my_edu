---
type: web_source
source_url: "https://vibe-hub.org/sql"
title: "SQL"
language: zh
category: "sql"
fetched_at: 2026-07-27T10:04:23+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←数据库浏览器存储→

# SQL

你可能会说

我想查出“最近 7 天下单的用户”，那句话怎么写？

**后端或数据库工具用来查找和修改关系型数据的语言**·例如，管理员筛选所有未付款订单时，后端会用 SQL 从订单表中查出结果。修改或删除数据前必须确认影响范围，用户输入也不能直接拼进 SQL 命令。

先知道

[数据库 **Database**](/database)

也常被叫作*SQL 查询**结构化查询语言*

`SELECT name, city`
`FROM users`
`WHERE city = '深圳'`

命中这些行

id名字城市

1小狸深圳

2阿机杭州

3小林上海

### 什么时候用

- 先学会用 SELECT、FROM 和 WHERE 查询目标数据，并检查返回结果

  先学会读数据

  查询**SELECT \* FROM users WHERE id = 42**
  *→*
  结果**42 · 小林**
- 修改或删除前，先用相同的 WHERE 条件执行 SELECT，确认影响范围

  删改前先预览影响范围

  SELECT ... WHERE id=42→确认 1 行→DELETE
- 使用参数化查询，让用户输入作为数据传入，而不是拼进 SQL 命令

  输入只作为数据

  SELECT \* FROM users WHERE email = **$1**$1 = "oil@example.com"

  参数不会被当作另一段 SQL 执行
- 让 AI 编写 SQL 时提供表结构，并要求它解释查询与修改范围

  把表结构一起交给 AI

  users.id**uuid**users.email**text · unique**输出**解释影响几行**

### 什么时候不用

- DELETE 缺少 WHERE 时会删除表中所有行；执行前必须确认范围并准备恢复方案

  少了 WHERE 的删除

  执行**DELETE FROM users**
  *→*
  影响**12,480 行被删除**
- 不要把表单内容直接拼进 SQL，这会产生 SQL 注入风险

  把输入直接拼进 SQL

  email = **' OR 1=1 --**SELECT \* FROM users WHERE email = '' OR 1=1
- 不要在生产数据库中边猜边试；先在测试数据或事务中验证

  未确认条件就在生产库执行写操作

  当前环境**PRODUCTION**准备执行**UPDATE users ...**

  先在测试数据或事务中验证
- 不要只设计展示文案，还要为数据定义稳定标识和合适字段类型

  展示文字不能代替稳定字段

  只存**“高级会员”**
  *→*
  应该**plan\_id: pro\_2026**

组成结构 · Anatomy

`SELECT name FROM users WHERE city = ?`

id名字城市

1小狸深圳

1操作ActionSELECT、INSERT、UPDATE 或 DELETE，决定要读取还是修改

2表Table要操作的关系型数据集合；先确认表名和字段结构

3条件ConditionWHERE 限定影响范围；问号等占位符由参数化查询安全传值

常见变体 · Variants

查询SELECT

**SELECT**读出匹配的行

读取记录，不修改数据

新增INSERT

**INSERT**加一行新记录

创建一条新记录

修改UPDATE

**UPDATE**改 WHERE 命中的行

更新指定记录，必须看 WHERE

删除DELETE

**DELETE**删 WHERE 命中的行

删除指定记录，先确认可恢复

典型使用场景

查询用户列表

查询用户**SELECT 找到符合条件的记录**

SELECT id, name, planFROM usersWHERE plan = 'pro';

结果：u\_23 · 林小狐 · pro

新增一条任务

新增任务**INSERT 创建一条记录**

执行**INSERT INTO tasks ...**
*→*
返回**id = task\_8842**

更新个人资料

更新资料**UPDATE 只修改指定用户**

UPDATE usersSET city = '深圳'WHERE id = 'u\_23';

影响 1 行 · 修改成功

按 id 删除一条记录

删除记录**DELETE 前先确认 WHERE**

SELECT WHERE id=t\_42→确认 1 行→DELETE

避免误删整张表

延伸阅读 · 权威出处

[SQL 注入MDN ↗](https://developer.mozilla.org/en-US/docs/Glossary/SQL_injection)
