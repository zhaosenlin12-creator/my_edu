---
type: project
status: active
domain: system
audience: teacher,manager,parent
repo: zhaosenlin12-creator/codebn-system
url: https://codebn.com
summary: 乐启享机构系统（Web 后台 + 微信小程序 + 教务 + 部署运维）
next_action: 生产部署重构 + 学员变动同步稳定化
updated_at: 2026-07-27
tags: system,prisma,next,ops
---

# codebn-system（乐启享机构系统）

> 乐启享的核心业务系统：机构管理、教师跟课、家长查看、微信小程序联动。

## 状态
- 本地仓：C:\kaifa\codebn-system-git
- 远端：zhaosenlin12-creator/codebn-system
- 当前分支：codex/contract-credit-governance-20260701
- 本地：dirty

## 技术栈
- Next.js 15 + Prisma + libSQL（本地 SQLite / 生产 Postgres）
- Radix UI + Tailwind（按需开启）
- Vitest + Playwright

## 下一步
- [ ] 部署脚本稳定化（runbook 已生效）
- [ ] 小程序路由审计 / 路由护栏
- [ ] 学员变动同步：审计 → 修复一键化