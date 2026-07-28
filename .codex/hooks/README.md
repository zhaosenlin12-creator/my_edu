# Codex 会话生命周期 Hooks

每次跟 Codex（或任何 skills-aware agent）对话时自动加载上下文，避免「每次都重新解释自己」。

## 两个 hook

### `session_start.py` — 开 session 自动跑

读三样东西并打印出来：
1. `AGENTS.md`（操作手册）
2. `brain/North Star.md`（长期目标）
3. `daily/<latest>.md`（最近一篇每日笔记）

### `session_end.py` — 关 session 自动跑

把这次会话的总结 append 到今天的 `daily/YYYY-MM-DD.md`。

## 怎么接 Codex desktop

Codex desktop 现在不直接支持 `session_start` / `session_end` 的 hook 事件触发，但**可以在 prompt 里手动调用**：

**开 session 时**：在第一条消息里说「读 `.codex/hooks/session_start.py` 的输出」或直接 `python .codex/hooks/session_start.py | head -200`。

**关 session 时**：说「把这次对话总结写到今天的 daily」或：

```bash
echo "今天做了什么...
决策...
待办..." | python .codex/hooks/session_end.py
```

## 怎么接 Codex CLI（命令行版）

在 `~/.codex/AGENTS.md` 或项目根 `AGENTS.md` 里写：

```
At every session start: run `python .codex/hooks/session_start.py` and read its output before responding.
At every session end: append a summary to today's daily note via `python .codex/hooks/session_end.py`.
```

Codex CLI 会自动遵守这种指令。

## 测试

```powershell
python C:\my_know\.codex\hooks\session_start.py
python C:\my_know\.codex\hooks\session_end.py --file C:\path\to\summary.md
```