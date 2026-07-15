# Contributing to rok-knowledge

Thanks for helping grow RoK Lab's knowledge base! You don't need to be a programmer — if you can edit a text file and copy-paste a template, you can contribute. This guide walks through everything step by step.

**No local setup required to write content.** You only need Python (already on most computers) to run the two checker scripts before submitting — see [Step 5](#step-5-validate-your-work).

---

## The 3-minute overview

1. This repo is a pile of small markdown files (one per commander/guide/equipment piece/etc.), each with a little metadata block at the top.
2. You pick a topic that's missing or wrong, write/fix a file following a template, run two scripts to check your work, and open a pull request.
3. **Golden rule: never invent numbers.** If you don't know the exact damage factor or drop rate, write "verify in-game" instead of guessing. See [Ground rule #1](#ground-rules) below — this is the one rule that really matters.

---

## Step 1: Pick something to work on

Not sure where to start? Pick whichever is easiest for you:

| I want to... | Go here |
|---|---|
| Fill in a missing commander | Open [`data/commander-roster-index.json`](data/commander-roster-index.json), find a name **not** listed under `has_detail_file`, or any commander file marked `detail_status: stub-pending-research` in [`data/commanders.json`](data/commanders.json) |
| Fix outdated numbers | Search for the commander/item/event you know has changed, check its `last_updated` date |
| Add a missing pairing | Look in [`pairings/`](pairings/) — some scenario folders (e.g. `barbarian-forts/`, `canyon/`) only have one or two entries |
| Add equipment | [`equipment/leadership/`](equipment/leadership/) and [`equipment/mixed/`](equipment/mixed/) are explicitly marked as stubs needing named pieces |
| Add/expand an event | Check [`events/special-events/`](events/special-events/) — Shadow Legion and Clarion Call are `stub-pending-research` |
| Write a guide | Anything in [`guides/`](guides/) can always use more detail or a fresher example |

If genuinely nothing above appeals to you, just fix a typo or clarify a confusing sentence — small corrections are welcome too.

---

## Step 2: Find your document type's template

Every file in this repo is one of 7 types. Click through to the matching template below, copy it into a new file (or open the existing file you're fixing), and fill in the blanks.

<details>
<summary><b>Commander</b> — a playable hero (<code>commanders/{legendary|epic|elite|advanced}/name.md</code>)</summary>

```markdown
---
id: commander-name-kebab-case
name: Commander Name
category: commander
rarity: Legendary
civilization: unspecified in sources
release_date: unknown
specialties: [Cavalry, Skill]
tags: [cavalry, open-field, rally]
aliases: []
last_updated: YYYY-MM-DD
sources:
  - "url or reference you actually used"
detail_status: partial
---

# Commander Name

## Overview
One paragraph: what makes this commander notable, and their overall role.

## Statistics
> Verify exact numbers in-game — note this if you're not 100% sure of a value.

- Specialties: ...
- Troop type: ...

## Skills
- **Active — Skill Name:** what it does, damage factor if known.
- **Passive:** what it does.

## Recommended Usage
Primary/secondary role, best scenario (open field / rally / garrison).

## Best Pairings
- **Other Commander** — why the pairing works.

## Equipment
Recommended gear category/set.

## Strategy Tips
Practical advice a real player would find useful.

## Strengths
- ...

## Weaknesses
- ...

## Sources
- List every source you actually consulted.
```
File location: `commanders/{rarity}/{kebab-case-name}.md`
</details>

<details>
<summary><b>Pairing</b> — two commanders that work well together (<code>pairings/{scenario}/name.md</code>)</summary>

```markdown
---
id: pairing-commander-a-commander-b
name: Commander A + Commander B
category: pairing
scenario: open-field
troop_type: Cavalry
primary_commander: Commander A
secondary_commander: Commander B
tags: [cavalry, open-field]
last_updated: YYYY-MM-DD
sources:
  - "url or reference"
detail_status: partial
---

# Commander A + Commander B

## Purpose
One sentence: what this pairing is for.

## Explanation
Why the two kits work together — be specific about which skill/passive synergizes with which.

## Strengths
- ...

## Weaknesses
- ...

## Alternatives
- Substitute commander if you don't have one of the pair.

## Sources
- ...
```
File location: `pairings/{open-field|rally|garrison|barbarians|barbarian-forts|gathering|canyon}/{name}.md`
</details>

<details>
<summary><b>Guide</b> — a how-to or strategy writeup (<code>guides/{section}/name.md</code>)</summary>

```markdown
---
id: guide-short-name
name: Guide Title
category: guide
section: beginner
audience: new-player
summary: One sentence describing what this guide covers.
tags: [beginner, ...]
last_updated: YYYY-MM-DD
sources:
  - "url or reference"
detail_status: partial
---

# Guide Title

## Overview
What this guide covers and why it matters.

## Recommended Usage
The actual advice, step by step if applicable.

## Strategy Tips
Extra practical tips.

## Sources
- ...
```
`section` must be one of: `beginner`, `progression`, `economy`, `combat`, `kvk`, `events`, `advanced`.
File location: `guides/{section}/{name}.md`
</details>

<details>
<summary><b>Equipment</b> — a weapon/armor/accessory piece (<code>equipment/{category}/name.md</code>)</summary>

```markdown
---
id: item-name-kebab-case
name: Item Name
category: equipment
slot: Weapon
rarity: Legendary
material_source: ["how it's obtained"]
set: Set name if applicable
best_for: ["Cavalry", "Rally leaders"]
tags: [cavalry, weapon, legendary]
last_updated: YYYY-MM-DD
sources:
  - "url or reference"
detail_status: partial
---

# Item Name

## Overview
What the item is and why it's used.

## Stats
> Note if exact values are unverified.

## Best Users
Which commanders/troop types benefit most.

## Best Pairings
Which other pieces it's typically used alongside.

## Crafting Priority
Where it ranks vs. other slots.

## F2P Alternatives
What a non-spender should use instead.

## Endgame Evaluation
Is it worth chasing, and for whom.

## Sources
- ...
```
`slot` must be one of: `Helmet`, `Chestplate`, `Weapon`, `Boots`, `Belt`, `Ring`, `Necklace`.
File location: `equipment/{infantry|cavalry|archer|leadership|mixed|gathering|accessories}/{name}.md`
</details>

<details>
<summary><b>Event</b> — a recurring in-game event (<code>events/{type}/name.md</code>)</summary>

```markdown
---
id: event-name-kebab-case
name: Event Name
category: event
event_type: alliance-event
frequency: "how often it recurs"
duration: "how long it lasts"
requirements: ["what you need to participate"]
rewards: ["what you get"]
tags: [alliance-event, ...]
last_updated: YYYY-MM-DD
sources:
  - "url or reference"
detail_status: partial
---

# Event Name

## Overview
What the event is and how it fits into the game.

## How It Works
Mechanics, step by step.

## Best Strategy
## F2P Strategy
## Common Mistakes

## Sources
- ...
```
`event_type` must be one of: `commander-event`, `alliance-event`, `solo-event`, `seasonal-event`, `special-event`.
File location: `events/{matching-folder}/{name}.md`
</details>

<details>
<summary><b>Civilization</b> — a starting civilization (<code>civilizations/name.md</code>)</summary>

```markdown
---
id: civilization-name
name: Civilization Name
category: civilization
bonuses: ["+X% something", "+Y% something else"]
best_for: ["Playstyle this suits"]
tags: [civilization]
last_updated: YYYY-MM-DD
sources:
  - "url or reference"
detail_status: partial
---

# Civilization Name

## Overview
What the civilization is good at.

## Bonuses
- List each bonus.

## Best For
Who should pick this civilization.

## Sources
- ...
```
File location: `civilizations/{name}.md`
</details>

---

## Step 3: Write honestly

This is the one rule that matters more than the others:

> **If you don't know an exact number, don't guess.** Write "verify in-game" or "pending research" instead. Set `detail_status: stub-pending-research` if most of the file is unverified, or `detail_status: partial` if the structure/role is solid but some numbers need checking.

Everything else follows from this:
- **Cite where you got your information** in the `sources:` list — a wiki page, a community guide, a YouTube video title, whatever you actually used.
- **One topic per file.** Don't combine two commanders or two events into one document.
- **Write like you're briefing a teammate**, not writing marketing copy — short, direct sentences.

---

## Step 4: Save your file in the right place

Match the file location shown in each template above. The **file name** should be the kebab-case version of the `id` field, e.g. `id: yi-seong-gye` → `commanders/legendary/yi-seong-gye.md`.

---

## Step 5: Validate your work

Run these two commands from the repository root (no installation needed — both scripts use only Python's standard library):

```bash
python3 scripts/markdown-to-json.py
python3 scripts/validate-data.py
```

- The first command regenerates the `data/*.json` files from your new/edited markdown.
- The second checks that your frontmatter has all required fields, your file has all required section headings, and there are no duplicate IDs.

If it prints `All checks passed`, you're good. If it lists problems, fix them and re-run — the error messages tell you exactly which file and which field.

**Commit the regenerated `data/*.json` files together with your markdown change** so they never drift out of sync.

> **This step is optional, but recommended for fast feedback.** Every pull request automatically runs the same two commands via [GitHub Actions](.github/workflows/validate-and-sync.yml): it verifies your PR the same way, and if you forgot to regenerate the JSON locally, the workflow **auto-commits the corrected `data/*.json` straight onto your PR branch** — as long as your PR is from a branch in this repository (not a fork; forks don't grant the bot push access, so fork contributors do need to run the scripts locally and push the result themselves).

---

## Step 6: Submit

Open a pull request with:
- A short title describing what you added/fixed (e.g. "Add commander: Example Name" or "Fix Ramesses II skill damage factor").
- If you're correcting an existing file, mention what was wrong and update its `last_updated` date.

Small, focused pull requests (one commander, one guide, one correction) are easier to review than large batches — don't feel like you need to fill in everything at once.

---

## Ground rules

1. **No fabricated data.** Covered above — this is the big one.
2. **Cite your sources.** Every document has a `sources:` field.
3. **Keep documents small.** One commander/pairing/guide/item/event per file.
4. **Follow the schema.** Match the templates above; they mirror `schemas/*.json`.
5. **Regenerate JSON after markdown edits.** `scripts/markdown-to-json.py` then `scripts/validate-data.py`, every time — or let CI do it for you automatically (see [Step 5](#step-5-validate-your-work)).

## Style

- No fictional lore embellishment — stick to what's documented/verifiable.
- Prefer short declarative sentences over marketing language.
- Use present tense for how mechanics currently work.

## Questions?

If a template doesn't fit what you're trying to add, open an issue describing what you want to contribute — it might mean the repo needs a new document type, which is a useful thing to know.
