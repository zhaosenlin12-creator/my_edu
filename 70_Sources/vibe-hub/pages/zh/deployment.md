---
type: web_source
source_url: "https://vibe-hub.org/deployment"
title: "部署上线 Deployment"
language: zh
category: "deployment"
fetched_at: 2026-07-27T10:04:15+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←环境变量持续交付 / 持续部署→

# 部署上线Deployment

你可能会说

我做好了，怎么才能让别人用一个网址就能打开我的页面？

**部署是把项目构建并发布到目标运行环境、让预期用户或系统能够使用的过程**·例如，平台可从仓库取得源码，执行构建或启动服务，再发布到测试、内部或公开环境。静态网站常得到访问网址，后端服务、定时任务或内部应用则未必公开。发布前要确认目标环境、构建与启动方式、输出目录和环境变量；失败时先查看日志。

先知道

[终端命令行 **Terminal**](/terminal)[npm](/npm)[环境变量 **Env Var**](/env-var)[域名 **Domain**](/domain)

本地文件
*→*
build 打包
*→*
托管平台
*→*
my-app.vercel.app

这是公开静态前端的示例；服务部署还需要运行与访问配置

### 什么时候用

- **确认构建或启动方式**：静态前端要看输出目录；服务还要看启动命令、端口和运行时

  📄 源码npm run build →📦 dist 成品
- 根据静态网站、长期运行服务、定时任务或内部应用等项目类型选择托管平台

  VercelNetlifyGitHub Pages
- **连 git 仓库自动部署**：按配置匹配的分支 push 可触发构建和发布

  git push☁️ 自动重新上线

  配置了仓库、分支和构建规则后，匹配的 push 才会触发发布
- **公开网站绑定自己的domain**：平台给的网址可换成你的域名

  my-app-x8k2.vercel.appwww.mysite.com平台给的网址能换成自己的域名

### 什么时候不用

- 不要把 localhost 地址当作已部署版本；它通常只在当前电脑上可用

  http://localhost:3000
- 双击 html **能打开不等于已经部署**：file:// 指向本机文件，不是可共享的部署地址

  file:///Users/…/index.html
- **不看平台配置就上传**：构建命令或输出目录错了，线上就会失败

  ⚙ 构建命令 / 输出目录填错→失败
- 上线后**不做正式环境验收**：资源 404、环境变量缺失等问题会直接出现在正式页面

  图片 404未做线上验收，资源路径和环境变量问题可能影响正式页面

组成结构 · Anatomy

💻源码
→
📦打包产物
→
☁️托管平台
→
🌐公网网址

1源码Source你写的或 AI 生成的源文件，浏览器不一定直接能跑

2打包产物Build Output静态前端常生成 dist；服务项目也可能由平台从源码构建并启动

3目标平台Runtime Platform平台按配置托管静态文件、函数或服务，并提供相应运行环境

4访问地址URL公开网站通常有平台分配的地址；内部服务可能只在私网或服务间访问

常见变体 · Variants

Vercel / NetlifyVercel & Netlify

vercel --prod

前端项目常用；函数和服务能力要看具体平台与套餐

GitHub PagesGitHub Pages

Settings → Pages

为仓库提供静态网站托管；权限和可用功能以当前方案为准

自建服务器VPS

ssh user@1.2.3.4

需要长期运行服务，并能自行维护系统与部署时

典型使用场景

Vercel 部署成功页

🎉

Congratulations!

my-first-page 部署成功

页面预览

my-first-page.vercel.app

Visit →

终端 npm run build

zsh — my-first-page

**$** **npm run build**
vite v6.0.0 building for production…
dist/index.html   0.5 kB
dist/assets/index-8fk2.js   142 kB
✓ built in 3.2s
dist 是此静态前端构建生成的输出目录

push 触发自动部署

Deployments

首页构建通过 ✓

1 分钟前 · 由 git push 触发

Ready

初始化项目

3 天前 · 由 git push 触发

Ready

浏览器打开公网网址

🔒 https://my-first-page.vercel.app

**小狸的主页**

我喜欢爬山和拍照。

看我的相册 →

🌐 公开部署时，这个网址可被外部访问

延伸阅读 · 权威出处

[发布你的网站MDN ↗](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website/Publishing_your_website)
