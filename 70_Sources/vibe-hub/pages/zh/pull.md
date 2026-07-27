---
type: web_source
source_url: "https://vibe-hub.org/pull"
title: "拉取 Pull"
language: zh
category: "pull"
fetched_at: 2026-07-27T10:04:19+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←合并推送→

# 拉取Pull

你可能会说

同事说他改完了，我怎么把他那版拿到我电脑上？

**Pull 是获取远程新提交并把它们整合到当前分支的 Git 操作**·它用于已在电脑上的项目，例如同步 GitHub 上队友新提交的版本。执行前先 Commit 或收好未完成改动；第一次完整下载仓库应使用clone。

先知道

[Git](/git)[提交 **Commit**](/commit)[合并 **Merge**](/merge)

**网上的项目**比电脑多 2 个新版本

下载并接上新版本pull*→*

**我的电脑**已经更新到最新

git pull

Pull 用在“电脑里已经有这个项目”之后：它把网上新增的版本取回，再接到你当前的版本线上。操作前先保存或收好手头改动。

### 什么时候用

- 开始协作前先取得网上的最新版本，减少之后的冲突

  **$** **git status --short**（没有输出，工作区干净）**$** **git pull**Fast-forward
- Pull 前先查看当前状态，保存或收好未完成改动

  设备 A 💻 push→☁️→设备 B 💻 pull
- 第一次取得仓库用clone，之后同步新增版本再用 Pull

  clone首次：复制工作文件与仓库历史

  pull后续：获取并整合远程更新
- 完成后运行项目，确认新版本在本机仍然正常

  **$** **git pull**Auto-merging index.htmlCONFLICT (content): Merge conflict in index.html拉取后也可能发生冲突，需要手动解决

### 什么时候不用

- 手头有混乱的半成品时直接 Pull，把两批改动搅在一起

  队友已推 12 个新提交本地仍是旧版本

  长期不同步远端，会扩大分支差异并增加合并冲突
- 遇到冲突就随意选择一边，而不理解双方修改

  Automatic merge failed;fix conflicts and then commit the result.**(main|MERGING) $** 冲突尚未处理
- 每次想更新都重新 Clone，制造多个重复项目文件夹

  pull 后有 3 个文件变化未检查改动

  继续修改可能覆盖协作者已经完成的工作
- 把 Pull 当成恢复工具；它不能找回从未 Commit 的本地改动

  **$** **git pull**Already up to date.未保存到 Git 历史的改动不会被取回

组成结构 · Anatomy

☁️ 远程仓库*GitHub 上的新提交*
git fetch →
🗄 本地仓库*先下载，不动你的文件*
git merge →
💻 工作区*新代码合进来*

1远程仓库Remote远程分支保存协作者已推送的提交

2获取Fetch将新提交下载到本地仓库，不修改工作目录文件

3本地仓库Local Repo获取的提交先保存于本地仓库，等待合并或变基

4合并Merge将获取的提交整合到当前分支，此时可能发生冲突

5工作区Working Dir合并完成后，工作目录更新为当前分支的文件版本

常见变体 · Variants

拉取更新git pull

git status && git pull

先确认工作区，再和远程对齐

仅获取git fetch

git fetch

获取远程更新，但暂不合并到当前分支

拉了最新up to date

Already up to date.

看到这句说明本地已是最新

典型使用场景

终端 git pull 获取更新

zsh — my-first-page

**$** **git pull**
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
Updating a3f9c21..e7b2d48
Fast-forward
 index.html | 12 +++++++-----
 1 file changed, 7 insertions(+), 5 deletions(-)

pull 发生冲突

zsh — my-first-page

**$** **git pull**
Auto-merging index.html
CONFLICT (content): Merge conflict in index.html
Automatic merge failed; fix conflicts and then commit the result.
打开冲突文件手选版本，再 add + commit 收尾

clone 与 pull 的区别

git clone

第一次：整个仓库连全部历史下载到本地

📦 36 个对象 · 包含提交历史

git pull

之后每次：获取本地尚未拥有的远程更新

📄 1 个文件 · 增量更新

两台设备通过 push 和 pull 同步

🏢💻

下班前  
**git push**

→

☁️

GitHub  
云端仓库

→

🏠💻

到家坐下  
**git pull**

两台设备完成 push 与 pull 后，可获得相同的提交历史

延伸阅读 · 权威出处

[git-pull 官方文档git-scm ↗](https://git-scm.com/docs/git-pull)[使用远程仓库（Pro Git）git-scm ↗](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes)
