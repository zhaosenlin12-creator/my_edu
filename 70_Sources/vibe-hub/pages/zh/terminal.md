---
type: web_source
source_url: "https://vibe-hub.org/terminal"
title: "终端命令行 Terminal"
language: zh
category: "terminal"
fetched_at: 2026-07-27T10:04:14+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←代码规范检查npm→

# 终端命令行Terminal

你可能会说

AI 丢给我一串命令让我运行，我都不知道它会干什么，敢直接跑吗？

**终端命令行是通过输入文字命令操作电脑和运行程序的界面**·许多项目命令和相对路径取决于当前目录，例如启动开发服务前要先进入项目目录并观察输出。删除文件、改权限或上传数据前，先确认命令作用的准确目标和影响。

zsh — my-first-page

**$** **npm run dev**
> my-first-page@0.1.0 dev
✓ Ready in 1.2s
→ Local: **http://localhost:3000**
浏览器打开这个地址，就能看见你的页面

### 什么时候用

- 运行命令前先用 **pwd / ls 确认项目目录**，再逐条执行

  **$** **npm run dev**✓ Ready in 1.2s→ http://localhost:3000
- **cd 进入目录、ls 查看内容**：先知道自己站在哪里

  **$** **ls** 列出当前目录内容index.html my-first-page**$** **cd my-first-page** 进入项目目录
- **先找第一条可操作错误**：连同执行命令、前后输出和环境信息一起分析

  ▲ 编译失败Error: Cannot find module 'react'at build (build.js:12)
- 安装依赖、启动项目和运行构建等开发任务

  **$** **npm install**added 42 packages in 6s**$** **npm run build**✓ built in 3.2s

### 什么时候不用

- 出现多条错误输出时直接**关闭窗口并重试**：会丢失定位问题所需的命令和首条错误

  Error: …Error: …（多条错误输出）

  ✕
- 未确认工作目录就执行命令：项目脚本可能找不到 package.json 或配置文件

  **~/Desktop $** **npm run dev**npm error: no package.json
- 一次**粘贴多条相互依赖的命令**：中间失败后，后续命令可能在错误状态下继续执行

  连续粘贴多条命令…**npm install**Error: 网络超时后续命令的结果难以归因
- 未理解错误就**加 sudo**：可能绕过权限保护并修改或删除错误目标

  **$** **sudo rm -rf** …以更高权限执行

组成结构 · Anatomy

$ npm run dev
✓ Ready in 1.2s → http://localhost:3000

1提示符Prompt$ 或 % 开头；前面的路径表示当前工作目录

2命令Command第一个词指定外部程序或 shell 内建功能，例如 npm、cd、ls、git

3参数Arguments命令后的补充信息，例如 run dev 指定要执行的脚本

4输出Output命令返回的结果、警告和错误；先找能够采取行动的线索

常见变体 · Variants

cd / ls 目录操作cd & ls

cd my-first-page  ls

进入项目目录并列出其中的文件

npm run 执行脚本npm run

npm run dev

执行 package.json 中声明的启动或构建脚本

Ctrl + C 中止Ctrl+C

Ctrl + C

中止前台运行的命令或开发服务

clear 清屏clear

clear

屏幕内容过多时清空显示

典型使用场景

npm run dev 启动项目

zsh — my-first-page

**$** **npm run dev**
> my-first-page@0.1.0 dev
> vite
✓ Ready in 1.2s
→ Local:   **http://localhost:3000**
开发服务在此进程中运行；中止进程后本地地址将停止响应

从首条错误开始定位

zsh — my-first-page

Failed to compile
Error: Cannot find module 'react'
  at build (vite.config.js:12)
  at processTicksAndRejections (node:internal)
↑ 错误信息和调用栈要结合执行命令一起判断

cd / ls 目录操作

zsh

**~/Desktop $** **ls**
Documents  Downloads  my-first-page
**~/Desktop $** **cd my-first-page**
**~/Desktop/my-first-page $** **ls**
index.html  package.json  README.md

Ctrl+C 中止服务

zsh — my-first-page

✓ Ready — http://localhost:3000
**^C**
**~/Desktop/my-first-page $** 服务已停止，终端返回提示符
Ctrl + C：中止正在前台运行的命令

延伸阅读 · 权威出处

[命令行速成MDN ↗](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Environment_setup/Command_line)
