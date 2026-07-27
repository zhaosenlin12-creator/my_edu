---
type: dossier
status: active
domain: project,game,teaching
audience: self
repo: zhaosenlin12-creator/python-adventure（GitHub 命名）
local_path: C:\kaifa\game-google
url: https://game.codebn.cn
related: "[[20_Projects/python-adventure]]"
updated_at: 2026-07-27
tags: project,dossier,nextjs,phaser,pyodide,fastapi,teaching
---

# Dossier · Python 冒险岛（game-google / python-adventure）

> 这是我从 package.json / README.md / MAINTENANCE.md / 后端路由表读到的事实。版本以 package.json 的 2.3.0 为准，README 写的 v2.4.7 是面向用户的发布号。

## 一句话
**面向宜昌猇亭小学生的 Python 学习游戏**，Next.js 16 + React 19 + Phaser 3 + Pyodide + FastAPI 全栈，配 DeepSeek AI 自动出题、按年龄段切题库、把宜昌本土地理文化塞进战役。

## 仓库与本地
- 本地仓：C:\kaifa\game-google
- 远程仓：zhaosenlin12-creator/python-adventure（GitHub 总账里没列，说明仓可能私有）
- 启动：本地后端 `python init_db_quick.py && python run.py`；前端 `npm install && npm run dev`
- 服务器：120.26.114.244 / game.codebn.cn / 前端 3003 (PM2 id=3) / 后端 8000 (PM2 id=4)

## 技术栈（来自 package.json）
- Next.js ^16.2.6 + React 19.2.0 + react-dom 19.2.0
- Phaser ^3.90.0（游戏引擎）+ Pyodide ^0.29.0（浏览器跑 Python）
- framer-motion ^12.23.24 + lottie-react ^2.4.1 + @react-spring/web ^10.0.3
- @monaco-editor/react ^4.7.0（代码编辑器）
- canvas-confetti + react-window + tailwindcss ^4
- zustand ^5.0.8 状态管理
- eslint / fast-check / jest ^29 / ts-jest / @playwright/test（测试与质量）
- 后端 FastAPI + SQLAlchemy + SQLite（MAINTENANCE.md 第 80 行）

## 三大模式（README + lib/campaigns*）
| 模式 | 内容 |
|---|---|
| 章节模式 | 8 大章节 40+ 关卡，Python 基础、逻辑、循环、函数 |
| 战役模式 | 10 大战役，平台跳跃 + 重力翻转 + Boss 战 + 风力系统 |
| 开放世界 | 自由探索猇亭地图，与 NPC 互动 |

## 年龄分段（lib/questionBank/）
- 小学低年级 (1-3 年级) / 小学高年级 (4-6 年级) / 初中 (7-9 年级)
- 10 个科目：数学 / 语文 / 英语 / 物理 / 化学 / Python / Scratch / 趣味推理 / 趣味历史 / 科学常识
- 物理 / 化学只对初中显示

## AI 智能出题（v2.3.0, 2024-12-28）
- 5 个快捷模板：口算练习 / 成语填空 / 单词拼写 / 脑筋急转弯 / 历史趣闻
- 后端读 `backend/.env` 里的 `DEEPSEEK_API_KEY` / `DEEPSEEK_API_URL` / `DEEPSEEK_MODEL`
- 生成结果可预览、编辑、选择性导入

## 安全机制（v2.3.0）
- JWT Token 黑名单（登出后立即失效）
- WebSocket 身份验证（PVP / 开放世界）
- bcrypt 密码哈希，兼容旧密码自动升级
- PVP 60s 内最多建 3 个房间
- 创意工坊 XSS 消毒

## 后端路由（backend/app/api/v1/）共 32 个
ai_questions / auth / battle_ws / battles / chat / coins / community / custom_levels / daily / decorations / error_logs / food / interactions / inventory / leaderboard / learning_assistant / pet_chat / pets / pvp / pvp_battle_royale / skills / tasks / typing / user_questions / users / workshop / world / achievements / admin
- pets.py 26976 字节（最大业务模块）
- pvp.py 33475 / pvp_battle_royale.py 66956 / typing.py 25847 / world.py 30098 都是重头

## 服务模型（models/）共 29 个
user / character / pet / pet_eggs / decoration / food / inventory / map_object / map_region / skill / task / task_submission / teacher / quiz_battle / custom_level / level_like / battle / chat / coin / user_question / user_skill / user_task / progress / achievement / dynamic_task / ai_robot / typing / user_location / error_log

## 部署强约束（MAINTENANCE.md 第 50-80 行）
1. Node 必须指定版本：`/www/server/nodejs/v20.19.6/bin/node`
2. Python 必须用项目 venv：`/www/wwwroot/game-backend/venv/bin/python`
3. 生产数据库在 `/www/data/game-backend/code_adventure.db`，**绝不能覆盖**
4. 宝塔面板在 8000 端口，**不要 `pkill -9 -f python`**，只杀 `kill $(lsof -t -i:8000)`
5. 部署唯一准则：`deploy/DEPLOY_SERVER_EXACT.md`，旧 quick-deploy.sh 已废弃
6. 前端必须指定端口 3003，否则 502
7. PM2 改完必须 `pm2 save`
8. 更新前端必须 `rm -rf /www/server/nginx/proxy_cache_dir/*` + `nginx reload`

## 真实运行 SOP（MAINTENANCE.md 验证项）
- PVP “简单”模式 AI 是否足够缓慢
- 血包功能：拾取血包回复 10-20 HP
- 复活逻辑：测试模式下死亡是否弹出答题弹窗
- 保存关卡：创建一个带血包的关卡并确认后端不报错

## 已知风险与卡点（来自 Codex 会话 + 维护文档）
- README 与 package.json 版本不一致（README v2.4.7 vs package.json v2.3.0）
- v2.4.8 引入金币奖励系统（`Transaction ID` 防重放），MAINTENANCE 标记为重要升级
- `deploy/` 目录下的脚本应该已经统一到 DEPLOY_SERVER_EXACT.md，但旧脚本还散落
- 启动 `start-game.ps1` / `stop-game.ps1` 走 PM2，部署脚本走宝塔面板，两套并存

## 我从这里学到的能力
- Next.js 16 + React 19 的 SSR/RSC 实战（含 Phaser 这种 client-only 包）
- 用 Pyodide 把 Python 跑进浏览器，做 in-game 代码执行
- FastAPI 后端用 JWT + bcrypt + WebSocket 整套鉴权
- 把“按年龄段分流”做到数据层（分题库 + 分课程）
- 复杂游戏版本管理：CI 出包 → 宝塔传包 → PM2 重启 → Nginx 缓存清理

## 下一步可做
- [ ] 把 package.json 版本与 README 对齐（v2.4.7 还是 v2.4.8）
- [ ] 给 v2.5 计划：用本地 LLM 替掉 DeepSeek 出题，省 token 钱
- [ ] 把宠物聊天本地预制对话做成独立模块（README 已说 v2.4.7 在用）
- [ ] 把 deploy/ 旧脚本删掉，只留 DEPLOY_SERVER_EXACT.md
- [ ] 把 PVP / 开放世界监控接入 PM2 + 飞书 / 钉钉告警

## 事实 / 推断 / 待确认

### 事实(可验证)
- package.json v2.3.0, README v2.4.7(不一致)
- Next.js 16.2.6 + Phaser 3.90 + Pyodide 0.29
- 后端 32 个路由(pets.py 26976 字节最大)
- 29 个 SQLAlchemy 模型
- 部署在 game.codebn.cn 120.26.114.244
- PM2 id=3(前端 3003) / id=4(后端 8000)
- DEEPSEEK_API_KEY 在 backend/.env

### 推断(基于事实,但要警惕)
- v2.4.7 是用户面向的发布号,v2.3.0 是 package.json
- v2.4.8 引入金币奖励系统(MAINTENANCE 提到)
- 学员群体是宜昌猇亭小学生

### 待确认(下次更新时核实)
- v2.5 是否要做本地 LLM 替 DeepSeek
- PVP 简单模式 AI 难度数据
- 学员真实日活数据
