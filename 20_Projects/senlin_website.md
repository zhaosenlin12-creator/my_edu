---
type: project
status: active
domain: web,business,brand
audience: parent,teacher,student
repo: zhaosenlin12-creator/senlin_website
local_path: C:\kaifa\my_website
url: https://senlin-c1n.pages.dev
business_url: https://codebn.cn / https://codebona.cn
dossier: "[[60_Assets/dossiers/senlin_website]]"
updated_at: 2026-07-27
tags: express,mysql,supabase,ai-proxy,brand
---

# senlin_website · 智创未来编程学院

> **证据第一**：详情看 [[60_Assets/dossiers/senlin_website]]。注意：GitHub 叫 `senlin_website`，本地叫 `my_website`，package.json 内部叫 `robotdoctor-tech-website`，业务域名 codebn / codebona。

## 一句话
**机构门面 + 业务承接站**：Express + MySQL 主站（3000），独立 AI 代理（3001）只允许白名单 origin 调 DeepSeek，关键词围绕“科技比赛 / 特长生 / NOIP / 机器人竞赛 / 宜昌 / 猇亭区”。

## 状态
- 本地仓：C:\kaifa\my_website
- 远程仓：zhaosenlin12-creator/senlin_website
- 主域名：senlin-c1n.pages.dev（Cloudflare Pages） / senlinwebsite.vercel.app 备用
- 业务域名：codebn.cn / codebona.cn / codebona.cn
- 部署：PM2 ecosystem.config.js（cwd `/var/www/codebn`，max_memory_restart 1G）

## 技术栈（实测自 package.json）
- Node.js >=14
- Express ^4.18.2 + cors ^2.8.5 + dotenv ^17.2.1 + uuid ^9.0.1
- mysql2 ^3.14.3
- @supabase/supabase-js ^2.56.0（可选）
- nodemon ^3.0.1（dev）

## 后端（server.js 32KB）
- MySQL 连接池（utf8mb4 / connectionLimit 10 / 自动 ping）
- CORS 白名单（env `ALLOWED_ORIGINS`，默认 codebn.cn 系列 + localhost）
- 文件访问黑名单：`/.env` / `/server.js` / `/package.json` 等
- 管理员登录：`/api/admin-login`，token 持久化到 `data/admin-tokens.json`（重启不丢）
- 频率限制：1 秒内同 IP 最多 10 次 `POST /api/*`，超过 429
- 访问记录：visits 表
- AI 代理路由：`/api/chat` 转发到 `http://localhost:3001/api/chat`
- 安全：`aes-256-cbc` 解密 env（密钥截前 32 位）

## AI 代理（ai-proxy.js 独立进程）
- 端口 3001
- origin 校验：localhost:3000 / codebona.cn
- DeepSeek：`deepseek-chat` + max_tokens 200 + temperature 0.3 + top_p 0.95
- ⚠️ **API key 用 base64 编码**（`sk-66b7d339bd1146b3b0de45dbbcaaa22a`），严重安全漏洞

## 关键文件
- admin-dashboard.html 92KB + admin-dashboard.js 48KB（管理后台）
- index.html 88KB + script.js 32KB（主页）
- server.js 32KB + styles.css 25KB
- competitions.html 123KB（赛事页面）+ booking.html 37KB

## 下一步
- [ ] ai-proxy 的 API key 改用 env，删 base64 行
- [ ] 管理员密码从硬编码迁到 `ADMIN_PASSWORD` env
- [ ] 文件型 token 改成 DB 或 Redis
- [ ] 加 helmet / hpp / compression
- [ ] bookings / competitions 单独拆表

## 关联
- [[60_Assets/dossiers/senlin_website]]
- [[20_Projects/open_leqixiang]]
- [[20_Projects/python-adventure]]
- [[40_Content/curerforest-channel]]（抖音承接入口）