#!/usr/bin/env python3
"""Convert YAML-frontmatter markdown knowledge docs into the JSON data files under data/.

Stdlib-only: implements a minimal frontmatter parser (flat scalars, inline
lists `[a, b]`, and block lists `- item`) sufficient for this repo's simple
frontmatter shape. It intentionally does not support nested mappings/lists.

Usage: python3 scripts/markdown-to-json.py   (run from repo root)
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _coerce_scalar(value: str):
    value = value.strip()
    if value.startswith(("'", '"')) and value.endswith(("'", '"')) and len(value) >= 2:
        return value[1:-1]
    return value


def parse_frontmatter(path: Path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
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
            items = [_coerce_scalar(x) for x in inner.split(",")] if inner else []
            meta[key] = items
            i += 1
        elif rest == "":
            # possible block list on following indented "- " lines
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
    return meta


def collect(dir_name: str, category: str):
    entries = []
    for path in sorted((ROOT / dir_name).rglob("*.md")):
        meta = parse_frontmatter(path)
        if not meta:
            continue
        if meta.get("category") != category:
            continue
        meta["_source_file"] = str(path.relative_to(ROOT))
        entries.append(meta)
    return entries


def main():
    # (source directories, category, output filename). Multiple source dirs
    # can feed the same output file (e.g. guides/ and crystal-tech/ both hold
    # category: guide documents).
    mapping = [
        (["commanders"], "commander", "commanders.json"),
        (["pairings"], "pairing", "pairings.json"),
        (["guides", "crystal-tech"], "guide", "guides.json"),
        (["equipment"], "equipment", "equipment.json"),
        (["events"], "event", "events.json"),
        (["civilizations"], "civilization", "civilizations.json"),
        (["mechanics"], "mechanic", "mechanics.json"),
    ]
    for dir_names, category, out_name in mapping:
        entries = []
        for dir_name in dir_names:
            entries.extend(collect(dir_name, category))
        entries.sort(key=lambda e: e.get("id", ""))
        out_path = ROOT / "data" / out_name
        out_path.write_text(json.dumps(entries, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"Wrote {len(entries)} entries to {out_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
