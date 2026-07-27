---
type: web_source
source_url: "https://vibe-hub.org/env-var"
title: "环境变量 Env Var"
language: zh
category: "env-var"
fetched_at: 2026-07-27T10:04:15+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←SEO部署上线→

# 环境变量Env Var

你可能会说

密钥不能直接写进代码里，那应该放哪？

**环境变量是在代码之外保存配置值、供不同运行环境读取的方式**·例如，本地、测试和线上可使用不同接口地址或密钥。前端公开变量会进入浏览器代码，真正的密钥只能由服务端读取；.env 是本地加载这些值的常见文件，不是加密保险箱，也必须避免提交到 Git。

先知道

[终端命令行 **Terminal**](/terminal)

.env · 本地开发配置
**OPENAI\_API\_KEY**=*sk-proj-••••••*
**DATABASE\_URL**=*postgres://••••*

process.env.OPENAI\_API\_KEY
🛡 .gitignore 规则已匹配；提交前再看 git status

### 什么时候用

- 在本地 .env 中保存服务端配置，代码只读取变量名

  .env  
  **OPENAI\_API\_KEY**=sk-••••••  
  **DATABASE\_URL**=postgres://••••本地配置一行一个；敏感值不要提交、截图或转发
- 按照所用框架的方式在服务端读取环境变量

  const key = **process.env.OPENAI\_API\_KEY**代码读取变量名；替换配置值通常无需修改代码
- 用gitignore排除本地配置，并在提交前再次检查

  .gitignore  
  node\_modules  
  **.env**匹配规则的未跟踪文件会被跳过；已跟踪文件要另行处理
- **本地与线上分别配置**：在 deployment 平台的设置页中配置线上值

  💻 本地 .env☁️ 平台设置页

### 什么时候不用

- 把密钥**直接写进代码并提交**：仓库访问者可能看到并使用这把密钥

  const key = "sk-proj-8fk2…"提交到仓库的密钥可能出现在提交历史、克隆副本或构建产物中
- 把 **.env 发给别人**：文件、截图或群聊转发都可能扩大敏感值的暴露范围

  .env→ 转发给同事 / 截图发群

  通过文件或截图分享可能暴露其中的敏感值
- 把 Key 写进**浏览器可获取的页面代码**：它可能被查看或提取，不应存放服务端密钥

  右键 → 查看网页源代码<script> key="sk-…" </script>写进前端代码后，访问者可能直接读取
- 改了 .env **不重启需要重载配置的服务**：程序仍可能读取旧值

  改了 .env，直接刷新页面…401 Unauthorized（仍在使用旧 Key）

组成结构 · Anatomy

OPENAI\_API\_KEY=sk-proj-••••••  # 本地开发用，别提交

1变量名Key全大写加下划线是惯例，代码里按这个名字读

2值Value等号后面是实际配置值；包含密钥时，截图前要遮盖

3注释Comment# 开头，给人看的备注，程序会忽略

常见变体 · Variants

本地 .env.env

.env

本地开发使用，通常应由 .gitignore 排除

平台环境变量Platform Env

Vercel → Settings → Env

部署平台设置页里再配一份

示例模板.env.example

.env.example

告诉别人要配啥，不写真值

典型使用场景

.env 文件示例

.env🔒 不提交

# 本地开发用  
**OPENAI\_API\_KEY**=sk-proj-8fk2••••••  
**DATABASE\_URL**=postgres://localhost:5432

代码读取变量名

api.js

const key = **process.env.OPENAI\_API\_KEY**;  
const res = await askAI(prompt, key);

代码读取变量名；本地变更配置值通常不需要修改代码

.gitignore 忽略未跟踪文件

.gitignore

node\_modules  
dist  
**.env**

🛡 匹配规则的未跟踪文件会被 git add 跳过；提交前仍要看 git status

Vercel 环境变量设置页

Environment Variables
+ Add

KEY

VALUE

环境

OPENAI\_API\_KEY

••••••••

Production

DATABASE\_URL

••••••••

Production
