---
type: web_source
source_url: "https://vibe-hub.org/clone"
title: "克隆 Clone"
language: zh
category: "clone"
fetched_at: 2026-07-27T10:04:20+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←推送合并请求→

# 克隆Clone

你可能会说

给我一个项目网址，我想把整套代码下载到自己电脑上改。

**Clone 是把远程 Git 仓库的代码和版本历史首次复制到本地的操作**·它会新建项目文件夹并下载代码、分支信息和提交历史。例如，进入目录后先读 README 再安装依赖；之后同步新增版本用pull。

先知道

[终端命令行 **Terminal**](/terminal)[Git](/git)

**GitHub 项目**代码和全部版本记录

第一次完整下载clone*→*

**新的项目文件夹**代码和历史都在电脑里

git clone 项目地址

Clone 是第一次取得一个项目：它会新建文件夹，并把代码与版本历史一起下载。以后获取新增内容使用 Pull，不必重新 Clone。

### 什么时候用

- 第一次参与一个 GitHub 项目时，复制正确的仓库地址再 Clone

  <> Code ▾https://github.com/oil-oil/my-first-page.git📋绿色 Code 按钮，复制 HTTPS 地址
- Clone 完先进入新文件夹，阅读 README 和项目配置

  **$** **git log --oneline**e7b2d48 修复按钮在手机上错位a3f9c21 完成首页导航栏0f1e2d3 初始化项目
- 确认项目需要的运行环境后，再安装依赖并启动

  第一次 clone 整仓→之后 pull 增量
- 之后同步新增版本使用 Pull，不要重复下载整个项目

  ⑂ Fork→在你的账号下创建仓库副本

  fork 在托管平台复制，clone 下载到本地

### 什么时候不用

- 把下载 ZIP 当成 clone；压缩包不包含 Git 历史

  Download ZIP→git log 无法运行

  ZIP 包含工作文件，但不包含 .git 目录和提交历史
- 在没有写入权限的仓库里直接尝试 Push

  **$** **git push**remote: Permission to oil-oil/my-first-page.git denied.
- 反复 Clone 出“项目-2”“项目-最新”等重复文件夹

  📁 my-first-page  
  📁 my-first-page-2  
  📁 my-first-page-最新clone 三份后，难以确认哪个目录最新
- 取得项目后没有安装依赖，就直接尝试启动

  **$** **npm run dev**Error: Cannot find module 'react'

组成结构 · Anatomy

https://github.com/oil-oil/my-first-page.git

1协议HTTPS可以先复制 HTTPS 地址，不需要另外配置 SSH 密钥

2平台Host仓库托管在哪个网站，GitHub、Gitee 都长这样

3账号名Owner仓库是谁的，fork 之后这一段会变成你的名字

4仓库名Repository项目名字，clone 下来的文件夹默认就叫它

常见变体 · Variants

克隆仓库git clone

git clone https://github.com/oil-oil/my-first-page.git

下载工作文件、仓库元数据和可达提交历史

改文件夹名clone + 名字

git clone <地址> my-app

想换个本地文件夹名

下载 ZIPDownload ZIP

Code ▾ → Download ZIP

仅需要工作文件且不需要 Git 历史时

派生仓库Fork

网页右上 ⑂ Fork

需要在自己的账号下建立远程副本时

典型使用场景

GitHub Code 按钮复制地址

my-first-page
<> Code ▾

HTTPSSSHGitHub CLI

https://github.com/oil-oil/my-first-page.git
📋 复制

终端 git clone 下载

zsh — ~/projects

**$** **git clone https://github.com/oil-oil/my-first-page.git**
Cloning into 'my-first-page'...
remote: Enumerating objects: 36, done.
remote: Counting objects: 100% (36/36), done.
Receiving objects: 100% (36/36), 12.4 KiB | 2.1 MiB/s, done.
当前目录多了一个 my-first-page 文件夹

clone 后查看提交历史

zsh — my-first-page

**$** **git log --oneline**
e7b2d48 修复按钮在手机上错位
a3f9c21 完成首页导航栏
b4c5d67 首页基础版本
0f1e2d3 初始化项目
clone 完成后可使用 git log 查看提交历史

fork 他人的仓库

oil-oil / my-first-page
⑂ Fork **12**

⑂

xiaoli / my-first-page

forked from oil-oil/my-first-page

Fork 在你的账号下创建副本；clone 到本地后可将提交推送到该副本

延伸阅读 · 权威出处

[git-clone 官方文档git-scm ↗](https://git-scm.com/docs/git-clone)
