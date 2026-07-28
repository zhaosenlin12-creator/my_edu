#!/usr/bin/env python3
"""Session-end hook: append a summary to today's daily note.

Reads a summary from stdin (or --file path) and appends a structured block
to daily/<today>.md. If today's note does not exist, it creates one from
the template.

Usage (interactive):
  echo "<summary>" | python .codex/hooks/session_end.py [VAULT_ROOT]

Usage (file):
  python .codex/hooks/session_end.py [VAULT_ROOT] --file path/to/summary.md

The appended block includes:
  - timestamp
  - topic (inferred from first 80 chars)
  - key points (provided by caller)
"""
from __future__ import annotations
import argparse, sys
from datetime import datetime, timezone
from pathlib import Path

VAULT = Path(r"C:\my_know")


def today_note(vault: Path) -> Path:
    date = datetime.now().strftime("%Y-%m-%d")
    note = vault / "daily" / f"{date}.md"
    return note


def ensure_today(vault: Path, template: Path) -> Path:
    note = today_note(vault)
    if not note.exists():
        tpl = template if template.exists() else vault / "_templates" / "daily.md"
        content = tpl.read_text(encoding="utf-8") if tpl.exists() else "# {{date}}\n\n## Codex 对话摘要\n\n"
        content = content.replace("{{date}}", note.stem).replace("{{date:YYYY-MM-DD}}", note.stem)
        note.write_text(content, encoding="utf-8")
        print(f"created: {note}")
    return note


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("vault", nargs="?", default=str(VAULT))
    p.add_argument("--file", help="read summary from this file instead of stdin")
    p.add_argument("--topic", default="")
    args = p.parse_args()

    vault = Path(args.vault)
    template = vault / "_templates" / "daily.md"
    note = ensure_today(vault, template)

    if args.file:
        summary = Path(args.file).read_text(encoding="utf-8")
    else:
        summary = sys.stdin.read().strip()

    if not summary:
        print("no summary provided", file=sys.stderr)
        sys.exit(1)

    now = datetime.now().strftime("%H:%M")
    topic = args.topic or summary.splitlines()[0][:80] if summary else "(no topic)"

    block = f"""

### 会话 · {now}

**主题**：{topic}

{summary}

"""

    with note.open("a", encoding="utf-8") as f:
        f.write(block)

    print(f"appended to: {note}")


if __name__ == "__main__":
    main()