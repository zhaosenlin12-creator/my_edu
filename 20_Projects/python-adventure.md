---
type: project
status: active
domain: game,teaching
audience: student,parent,teacher
repo: zhaosenlin12-creator/python-adventure（GitHub 命名）
local_path: C:\kaifa\game-google
url: https://game.codebn.cn
server_ip: 120.26.114.244
dossier: "[[60_Assets/dossiers/python-adventure]]"
updated_at: 2026-07-27
tags: nextjs,phaser,pyodide,fastapi,deepseek,teaching
---

# python-adventure · Python 冒险岛

> **证据第一**：详情看 [[60_Assets/dossiers/python-adventure]]。

## 一句话
**面向宜昌猇亭小学生的 Python 学习游戏**：Next.js 16 + React 19 + Phaser 3 + Pyodide + FastAPI 全栈，DeepSeek AI 自动出题、按年龄段切题库、宜昌本土地理文化塞进战役。

## 状态
- 本地仓：C:\kaifa\game-google
- 远程仓：zhaosenlin12-creator/python-adventure（GitHub 总账未列，可能私有）
- 部署：game.codebn.cn / 前端 3003 (PM2 id=3) / 后端 8000 (PM2 id=4)
- 版本：package.json v2.3.0，README v2.4.7（**不一致**）
- 启动：本地后端 `python init_db_quick.py && python run.py`；前端 `npm install && npm run dev`

## 技术栈（实测自 package.json）
- Next.js ^16.2.6 + React 19.2.0 + react-dom 19.2.0
- Phaser ^3.90.0 + Pyodide ^0.29.0
- framer-motion ^12.23.24 + lottie-react ^2.4.1 + @react-spring/web ^10.0.3
- @monaco-editor/react ^4.7.0
- canvas-confetti + react-window + tailwindcss ^4 + zustand ^5.0.8
- 后端：FastAPI + SQLAlchemy + SQLite
- 测试 / 质量：jest ^29 / ts-jest / fast-check / @playwright/test ^1.58.2 / eslint ^9

## 三大模式
| 模式 | 内容 |
|---|---|
| 章节模式 | 8 大章节 40+ 关卡，Python 基础 / 逻辑 / 循环 / 函数 |
| 战役模式 | 10 大战役，平台跳跃 + 重力翻转 + Boss 战 + 风力系统 |
| 开放世界 | 自由探索猇亭地图，与 NPC 互动 |

## 年龄分段（lib/questionBank/）
- 小学低年级 (1-3) / 小学高年级 (4-6) / 初中 (7-9)
- 10 个科目：数学 / 语文 / 英语 / 物理 / 化学 / Python / Scratch / 趣味推理 / 趣味历史 / 科学常识
- 物理 / 化学只对初中显示

## AI 智能出题（v2.3.0, 2024-12-28）
- 5 个模板：口算 / 成语 / 单词 / 脑筋急转弯 / 历史趣闻
- 后端读 `backend/.env` 里的 `DEEPSEEK_API_KEY` / `DEEPSEEK_API_URL` / `DEEPSEEK_MODEL`
- 生成结果可预览、编辑、选择性导入

## 安全机制（v2.3.0）
- JWT Token 黑名单（登出后立即失效）
- WebSocket 身份验证（PVP / 开放世界）
- bcrypt 密码哈希，兼容旧密码自动升级
- PVP 60s 内最多建 3 个房间
- 创意工坊 XSS 消毒

## 后端（backend/app/api/v1/）共 32 个路由
pets.py 26976 / pvp.py 33475 / pvp_battle_royale.py 66956 / typing.py 25847 / world.py 30098 是重头
29 个 SQLAlchemy 模型：user / character / pet / decoration / food / skill / task / quiz_battle / custom_level / battle / chat / coin / user_question / progress / achievement / dynamic_task / ai_robot / typing / user_location / error_log ...

## 部署强约束（MAINTENANCE.md）
1. Node 必须指定版本：`/www/server/nodejs/v20.19.6/bin/node`
2. Python 必须用项目 venv：`/www/wwwroot/game-backend/venv/bin/python`
3. 生产数据库在 `/www/data/game-backend/code_adventure.db`，**绝不能覆盖**
4. **不要 `pkill -9 -f python`**（会杀宝塔面板），只杀 `kill $(lsof -t -i:8000)`
5. 唯一部署准则：`deploy/DEPLOY_SERVER_EXACT.md`
6. 前端必须指定端口 3003，否则 502
7. PM2 改完必须 `pm2 save`
8. 更新前端必须 `rm -rf /www/server/nginx/proxy_cache_dir/*` + `nginx reload`

## 下一步
- [ ] 把 package.json 版本与 README 对齐
- [ ] 用本地 LLM 替掉 DeepSeek 出题
- [ ] 宠物聊天本地预制对话做成独立模块
- [ ] 删 deploy/ 旧脚本，只留 DEPLOY_SERVER_EXACT.md
- [ ] PVP / 开放世界监控接入 PM2 + 飞书/钉钉告警

## 关联
- [[60_Assets/dossiers/python-adventure]]
- [[20_Projects/open_leqixiang]]
- [[20_Projects/senlin_website]]
- [[30_Teaching/index]]（AI 出题对接教学）