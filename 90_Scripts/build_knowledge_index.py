#!/usr/bin/env python3
"""Build a CSV index of every knowledge card in the vault."""
from __future__ import annotations
import argparse, csv, re
from pathlib import Path
DEFAULT_VAULT = Path(r"C:\my_know")
EXCLUDE_DIRS = {".git", ".obsidian", "70_Sources", "90_Scripts"}
FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)
PROPERTY = re.compile(r"^([A-Za-z_]+):\s*(.*)$")


def parse_card(path):
    text = path.read_text(encoding="utf-8", errors="replace")
    meta = {}
    body = text
    match = FRONTMATTER.match(text)
    if match:
        for line in match.group(1).splitlines():
            prop = PROPERTY.match(line)
            if prop:
                meta[prop.group(1).strip()] = prop.group(2).strip()
        body = match.group(2)
    title = re.search(r"^# (.+)$", body, re.MULTILINE)
    return {
        "path": str(path),
        "folder": path.parent.name,
        "title": (title.group(1).strip() if title else path.stem),
        "type": meta.get("type", ""),
        "status": meta.get("status", ""),
        "domain": meta.get("domain", ""),
        "audience": meta.get("audience", ""),
        "summary": meta.get("summary", ""),
        "next_action": meta.get("next_action", ""),
        "updated_at": meta.get("updated_at", ""),
        "tags": meta.get("tags", ""),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--vault", type=Path, default=DEFAULT_VAULT)
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()
    rows = []
    for path in args.vault.rglob("*.md"):
        rel = path.relative_to(args.vault)
        if any(part in EXCLUDE_DIRS for part in rel.parts):
            continue
        if "vibe-hub" in rel.parts:
            continue
        rows.append(parse_card(path))
    rows.sort(key=lambda r: (r["folder"], r["title"]))
    out = args.out or (args.vault / "60_Assets" / "knowledge-index.csv")
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["path", "folder", "title", "type", "status", "domain", "audience", "summary", "next_action", "updated_at", "tags"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {len(rows)} cards to {out}")


if __name__ == "__main__":
    main()
