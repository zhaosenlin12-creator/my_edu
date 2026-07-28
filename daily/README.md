# daily/

每日笔记目录。每天一篇 `YYYY-MM-DD.md`，记录：

- 今日三件事
- 跟 Codex / Claude 的会话摘要
- 决策（长决策写 ADR 到 `decisions/`，这里只放简版）
- 待办
- 一句话反思

## 用法

**新一天**：复制 `_templates/daily.md` 为 `YYYY-MM-DD.md`，填日期 frontmatter。

**会话结束**：粘 Codex 对话的关键发现 / 决策到今日笔记。

**回看**：每周看最近 7 篇，月度复盘时看当月所有笔记。

## 自动生成（未来）

`build_daily_index.py` 可以从每日笔记生成周报、月报。