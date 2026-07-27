---
type: web_source
source_url: "https://vibe-hub.org/worktree"
title: "工作树 Worktree"
language: zh
category: "worktree"
fetched_at: 2026-07-27T10:04:20+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←合并请求贮藏→

# 工作树Worktree

你可能会说

功能改到一半突然要修紧急 bug，我又不想收拾现在这个现场。

**让同一个 Git 仓库同时出现在多个文件夹里，每个文件夹处理一条分支**·例如，原文件夹继续做首页，另一个文件夹单独处理线上修复，两边可以同时打开和运行。移除额外文件夹前，先保存其中的改动并停止正在运行的服务；不要直接删除文件夹，应使用 Git 的 worktree 命令移除。

先知道

[分支 **Branch**](/branch)[终端命令行 **Terminal**](/terminal)

同一份 Git 历史

**项目主版本**继续保持运行

**新功能版本**在另一个文件夹修改

git worktree add 新文件夹 新分支

Worktree 让同一个 Git 项目同时出现在两个文件夹里，每个文件夹打开不同分支。它适合不想中断当前工作、又要临时处理另一件事。

### 什么时候用

- 当前任务不能中断、又要临时处理另一件事时创建 Worktree

  **$** **git worktree add -b hotfix/login ../my-first-page-hotfix main**Preparing worktree (new branch 'hotfix/login')HEAD is now at a1b2c3d 首页基础版本
- 让每个文件夹对应一条明确分支，避免内容混在一起

  📁 my-first-pagemain · 首页改动尚未提交📁 my-first-page-hotfixhotfix/login · 修复登录问题
- 使用列表命令确认每个文件夹与分支的对应关系

  窗口 AAI 修改 feat/nav 导航

  窗口 BAI 修改 feat/pricing 定价页

  每个目录对应独立分支，改动不会互相覆盖
- 确认改动已保存且服务已停止后，再移除 Worktree

  **$** **git worktree remove ../my-first-page-hotfix****$** **git worktree list**/Users/hu/my-first-page a1b2c3d [main]已移除链接工作目录，仅保留主工作目录

### 什么时候不用

- 只是普通切换任务也创建许多工作树，让目录越来越难管理

  **$** **git checkout hotfix/login**error: Your local changes would be overwritten by checkout.未提交改动阻止切换分支，需要先处理这些改动
- 在两个文件夹里同时尝试打开同一条分支

  **$** **git worktree list**my-first-page a1b2c3d [main]my-first-page-hotfix a1b2c3d [hotfix/login]my-first-page-test 0f1e2d3 [feat/test]my-first-page-old 9a8b7c6 [feat/old]未清理的工作目录会占用磁盘并增加维护成本
- 未保存改动或仍有服务运行时就移除目录

  **$** **git worktree add ../dup main**fatal: 'main' is already checked out at '…/my-first-page'同一个分支同时只能在一个目录工作
- 直接删除文件夹；应使用 Worktree 的移除命令更新 Git 记录

  📁 my-first-page-hotfix右键 → 移到废纸篓

  Git 仍保留该工作目录的注册信息

组成结构 · Anatomy

🗄 同一个本地仓库（.git）共享历史和分支引用

📁 my-first-pagemain主工作目录
📁 my-first-page-hotfixhotfix/loginadd 出来的隔壁目录

1本地仓库Repository主工作目录包含 .git；所有 worktree 共享同一套历史和分支引用

2主工作目录Main Worktree常用的工作目录，当前检出 main 分支

3链接工作目录Linked Worktree通过 worktree add 创建的额外目录，检出另一条分支

常见变体 · Variants

新建分支目录Add

git worktree add -b hotfix/login ../hotfix main

要从 main 新开分支和工作目录时

查看清单List

git worktree list

查看已有工作目录及其分支

移除目录Remove

git worktree remove ../hotfix

完成任务并确认无需保留目录后

典型使用场景

git worktree add 创建目录

zsh — my-first-page

**$** **git worktree add -b hotfix/login ../my-first-page-hotfix main**
Preparing worktree (new branch 'hotfix/login')
HEAD is now at a1b2c3d 首页基础版本
**$** **ls ..**
my-first-page my-first-page-hotfix
已创建额外工作目录，共用同一仓库历史

额外目录处理修复

📁 my-first-page

main

首页改动尚未完成  
3 个文件尚未提交

📁 my-first-page-hotfix

hotfix/login

正式环境登录失败  
在这里修复 → Commit → Push

AI 两个窗口并行修改

窗口 A

AI 正在改导航栏

my-first-page-nav · feat/nav

运行中…

窗口 B

AI 正在改定价页

my-first-page-pricing · feat/pricing

运行中…

各占一个 worktree，改完各自开 PR，互不覆盖

list 查看与 remove 清理

zsh — my-first-page

**$** **git worktree list**
/Users/hu/my-first-page a1b2c3d [main]
/Users/hu/my-first-page-hotfix e5f6a7b [hotfix/login]
**$** **git worktree remove ../my-first-page-hotfix**
**$** **git worktree list**
/Users/hu/my-first-page a1b2c3d [main]
修复完成后，已移除链接工作目录

延伸阅读 · 权威出处

[git-worktree 官方文档git-scm ↗](https://git-scm.com/docs/git-worktree)
