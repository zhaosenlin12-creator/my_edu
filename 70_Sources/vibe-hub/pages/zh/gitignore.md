---
type: web_source
source_url: "https://vibe-hub.org/gitignore"
title: "忽略文件 .gitignore"
language: zh
category: "gitignore"
fetched_at: 2026-07-27T10:04:21+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←贮藏差异对比→

# 忽略文件.gitignore

你可能会说

有些文件我不想让 Git 管，比如密钥和依赖包，怎么排除掉？

**告诉 Git 哪些本地文件不要加入版本记录的规则清单**·例如，node\_modules 可以重新安装，.env 可能包含密钥，所以通常会写进 .gitignore。它只对尚未被 Git 跟踪的文件生效；文件已经 Commit 过，补写规则不会删除旧记录，已经泄露的密钥也必须立即更换。

先知道

[Git](/git)[环境变量 **Env Var**](/env-var)

index.html **会记录**style.css **会记录**.env **不记录**

×**.gitignore**把本地密钥挡在版本历史外

.gitignore 中写入 .env

.gitignore 告诉 Git 哪些“还没被记录过的新文件”不要加入版本历史。它不能清除已经提交的密钥；密钥一旦泄露，要立即更换。

### 什么时候用

- 在项目开始时就建立 .gitignore，并用状态列表检查结果

  .gitignore  
  node\_modules/  
  .next/  
  .env  
  .DS\_Store匹配规则且尚未跟踪的文件会被忽略
- 排除 node\_modules 等能根据项目配置重新生成的内容

  **$** **git status**working tree cleannode\_modules 占用 380MB，未出现在待提交列表中
- 排除真实密钥文件，并提交不含真值的示例配置

  .env🔒 仅保留在本地

  密钥保留在本地，不提交到远程仓库
- 参考官方或社区模板后，再按当前项目调整规则

  Add .gitignoreNode

  模板库：github.com/github/gitignore

### 什么时候不用

- 把依赖目录提交到仓库，增加体积并制造无关差异

  node\_modules 380MBgit push →

  大量可重新安装的依赖进入仓库，应由 .gitignore 排除
- 把 .gitignore 当成加密工具；它只是告诉 Git 不要记录

  .env 已推送到远程。  
  ① 立即到服务平台**轮换或吊销密钥**  
  ② 使用 BFG / filter-repo **清理历史**删除当前文件不会移除历史提交中的敏感内容
- 文件已经被跟踪后才补规则；还要另外停止跟踪

  .env 已提交，之后才添加 .gitignore 规则…**$** **git status**modified: .env已跟踪文件不受 .gitignore 影响，需要 git rm --cached
- 密钥已经泄露却只删除文件，没有立即更换密钥

  .gitignore  
  \*忽略全部文件会使新增页面无法进入版本控制

组成结构 · Anatomy

.gitignore
node\_modules/ 依赖目录，npm install 随时装回来
.next/ 构建产物，npm run build 会重新生成
.env 密钥文件，见 {c:env-var}，不应提交到仓库
.DS\_Store mac 系统生成文件，与项目代码无关

1依赖目录node\_modules/体积较大的第三方包；按 package.json 和锁文件可重新安装

2构建产物.next/打包生成的结果，每次 build 都会重新产出

3本地配置.env可能包含 API 密钥等敏感配置，不应提交到仓库

4系统生成文件.DS\_Store操作系统自动生成的小文件，与代码无关

常见变体 · Variants

指定文件Exact

.env

只忽略名称完全匹配的文件

整个目录Directory

node\_modules/

末尾加斜杠，忽略整个文件夹

通配一类Wildcard

\*.log

同后缀的一类文件全部忽略

保留例外Negate

!keep.log

以感叹号开头，使该文件不受前面规则忽略

典型使用场景

新建 .gitignore 文件

.gitignore

node\_modules/ # 依赖，能装回来

.next/ # 构建产物

.env # 密钥，不应提交

.DS\_Store # mac 系统生成文件

git status 前后对比

zsh — my-first-page

# 没写 .gitignore 时：
**$** **git status**
Untracked: node\_modules/ .next/ .env .DS\_Store …（列表很长）
# 写好 .gitignore 后：
**$** **git status**
Changes not staged: modified: index.html
列表仅显示需要处理的项目文件

GitHub 模板库

Create a new repository

Add .gitignore
Node ▾

💡 已有项目想补模板？去 github.com/github/gitignore，搜 Node 复制整份

.env 泄露补救

⚠ .env 已经推送到远端

应立即把其中的密钥视为已经泄露

1

立即到服务平台**轮换或吊销该密钥**，并创建新的密钥

2

先备份，并按托管平台与团队流程评估是否清理历史。共享仓库需要协调协作者、分支和开放中的 PR；个人不要直接改写历史

BFG 或 git filter-repo 只是可选工具，改写后通常还涉及受控强推；Fork、缓存或旧克隆也可能保留对象。验收时先确认旧密钥已经失效

延伸阅读 · 权威出处

[gitignore 官方文档git-scm ↗](https://git-scm.com/docs/gitignore)
