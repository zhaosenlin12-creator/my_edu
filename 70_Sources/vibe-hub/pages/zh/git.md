---
type: web_source
source_url: "https://vibe-hub.org/git"
title: "Git"
language: zh
category: "git"
fetched_at: 2026-07-27T10:04:14+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←差异对比提交→

# Git

你可能会说

AI 把我的代码改崩了，我想回到上一个能用的版本。

**Git 是在本地记录文件版本历史、比较改动并协作同步的版本控制工具**·例如，完成并检查首页导航后，可以用commit把相关改动保存成一个本地版本，以后查看或恢复；只有push后 GitHub 才有副本。未 Commit 的改动不会自动进入历史。

先知道

[终端命令行 **Terminal**](/terminal)

也常被叫作*Git 版本控制**版本控制*

**页面改好了**还有未保存改动

保存一个版本commit*→*

✓**首页可以使用**以后能找回

同步一份到网上push*→*

**GitHub**远端也有一份

Git 记录版本，GitHub 保存远端副本

先把完成的小改动保存成版本；需要协作或备份时，再把已经保存的版本同步到 GitHub。未保存的改动不会自动进入历史。

### 什么时候用

- 每完成一个能运行的小改动，就保存一个有说明的版本

  init 初始化→add 选择改动→commit 记录版本
- 保存前先看改动清单，确认这次记录的内容正确

  每个稳定小步都可以成为一次提交
- 出现问题时，先查版本历史，再决定怎样恢复

  改动出现问题时可以回到之前的提交
- 需要协作或远端副本时，把已保存的版本推到 GitHub

  💻 本地仓库git push →☁️ GitHub

### 什么时候不用

- 连续改很多天却不保存版本，出问题后没有清楚的恢复点

  长时间没有提交记录，难以恢复稳定版本
- 版本说明只写“改了”“111”，之后看不出完成了什么

  ● 111  
  ● 改了下  
  ● asdf说明含义不清，之后难以定位版本
- 遇到问题就删除项目目录，本地版本历史也会一起丢失

  🗂my-first-page🗑 删除

  删除项目目录会同时丢失本地历史
- 把包含真实密钥的 .env 保存进版本历史

  .envgit push →☁️

  密钥会进入远程提交历史

组成结构 · Anatomy

💻 工作区*你正在改的文件*
git add →
📥 暂存区*选好这次要记录的改动*
git commit →
🗄 本地仓库*存档点在这*
git push →
☁️ 云端仓库*GitHub*

1工作区Working Dir你电脑上正在修改的文件，这些变化还没有进入版本历史

2暂存区Staginggit add 选择下一次 commit 要记录的改动，文件本身不会被搬走

3本地仓库Repositorygit commit 把暂存区内容写进本地历史，生成带编号和说明的记录

4远程仓库Remotegit push 后远程才会收到本地的新提交，可用于协作和异地副本

典型使用场景

GitHub 提交记录页

Commits · main

狸

导航栏在手机上错位

10 分钟前

c7d8e9f

狸

首页能跑了 ✓

2 小时前

a1b2c3d

狸

初始化项目

3 天前

0f1e2d3

终端里 git log 翻历史

zsh — my-first-page

**$** **git log --oneline**
c7d8e9f 导航栏在手机上错位
a1b2c3d 首页能跑了 ✓
0f1e2d3 初始化项目
每行一个存档点：前面是编号，后面是说明

回滚到上一个 commit

zsh — my-first-page

**$** **git revert c7d8e9f**
[main f4e5d6c] Revert "AI 改导航栏"
新增一条反向提交，旧历史仍然保留

GitHub 仓库首页

my-first-page
<> Code ▾

📄 index.html首页能跑了 ✓2 小时前

📄 README.md初始化项目3 天前

📄 .gitignore初始化项目3 天前

延伸阅读 · 权威出处

[Pro Git 官方书籍git-scm ↗](https://git-scm.com/book/en/v2)[Git 命令参考git-scm ↗](https://git-scm.com/docs)
