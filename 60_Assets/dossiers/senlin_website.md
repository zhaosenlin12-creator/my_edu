---
type: dossier
status: active
domain: project,web,business
audience: self
repo: zhaosenlin12-creator/senlin_website
local_path: C:\kaifa\my_website
url: https://senlin-c1n.pages.dev
related: "[[20_Projects/senlin_website]]"
updated_at: 2026-07-27
tags: project,dossier,express,mysql,supabase,ai-proxy
---

# Dossier · 智创未来编程学院（my_website / senlin_website）

> 这是我从 package.json / server.js / ai-proxy.js / .env.example 读到的事实。**注意**：GitHub 上叫 `senlin_website`，本地叫 `my_website`，package.json 内部名 `robotdoctor-tech-website`。

## 一句话
**机构门面 + 业务承接站**：Express + MySQL 主站（3000），Node 写的小型 AI 代理（3001）只允许白名单 origin（codebn.cn / codebona.cn）调用 DeepSeek。还有 Supabase / Netlify 两套部署选项（看 netlify.toml 是 . 当前目录直接 publish）。

## 仓库与本地
- 本地仓：C:\kaifa\my_website
- 远程仓：zhaosenlin12-creator/senlin_website
- 主域名：senlin-c1n.pages.dev（Cloudflare Pages） + senlinwebsite.vercel.app 备用
- 业务域名：codebn.cn / codebona.cn / codebona.cn
- 部署：服务器 `/var/www/codebn`，PM2 ecosystem.config.js

## 技术栈（来自 package.json）
- Node.js >=14
- Express ^4.18.2 + cors ^2.8.5 + dotenv ^17.2.1 + uuid ^9.0.1
- MySQL via mysql2 ^3.14.3
- Supabase JS ^2.56.0（可选）
- nodemon ^3.0.1（dev）
- 关键词（来自 keywords 列表）：科技比赛 / 特长生 / NOIP / 机器人竞赛 / 宜昌 / 猇亭区

## 后端路由与中间件（来自 server.js）
- MySQL 连接池：`utf8mb4` / `connectionLimit: 10` / 自动 ping
- CORS 白名单：env `ALLOWED_ORIGINS`，默认 `codebn.cn` 系列 + localhost
- 文件访问黑名单：`BLOCKED_FILES = /.env, /server.js, /package.json, /package-lock.json, /contacts.json, /quick_contacts.json, /ecosystem.config.js, /start-all.js`，前缀禁 `node_modules/` 和 `.git/`
- 管理员登录：`/api/admin-login`，username/password（明文 ADMIN_CREDENTIALS），token 持久化到 `data/admin-tokens.json`（重启不丢）
- 频率限制：1 秒内同 IP 最多 10 次 `POST /api/*`，超过 429
- 访问记录：visits 表（user_id / page / action_type / browser / device / user_agent / referrer / item_id / ip_address）
- AI 代理路由：`/api/chat` 转发到 `http://localhost:3001/api/chat`
- 安全：`aes-256-cbc` 解密 env（密钥截前 32 位）

## AI 代理（ai-proxy.js 独立进程）
- 端口 3001
- origin 校验：`http://localhost:3000` / `https://codebona.cn` / `http://codebona.cn`
- DeepSeek：`deepseek-chat` + systemPrompt + max_tokens 200 + temperature 0.3 + top_p 0.95
- **API key 用 base64 编码**：`sk-66b7d339bd1146b3b0de45dbbcaaa22a` → ⚠️ 严重安全漏洞，应改用 env

## 关键脚本
- `start-all.js`：spawn 两个进程（mainServer + aiProxy），统一优雅关闭 SIGINT/SIGTERM
- `ecosystem.config.js`：PM2 配置，cwd `/var/www/codebn`，max_memory_restart 1G
- `netlify.toml`：publish `.` / build command 空（说明 Cloudflare / Netlify 直接部署静态文件）
- `mysql-client.js`：9568 字节，封装数据库查询

## 关键文件大小
- admin-dashboard.html 92KB（管理后台 UI）
- admin-dashboard.js 48KB
- index.html 88KB（主页）
- script.js 32KB（主页交互）
- server.js 32KB（API 主入口）
- styles.css 25KB
- competitions.html 123KB（赛事页面）
- booking.html 37KB

## 真实风险（从代码 + Codex 会话总结出来）
- AI API key 用 base64 编码而不是真加密 → 必须切到 env 或 KMS
- 管理员账号密码在代码里硬编码 → 必迁到 env
- admin-tokens.json 持久化到明文 → 加 hash
- CORS / 文件黑名单虽然有，但 origin 校验宽松（用 `.includes` 匹配 host 名），`http://localhost:3000` 允许任意端口
- ai-proxy.js 把 origin 校验和 API 转发耦合在一起，不好测

## 我从这里学到的能力
- Express 中间件链：CORS / 静态 / 鉴权 / 限流 / 黑名单
- 把 AI 代理拆成独立服务（避免泄漏主站代码 + 便于限流）
- 文件型 token 持久化（重启不丢）
- PM2 ecosystem 配置 + Nginx + Cloudflare Pages / Netlify 多端部署
- 业务域关键字 SEO（keywords 数组）

## 下一步可做
- [ ] 把 ai-proxy 的 API key 改成读 env，并把 base64 行删了
- [ ] 把管理员密码从硬编码迁到 `ADMIN_PASSWORD` env
- [ ] 把文件型 token 改成 DB 或 Redis
- [ ] 给 server.js 加 helmet / hpp / compression
- [ ] 给 bookings / competitions 单独拆数据库表