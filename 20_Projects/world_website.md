---
type: project
status: active
domain: web,3d,interactive
audience: parent,teacher,student
repo: zhaosenlin12-creator/world_website
local_path: C:\kaifa\world_website（C:\kaifa_senlin\world_website 是副本）
url: https://senlin-c1n.pages.dev
dossier: "[[60_Assets/dossiers/world_website]]"
updated_at: 2026-07-27
tags: nextjs,three,r3f,framer-motion,3d
---

# world_website · 宇宙探索互动站

> **证据第一**：详情看 [[60_Assets/dossiers/world_website]]。

## 一句话
**3D 宇宙探索互动站**：Next.js 14 + React 18 + Three.js + R3F 8 + drei 9，纯前端无后端，太阳系动画 / 行星点击 / 飞船降落 / 地表采样 / 多阶段任务。

## 状态
- 本地仓：C:\kaifa\world_website（另一个副本 C:\kaifa_senlin\world_website，**未定主仓**）
- 远程仓：zhaosenlin12-creator/world_website（2026-07-07 最近更新）
- 部署：Cloudflare Pages（senlin-c1n.pages.dev）
- 启动：`npm run dev` (next dev -p 3000)

## 技术栈（实测自 package.json）
- Next.js 14.2.15 + React 18.3.1 + react-dom 18.3.1
- three 0.169.0 + @react-three/fiber 8.17.10 + @react-three/drei 9.117.0
- framer-motion 11.11.10
- TypeScript 5.6.3 + Tailwind 3.4.14
- @types/react 18.3.12 / @types/node 22.7.5 / @types/three 0.169.0

## 关键页面
- 首页：`/`（3D 太阳系 + 宇宙动画）
- 游戏页：`/play`
- 调试入口：`/play?qa=1`

## 自检脚本（来自 README）
- `npx tsx scripts/test-descent-flight.ts`（飞船降落飞行测试）
- `npx tsx scripts/surface-runtime-check.ts`（地表运行时检查）
- `npx tsx scripts/surface-component-stability-check.ts`（地表组件稳定性）
- `npx tsx scripts/surface-boost-check.ts`（地表加速检查）

## Codex 会话中的演化
- 用户多次让 Codex“进入博物馆之后改成长廊的样式，墙上挂上真实宜昌博物馆的真实经典馆藏的文物照片”
- Codex 用 Vite + TypeScript + Three.js 路线，找到“楚季”铜甬钟 / 虎钮錞于 / 春秋木质建鼓等真实馆藏作为素材
- 项目本地不是 git 仓库（所以改完没历史）

## 下一步
- [ ] 决定主仓是 C:\kaifa\world_website 还是 C:\kaifa_senlin\world_website，删另一个或合并
- [ ] 把宜昌博物馆真实馆藏做成 ContentBundle，跟 open_leqixiang 一样
- [ ] Playwright 端到端：降落到地表 → 旋转 → 离开
- [ ] tsx 检查脚本改成 vitest，跑进 npm test

## 关联
- [[60_Assets/dossiers/world_website]]
- [[20_Projects/open_leqixiang]]（同样 Vite + React + 数据驱动思路）
- [[20_Projects/img2threejs]]（3D 资源补充）
- [[30_Teaching/宇宙探索营]]（待建）