#!/usr/bin/env python3
"""Generate a course plan markdown from a short brief."""
from __future__ import annotations
import argparse, datetime, re
from pathlib import Path
DEFAULT_VAULT = Path(r"C:\my_know")
SECTIONS = [
    "5 分钟：复盘 + 目标",
    "20 分钟：核心概念 + 示范",
    "20 分钟：学员实作",
    "5 分钟：作品展示 + 评价",
]


def render(name, grade, lessons, goals, deliverables):
    today = datetime.date.today().isoformat()
    lines = [
        "---",
        "type: course_plan",
        "status: draft",
        "domain: teaching",
        "audience: self,teacher",
        f"updated_at: {today}",
        "tags: course,plan",
        "---",
        "",
        f"# 课程计划：{name}",
        "",
        "## 目标学生",
        "- 学段 / 年级：" + (grade or "待填"),
        f"- 总节数：{lessons}",
        "",
        "## 教学目标",
    ]
    for goal in goals or ["知识", "能力", "作品"]:
        lines.append(f"- {goal}")
    lines += ["", "## 每节结构"]
    for section in SECTIONS:
        lines.append(f"- {section}")
    lines += ["", "## 课节表"]
    for i in range(1, max(1, lessons) + 1):
        lines.append(f"- 第 {i} 节：主题 → 实作 → 作品")
    lines += ["", "## 评价 / 交付物"]
    for item in deliverables or ["完成度", "创意", "表达", "团队协作"]:
        lines.append(f"- {item}")
    lines += ["", "## 配套模板", "- 复制 00_Home/_templates/course_plan.md 进一步细化", "- 每节课课件放 30_Teaching/<课程名>/ 目录", "- 学员作品放 30_Teaching/_students-mirror.md"]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--vault", type=Path, default=DEFAULT_VAULT)
    parser.add_argument("--name", required=True)
    parser.add_argument("--grade", default="")
    parser.add_argument("--lessons", type=int, default=6)
    parser.add_argument("--goals", nargs="*", default=[])
    parser.add_argument("--deliverables", nargs="*", default=[])
    args = parser.parse_args()
    md = render(args.name, args.grade, args.lessons, args.goals, args.deliverables)
    safe = re.sub(r"[^A-Za-z0-9._-]+", "-", args.name).strip("-") or "course"
    out = args.vault / "30_Teaching" / f"course-{safe}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(md, encoding="utf-8")
    print(f"wrote course plan to {out}")


if __name__ == "__main__":
    main()
