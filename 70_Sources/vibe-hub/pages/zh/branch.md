---
type: web_source
source_url: "https://vibe-hub.org/branch"
title: "分支 Branch"
language: zh
category: "branch"
fetched_at: 2026-07-27T10:04:19+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←提交合并→

# 分支Branch

你可能会说

我想试试另一种做法，但又怕把现在这个能跑的版本搞坏。

**从当前版本另开一条修改路线，让新功能先不混进主版本**·例如，从 main 新建 feature/new-nav，只在这条路线修改和测试导航，确认后再通过merge或pull-request合回 main。新分支与 main 共享已有历史，只是从分开的地方继续记录新改动；切换前还要检查未提交内容。

先知道

[提交 **Commit**](/commit)

主版本保持稳定

从这里分开

新功能单独修改

git switch -c feature/new-nav

分支像一条独立的版本线。你可以在“新功能”这条线上修改和测试，主版本仍停在原来的稳定状态。

### 什么时候用

- 开发新功能或尝试较大的修改时，先从稳定版本创建分支

  main
- 用 feature/new-nav 等能说明用途的名称

  feature/new-navfeature/dark-mode
- 切换前先确认当前改动已经 Commit 或暂时收好

  **$** **git switch main**Switched to branch 'main'工作目录更新为 main 分支对应的文件版本
- 完成并测试后及时合回主版本，不让两边相差太久

  main

  feature

### 什么时候不用

- 直接在主版本上做不确定的大改动

  main
- 使用 test1、aaa 等无法说明用途的分支名称

  ⑂ test1  
  ⑂ aaa  
  ⑂ 新建分支2名称未说明用途，后续难以区分分支
- 带着未保存的改动随意切换，导致内容出现在错误分支

  **$** **git switch main**error: Your local changes would beoverwritten by checkout.未提交改动可能阻止切换，或在切换后仍保留在工作目录
- 功能完成很久仍不合回，增加之后的合并难度

  main

组成结构 · Anatomy

main

feature/new-nav

HEAD → 你现在在 feature/new-nav

1主线main常见的默认分支，通常保留已验证的改动；是否允许直接提交要看团队规则

2分叉点Base新分支从某个 commit 创建，起点对应当时的快照

3功能分支Feature Branch可按 feature/功能名命名，用于独立开发和测试

4当前位置HEADHEAD 指向当前检出的分支或提交，git switch 会更新其指向

常见变体 · Variants

创建分支switch -c

git switch -c feature/new-nav

从当前提交创建并切换到新分支

切回主分支switch

git switch main

切换工作目录到 main 的文件版本

列出分支branch

git branch

查看本地分支列表

删除分支branch -d

git branch -d feature/new-nav

确认分支已合并或不再需要后

典型使用场景

终端开新分支

zsh — my-first-page

**$** **git switch -c feature/new-nav**
Switched to a new branch 'feature/new-nav'
从当前提交创建并切换到新分支

GitHub 分支下拉切换

my-first-pagePublic

⑂ main ▾

切换分支

**✓ main** 默认

feature/new-nav

查看所有分支（2）

VS Code 左下角分支名

<nav class="top-nav">  
  <a>首页</a>  
</nav>

⑂ **feature/new-nav**⊘ 0　⚠ 0Ln 3, Col 1

开始修改前确认左下角显示的当前分支

GitHub 分支列表页

你的分支

⑂ main默认2 小时前更新

⑂ feature/new-nav5 分钟前更新New pull request

延伸阅读 · 权威出处

[git-branch 官方文档git-scm ↗](https://git-scm.com/docs/git-branch)[分支简介（Pro Git）git-scm ↗](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)
