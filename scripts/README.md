# Scripts

Stdlib-only Python 3 utilities for maintaining this repository. No third-party dependencies required.

## `validate-data.py`

Run before committing any change to `commanders/`, `pairings/`, `guides/`, `crystal-tech/`, `equipment/`, `events/`, `civilizations/`, `mechanics/`, or `data/`:

```bash
python3 scripts/validate-data.py
```

Checks:
- All JSON in `data/` and `schemas/` parses.
- Every markdown knowledge doc has the frontmatter keys required by its category (`commander`, `pairing`, `guide`, `equipment`, `event`, `civilization`, `mechanic`).
- No duplicate `id` values within a category.
- Commander, pairing, equipment, event, civilization, and mechanic docs contain their required section headings.

Exits non-zero and prints a list of issues if anything fails.

## `markdown-to-json.py`

Regenerates every `data/*.json` file directly from the frontmatter of the corresponding markdown source directories:

| Output | Source directories | Category |
|---|---|---|
| `data/commanders.json` | `commanders/` | `commander` |
| `data/pairings.json` | `pairings/` | `pairing` |
| `data/guides.json` | `guides/` + `crystal-tech/` | `guide` |
| `data/equipment.json` | `equipment/` | `equipment` |
| `data/events.json` | `events/` | `event` |
| `data/civilizations.json` | `civilizations/` | `civilization` |
| `data/mechanics.json` | `mechanics/` | `mechanic` |

```bash
python3 scripts/markdown-to-json.py
```

Run this any time you add or edit a markdown knowledge doc, then re-run `validate-data.py` and commit the regenerated JSON alongside your markdown change so the two never drift apart.

`data/PROGRESS.md` (not JSON) is the internal working checklist used while researching the commander roster — safe to ignore for downstream consumers, useful for future contributors picking up remaining gaps.
