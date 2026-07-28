# decisions/

> Architecture Decision Records (ADR) — 关键决策日志

每个长效决定都写一份 ADR。模板看 `[[../_templates/adr]]`。

## 命名

`YYYY-MM-DD-title.md`，例如 `2026-07-28-knowledge-base-upgrade.md`

## 当前决策（按时间倒序）

> 这些是我们这条会话里做出的关键决策。

### 2026-07-28

- **knowledge-base-upgrade**：升级知识库到「专业级 AI 记忆库」标准
- **dual-agents-md**：AGENTS.md 同时放在 vault 根和 Codex cwd
- **vibe-hub-mirror-strategy**：pages/ 进 git，site/ 本地按需生成
- **obsidian-mind-as-reference**：参考 obsidian-mind 的三层记忆模型（长期 / 中期 / 短期）

### 待回填

- 知识库命名（my_know vs my_edu）的历史原因
- vibe-hub 为什么用 Python http.server 而不是 npx serve
- 选用 Obsidian 而不是 Notion / Logseq 的理由
- 四个徒弟未来怎么跟进这套系统

## 怎么用

- 写新 ADR：复制 `_templates/adr.md` 为 `decisions/YYYY-MM-DD-title.md`
- 找决策：`rg "^- \*\*" decisions/` 或用 Obsidian Bases 查询
- 改决策：不要改原 ADR，新写一份 supersede 旧的