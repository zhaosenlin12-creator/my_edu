#!/usr/bin/env python3
"""Summarise a live stream session into the knowledge base."""
from __future__ import annotations
import argparse, csv, datetime, json
from pathlib import Path
DEFAULT_VAULT = Path(r"C:\my_know")


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--vault", type=Path, default=DEFAULT_VAULT)
    p.add_argument("--date", required=True)
    p.add_argument("--title", required=True)
    p.add_argument("--peaks", type=int, default=0)
    p.add_argument("--new-followers", type=int, default=0)
    p.add_argument("--conversions", type=int, default=0)
    p.add_argument("--qa", default="")
    p.add_argument("--failure", default="")
    p.add_argument("--improvement", default="")
    return p.parse_args()


def write_card(args):
    card_dir = args.vault / "40_Content" / "live"
    card_dir.mkdir(parents=True, exist_ok=True)
    out = card_dir / f"{args.date}.md"
    body = "\n".join([
        "---",
        "type: live_recap",
        "status: done",
        "domain: content",
        "audience: self",
        f"date: {args.date}",
        f"updated_at: {datetime.date.today().isoformat()}",
        "tags: live,recap",
        "---",
        "",
        f"# 直播复盘 {args.date}：{args.title}",
        "",
        "## 数据",
        f"- 峰值在线：{args.peaks}",
        f"- 新增粉丝：{args.new_followers}",
        f"- 转化：{args.conversions}",
        "",
        "## 答疑关键词",
        "- " + (args.qa or "无记录"),
        "",
        "## 翻车 / 低潮",
        "- " + (args.failure or "无"),
        "",
        "## 下轮改进",
        "- " + (args.improvement or "待填"),
        "",
        "## 复盘动作",
        "- 把数据写入 40_Content/curerforest-channel.md",
        "- 把可复用的提问 / 答法写入 50_AI 对应工具卡",
    ])
    out.write_text(body, encoding="utf-8")
    return out


def update_csv(args):
    csv_path = args.vault / "60_Assets" / "live-summary.csv"
    new_row = {"date": args.date, "title": args.title, "peaks": args.peaks, "new_followers": args.new_followers, "conversions": args.conversions, "qa_keywords": args.qa, "failure": args.failure, "improvement": args.improvement}
    existing = []
    if csv_path.exists():
        with csv_path.open(encoding="utf-8-sig", newline="") as f:
            existing = list(csv.DictReader(f))
    existing = [r for r in existing if r.get("date") != args.date]
    existing.append(new_row)
    existing.sort(key=lambda r: r.get("date", ""))
    with csv_path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "title", "peaks", "new_followers", "conversions", "qa_keywords", "failure", "improvement"])
        writer.writeheader()
        writer.writerows(existing)
    return csv_path


def main():
    args = parse_args()
    card = write_card(args)
    csv_path = update_csv(args)
    print(json.dumps({"card": str(card), "csv": str(csv_path)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
