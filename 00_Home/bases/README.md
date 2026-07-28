# Bases

Obsidian Bases — 把 vault 里的结构化数据变成可查询、可排序、可看板的视图。

## 列表

| Base | 看什么 |
|------|--------|
| [[projects]] | 20_Projects/ 里的项目，按状态 / 优先级看板 |
| [[decisions]] | decisions/ 里的 ADR 时间线 |
| [[daily]] | daily/ 里所有每日笔记 |
| [[dossiers]] | 60_Assets/dossiers/ 所有 dossier |
| [[sources]] | 70_Sources/ 所有抓取的页面 |

## 怎么打开

在 Obsidian 里：
1. Ribbon 打开 Bases 插件（如果还没装：`Settings → Community plugins → Bases`）
2. 在文件树里右键 `xxx.base` → Open in Bases

或者在 command palette 搜 `Bases: Open base file`，选对应 .base 文件。

## frontmatter 约定

这些 base 通过 frontmatter 字段查询，所以 `20_Projects/` 下的每个项目最好有：

```yaml
---
type: project
status: active|paused|done
priority: high|medium|low
deadline: 2026-12-31
tags: [web, ai]
---
```

`daily/` 下的笔记：

```yaml
---
type: daily
date: 2026-07-28
status: active
tags: [daily]
---
```

`decisions/` 下的 ADR：

```yaml
---
type: adr
status: proposed|accepted|superseded
date: 2026-07-28
tags: [decision]
---
```

## 维护

加新 base 文件就放在这目录，参考 `projects.base` 的语法（YAML）。