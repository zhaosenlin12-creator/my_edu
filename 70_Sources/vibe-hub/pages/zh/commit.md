---
type: web_source
source_url: "https://vibe-hub.org/commit"
title: "提交 Commit"
language: zh
category: "commit"
fetched_at: 2026-07-27T10:04:19+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←Git分支→

# 提交Commit

你可能会说

帮我把现在改好的代码存一下，我怕等下越改越乱，回不去了。

**给当前项目保存一个可以回看、带说明的版本**·例如，修好手机端按钮后，先用 git add 把这部分改动选进暂存区，也就是“这次准备保存的清单”，再 Commit 并写明“修复手机端按钮错位”。撤销前要先区分未提交改动和已经推送的提交；共享历史通常用 Revert 追加一次反向修改，不直接改写旧记录。

先知道

[Git](/git)

**导航栏改好了**这还是当前改动

保存为一个版本commit*→*

✓**完成首页导航**刚刚 · 保存在这台电脑

git commit -m "完成首页导航"

Commit 是给这次改动建立一个有名字的版本记录。它先保存在本机；要让 GitHub 也收到，还需要 Push。

常见变体 · Variants

选择改动git add

git add index.html

指定下一次 commit 要记录的改动

创建提交git commit

git commit -m "说明"

完成一个可独立说明的改动后

查看提交git log

git log --oneline

查看提交记录或在恢复前定位提交

看看现状git status

git status

不确定改了哪些文件，先问它

典型使用场景

终端里 add + commit

zsh — my-first-page

**$** **git add index.html**
**$** **git commit -m "修复按钮在手机上错位"**
[main e7b2d48] 修复按钮在手机上错位
 1 file changed, 6 insertions(+), 3 deletions(-)

VS Code 源代码管理面板

源代码管理 2

消息（按 ⌘Enter 提交）

更改

📄 index.htmlM

📄 style.cssM

✓ 提交

⑂ main\*　⊘ 0　⚠ 0

git log 查看提交记录

zsh — my-first-page

**$** **git log --oneline**
e7b2d48 修复按钮在手机上错位
a3f9c21 完成首页导航栏
b4c5d67 首页基础版本
0f1e2d3 初始化项目
前 7 位是短哈希值，可用于定位提交

GitHub 查看一次 commit 的 diff

完成首页导航栏

oil-oil committed 2 小时前　a3f9c21

📄 index.html　+48 -5

- <nav>旧导航</nav>

+ <nav class="top-nav">新导航</nav>

<main>…</main>

延伸阅读 · 权威出处

[git-commit 官方文档git-scm ↗](https://git-scm.com/docs/git-commit)[记录仓库的改动（Pro Git）git-scm ↗](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)
