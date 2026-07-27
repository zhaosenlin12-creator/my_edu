#!/usr/bin/env python3
"""audit_dossiers.py · 审计 60_Assets/dossiers/"""
from __future__ import annotations
import re, sys
from pathlib import Path

ROOT = Path(r"C:\my_know")
DOSSIERS = ROOT / "60_Assets" / "dossiers"
REQUIRED_FRONTMATTER = {"type", "status", "domain", "audience", "updated_at", "tags"}
SECTION_KEYS = {
    "evidence": ["证据", "关键证据", "事实"],
    "risk": ["痛点", "已知痛点", "风险", "已知风险", "真实卡点", "卡点"],
    "learned": ["学到", "学到的能力", "我学到的能力", "我学到"],
    "next": ["下一步", "下一步可做", "接下来"],
}
FILE_PATH_PATTERN = re.compile(r"C:\\\\[^\s`*]+|\bC:[\\/][^\s`*]+")

def has_any(text, keys):
    return any(k in text for k in keys)

def audit_one(path):
    text = path.read_text(encoding="utf-8")
    issues = []
    has_3tag = bool(re.search(r"事实\s*/\s*推断\s*/\s*待确认", text))
    fm = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not fm:
        issues.append("frontmatter 缺失")
    else:
        present = set(re.findall(r"^([a-z_]+):", fm.group(1), re.M))
        missing = REQUIRED_FRONTMATTER - present
        if missing:
            issues.append("frontmatter 缺:" + ",".join(missing))
    if not has_any(text, SECTION_KEYS["evidence"]):
        issues.append("缺证据段")
    if not has_any(text, SECTION_KEYS["risk"]):
        issues.append("缺痛点段")
    if not has_any(text, SECTION_KEYS["learned"]):
        issues.append("缺学到段")
    if not has_any(text, SECTION_KEYS["next"]):
        issues.append("缺下一步段")
    if not FILE_PATH_PATTERN.search(text):
        issues.append("没引用本地真实路径")
    return {"file": path.name, "size": path.stat().st_size, "issues": issues, "has_3tag": has_3tag}

def main(argv):
    if not DOSSIERS.exists():
        print("找不到:" + str(DOSSIERS))
        return 1
    files = sorted(DOSSIERS.glob("*.md"))
    if not files:
        print(str(DOSSIERS) + " 下没有 .md 文件")
        return 1
    print("审计 " + str(len(files)) + " 个 dossier:\n")
    fails = 0
    for p in files:
        r = audit_one(p)
        ok = not r["issues"] and r["has_3tag"]
        if not ok:
            fails += 1
        marker = "[OK]" if ok else "[FAIL]"
        line = "  " + marker + " " + r["file"].ljust(28) + " " + str(r["size"]).rjust(5) + "B"
        if r["issues"]:
            line += "  -> " + "; ".join(r["issues"])
        print(line)
        if not r["has_3tag"]:
            print("       -> 缺 事实/推断/待确认 三段标注")
    print("\n共 " + str(len(files)) + " 个," + str(fails) + " 个待修")
    return 0 if fails == 0 else 1

if __name__ == "__main__":
    sys.exit(main(sys.argv))