---
type: web_source
source_url: "https://vibe-hub.org/merge"
title: "合并 Merge"
language: zh
category: "merge"
fetched_at: 2026-07-27T10:04:19+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←分支拉取→

# 合并Merge

你可能会说

我在另一边试的功能成了，怎么把它并回正式版本？

**Merge 是把另一条分支的提交整合到当前分支的 Git 操作**·例如，功能完成后可把功能分支合入主版本。两边改了同一处时 Git 会标出冲突，需要决定最终内容、清理标记并重新测试。

先知道

[分支 **Branch**](/branch)[提交 **Commit**](/commit)

主版本

新功能

✓**主版本已更新**两边的改动放到了一起

git merge feature/new-nav

Merge 把另一条分支已经完成的改动带进当前分支。若两边改了同一处，Git 会暂停并请你决定最后保留什么。

### 什么时候用

- 功能分支已经完成并通过测试后，再合回主版本

  main
- 合并前先确认自己站在准备接收改动的分支上

  main
- 出现冲突时逐处理解两边改动，再决定最终结果

  <<<<<<< HEAD标题：小狸的主页=======标题：小狸的摄影主页>>>>>>> feature
- 合并完成后重新运行项目，确认两边功能仍然正常

  编辑最终内容→git add→git commit

### 什么时候不用

- 没有确认当前分支就开始合并，导致改动进入错误位置

  功能分支仍存在错误→ merge →main 包含同一错误

  未验证的改动合入 main，会增加发布风险
- 把冲突处理成只保留一边，却没有理解另一边的用途

  ~~标题：小狸的主页~~  
  ~~标题：小狸的摄影主页~~删除双方内容可能移除原有功能
- 冲突标记没有清理完整就保存版本

  <<<<<<< HEAD  
  标题：小狸的主页保留冲突标记可能导致代码无法解析
- 看到命令成功就结束，忘记重新运行和测试

  merge ✓→push ✓→线上报错

组成结构 · Anatomy

<<<<<<< HEAD
<h1>小狸的主页</h1>
=======
<h1>小狸的摄影主页</h1>
>>>>>>> feature/new-nav

1冲突开始标记<<<<<<< HEAD从这里开始是冲突区，HEAD 指你当前所在分支的版本

2你这边的版本Current Change当前分支上这行长什么样，通常是 main 主线的内容

3分隔线=======上下两个版本的分界，解冲突时要一起删掉

4对方分支的版本Incoming Change被合进来的那条分支上这行长什么样

5冲突结束标记>>>>>>> branch冲突区到此为止，标着内容来自哪条分支

常见变体 · Variants

快进合并Fast-forward

Updating a3f9c21..e7b2d48

目标分支没有独立的新提交

合并提交Merge Commit

Merge made by the 'ort' strategy.

两侧均有新提交，需要保留合并节点

中止合并merge --abort

git merge --abort

需要放弃当前尚未完成的合并时

典型使用场景

终端 git merge 合回主线

zsh — my-first-page

**$** **git switch main**
Switched to branch 'main'
**$** **git merge feature/new-nav**
Merge made by the 'ort' strategy.
 index.html | 24 ++++++++++++++-----
 1 file changed, 16 insertions(+), 8 deletions(-)

冲突文件里的标记

📄 index.html⚠ 1 处冲突

<<<<<<< HEAD（主线）

<h1>小狸的主页</h1>

=======

<h1>小狸的摄影主页</h1>

>>>>>>> feature/new-nav（分支）

编辑为最终内容，移除全部冲突标记后重新提交

VS Code 冲突解决按钮

📄 index.html 合并冲突

采用当前更改采用传入的更改保留双方更改

<h1>小狸的主页</h1>（当前 · HEAD）

<h1>小狸的摄影主页</h1>（传入 · 分支）

可选择保留当前更改、传入更改或双方更改

GitHub PR 合并按钮

新导航栏 #2

oil-oil 想把 feature/new-nav 合并到 main

✓
此分支与基础分支没有冲突

Merge pull request

网页上点这个绿按钮，效果等同于 git merge

延伸阅读 · 权威出处

[git-merge 官方文档git-scm ↗](https://git-scm.com/docs/git-merge)[分支与合并基础（Pro Git）git-scm ↗](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)
