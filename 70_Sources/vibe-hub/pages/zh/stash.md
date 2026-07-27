---
type: web_source
source_url: "https://vibe-hub.org/stash"
title: "贮藏 Stash"
language: zh
category: "stash"
fetched_at: 2026-07-27T10:04:21+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←工作树忽略文件→

# 贮藏Stash

你可能会说

改到一半要切去干别的，先把现在这些东西临时收起来。

**把当前没做完的改动临时收起来，让工作区先恢复干净**·例如，首页改到一半却要切去修 Bug，可以先 Stash，处理完再恢复。刚新建且从未加入 Git 的文件默认不会被收起，操作前要看 git status；Stash 只适合短期中转，正式成果仍要commit。

先知道

[Git](/git)[分支 **Branch**](/branch)

**表单还没改完**暂时不能保存成版本

临时收起stash*→*

**未完成改动**需要时再放回

*✓***工作区已清爽**可以先切换任务

git stash push -m "表单做到一半"

Stash 只适合短暂收起未完成改动，方便切换分支或处理急事。它不是正式版本，也不是远端备份；完成后仍要 Commit。

### 什么时候用

- 临时切换任务前，用清楚的说明收起未完成改动

  **$** **git stash push -m "首页改动尚未完成"**Saved working directory and index state On main: 首页改动尚未完成
- 回来后先放回改动并确认内容，再继续修改

  **$** **git stash apply stash@{0}**Changes restored to the working tree先保留 stash，确认恢复正确后再 drop
- 忘记收过什么时，用列表查看已有记录和说明

  **$** **git stash list**stash@{0}: On main: 首页改动尚未完成stash@{1}: WIP on main: a1b2c3d 首页基础版本每次保存生成一条记录，最新记录编号为 0
- 任务完成后仍要 Commit，不要长期依赖 Stash 保存成果

  stash@{0}首页改动尚未完成

  stash@{1}WIP on main: a1b2c3d

  使用描述性名称，便于识别保存的改动

### 什么时候不用

- 把 Stash 当成正式版本或远端备份

  stash@{0} … stash@{7}共有 8 条记录，最早创建于上个月长期不整理会增加识别每条记录用途的难度
- 不写说明就连续收起多次，之后无法判断每一份是什么

  当前分支：hotfix/login**$** **git stash pop**首页改动已应用到 hotfix/login 分支执行 pop 前先确认当前分支
- 恢复后没有检查内容，就直接删除 Stash 记录

  stash@{2}WIP on main: 三周前

  缺少说明，无法快速确认记录内容
- 长期把重要成果放在 Stash 中，却一直不 Commit

  修复完成后重新实现了此前的改动未恢复已有 stash，造成重复工作

组成结构 · Anatomy

**🛠 工作区**尚未完成修改的 index.html
stash push →

**stash@{0}** 首页改动尚未完成 ← 最新
**stash@{1}** WIP on main: a1b2c3d
**stash@{2}** WIP on main: 0f1e2d3

1工作区改动Working Dir尚未 commit 的改动，可通过 stash 临时保存

2最新一包stash@{0}最后一次 git stash push 保存的改动；未指定时 pop 默认取它

3较早记录stash@{1}每次执行 git stash push 后，已有记录的编号依次增加

4更早记录stash@{2}编号越大表示记录越早；应及时确认是否恢复或删除

常见变体 · Variants

保存git stash push

git stash push -m "首页改动尚未完成"

需要暂存改动后切换任务；不会推送到远程

查看List

git stash list

查看已有的 stash 记录

恢复Apply

git stash apply stash@{0}

先恢复但保留备份，确认后再 drop

应用并保留Apply

git stash apply

恢复改动，同时保留 stash 记录

典型使用场景

未完成改动时执行 stash push

zsh — my-first-page

**$** **git status**
modified: index.html（改动尚未完成）
⚡ 正式环境登录失败，需要切换到 hotfix/login
**$** **git stash push -m "首页改动尚未完成"**
Saved working directory and index state On main: 首页改动尚未完成
**$** **git checkout hotfix/login**
Switched to branch 'hotfix/login'

stash list 查看暂存清单

zsh — my-first-page

**$** **git stash list**
stash@{0}: On main: 首页改动尚未完成
stash@{1}: WIP on main: a1b2c3d 首页基础版本
编号越小越新，pop 默认取 stash@{0}

stash apply 恢复

zsh — my-first-page

**$** **git checkout main**
Switched to branch 'main'
**$** **git stash apply stash@{0}**
On branch main
Changes not staged for commit:
modified: index.html
Changes restored to the working tree
改动已恢复，确认无误后再执行 drop

确认后 drop 清理

🛠 首页改动尚未完成
stash push →
📦 stash@{0}
→ 处理其他任务 →
🛠 stash apply 恢复

延伸阅读 · 权威出处

[git-stash 官方文档git-scm ↗](https://git-scm.com/docs/git-stash)[贮藏与清理（Pro Git）git-scm ↗](https://git-scm.com/book/en/v2/Git-Tools-Stashing-and-Cleaning)
