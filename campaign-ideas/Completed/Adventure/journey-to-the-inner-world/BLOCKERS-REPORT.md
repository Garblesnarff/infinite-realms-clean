# Journey to the Inner World — Section 0 Blockers: Done

**From:** Campaign Claude, 2026-09-24. **For:** Rob, Asset Claude, Muse.
**Input:** `ART-DIRECTION.md` §0. **Verified with:** the real lore-keeper chunker bundle (production parser blobs unchanged on `main`).

## Result

| | Before | After |
|---|---|---|
| Parser verdict | FIXABLE | **CONFORMING** |
| Rows the ingest will write | 172 | **205** |
| Side quests reaching the DB | **0** (heading hid all 30) | **30** |
| Session outline names | `Session 1: **` (broken) ×12 | `Session 1: The Great Quake` … |
| Monster names with parentheticals | 3 | 0 |
| Causality rules | 0 | 8 |
| Card metadata | old draft: "Exploration / Lost World", 6–8 sessions, level 7→11–12, fading-sun premise | Adventure / Exploration / Weird Fantasy · 12–16 sessions · level 1→10 · Hard · new premise |
| Old-draft or IP terms left | many | **0** |

## Blocker 1 — companion files rewritten to match the bible

The brief, the **overview** and the **world-building spec** all described the abandoned draft: serpent men, an aboleth, dinosaurs, a fading crystal sun, "Professor" Finch. All three are ingested — the overview becomes the storefront card and the spec becomes DM lore — so all three were rewritten from the bible.

- `creative-brief.md` — new. It carries ART-DIRECTION §2: palette, colour script, faction colour keys, motifs, do-nots. The style line is now set to Ink & Glow (bake-off 2026-09-24). New tagline: *"The world is an egg — and it is hatching."*
- `journey-to-the-inner-world.md` (overview) — new, with the parser label block and a premise under 500 characters.
- `world-building-spec.md` — new, with 8 single-line IF/THEN rules that the parser reads.

## Blocker 2 — IP renames

| Was | Now | Where |
|---|---|---|
| Myconid (all uses) | **Sporefolk** | faction "The Sporefolk Sovereignty", its capital, 4 tier-2 roles, 2 items, quests, encounters, index |
| Kenku (The Silent) | Ravenfolk | app race name |
| Tabaxi (The Echo-Hunter) | Catfolk | app race name |
| Aasimar (The Luminous One) | Celestialborn | app race name; Aasimar is not in the app |
| Artificer (Progenitor Prime) | Wizard | seeding rejects non-SRD classes |
| "The Self-Solving Rubik's Cube" | "The Self-Solving Puzzle Cube" | trademark |

## Blocker 3 — starter characters (5)

`seed-journey-to-the-inner-world-character-templates.sql`, summarised in `STARTER-CHARACTERS.md`:

| Character | Race | Class |
|---|---|---|
| The Driller | Dwarf (Mountain Dwarf) | Fighter |
| The Surveyor | Human | Wizard |
| The Lamplighter | Halfling (Lightfoot Halfling) | Rogue |
| The Chaplain | Human | Cleric |
| The Echo | Ravenfolk | Bard |

- **Classes are SRD only, and races use the app's names.** SRD equipment names are used, so armour equips and sets AC.
- **Every hook starts from the bible's sessions 1–2:** the Great Quake, then being hired by Baron Finch.
- **The SQL was tested in a real Postgres** with the production table definition. It applied cleanly **twice**, because of the `ON CONFLICT` upsert, and gave 5 rows.
- **Apply order:** only after the campaign is ingested, because of the FK. It becomes a migration PR, as with Midsummer #2204.

## Blocker 4 — name cleanup

- **Monster parentheticals removed:** Fungal-Zombie, Grafted Horror, Chaos-Mutant. The tag moved to the type line.
- **Renames to avoid reuse across campaigns:**
  - Dr. Aris Thorne → **Dr. Tobias Venn**. The old name is also in Abyssal Descent and 7 other bibles. His secret no longer points to an NPC from another campaign.
  - Warden-Unit 734 → **Warden-Unit 9**. "Unit 734" appears in 3 other bibles.
- **Structure fixes the parser needed:**
  - Added a `## Side Quests` heading and bolded the quest names, which recovers 30 quests.
  - Added a `## Mechanics` heading.
  - Session titles now use the `**Session N: Title**` form, which fixes 12 broken names.
- **Small fixes:**
  - The Surface Sentinels had two `Leader:` lines; the second is now `Agenda:`.
  - "The shores of the Sea of Chaos" → "The Shores of the Sea of Chaos".
- **Off-theme side quests re-themed.** 5 side quests came from a pirate campaign (Orla, Rhys, "The Parrot", a reformed pirate, a ship's captain). They now use this bible's own NPCs and places: Boro, Umbra, Lila, a cave-parrot from the Canopy of Stars, and a Flesh-Weaver ship's pilot.
- **Checked and fine:** numbered NPC and item lists do **not** leak numbers into names here. Trailing colons on items and quests are stripped by the ingest.

## Decisions for Rob

1. **The level range (1→10) and length (12–16 sessions) are proposals.** The bible states neither. Level 1 matches the pregens. The final monsters, CR 8–9, suit roughly level 9–10 by the end.
2. ~~**Pick the style:** run the 6 prompts in `STYLE-BAKE-OFF-PROMPTS.md`.~~ **Done 2026-09-24: graphic novel "Ink & Glow" locked (2 of 3).**

## Not done here (next steps)

- **Monster attack lines** (#2212 rules) — a Muse task, after the style is locked.
- **Commit:** these files are on the Mac as uncommitted changes. They need a commit plus a PR to `infinite-realms-clean`.
- **Order after that:** merge → ingest → pregen migration → generate art → manifest → upload.
