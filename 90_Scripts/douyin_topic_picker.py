#!/usr/bin/env python3
"""Generate a Douyin topic card from the local knowledge base."""
from __future__ import annotations
import argparse, datetime, json, re
from pathlib import Path

DEFAULT_VAULT = Path(r"C:\my_know")
GOAL_KEYWORDS = {"vibe", "ai", "codex", "intellij", "obsidian", "github", "deploy", "project", "git", "prompt"}


def read_cards(vault: Path, folder: str):
    out = []
    for path in (vault / folder).glob("*.md"):
        text = path.read_text(encoding="utf-8", errors="replace")
        title_match = re.search(r"^# (.+)$", text, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else path.stem
        summary_match = re.search(r"summary:\s*(.+)$", text, re.MULTILINE)
        summary = summary_match.group(1).strip() if summary_match else ""
        next_match = re.search(r"next_action:\s*(.+)$", text, re.MULTILINE)
        next_action = next_match.group(1).strip() if next_match else ""
        out.append({"title": title, "summary": summary, "next_action": next_action, "path": str(path.relative_to(vault))})
    return out


def load_vibe_terms(vault: Path):
    import csv
    csv_path = vault / "70_Sources" / "vibe-hub" / "index.csv"
    if not csv_path.exists():
        return []
    with csv_path.open(encoding="utf-8-sig", newline="") as f:
        return [row for row in csv.DictReader(f) if row.get("language") == "zh"]


def pick_topic(cards, terms):
    today = datetime.date.today()
    candidate = None
    for card in cards:
        if not card["summary"]:
            continue
        if any(k in (card["summary"] + card["title"]).lower() for k in GOAL_KEYWORDS):
            candidate = card
            break
    if candidate is None and cards:
        candidate = cards[0]
    matched_terms = []
    if candidate:
        tokens = [t.lower() for t in re.findall(r"[A-Za-z]+", candidate["summary"])]
        for term in terms[:120]:
            text = (term.get("summary", "") + term.get("title", "")).lower()
            if any(tok in text for tok in tokens[:5]):
                matched_terms.append(term)
                if len(matched_terms) >= 5:
                    break
    return {"project": candidate, "terms": matched_terms, "weekday": today.strftime("%A")}


def render(result, vault: Path):
    today = datetime.date.today().isoformat()
    project = result["project"]
    lines = [f"---", "type: douyin_topic", "status: draft", "domain: content", "audience: self", f"updated_at: {today}", "tags: douyin,draft", "---", "", f"# 抖音选题草稿 {today}"]
    if project:
        lines.extend(["", "## 一句话选题", f"- {project['summary'] or project['title']}", "", "## 对应项目卡", f"- {project['path']}"])
    else:
        lines.extend(["", "## 选题来源缺失", "- 请先在 20_Projects / 30_Teaching / 40_Content 中维护至少一张带 summary 的卡"])
    lines.extend(["", "## 推荐术语（来自 VibeHub 本地）"])
    for term in result["terms"]:
        lines.append(f"- [{term['title']}]({term['url']})：{term['summary']}")
    lines.extend(["", "## 30 秒钩子", "- 我用 30 秒给你看 / 我家学生是这样做出来的 / 你以为很难其实只要三步", "", "## 行动指令", "- 关注我，下一条带你做下一步", "- 评论区告诉我你的孩子 / 你现在在用什么工具", "", "## 发布后跟踪", "- 24h 播放、转粉率、评论关键词", "- 写入 40_Content/curerforest-channel.md"])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--vault", type=Path, default=DEFAULT_VAULT)
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()
    cards = read_cards(args.vault, "20_Projects") + read_cards(args.vault, "30_Teaching") + read_cards(args.vault, "40_Content")
    terms = load_vibe_terms(args.vault)
    result = pick_topic(cards, terms)
    markdown = render(result, args.vault)
    output = args.out or (args.vault / "40_Content" / f"draft-{datetime.date.today().isoformat()}.md")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(markdown, encoding="utf-8")
    print(f"wrote topic draft to {output}")
    print(json.dumps({"matched_terms": [t["title"] for t in result["terms"]]}, ensure_ascii=False))


if __name__ == "__main__":
    main()