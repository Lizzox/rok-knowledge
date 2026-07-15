# Contributing to rok-knowledge

Thank you for helping expand RoK Lab's knowledge base. This repository is deliberately structured for two consumers at once: **humans** (readable markdown) and **machines** (a local RAG pipeline + JSON API data). Please respect both when contributing.

## Ground rules

1. **No fabricated data.** If you don't have a verified value (exact damage factor, rage cost, event schedule, etc.), write `pending research` or a clear approximate range and set `detail_status: partial` or `stub-pending-research` in the frontmatter — never invent a plausible-looking number.
2. **Cite your sources.** Every document has a `sources:` frontmatter field. Add the wiki page, patch note, or community guide you used.
3. **Keep documents small.** This repo is RAG-optimized — one commander/pairing/guide per file, one concept per section. Don't merge multiple commanders into one file.
4. **Follow the schema.** Validate frontmatter against `schemas/commander-schema.json`, `schemas/pairing-schema.json`, or `schemas/guide-schema.json` before submitting.
5. **Regenerate JSON after markdown edits.** Run:
   ```bash
   python3 scripts/markdown-to-json.py
   python3 scripts/validate-data.py
   ```
   and commit the regenerated `data/*.json` alongside your markdown change.

## Document structure

Every knowledge document (commander, pairing, guide) starts with YAML frontmatter and follows this section template:

```markdown
---
id: kebab-case-id
name: Display Name
category: commander | pairing | guide
...schema-specific fields...
tags: [tag1, tag2]
last_updated: YYYY-MM-DD
sources:
  - "source url or reference"
detail_status: complete | partial | stub-pending-research
---

# Title

## Overview
## Statistics
## Skills          (commanders only)
## Recommended Usage
## Best Pairings    (commanders only)
## Equipment        (commanders only)
## Strategy Tips
## Strengths
## Weaknesses
## Sources
```

Pairings use `## Purpose`, `## Explanation`, `## Strengths`, `## Weaknesses`, `## Alternatives`, `## Sources` instead.

## Adding a new commander

1. Pick the correct rarity folder: `commanders/{legendary,epic,elite,advanced}/`.
2. File name: `commander-name.md` (kebab-case, matching `id`).
3. Fill in every section honestly. If you can't verify skill numbers, say so explicitly rather than guessing.
4. Cross-link related pairings using `[[pairing-id]]`-style references in prose where useful (this repo's convention for RAG-friendly cross-referencing is a plain markdown link to the relative file path).
5. Add the commander to `data/commander-roster-index.json` under `has_detail_file` once merged.

## Adding a pairing / guide

Same process, in `pairings/{scenario}/` or `guides/{section}/`.

## Filing a correction

If you spot outdated numbers (very likely — RoK rebalances frequently), open a PR updating the file's `last_updated` date and the specific value, with a source link. Small, frequent corrections are preferred over large speculative rewrites.

## Style

- No fictional lore embellishment — stick to what's documented/verifiable.
- Prefer short declarative sentences over marketing language.
- Use present tense for how mechanics currently work.
