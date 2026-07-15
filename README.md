# rok-knowledge

[![Validate & Sync Knowledge Base](https://github.com/Lizzox/rok-knowledge/actions/workflows/validate-and-sync.yml/badge.svg)](https://github.com/Lizzox/rok-knowledge/actions/workflows/validate-and-sync.yml)

The official knowledge base for **RoK Lab** — a Rise of Kingdoms platform combining an AI assistant (RAG), a Commander Pairing Engine, a guide system, a strategy database, and future API integrations.

This repository is built to serve **two audiences simultaneously**:
- **Humans** browsing readable, well-organized markdown.
- **Machines** — a local LLM/RAG pipeline and RoK Lab's application backend — consuming small, metadata-rich documents and structured JSON.

> **Unofficial fan project.** Not affiliated with or endorsed by Lilith Games. See [LICENSE](LICENSE).

## Repository structure

```
rok-knowledge/
├── commanders/          # One file per commander, by rarity
│   ├── legendary/
│   ├── epic/
│   ├── elite/
│   └── advanced/
├── pairings/             # Commander pairing database, by scenario
│   ├── open-field/  rally/  garrison/  barbarians/
│   └── barbarian-forts/  gathering/  canyon/
├── guides/               # Strategy guides, by topic
│   ├── beginner/  progression/  economy/  combat/
│   └── kvk/  events/  advanced/
├── mechanics/            # Core game-system reference docs
├── civilizations/        # Per-civilization database (all 15 civilizations)
├── equipment/            # Per-item equipment database, by category
│   ├── infantry/  cavalry/  archer/  leadership/  mixed/  gathering/  accessories/
├── events/               # Per-event database, by type
│   ├── commander-events/  alliance-events/  solo-events/  seasonal-events/  special-events/
├── research/             # Research strategy index, by branch
│   ├── military/  economic/  academy/  civilization/  optimization/
├── crystal-tech/         # Season of Conquest Crystal Technology guides
├── kvk/                   # Machine-readable season schedules (stub)
├── data/                  # Generated + hand-maintained JSON (API-ready)
├── schemas/               # JSON Schemas defining every document's data contract
└── scripts/                # Validation + markdown→JSON generation tooling
```

## Data standards

Every knowledge document (commander, pairing, guide) is a markdown file with YAML frontmatter conforming to one of the schemas in `schemas/`, followed by a fixed section template:

```markdown
---
id: kebab-case-id
name: Display Name
category: commander | pairing | guide
tags: [...]
last_updated: YYYY-MM-DD
sources: ["..."]
detail_status: complete | partial | stub-pending-research
---

# Title
## Overview
## Statistics
## Skills
## Recommended Usage
## Best Pairings
## Equipment
## Strategy Tips
## Strengths
## Weaknesses
## Sources
```

Full detail and rationale live in [CONTRIBUTING.md](CONTRIBUTING.md).

### `detail_status` — read this before trusting a number

Every document is honestly labeled:
- **`complete`** — mechanic/guide content that is stable and unlikely to be patch-sensitive.
- **`partial`** — real, structurally accurate content where exact numeric values (damage factors, rage costs, percentages) should be cross-checked in-game, because RoK rebalances frequently and this repo is not live-synced to the game client.
- **`stub-pending-research`** — a placeholder acknowledging a gap rather than inventing content to fill it.

This repository deliberately does **not** fabricate commander stats, skill numbers, or event schedules it hasn't verified. Where exact current values matter, each document says so explicitly and points to `sources:`.

## What's actually in here today

- **135 fully-written commander files** (105 Legendary, 21 Epic, 9 Elite) — essentially the complete known playable roster, each researched against multiple community sources (AllClash, riseofkingdomsguides.com, techgamesnews.com, and others cited per-file) covering skills, talents, pairings, equipment, and strategy.
- **6 very recent commanders** (Alp Arslan, Hayam Wuruk, Yahya ibn Khalid, Elizabeth I, Mary I, Archimedes) have files but are explicitly marked `stub-pending-research` — their existence and rough role are confirmed, but full skill numbers weren't independently verified in this research pass.
- **`data/commander-roster-index.json`** cross-references the full roster against `data/commanders.json` and tracks the handful of remaining gaps.
- **9 mechanics references** covering the commander system, talents, troops, equipment, armaments, formations, rage, museum, and VIP.
- **7 pairing documents**, one per scenario (open-field, rally, garrison, barbarians, barbarian forts, gathering, canyon).
- **All 15 civilizations** — China, Rome, Britain, Germany, Arabia, Japan, Korea, Spain, Ottoman, Byzantium, Vikings, France, Egypt, Maya, Greece — each with sourced bonus values and role recommendations.
- **An equipment database** — Legendary weapon/armor/accessory pieces across Infantry, Cavalry, Archer, Leadership, Mixed, Gathering, and Accessories, plus beginner/midgame/endgame equipment guides and per-role optimization guides (Infantry, Cavalry, Archer, Rally, Garrison, Open Field, Gathering).
- **An event database** — Wheel of Fortune, Mightiest Governor, Ark of Osiris, Lucerne Scrolls, Sunset Canyon, The Karuak Ceremony, Silk Road, Shadow Legion, Ceroli Crisis, Alliance Mobilization, and Clarion Call, each with mechanics, F2P strategy, spending strategy, and common mistakes.
- **A research database** — fundamentals, military/economic research priorities, a full T5 progression guide, and research-during-KvK sequencing.
- **A Crystal Technology database** (Season of Conquest) — overview, early/mid/late-season strategy, and a condensed priority checklist for F2P and whale accounts.
- **Progression guides** spanning beginner (Day 1 / Day 7 / Day 30 / First 90 Days), midgame (City Hall 21-25, T4 unlocking, commander investment, equipment transition, KvK prep, alliance participation), and endgame (T5 play, Season of Conquest, meta commander investment, Armaments, fighting efficiency).
- **Advanced guides** — account/farm-account optimization, war guides (open field, target selection, rally/garrison support, hospital management, kill events), and alliance leadership (officers, kingdom management, KvK leadership, diplomacy, rules creation).
- **Generated JSON** (`data/commanders.json`, `pairings.json`, `guides.json`, `equipment.json`, `events.json`, `civilizations.json`, `mechanics.json`) kept in sync with markdown via `scripts/markdown-to-json.py`.

See [CHANGELOG.md](CHANGELOG.md) for the full version history and known gaps.

## Using this repo with a local LLM (RAG)

Documents are intentionally kept small (one commander/pairing/guide per file) with rich frontmatter (`tags`, `aliases`, `sources`) to maximize retrieval precision. When indexing:
- Chunk per-file, not per-repo — files are already sized for single-chunk retrieval in most cases.
- Surface `detail_status` to the end user or downstream LLM prompt so it can hedge appropriately on `partial`/`stub-pending-research` content instead of asserting it as verified fact.
- Use `data/*.json` directly for structured lookups (e.g., "list all Cavalry Legendary commanders") rather than re-parsing markdown at query time.

## Validating the repository

```bash
python3 scripts/markdown-to-json.py   # regenerate data/*.json from markdown
python3 scripts/validate-data.py      # check schema compliance, duplicate IDs, JSON validity
```

Both scripts are stdlib-only (no pip install required). Current status: **263 documents validated across 7 categories, 0 duplicate IDs, 0 invalid JSON** (see `scripts/README.md`).

## Automated verification (CI)

Every pull request and every push to `main` runs [`.github/workflows/validate-and-sync.yml`](.github/workflows/validate-and-sync.yml), which:

1. **Regenerates** `data/*.json` from the current markdown.
2. **Verifies** the whole repository with `scripts/validate-data.py` — the check goes red and blocks merge if any frontmatter field, required section, or duplicate ID is wrong.
3. **Auto-commits** the regenerated `data/*.json` straight back onto the branch if verification passed and something had drifted (e.g. a contributor edited markdown but forgot to run the scripts locally).

This means running the scripts locally before submitting is a nice-to-have for fast feedback, not a hard requirement — CI catches and self-heals JSON drift automatically. Auto-commit only runs for branches within this repository; pull requests from forks still get full verification, but the contributor (or a maintainer, via "Allow edits from maintainers") needs to run the scripts and push the regenerated JSON themselves, since `GITHUB_TOKEN` can't push to a fork.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full step-by-step guide with copy-paste templates. The single most valuable contribution right now is picking a commander from `data/commander-roster-index.json` that lacks a detail file and researching/writing it against a verified source.

## License

[MIT](LICENSE) for the repository structure/tooling/writing. Game content, names, and trademarks belong to Lilith Games.
