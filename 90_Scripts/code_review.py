#!/usr/bin/env python3
"""Run a basic code review checklist against a git diff."""
from __future__ import annotations
import argparse, re, subprocess
from pathlib import Path
DEFAULT_VAULT = Path(r"C:\my_know")
SECRET_PATTERNS = [
    re.compile(r"(?i)api[_-]?key\s*[:=]\s*[\"\x27]([^\"\x27]{8,})"),
    re.compile(r"(?i)secret\s*[:=]\s*[\"\x27]([^\"\x27]{8,})"),
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
]
RISK_PATH = re.compile(r"(\.env|secrets|student|学生|家长|家庭)", re.IGNORECASE)


def run_diff(repo):
    res = subprocess.run(["git", "-C", str(repo), "diff", "--cached"], capture_output=True, text=True)
    return res.stdout


def scan(diff):
    secrets = []
    risks = []
    for pattern in SECRET_PATTERNS:
        for match in pattern.finditer(diff):
            secrets.append(match.group(0))
    for line in diff.splitlines():
        if line.startswith("+") and RISK_PATH.search(line):
            risks.append(line)
    return {"secrets": secrets, "risks": risks}


def render(result):
    lines = ["# 代码审查扫描结果", "", "## 密钥 / 敏感串", ""]
    if result["secrets"]:
        for hit in result["secrets"]:
            lines.append(f"- ⚠️ {hit}")
    else:
        lines.append("- 未发现明显密钥。")
    lines += ["", "## 风险路径"]
    if result["risks"]:
        for line in result["risks"]:
            lines.append(f"- {line}")
    else:
        lines.append("- 未发现学生 / 家长 / 密钥路径。")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()
    diff = run_diff(args.repo)
    if not diff:
        print("no staged diff")
    result = scan(diff)
    report = render(result)
    out = args.out or (DEFAULT_VAULT / "40_Content" / f"code-review-{args.repo.name}.md")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(report, encoding="utf-8")
    print(f"wrote review to {out}")
    return 1 if result["secrets"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
