---
type: web_source
source_url: "https://vibe-hub.org/push"
title: "推送 Push"
language: zh
category: "push"
fetched_at: 2026-07-27T10:04:19+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←拉取克隆→

# 推送Push

你可能会说

我本地改好了，怎么传到 GitHub 上让别人也能看到？

**Push 是把本地已提交的版本发送到远程仓库的 Git 操作**·例如，把完成的 Commit 上传到 GitHub 供协作或触发部署。它不会上传未 Commit 的改动；被拒绝时先读取原因并处理远程变化，不要直接强制覆盖。

先知道

[Git](/git)[提交 **Commit**](/commit)

**我的电脑**多 2 个已保存版本

把新版本上传push*→*

**网上的项目**GitHub 收到更新

git push

Push 只上传已经 Commit 的版本，不会替你保存尚未提交的文件。完成后在 GitHub 检查最新版本是否出现。

### 什么时候用

- 完成 Commit 后，把需要共享的版本上传到 GitHub

  💻 本地仓库git push →☁️ GitHub
- 推送完成后刷新仓库页面，确认最新版本已经出现

  **$** **git push**! [rejected] main -> main (non-fast-forward)hint: 'git pull' before pushing again.
- 推送前检查版本范围，并确认真实密钥没有被记录

  .gitignore  
  node\_modules  
  **.env**匹配规则的未跟踪文件会被跳过；已跟踪文件要另行处理
- 被拒绝时先取得网上变化，处理并测试后再重新 Push

  刷新 GitHub，最新提交已出现✓ 已上传

  Push 后核对远端分支和最新 Commit

### 什么时候不用

- 只 Commit 不 Push，却以为 GitHub 已经有远端副本

  💻 本地 ●●●●☁️ 空的

  只 commit 而不 push，远程仓库不会保存这些提交
- 被拒绝后直接强制推送，可能覆盖别人已经上传的版本

  **$** **git push --force**+ a3f9c21...e7b2d48 main -> main (forced update)远程分支上已有的提交可能被重写
- 把真实密钥推到远程；之后删除文件也不能消除泄露风险

  .env已在 GitHub 上公开可见

  密钥一旦推送到远程仓库，即使删除提交也要按泄露处理
- 没有检查就把所有文件加入版本，可能连依赖和产物一起记录

  node\_modules 380MBgit push →

  大量可重新安装的依赖进入仓库，应由 .gitignore 排除

组成结构 · Anatomy

git pushoriginmain

1推送命令git push将本地分支的提交同步到远程仓库

2远程别名origin远程仓库的代号，clone 下来的项目默认就叫 origin

3目标分支Branch指定要推送的本地分支，通常是 main 或功能分支

常见变体 · Variants

常规推送git push

git push

将本地分支提交同步到远程

首次推送push -u

git push -u origin main

首次推送时建立本地与远程分支的跟踪关系

强制推送push --force

git push --force

会重写远程分支历史，仅在明确了解影响时使用

典型使用场景

终端 git push 上云

zsh — my-first-page

**$** **git push**
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Writing objects: 100% (8/8), 1.24 KiB | 1.24 MiB/s, done.
To github.com:oil-oil/my-first-page.git
 a3f9c21..e7b2d48 main -> main

push 被拒的现场

zsh — my-first-page

**$** **git push**
To github.com:oil-oil/my-first-page.git
! [rejected] main -> main (non-fast-forward)
error: failed to push some refs
hint: Updates were rejected because the remote contains
hint: work that you do not have locally.
hint: 'git pull' before pushing again.
别人先推了 → 先 git pull 合回来，再 push

GitHub 上确认新 commit

my-first-page
刚刚刷新

📄 index.html修复按钮在手机上错位1 分钟前

📄 style.css修复按钮在手机上错位1 分钟前

📄 .gitignore初始化项目3 天前

✓ 最新提交已同步到远程仓库

.gitignore 挡住 .env

本地文件夹

📄 index.html  
📄 style.css  
📄 .gitignore  
📄 .env　🔑

GitHub 仓库

📄 index.html  
📄 style.css  
📄 .gitignore  
没有 .env ✓

延伸阅读 · 权威出处

[git-push 官方文档git-scm ↗](https://git-scm.com/docs/git-push)[使用远程仓库（Pro Git）git-scm ↗](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes)
