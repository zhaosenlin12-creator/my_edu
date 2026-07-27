---
type: moc
status: active
domain: projects
audience: self,parent,teacher,student
updated_at: 2026-07-27
tags: moc,projects
---

# 项目地图入口

> 找项目的两个路径:**全景图**(下面)或者**真实档案**([[60_Assets/dossiers/]])。

## 按"做完了 / 正在做 / 想做"分

```mermaid
graph LR
  M[项目状态] --> Done[做完了]
  M --> Doing[正在做]
  M --> Want[想做]

  Done --> d1[机构站 senlin_website]
  Done --> d2[展览大屏 open_leqixiang]
  Done --> d3[3D 互动 world_website]
  Done --> d4[抖音 SOP]
  Done --> d5[直播 6 轮 SOP]

  Doing --> n1[Python 冒险岛 v2.5]
  Doing --> n2[7 天营 ISO 化]
  Doing --> n3[本知识库升级]
  Doing --> n4[抖音栏目定型]

  Want --> w1[线上录播课 12 节]
  Want --> w2[本地 LLM 替 DeepSeek]
  Want --> w3[教学方法论授权产品]
```

## 按"对谁"分

| 受众 | 项目 |
|---|---|
| **家长** | senlin_website / 个人站 / 抖音 |
| **学员(小学生)** | Python 冒险岛 / 7 天营 / 寒创赛营 |
| **学员(初中)** | 宇宙探索 / 坦克大战 / 个人作品集 |
| **同行老师** | 本知识库 / 教案包 / VibeHub 资料 |
| **机构来访者** | 乐其翔展览大屏 |

## 找具体项目

- 全景:`[[20_Projects/index]]`
- 真实档案:`[[60_Assets/dossiers/]]`

## 入口也看

- [[00_Home/MOCs/teaching]] · 教学体系入口
- [[00_Home/MOCs/content]] · 内容体系入口
- [[00_Home/MOCs/ai_tools]] · AI 工具入口