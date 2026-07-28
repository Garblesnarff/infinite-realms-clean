# Batch 2 — Next Ten Launch Readiness

**Branch:** `content/launch-ten-readiness`  
**Date:** 2026-07-27  
**Method:** Same as batch 1 — production parser + production chunker extract patterns; no invented stats; staged commits.

---

## Selection (batch 2)

| # | Campaign | Genre | Why |
|--:|----------|-------|-----|
| 1 | clash-of-olympus | Fantasy | Phase 1 alternate; traditional demigod epic |
| 2 | chronicles-of-the-somnolent-oracle | Fantasy | Original dream/oracle; not a film remake |
| 3 | ascension-protocol | Adventure | Phase 1 alternate; Titan / protocol climb |
| 4 | against-the-titans | Adventure | Slayer’s Guild colossus hunts |
| 5 | way-of-the-fading-blade | Historical | Phase 1 alternate; full package |
| 6 | the-chosen-slayer | Urban | Full-parse urban action |
| 7 | calypsos-death-derby | Horror | Vehicular death-tournament (distinct from batch-1 horror) |
| 8 | the-revolutionaries-anthem | Intrigue | Only other full-parse intrigue besides Eternal Feast |
| 9 | the-verdant-codex | Mystery | Full parse; PI/TM cleanup required |
| 10 | see-you-space-cowboy | Sci-Fi | Only sci-fi with real HP/AC after crows failed |

**Not selected**

| Campaign | Reason |
|----------|--------|
| wings-of-the-crows | Bestiary abilities only — **no HP/AC numbers** (would require inventing stats) |
| winters-ambassadors | Direct Le Guin names |
| dust-devils-due / all Post-Apoc | Still 0% parse, thin packages |
| academy-of-legends | Strong stats but heavy My Hero Academia pastiche |

**Genres covered:** Fantasy×2, Adventure×2, Historical, Urban, Horror, Intrigue, Mystery, Sci-Fi = **8**. Post-Apoc still empty.

---

## Parser / chunker coverage

| Campaign | Before | After |
|----------|--------|-------|
| clash-of-olympus | 10/10 | 10/10 |
| chronicles-of-the-somnolent-oracle | 9/9 | 9/9 |
| ascension-protocol | 0 chunker (porcelain one-liners) | **10/10 full** |
| against-the-titans | 0 chunker | **10/10 full** |
| way-of-the-fading-blade | 0 chunker (`# 7. Bestiary` single-hash + list dialect) | **10/10 full** |
| the-chosen-slayer | 0 chunker | **10/10 full** |
| calypsos-death-derby | 0 chunker | **10/10 full** |
| the-revolutionaries-anthem | 5/5 | 5/5 |
| the-verdant-codex | 0 chunker | **10/10 full** |
| see-you-space-cowboy | numbers present / 0 chunker shape | **10/10 full** |

Verified: `bun tools/launch-readiness/sim-chunker-coverage.ts --batch2`

Stats scale: unchanged (party of four). No invented numbers.

---

## Product Identity renames (batch 2)

All in **the-verdant-codex**:

| Old | New | File(s) |
|-----|-----|---------|
| Blink Dog companions | **Flickerhound** companions | overview |
| Blink dogs rule here | **Flickerhounds** rule here | bible |
| "Blink Dog (Creature)" | "Flickerhound (Creature)" | world-building-spec |
| Captain Hesperus (Githyanki…) | (Silverblade astral-sailor / corsair) | bible |
| Void-Eye (Beholder) / tiny beholder | grape-sized floating **eye-cluster spirit** | bible |

No PI hits remaining on batch-2 paths after renames.

---

## Trademark fixes

| Old | New | File |
|-----|-----|------|
| `## D&D Twist` | `## 5E-Compatible Twist` | the-verdant-codex.md |

---

## Commercial / pastiche flags (not auto-rewritten)

| Campaign | Flag |
|----------|------|
| see-you-space-cowboy | **Heavy Cowboy Bebop** (ship named Bebop, crew archetypes, “carry that weight”) — mechanical-ready, commercial risk high |
| the-chosen-slayer | Buffy / Hellmouth structure |
| way-of-the-fading-blade | Last Samurai structure |
| the-revolutionaries-anthem | Hamilton-adjacent revolution musical |
| calypsos-death-derby | Twisted Metal structure |
| verdant-codex | Still mentions “Red Wizards of Thay” as optional parallel — **flag** (FR proper name); not on your PI monster list |

---

## Openings

| Campaign | Judgement |
|----------|-----------|
| clash-of-olympus | **Strong** — demigod labors, Titans stir |
| chronicles-of-the-somnolent-oracle | **Adequate** — high-concept temporal dream; needs a concrete first scene (where are we when we wake?) for trial |
| ascension-protocol | **Strong** — climb / Protocol / Vertigo Syndicate |
| against-the-titans | **Strong** — Guild contract, research, hunt |
| way-of-the-fading-blade | **Strong** — hire / train / modernization threat |
| the-chosen-slayer | **Strong** — Hellmouth + high school + patrol |
| calypsos-death-derby | **Strong** — invitation cannot be declined; fight now |
| the-revolutionaries-anthem | **Strong** — uprising / nation-forging |
| the-verdant-codex | **Strong** — page in hand, two factions hunting |
| see-you-space-cowboy | **Strong open, IP problem** — bounty pitch works cold |

---

## Assets

- No broken image paths in batch-2 packages.
- No in-repo art for these ten under `campaign-assets/`.

---

## Ingest structure

All ten: overview + creative-brief + world-building + bible.  
Monsters extract as `chunk_type='monster'` with entity names after reshape.  
Revolutionaries has only **5** monsters (authored depth is lighter).

---

## Commits (expected staging)

1. Mechanical bestiary reshape (chunker + HP/AC labels) — batch 2 campaigns  
2. PI renames — verdant codex  
3. Trademark — verdant `D&D Twist`  
4. Docs — this report + batch2-campaigns.json  

---

## Running total (batch 1 + 2)

**20 campaigns** mechanical-ready for ingest under production parser/chunker, on branch `content/launch-ten-readiness`.
