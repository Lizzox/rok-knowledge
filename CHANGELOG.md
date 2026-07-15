# Changelog

All notable changes to this knowledge base are documented here. Format loosely follows [Keep a Changelog](https://keepachangelog.com/).

## [0.5.0] — 2026-07-15

### Added
- **`.github/workflows/validate-and-sync.yml`** — CI pipeline running on every pull request and every push to `main`: regenerates `data/*.json`, runs `scripts/validate-data.py` (blocks merge on any failure), and auto-commits regenerated JSON back onto same-repo branches if it drifted from what the contributor committed. Fork PRs get full verification but not auto-commit, since `GITHUB_TOKEN` can't push to a fork.
- CI status badge in `README.md`, plus a new "Automated verification (CI)" section explaining the pipeline.
- `CONTRIBUTING.md` rewritten as a step-by-step, template-driven guide (previously reference-style only): pick-a-task table, copy-paste `<details>` templates for all 6 contributor-facing document types, and an explicit "write honestly" step foregrounding the no-fabrication rule.

### Notes
- Local script execution (Step 5 in `CONTRIBUTING.md`) is now optional for fast feedback rather than mandatory — CI catches and self-heals JSON drift automatically for same-repo branches.

## [0.4.0] — 2026-07-15

### Added
- **Full `civilizations/` database**: all 15 known civilizations (China, Rome, Britain, Germany, Arabia, Japan, Korea, Spain, Ottoman, Byzantium, Vikings, France, Egypt, Maya, Greece), each with sourced bonus values and role recommendations. New `schemas/civilization-schema.json` and `data/civilizations.json` (previously an unverified 12-entry stub).
- **New `data/mechanics.json`**, generated from the 9 existing `mechanics/*.md` files — previously these were never exported to JSON despite having `category: mechanic` frontmatter.
- `guides/beginner/civilization-choice.md` rewritten with role-based civilization recommendations (rally leader → Arabia, garrison defense → Vikings/Rome, etc.) instead of generic "don't overthink it" advice only.

### Fixed
- **`scripts/markdown-to-json.py` was silently skipping `crystal-tech/`** — the 4 Crystal Technology guides (`overview`, `beginner`, `optimization`, `priorities`) have `category: guide` frontmatter but live outside `guides/`, so they were never being collected into `data/guides.json` despite passing individual validation. The script now supports multiple source directories per output file; `crystal-tech/` and `mechanics/` are both wired in.
- A repository-wide `[[wikilink]]` cross-reference audit found and fixed 11 broken internal links (all caused by the `crystal-tech`/`mechanics` collection gap above, not by typos) — 0 broken links remain outside one intentional documentation example in `CONTRIBUTING.md`.
- `scripts/README.md` was out of date (referenced only 3 of what are now 7 categories, described `equipment`/`events`/`civilizations` as hand-maintained stubs) — rewritten to match the current script behavior and category table.

### Notes
- Validation after this QA pass: **263 documents across 7 categories, 0 duplicate IDs, 0 invalid JSON, 0 unintended broken cross-references** (up from 235 across 5 categories at `0.3.0`).
- This pass was a full-repository audit requested ahead of publishing the repo: every JSON file, every markdown category, and every internal cross-reference was checked, not just newly-added content.

## [0.3.0] — 2026-07-15

### Added
- **New top-level `equipment/` database** (replacing the earlier stub), organized by `infantry/`, `cavalry/`, `archer/`, `leadership/`, `mixed/`, `gathering/`, `accessories/` — 17 individual Legendary equipment/accessory pieces (Hammer of the Sun and Moon, Conqueror's Helm, Eternal Knight set, Karuak's Humility, Pride of the Khan, Hope Cloak, Navar's Control, Ash of the Dawn, the Legendary Archer set, The Bard's Pendant, Pendant of Eternal Night, Ring of Doom, Horn of Fury, Scolas' Lucky Coin, Vengeance, plus 2 category stubs for Leadership/Mixed pending named-piece research).
- New `schemas/equipment-schema.json`-conformant `data/equipment.json`, generated from markdown like every other category.
- **9 equipment guides** under `guides/equipment/`: beginner, midgame, endgame, and per-role optimization (Infantry, Cavalry, Archer, Rally, Garrison, Open Field, Gathering).
- **New top-level `events/` database** (replacing the earlier stub), organized by `commander-events/`, `alliance-events/`, `solo-events/`, `seasonal-events/`, `special-events/` — 11 individual event files (Wheel of Fortune, Mightiest Governor, Ark of Osiris, Lucerne Scrolls, Sunset Canyon, The Karuak Ceremony, Silk Road, Shadow Legion, Ceroli Crisis, Alliance Mobilization, Clarion Call), each covering mechanics, F2P/spending strategy, and common mistakes.
- New `schemas/event-schema.json`-conformant `data/events.json`.
- **New top-level `research/` structure** (`military/`, `economic/`, `academy/`, `civilization/`, `optimization/`) cross-linking to 5 new research guides: fundamentals, military research, economic research, T5 progression, and research-during-KvK.
- **New top-level `crystal-tech/` database**: overview, beginner (early season), optimization (mid/late season), and a condensed priority checklist.
- **13 new progression guides**: 4 beginner (Day 1, Day 7, Day 30, First 90 Days), 6 midgame (CH21-25, T4 unlocking, commander investment, equipment transition, KvK prep, alliance participation), and — combined with equipment/crystal-tech — a full endgame set (T5 players, Season of Conquest, meta commander investment, Armaments, fighting efficiency).
- **13 new advanced guides**: account/farm-account optimization (2), war guides (open field, target selection, rally support, garrison support, hospital management, kill events — 6), and alliance leadership (officer, kingdom management, KvK leadership, diplomacy, rules creation — 5).
- Corrected `mechanics/armaments.md`, which previously mischaracterized Armaments as a kingdom/alliance-wide buff system — it is in fact an individual-account, Formation-attached stat-boost system obtained via daily Travel/Dispatch activities. Fixed based on this pass's research.
- `scripts/markdown-to-json.py` and `scripts/validate-data.py` extended to cover the new `equipment` and `event` categories alongside `commander`, `pairing`, and `guide`.

### Known gaps (tracked, not hidden)
- Equipment coverage is representative (named top-tier Legendary pieces cited across multiple high-spender build guides), not exhaustive — RoK has dozens of Purple/Gold-tier pieces and several more named Legendary sets not yet individually filed.
- Several event files (Shadow Legion, Clarion Call) are marked `stub-pending-research` — their existence is confirmed via community event-calendar tracking, but current-run mechanics weren't independently verified this pass.
- `civilizations/` remains a stub from `0.1.0`.
- As always, exact numeric values (equipment stats, event point thresholds, research costs) are marked `partial` and should be cross-checked in-game.

### Notes
- This pass focused on breadth across six new knowledge domains (equipment, events, research, crystal tech, progression, advanced/war/leadership) rather than commander-roster depth, which was the focus of `0.2.0`.
- Validation after this pass: **235 documents across 5 categories, 0 duplicate IDs, 0 invalid JSON** (up from 164 across 3 categories at `0.2.0`) — 33 guides added, 17 equipment items, 11 events.

## [0.2.0] — 2026-07-15

### Added
- **118 additional commander files**, bringing total commander coverage from 17 to **135** (105 Legendary, 21 Epic, 9 Elite) — essentially the complete known playable roster.
- Full Epic tier coverage (21/21) and full Elite tier coverage (9/9), each researched against multiple community build guides (AllClash, riseofkingdomsguides.com, techgamesnews.com, heaven-guardian.com, kangfumaster.com, and others cited per-file).
- 3 additional current-meta Legendary commanders discovered through pairing research and added beyond the original roster index: Liu Che, Arthur Pendragon, David IV.
- `data/PROGRESS.md` — internal working checklist tracking every commander against the roster index, used to drive this expansion and left in place for future contributors picking up remaining gaps.
- `data/commander-roster-index.json` updated to `near-complete` status with a `known_gaps` field replacing the old "mostly a to-do list" framing.

### Known gaps (tracked, not hidden)
- **6 very recently released commanders** (Alp Arslan, Hayam Wuruk, Yahya ibn Khalid, Elizabeth I, Mary I, Archimedes) have files but are marked `detail_status: stub-pending-research` — their existence, rarity, and rough role/pairings are confirmed from community tier-list mentions, but independently verified skill/talent numbers were not found in this research pass. These are 2026-era releases that dedicated build guides hadn't fully documented yet at research time.
- Advanced-rarity starter commanders remain intentionally un-itemized (see `commanders/advanced/README.md`) — low strategic value, high churn across client versions.
- `civilizations/`, `equipment/`, `events/`, and `kvk/` top-level folders remain stubs from `0.1.0`.
- As always, exact numeric skill/talent/damage values are marked `partial` and should be cross-checked in-game — this pass prioritized breadth (getting every commander a real, sourced file) over re-verifying numbers against the live client.

### Notes
- Validation after this pass: **164 documents, 0 duplicate IDs, 0 invalid JSON** (up from 46 at `0.1.0`).
- Next milestone: close the 6 stub-pending-research entries once dedicated build guides for those commanders mature, and begin populating `civilizations/`, `equipment/`, and `events/`.

## [0.1.0] — 2026-07-15

### Added
- Initial repository architecture: `commanders/`, `pairings/`, `guides/`, `mechanics/`, `civilizations/`, `equipment/`, `events/`, `kvk/`, `data/`, `schemas/`, `scripts/`.
- Four JSON Schemas (`commander`, `pairing`, `guide`, `equipment`) defining the data contract for all knowledge documents.
- 9 mechanics reference docs (commanders, talents, troops, equipment, armaments, formations, rage, museum, VIP).
- 17 fully-written commander files (10 Legendary, 6 Epic, 1 Elite) covering long-standing, high-confidence meta commanders, each with skills, pairings, equipment guidance, strengths/weaknesses.
- 7 pairing documents, one per scenario category (open-field, rally, garrison, barbarians, barbarian forts, gathering, canyon).
- 22 guide documents across beginner, progression, economy, combat, KvK, events, and advanced sections.
- `data/commanders.json`, `data/pairings.json`, `data/guides.json` — auto-generated from markdown frontmatter via `scripts/markdown-to-json.py`.
- `data/equipment.json`, `data/civilizations.json`, `data/events.json` — hand-maintained structural stubs pending deeper per-item research.
- `data/commander-roster-index.json` — a name/rarity index of the broader known commander roster (~130 names across all rarities), explicitly marked as unverified reference material, not gameplay-ready data.
- `scripts/validate-data.py` and `scripts/markdown-to-json.py` — stdlib-only Python 3 tooling; both pass clean against this initial content set (46 documents validated, 0 duplicate IDs, 0 invalid JSON).

### Known gaps (tracked, not hidden)
- The vast majority of the ~130-name commander roster does not yet have an individual detail file — see `data/commander-roster-index.json` for the to-do list.
- `civilizations/`, `equipment/`, `events/`, and `kvk/` top-level folders are stubs; narrative guidance for events/KvK lives under `guides/` in the meantime.
- Exact numeric skill/talent/damage values throughout are marked `partial` and flagged for in-game verification — RoK rebalances frequently enough that hardcoding precise numbers without a live source risks going stale immediately.

### Notes
- This is a living knowledge base intended to grow via `CONTRIBUTING.md`'s process. Version numbers will bump as coverage expands (target: full Legendary roster at `0.2.0`).
