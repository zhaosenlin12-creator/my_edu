---
type: web_source
source_url: "https://vibe-hub.org/pull-request"
title: "合并请求 Pull Request"
language: zh
category: "pull-request"
fetched_at: 2026-07-27T10:04:21+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←克隆工作树→

# 合并请求Pull Request

你可能会说

我改完了，想请人看一眼没问题，再合进正式版本。

**GitHub 或 GitLab 上查看分支改动、讨论并决定是否合并的页面**·例如，新导航分支push后创建 Pull Request，评审者可以逐行查看diff、留言并确认检查结果，再决定是否合入 main。它不是 Git 命令，也不表示改动已经进入主版本。

先知道

[分支 **Branch**](/branch)[推送 **Push**](/push)[差异对比 **Diff**](/diff)

新功能分支**更新首页导航**3 个文件有改动

发给别人检查Pull Request*→*

*✓* 说明清楚*✓* 检查通过**可以合入主版本**

在 GitHub 上创建 Pull Request

Pull Request 是一个检查页面，不是终端命令。它把“为什么改、改了什么、怎样验证”集中给团队确认，确认后才合入主版本。

### 什么时候用

- 把功能分支 Push 到远程后，在 GitHub 创建 Pull Request

  feat/dark-mode 已推送到远程

  feat/dark-modeCompare & pull request
- 写清目的、主要改动、验证步骤和已知问题

  feat: 首页加上深色模式改了什么：导航栏 + 卡片支持深色  
  怎么验证：切换右上角开关
- 逐页查看改动清单，并等待必要的自动检查通过

  Squash and merge ▾

  Create a merge commitSquash and mergeRebase and merge

  将 7 条中间提交整理为 1 条主分支提交
- 确认反馈已经处理后，再按项目约定合入主版本

  Merged#12 feat: 深色模式

  Merged#11 fix: 手机端导航换行

  个人项目也可保留带说明的改动记录

### 什么时候不用

- 把 Pull Request 当成可以在终端直接运行的 Git 命令

  **$** **git pull-request**git: 'pull-request' is not a git command.PR 是 GitHub 的网页功能，不是命令
- 只写“改好了”，没有说明目的和验证方式

  Openupdate #14

  标题与说明过于笼统，难以理解改动范围
- 没有查看改动内容，只因为自动检查通过就直接合入

  Files changed **37**+2,140 −867

  一个 PR 包含三个功能，评审范围过大
- 收到反馈后继续修改，却没有重新检查最新变化

  提交说明：  
  ● wip  
  ● 调整实现  
  ● 修正样式  
  ● 完成修改未按项目约定整理历史，后续追溯会更困难

组成结构 · Anatomy

● Openfeat: 首页加上深色模式 #12

xiao-hu 想把 **feat/dark-mode** 合并进 **main**

ConversationCommits 3Checks ✓Files changed 2

✓ 没有冲突，可以自动合并Squash and merge ▾

1标题与编号Title & #一句话说清改了什么；#12 是这张申请单的编号

2分支对Branches从哪个分支合进哪个分支：feat/dark-mode → main

3对话与改动TabsConversation 讨论、Commits 存档点、Files changed 逐行改动

4合并按钮Merge Button检查、测试和审批通过后再点；合并方式遵循项目约定

常见变体 · Variants

Squash and mergeSquash

3 commits → 整理为 1 条进入 main

需要将一组中间提交整理为一个完整改动时

Create a merge commitMerge Commit

每条 commit 原样保留 + 合并节点

需要保留完整过程记录时用

Rebase and mergeRebase

commits 排队接到 main 尾巴上

历史一条直线，没有合并节点

典型使用场景

GitHub 开 PR 页

Open a pull request

base: main
←
compare: feat/dark-mode
✓ Able to merge

改了什么：导航栏 + 卡片支持深色  
怎么验证：切换右上角开关看效果

Create pull request

PR 对话与 review

feat: 首页加上深色模式 #12

● Open
xiao-hu 想把 3 个 commits 从 feat/dark-mode 合并进 main

狸

you · 2 小时前 · **Approved**

说明写得很清楚，深色下导航栏对比度也没问题，可以合。

ConversationCommits 3Checks ✓Files changed 2

Files changed 看改动

**Files changed 2**
+18 −4

📄 index.html

- <button>点我</button>

+ <button class="btn btn-primary">立即开始</button>

</section>

按项目约定选择合并方式

✓ This branch has no conflicts with the base branch

Squash and merge ▾

3 个 commits 将压成 1 条进入 main：feat: 首页加上深色模式 (#12)

⤴ Merged
xiao-hu merged 3 commits into main

延伸阅读 · 权威出处

[为项目做贡献（Pro Git）git-scm ↗](https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project)
