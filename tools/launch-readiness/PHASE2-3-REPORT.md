# Phase 2 + 3 Report — Launch Ten Readiness

**Branch:** `content/launch-ten-readiness`  
**Date:** 2026-07-27  
**Production repo:** read-only throughout

---

## 1. Prior work (recap)

No content-side stat normalization branch existed. Production `e98dc132` parser + audit script define FULL coverage (`HP` + `AC` via labelled fields). This branch built on that by importing the real parser and aligning content to it.

---

## 2. The ten (approved)

| # | Campaign | Genre |
|--:|----------|-------|
| 1 | the-eternal-feast | Intrigue |
| 2 | the-porcelain-court | Horror |
| 3 | abyssal-descent | Horror |
| 4 | seven-swords-for-hire | Adventure |
| 5 | the-impossible-vault | Intrigue |
| 6 | academy-of-arcane-gastronomy | Fantasy |
| 7 | the-crimson-thread-of-silverport | Urban |
| 8 | murder-on-the-astral-express | Mystery |
| 9 | the-weather-weavers | Historical |
| 10 | wings-of-the-void | Sci-Fi |

---

## 3. Per-campaign results

### Parser coverage (production `gradeCoverage` after chunker extract)

Verified with `tools/launch-readiness/sim-chunker-coverage.ts` (mirrors production `extractEncounters` + real parser).

| Campaign | Before | After | Creatures fixed |
|----------|--------|-------|-----------------|
| the-eternal-feast | 10/10 full | 10/10 full | none (already good) |
| the-porcelain-court | numbers present; **0 chunker hits** | **10/10 full** | restructured bestiary to `### N. Name (CR X)` + `**HP:**` / `**AC:**` |
| abyssal-descent | 10/10 full | 10/10 full | none |
| seven-swords-for-hire | 10/10 full | 10/10 full | none |
| the-impossible-vault | **0/10** (no colons; wrong shape for chunker) | **10/10 full** | colon labels + `###` headers |
| academy-of-arcane-gastronomy | numbers present; **0 chunker hits** | **10/10 full** | restructured like Porcelain |
| the-crimson-thread-of-silverport | 10/10 full | 10/10 full | none |
| murder-on-the-astral-express | numbers present; **0 chunker hits** | **9/9 full** | restructured (9 monsters authored) |
| the-weather-weavers | multi-line dialect; **0 chunker hits** | **10/10 full** | restructured |
| wings-of-the-void | **0/10** (no colons; wrong shape) | **10/10 full** | colon labels + `###` headers |

**Stats scale:** all authored numbers left as written (party-of-four assumption). No pre-weakening for solo.

**No stats invented.** Only reformatted existing numbers.

### Product Identity renames (old → new)

| Campaign | Old | New |
|----------|-----|-----|
| the-eternal-feast | Cork (A one-eyed **Beholder**) | Cork (A sentient wine-cask spirit who peels open a knothole like a single staring pupil) |
| the-eternal-feast | **Kuo-Toa** (Krill race) | **Deepfin fishfolk** |
| the-eternal-feast | **Yuan-Ti** (Hiss race) | **Scalebound humanoid** |
| the-eternal-feast | **Blink Dog** (Shift race) | **Flickerhound** |
| abyssal-descent | graft a **Beholder** eye | graft a **void-socket eye** (torn from something that should not see) |
| abyssal-descent | live **Carrion Crawler** | live **bile-grub crawler** (many-legged corpse-scavenger) |
| murder-on-the-astral-express | **Githyanki** pirates / Heist | **Silverblade** astral corsairs / Silverblade Heist |
| murder-on-the-astral-express | **Githzerai** (Poinsettia, Philosopher, index) | **Aetherbound** / Aetherbound void-ascetic / Aetherbound Monk |

**False positive cleared:** Impossible Vault “Spectator Domes” = arena seating, not the beholder-kin. Left unchanged.

**Flagged (not on your explicit list; not renamed):** Eternal Feast staff table still uses **Drider**, **Rakshasa** (Rakshasa is SRD), **Otyugh** (SRD). **Drider** is commonly treated as Product Identity outside SRD — recommend a legal pass. Astral Express still names **Modron**, **Asmodeus Jr.**, **Zariel** (Planescape/archdevil flavour) — flag for commercial legal review, not auto-renamed.

### Trademark fixes

| File | Old | New |
|------|-----|-----|
| murder-on-the-astral-express.md | “Agatha Christie in **D&D** form” | “Agatha Christie in **tabletop RPG** form” |

No other `D&D` / `Dungeons & Dragons` / `DnD` hits in the ten after fix.

### Missing assets

- **No image file references** (`![](…)` or `.png`/`.jpg` paths) in the ten packages.
- In-repo `campaign-assets/` only has **blades-of-the-holy-war** (not in the ten).
- Prior catalog noted **Eternal Feast** Drive assets (partial: 5 chars / 3 monsters / 3 locations / 3 items) — **not present in this repo**. Report as external gap; do not block ingest of text.
- Creative briefs contain **prompt examples** for art generation, not broken relative paths.

### Openings (cold-read judgement)

| Campaign | Open | Problem (if any) |
|----------|------|------------------|
| the-eternal-feast | **Strong** | First shift / hire works cold. |
| the-porcelain-court | **Strong** | New dolls + Protocols + Basement. |
| abyssal-descent | **Strong** | Expedition begins; survival stakes immediate. |
| seven-swords-for-hire | **Strong** | Village hire; clear reason to act. |
| the-impossible-vault | **Strong** | Mastermind pitch session 1. |
| academy-of-arcane-gastronomy | **Strong** | Arrival / houses / first disasters. |
| the-crimson-thread-of-silverport | **Adequate / weak for trial** | Boomtown job works, but **multi-generation framing** is heavy for a new $15 subscriber’s first ten minutes. PO may want a “Act I only” launch blurb. |
| murder-on-the-astral-express | **Strong case, branding caution** | Locked train murder works. Overview still leans **Agatha Christie / Poirot-style detective** (Hercule Poinsettia) — not a trademark of Wizards, but **character IP risk** separate from this PI pass. |
| the-weather-weavers | **Strong** | Weather monopoly + Rogue Skies; clear sides. |
| wings-of-the-void | **Strong** | First jump / Fallers initiation is cinematic. |

**Did not rewrite prose** for openings — report only.

### Ingest structure

| Check | Result |
|-------|--------|
| Package files | All ten have overview + creative-brief + world-building + campaign-bible |
| `chunk_type` enum fit | Standard sections map to `creative_brief`, `world_building`, `faction`, `npc_tier*`, `location`, `quest_*`, `mechanic`, `item`, `monster`, `encounter`, `session_outline` |
| Monsters → `chunk_type='monster'` + `entity_name` | **All ten now extract** under production patterns (was 4/10 before reshape) |
| Structural risks | Bestiary still uses free prose abilities (fine). Encounter tables after `[TAG: ENCOUNTER_TABLE]` stay as `encounter` if patterns match. **Handouts** sparse — not required for combat. |

exFAT note: AppleDouble `._*` files litter some dirs — **do not commit**; already gitignored typically.

---

## 4. Git commits (reviewable stages)

| Commit | Scope |
|--------|--------|
| `docs(launch): Phase 1 selection…` | Selection + filesystem audit tooling |
| `fix(content): label HP/AC for Impossible Vault and Wings…` | Mechanical colon labels only |
| `legal(content): rename Product Identity creatures…` | PI renames only |
| `legal(content): remove D&D trademark…` | Trademark only |
| `fix(content): normalize launch-ten bestiaries for lore-keeper chunker` | Ingest shape (### CR headers) without changing numbers |

---

## 5. Phase 3 — SRD catalog audit (`monsters.json`)

**File (read-only):**  
`infinite-realms-production/ai-adventure-scribe-main/src/data/srd/monsters.json`  
**Count:** 334 entries.

### Against your Product Identity list

| Name | In catalog? | Recommendation |
|------|-------------|----------------|
| beholder / spectator / death tyrant / gauth | **No** | OK |
| mind flayer / illithid / elder brain / intellect devourer | **No** | OK |
| displacer beast | **No** | OK |
| githyanki / githzerai | **No** | OK |
| umber hulk | **No** | OK |
| carrion crawler | **No** | OK |
| yuan-ti | **No** | OK |
| slaad | **No** | OK |
| kuo-toa | **No** | OK |
| **blink dog** | **Yes** — `srd:blink-dog` | **Review.** User listed as PI; OGL 5.1 §PI enumeration does *not* name blink dog; Open5e tags it `wotc-srd`. Prefer counsel before shipping. |
| hook horror | **No** | OK |

### Additional catalog notes

| Entry | Why flagged |
|-------|-------------|
| **Drider** (`srd:drider`) | Not on classic OGL PI name list; not always treated as open. Present in Open5e `wotc-srd`. **Legal review.** |
| **Drow** (`srd:drow`) | Open content historically; OK for SRD use. |
| Vampire / were* **form splits** (18 entries) | Same creatures as Open5e’s 6 lycanthrope/vampire rows, expanded into form variants. Not PI; structural choice. |
| Owlbear | **SRD-legal** — not PI. |

### Diff vs Open5e `document=wotc-srd` (322 monsters)

- Production has **+18 form-variant rows** (vampire/were*).
- Production **missing** the 6 combined Open5e names (covered by form splits).
- **No bulk of illegal MM-only icons** (beholders, illithids, etc.) in this dump.

**Contamination severity:** Low for the classic PI set. Two entries need a human legal call (**Blink Dog**, **Drider**), not a mass purge.

### Clean-vs-replace recommendation

**Prefer targeted removal/replace of questionable rows over full catalog replace**, because:

1. Catalog is already ~aligned with Open5e WotC SRD.
2. Combat code may hard-reference `srd:…` ids; a wholesale replace risks id drift.
3. Form-split vampires/weres may be intentional for the engine.

**If you replace anyway:**  
Use **Open5e** (`https://api.open5e.com`, filter `document__slug=wotc-srd`, licence **CC-BY-4.0** on WotC SRD content) as the source of truth with explicit per-source tags.  
**5e-bits/5e-database** is fine for MIT tooling + OGL data dumps, but Open5e’s licence tags reduce “what may we ship?” ambiguity.

Suggested production wave actions (do **not** edit there from this worker):

1. Legal: keep or rename/remove **Blink Dog** and **Drider**.
2. Optionally reconcile form-split ids with whatever the combat resolver expects.
3. Re-run `scripts/audit-campaign-monster-stats.ts` against DB after ingesting the ten.

---

## 6. Structural issues that would break ingestion

| Issue | Status |
|-------|--------|
| Monsters not extractable by chunker | **Fixed** for all ten |
| HP/AC without colons | **Fixed** where present |
| Incomplete packages | **None** in the ten |
| Post-apoc genre hole | Unchanged — no post-apoc in launch ten |
| AppleDouble `._*` files on exFAT | Present locally; must not be committed |

---

## 7. Branch name

```
content/launch-ten-readiness
```

Push when ready: `git push origin content/launch-ten-readiness` (already tracking).

---

## 8. Remaining for product owner

1. Legal: Blink Dog + Drider in SRD catalog; Drider on Eternal Feast staff table; Astral Express detective branding; Modron/Asmodeus/Zariel names.  
2. Assets: External Drive art for Eternal Feast (and any future gen) not in repo.  
3. Crimson Thread trial UX: consider Act-I-only marketing copy.  
4. Production wave: ingest the ten → run DB audit script → ship.
