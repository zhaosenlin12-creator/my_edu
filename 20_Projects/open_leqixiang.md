---
type: project
status: active
domain: web,education,kiosk
audience: parent,teacher,student
repo: （暂未推 GitHub）
local_path: C:\kaifa\open_leqixiang
url: （部署在局域网 / 内网大屏）
dossier: "[[60_Assets/dossiers/open_leqixiang]]"
updated_at: 2026-07-27
tags: vite,react,typescript,vitest,performance,kiosk
---

# open_leqixiang · 乐其翔展览系统

> **证据第一**：详情看 [[60_Assets/dossiers/open_leqixiang]]。

## 一句话
**机构展览大屏站**：Vite 7 + React 19 + TypeScript 5.9，把学生作品 / 课程 / 价格 / 教师能力铺在墙上，给家长、学生、来访者一个可点可看的“学校门面”。

## 状态
- 本地仓：C:\kaifa\open_leqixiang（**未推 GitHub**）
- package.json 内部名 `leqixiang-display-system`，版本 `0.1.0`
- README 只有标题（32 字节），AGENTS.md / CLAUDE.md 是 Karpathy LLM coding guidelines 复制粘贴
- 构建：`npm run build` = `tsc -b && vite build && postbuild-css-defer && emit-cache-headers`

## 技术栈（实测自 package.json）
- Vite ^7.2.7 + @vitejs/plugin-react ^5.1.1
- React ^19.2.1 + react-dom ^19.2.1 + TypeScript ^5.9.3
- lucide-react ^0.561.0
- Vitest ^4.0.15（dev）
- sharp ^0.35.2 + ffmpeg-static ^5.3.0（图片/视频处理）

## 强项（来自源码）
- 内容数据完全数据驱动：ContentBundle 12 个 JSON（site / modules / courses / tours / playlists / pricing / achievements / students / staff / assets + import.pdf + imported）
- 学生作品走 student-archive 单独目录（dist/content/students.json 仅 57 字节占位）
- 启动时预热学生档案：[src/main.tsx](file:///C:/kaifa/open_leqixiang/src/main.tsx) 调用 `warmStudentGallery(2000, 12)`（空闲 2 秒后预热前 12 张缩略图，防白屏 8x 闪烁）
- 大组件懒加载：HeroCarousel / CategoryStage / LayeredDrawer（[src/App.tsx:14-22](file:///C:/kaifa/open_leqixiang/src/App.tsx)）
- 自带 web-vitals 监控：[src/lib/perf.ts](file:///C:/kaifa/open_leqixiang/src/lib/perf.ts) 监听 LCP / CLS / INP + longtask，写入 50 条 ring buffer 到 `window.__leqxPerf`，**不上报网络**

## 已确认配置
- `StudentsConfig.policy: 'manual-review'`（学生作品需人工审核）
- `StaffConfig.mode: 'capability-template'`（默认能力模板，可切 real-profiles）
- 资源路径：`/content/*.json`，挂载在 dist/content/

## 痛点
- 弱网和低端机卡顿（[docs/performance.md](file:///C:/kaifa/open_leqixiang/docs/performance.md) + 长文件名 `这个项目需要进行一轮性能和加载优化`）
- Vite preview 与 dev 端口冲突（Codex 会话里反复出现 4173 / 5173）
- smoke-browser 自检常因 `/assets/brand/logo.png` 失败需要重生成
- OrbitGallery / styles.css opacity 反复调试

## 下一步
- [ ] 把学生档案扫描进 git-lfs，避免 100MB+ 二进制污染 GitHub
- [ ] 把 staff.mode 切到 'real-profiles' 并写真实教师资料
- [ ] 把 smoke-browser 失败的处理写成 self-healing
- [ ] 给 README 写一个“数据从哪里来、谁可以改”的小节

## 关联
- [[60_Assets/dossiers/open_leqixiang]]
- [[20_Projects/senlin_website]]（业务承接站）
- [[20_Projects/python-adventure]]（同机构作品）