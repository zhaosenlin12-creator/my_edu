---
type: dossier
status: active
domain: project,web,3d
audience: self
repo: zhaosenlin12-creator/world_website
local_path: C:\kaifa\world_website（C:\kaifa_senlin\world_website 是副本）
url: https://senlin-c1n.pages.dev
related: "[[20_Projects/world_website]]"
updated_at: 2026-07-27
tags: project,dossier,nextjs,three,r3f,3d
---

# Dossier · 宇宙探索互动站（world-website）

> 这是我从 package.json + README 读到的事实。本地两个副本（C:\kaifa\world_website + C:\kaifa_senlin\world_website），GitHub 仓库 zhaosenlin12-creator/world_website。

## 一句话
**3D 宇宙探索互动站**：Next.js 14 + React 18 + Three.js + R3F 的前端项目，做太阳系动画、行星点击、飞船降落到地表采样等“多阶段任务体验”，**完全是前端 + 浏览器渲染**，没有后端。

## 仓库与本地
- 本地仓：C:\kaifa\world_website（另一个副本 C:\kaifa_senlin\world_website）
- 远程仓：zhaosenlin12-creator/world_website（GitHub 总账显示 2026-07-07 最近更新）
- 部署：Cloudflare Pages（senlin-c1n.pages.dev 域名下，与个人站共部署）
- 启动：`npm run dev` (next dev -p 3000) / `npm run build` / `npm run start` / `npm run lint`

## 技术栈（来自 package.json）
- Next.js 14.2.15 + React 18.3.1 + react-dom 18.3.1
- three 0.169.0
- @react-three/fiber 8.17.10 + @react-three/drei 9.117.0
- framer-motion 11.11.10
- TypeScript 5.6.3 + Tailwind 3.4.14 + PostCSS 8.4.47 + autoprefixer 10.4.20
- @types/react 18.3.12 / @types/node 22.7.5 / @types/three 0.169.0
- eslint 8.57.1 + eslint-config-next 14.2.15

## 关键页面
- 首页：`/`（3D 太阳系 + 宇宙动画）
- 游戏页：`/play`
- 调试入口：`/play?qa=1`

## 项目自检脚本（README 列出）
- `npx tsx scripts/test-descent-flight.ts`（飞船降落飞行测试）
- `npx tsx scripts/surface-runtime-check.ts`（地表运行时检查）
- `npx tsx scripts/surface-component-stability-check.ts`（地表组件稳定性）
- `npx tsx scripts/surface-boost-check.ts`（地表加速检查）

## Codex 会话上下文
- 会话频繁提到“进入博物馆之后改成长廊的样式，墙上挂上真实宜昌博物馆的真实经典馆藏的文物照片，玩家靠近之后文物上面会有交互按钮出现提醒进入，进入之后就开始讲解和打开该文物的精致特效模型的3D效果，可以控制画面放大所有看更多细节”
- 会话提到“宜昌博物馆官网“馆藏精品/藏品数据库”有多件藏品条目，人民日报海外版也明确提到“楚季”铜甬钟、虎钮錞于、春秋木质建鼓等真实展品”
- 项目目前不是 git 仓库（本地），只基于文件内容和测试结果

## 真实风险
- 同一个项目两个本地副本（C:\kaifa\world_website vs C:\kaifa_senlin\world_website），容易改 A 不改 B
- README 编码显示是 GBK 转出来的乱码（`涓€涓?` / `瀹囧畽`），但内部 README 实际是 UTF-8 + 中文，PowerShell 默认编码显示错位
- 启动卡 3000 端口：README 已经写 `npx next dev -p 3001` 兜底
- 项目不是 git 仓库，所以改完没历史；测试脚本也只能手跑

## 我从这里学到的能力
- Next.js 14 + R3F 8 搭建 3D 场景
- three.js 0.169 + @react-three/drei 9 用现成的相机 / 控制器 / 加载器
- 把 3D 场景拆成多个 surface 阶段，每个阶段配独立 tsx 检查脚本
- 用 framer-motion 做 2D 覆盖层交互

## 下一步可做
- [ ] 决定主仓是 C:\kaifa\world_website 还是 C:\kaifa_senlin\world_website，删另一个或合并
- [ ] 把宜昌博物馆真实馆藏做成 ContentBundle，跟 open_leqixiang 一样
- [ ] 加 Playwright 端到端：降落到地表 → 旋转 → 离开
- [ ] 把 tsx 检查脚本改成 vitest，跑进 npm test