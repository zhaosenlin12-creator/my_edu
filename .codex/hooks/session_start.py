#!/usr/bin/env python3
"""Session-start hook: load context into the agent's working memory.

Reads (in order):
  1. AGENTS.md           - the operating manual
  2. brain/North Star.md - long-term goals
  3. daily/<latest>.md   - most recent daily note

Prints each to stdout with a section header. Codex picks this up as
session-start context.

Usage:
  python .codex/hooks/session_start.py [VAULT_ROOT]
"""
from __future__ import annotations
import sys
from pathlib import Path

VAULT = Path(sys.argv[1] if len(sys.argv) > 1 else r"C:\my_know").resolve()


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="replace") if p.exists() else f"(missing: {p})"


def latest_daily(vault: Path) -> Path | None:
    daily = vault / "daily"
    if not daily.exists():
        return None
    candidates = [p for p in daily.glob("????-??-??.md") if p.is_file()]
    return max(candidates, key=lambda p: p.name) if candidates else None


def main() -> None:
    print("=" * 70)
    print(f"SESSION START CONTEXT (vault: {VAULT})")
    print("=" * 70)

    print("\n>>> AGENTS.md (operating manual)\n")
    print(read(VAULT / "AGENTS.md"))

    north = VAULT / "brain" / "North Star.md"
    print("\n" + "=" * 70)
    print(f">>> brain/North Star.md ({north})\n")
    print(read(north))

    latest = latest_daily(VAULT)
    if latest:
        print("\n" + "=" * 70)
        print(f">>> daily/{latest.name} (most recent)\n")
        print(read(latest))
    else:
        print("\n(no daily notes yet)")

    print("\n" + "=" * 70)
    print("END OF SESSION-START CONTEXT")
    print("=" * 70)


if __name__ == "__main__":
    main()