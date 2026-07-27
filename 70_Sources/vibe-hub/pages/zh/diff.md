---
type: web_source
source_url: "https://vibe-hub.org/diff"
title: "差异对比 Diff"
language: zh
category: "diff"
fetched_at: 2026-07-27T10:04:21+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←忽略文件Git→

# 差异对比Diff

你可能会说

帮我看看这次到底改了哪几行，加了什么、删了什么。

**把改动前后的内容逐行摆在一起，标出删了什么、加了什么**·例如，AI 修改首页后，先看 Diff：带 - 的行是旧内容被删掉，带 + 的行是新内容加进来。Commit 前要同时检查尚未 add 和已经 add 的 Diff，避免把误删、调试代码或密钥保存进去。

先知道

[Git](/git)[提交 **Commit**](/commit)

改动前按钮文字***−* 点我**

→

改动后按钮文字***＋* 立即开始**

git diff

Diff 是改动清单：红色减号表示删掉的内容，绿色加号表示新增的内容。提交前看一遍，确认没有误删、调试内容或密钥。

### 什么时候用

- AI 完成一轮修改后，先看 Diff 再决定是否保存版本

  **$** **git diff**- <button>点我</button>+ <button class="btn btn-primary">立即开始</button>红色表示删除，绿色表示新增；显示尚未 add 的改动
- 提交前分别检查尚未选择和已经选择的改动

  **$** **git diff HEAD~1 HEAD** 2 files changed, 18 insertions(+), 4 deletions(-)明确比较最近两个提交
- 在 Pull Request 的 Files changed 页面集中检查变化

  📄 index.html+18 −4

  - 点我+ 立即开始
- 看到大段删除时暂停确认，避免旧功能被意外移除

  AI 完成修改→git diff 逐行检查→commit 提交记录

### 什么时候不用

- 只看改了哪些文件，不看每个文件具体变化

  **$** **git add . && git commit -m "AI 修改"**47 files changed，未经过逐项检查出现问题后，难以确认具体改动
- 一次出现大量无关变化仍直接 Commit

  + console.log("test 123")+ // debugger;临时调试代码被一并提交在提交前通过 diff 移除调试代码
- 调试文字、临时文件或真实密钥仍在 Diff 中就提交

  3 files changed仅查看文件列表，无法确认各行的具体改动
- 只因为绿色很多就认为改动正确，仍要理解实际内容

  - <nav>…整个导航栏…</nav>- <footer>…</footer>+ <nav>新导航</nav>删除范围包含页脚，需要确认是否符合预期

组成结构 · Anatomy

📄 **index.html**
@@ -12,5 +12,5 @@
- <button>点我</button>
+ <button class="btn btn-primary">立即开始</button>

1文件头File Header这段改动属于哪个文件，一个文件一段

2位置标记Hunk @@@@ -12,5 +12,5 @@：改动在第 12 行附近

3删除行- Removed红色带 - 号：旧版本有、新版本删掉的行

4新增行+ Added绿色带 + 号：新版本多出来的行

常见变体 · Variants

看未暂存改动git diff

git diff

查看工作区相对暂存区改了什么

看已暂存改动git diff --staged

git diff --staged

add 之后、commit 之前复核

比较最近两次提交git diff commits

git diff HEAD~1 HEAD

复核最近一次提交的具体变化

两个分支比git diff main..feat

git diff main..feat/dark-mode

合并前先看分支领先了多少

典型使用场景

终端 git diff

zsh — my-first-page

**$** **git diff**
diff --git a/index.html b/index.html
@@ -12,5 +12,5 @@
- <button>点我</button>
+ <button class="btn btn-primary">立即开始</button>
红色带 - 是删的，绿色带 + 是加的

比较最近两个提交

zsh — my-first-page

**$** **git diff HEAD~1 HEAD --stat**
 index.html | 10 ++++++----
 style.css | 12 ++++++++++++
 2 files changed, 18 insertions(+), 4 deletions(-)
**$** **git diff HEAD~1 HEAD**
再查看逐行明细，确认本轮 AI 修改内容

GitHub Files changed 页

ConversationCommits 3Checks ✓Files changed 2

**📄 index.html**
+18 −4

@@ -12,5 +12,5 @@

- <button>点我</button>

+ <button class="btn btn-primary">立即开始</button>

AI 修改后先 diff 再 commit

🤖 AI 完成一轮修改
→
🔍 git diff 逐行看
→
✅ git commit 提交记录

延伸阅读 · 权威出处

[git-diff 官方文档git-scm ↗](https://git-scm.com/docs/git-diff)
