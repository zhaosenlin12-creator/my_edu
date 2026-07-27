---
type: project
status: active
domain: web
audience: parent,student
repo: zhaosenlin12-creator/gaokao_design
url: https://gaokao.com
summary: 高考志愿地图（Vite + React + MapLibre GL），全国 1500+ 大学
next_action: 接入校情 / 分数段 / 选科推荐
updated_at: 2026-07-27
tags: web,education,mapping
---

# gaokao_design（高考志愿地图）

> 把全国 1500+ 所大学放在真实山川地图上；按分数 / 位次 / 兴趣分冲稳保。

## 状态
- 本地仓：C:\kaifa_senlin\gaokao_design
- 远端：zhaosenlin12-creator/gaokao_design

## 技术栈
- 前端：Vite + React 19 + 自定义动画
- 地图：MapLibre GL + 1596 所大学数据
- 后端：crawled/backend.py（端口 8787，Python 3.10+）
- 静态服务：crawled/serve.py（端口 8765）

## 下一步
- [ ] LLM 推荐解析加固
- [ ] 瓦片探测兼容
- [ ] 接管「教育自媒体」内容端