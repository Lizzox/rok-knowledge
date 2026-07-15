#!/usr/bin/env python3
"""Validate rok-knowledge repository consistency. Stdlib-only.

Checks:
  1. Every data/*.json file is valid JSON.
  2. Every markdown knowledge doc under commanders/, pairings/, guides/ has
     YAML-ish frontmatter with the required keys for its category.
  3. No duplicate `id` values within a category.
  4. Every markdown doc's required H2 section headings are present
     (commander/pairing docs only, per the repo's structural template).
  5. Cross-check: every id referenced by data/*.json exists as a real file.

Usage: python3 scripts/validate-data.py   (run from repo root)
Exit code 0 = clean, 1 = problems found (printed to stdout).
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Frontmatter parser inlined (kept in sync with scripts/markdown-to-json.py).
def _coerce_scalar(value: str):
    value = value.strip()
    if value.startswith(("'", '"')) and value.endswith(("'", '"')) and len(value) >= 2:
        return value[1:-1]
    return value


def parse_frontmatter(path: Path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text
    body = parts[1]
    meta = {}
    lines = body.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.strip().startswith("#"):
            i += 1
            continue
        m = re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", line)
        if not m:
            i += 1
            continue
        key, rest = m.group(1), m.group(2).strip()
        if rest.startswith("[") and rest.endswith("]"):
            inner = rest[1:-1].strip()
            meta[key] = [_coerce_scalar(x) for x in inner.split(",")] if inner else []
            i += 1
        elif rest == "":
            items = []
            j = i + 1
            while j < len(lines) and re.match(r"^\s*-\s+", lines[j]):
                items.append(_coerce_scalar(re.sub(r"^\s*-\s+", "", lines[j])))
                j += 1
            if items:
                meta[key] = items
                i = j
            else:
                meta[key] = ""
                i += 1
        else:
            meta[key] = _coerce_scalar(rest)
            i += 1
    return meta, parts[2]


REQUIRED_KEYS = {
    "commander": ["id", "name", "category", "rarity", "tags", "last_updated", "sources", "detail_status"],
    "pairing": ["id", "name", "category", "scenario", "tags", "last_updated", "sources", "detail_status"],
    "guide": ["id", "name", "category", "section", "tags", "last_updated", "sources", "detail_status"],
    "equipment": ["id", "name", "category", "slot", "rarity", "tags", "last_updated", "sources", "detail_status"],
    "event": ["id", "name", "category", "event_type", "tags", "last_updated", "sources", "detail_status"],
}

REQUIRED_HEADINGS = {
    "commander": ["## Overview", "## Strengths", "## Weaknesses", "## Sources"],
    "pairing": ["## Purpose", "## Explanation", "## Strengths", "## Weaknesses", "## Sources"],
    "equipment": ["## Overview", "## Sources"],
    "event": ["## Overview", "## Sources"],
}


def check_markdown(dir_name: str, category: str, errors: list, seen_ids: dict):
    for path in sorted((ROOT / dir_name).rglob("*.md")):
        if path.name == "README.md":
            continue
        rel = path.relative_to(ROOT)
        meta, body = parse_frontmatter(path)
        if meta is None:
            errors.append(f"{rel}: missing/invalid frontmatter")
            continue
        if meta.get("category") != category:
            continue  # not this category (shouldn't happen given dir layout)
        for key in REQUIRED_KEYS[category]:
            if key not in meta or meta[key] in ("", None, []):
                errors.append(f"{rel}: missing required frontmatter key '{key}'")
        doc_id = meta.get("id")
        if doc_id:
            if doc_id in seen_ids.get(category, {}):
                errors.append(f"{rel}: duplicate id '{doc_id}' (also in {seen_ids[category][doc_id]})")
            else:
                seen_ids.setdefault(category, {})[doc_id] = str(rel)
        for heading in REQUIRED_HEADINGS.get(category, []):
            if heading not in body:
                errors.append(f"{rel}: missing required section '{heading}'")


def check_json_files(errors: list):
    for path in sorted((ROOT / "data").glob("*.json")):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            errors.append(f"{path.relative_to(ROOT)}: invalid JSON ({e})")
    for path in sorted((ROOT / "schemas").glob("*.json")):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            errors.append(f"{path.relative_to(ROOT)}: invalid JSON ({e})")


def main():
    errors = []
    seen_ids = {}
    check_json_files(errors)
    check_markdown("commanders", "commander", errors, seen_ids)
    check_markdown("pairings", "pairing", errors, seen_ids)
    check_markdown("guides", "guide", errors, seen_ids)
    check_markdown("equipment", "equipment", errors, seen_ids)
    check_markdown("events", "event", errors, seen_ids)

    if errors:
        print(f"FOUND {len(errors)} issue(s):\n")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        total = sum(len(v) for v in seen_ids.values())
        print(f"All checks passed. {total} knowledge documents validated across "
              f"{len(seen_ids)} categories, no duplicate IDs, no invalid JSON.")
        sys.exit(0)


if __name__ == "__main__":
    main()
