# Scripts

Stdlib-only Python 3 utilities for maintaining this repository. No third-party dependencies required.

## `validate-data.py`

Run before committing any change to `commanders/`, `pairings/`, `guides/`, or `data/`:

```bash
python3 scripts/validate-data.py
```

Checks:
- All JSON in `data/` and `schemas/` parses.
- Every markdown knowledge doc has the frontmatter keys required by its category.
- No duplicate `id` values within a category.
- Commander and pairing docs contain their required section headings.

Exits non-zero and prints a list of issues if anything fails.

## `markdown-to-json.py`

Regenerates `data/commanders.json`, `data/pairings.json`, and `data/guides.json` directly from the frontmatter of every markdown file under `commanders/`, `pairings/`, and `guides/`.

```bash
python3 scripts/markdown-to-json.py
```

Run this any time you add or edit a markdown knowledge doc, then re-run `validate-data.py` and commit the regenerated JSON alongside your markdown change so the two never drift apart.

`data/equipment.json`, `data/civilizations.json`, and `data/events.json` are currently maintained by hand (no matching per-item markdown folders exist yet) — update them directly when the corresponding stub folders (`equipment/`, `civilizations/`, `events/`) gain real content.
