# Phase 1 — Launch Ten Selection

**Branch:** `content/launch-ten-readiness`  
**Date:** 2026-07-27  
**Status:** STOPPED for product-owner approval — no readiness fixes applied yet.

---

## 1. Prior normalization work found

### Content repo (`infinite-realms-clean`)

| Finding | Detail |
|--------|--------|
| Branches | `main`, remotes: `agent/add-godskin-atlas-campaign-package`, `chore/campaign-catalog-and-reorganization`, `chore/campaign-pilot-migration`, `claude/improve-dnd-campaign-agent-…` |
| Stat-block normalization branch | **None.** No commits, stashes, or branches rename/reformat bible stat blocks for the production parser. |
| Related prior work | Catalog + pilot migration branches (`a0539c94`, `a892fe2d`) add schema, launch-readiness slate, IP triage, pilot package moves for Eternal Feast / Porcelain Court / St. Mercy’s / Combat Healer — **not** parser coverage fixes. |
| Coverage numbers from content work | **None recorded.** Nothing in this repo graded monsters with `gradeCoverage()`. |

### Production repo (read-only — where the real prior work lives)

Recent combat work (not in this content repo) is what “normalization” actually means so far:

| Commit | What it did |
|--------|-------------|
| `e98dc132` | `feat(combat): make campaign-authored monsters fight at their authored stats` — campaign_chunks → SRD → generic ladder; **authored-stat-block-parser**; handles Eternal Feast `**HP:** 90` and Abyssal Descent `*HP:* 80` dialects |
| `0525400b` | Attacks from catalog / bible / CR derivation |
| `0abc7383` | Scale monsters by `partySize/4` at runtime |
| Audit script | `scripts/audit-campaign-monster-stats.ts` — DB-backed, uses same parser; needs `DATABASE_URL` |

**Playtest context from parser commit message:** Eternal Feast creatures (Gluten Golem 90 HP, Shadow Roach 20, etc.) were fighting as 11 HP generics before the ladder. Three campaigns are referenced as ingested/playtested dialects: **the-eternal-feast**, **abyssal-descent**, and (by catalog/pilot) **the-porcelain-court**.

**Implication for Phase 2:** There is **no established house curve for inventing missing stats**. Do not invent HP/AC unless a creature already has numbers in a non-colon dialect that only needs label/format fixes for the real parser. Gaps with zero numbers get reported, not filled.

---

## 2. Selection criteria (defended)

Weighted for a **$15/mo solo AI DM trial conversion** plus a flagship shelf, not a museum of 163:

| Weight | Criterion | Why |
|--------|-----------|-----|
| **Highest** | **Parser full coverage today** (or one mechanical format fix: add colons) under the **production** `gradeCoverage()` | A catalog where creature four of campaign eleven is a silent 11 HP placeholder is worse than ten that work. Measured, not estimated. |
| **High** | **Completeness** — overview + creative-brief + world-building + campaign-bible | Ingestion needs structure; half-packages waste engineering time. |
| **High** | **Genre spread** | Nine genres exist; ten horrors is a worse product than ~8 genres with two flagship lengths. |
| **High** | **Opening runnability** | First ten minutes decide trial conversion: place + situation + reason to act, cold. |
| **Medium** | **Legal cleanliness** | Product Identity creature names and Wizards trademarks are fix-or-skip. Heavy film/novel pastiches (Le Guin names, Last of Us, pure Poirot) are flagged even when stats parse. |
| **Medium** | **Length mix** | Prefer several **short/medium** (8–18 sessions) for trials + **1–2 long flagships** for “I subscribed and want a world.” |
| **Lower** | **Assets on disk** | Almost none in-repo; Eternal Feast has Drive partial coverage per prior catalog. Missing assets reported in Phase 2, not used as a hard gate when the writing is the unique asset. |
| **Lower** | **Already in pilot / playtest path** | Bias toward Eternal Feast / Porcelain / Abyssal only when they also win on coverage and originality. |

### How coverage was measured

- Script: `tools/launch-readiness/audit-bible-monster-stats.ts`
- **Imports** production `parseAuthoredStatBlock` / `gradeCoverage` from the sibling production path (no reimplementation).
- Extracts monster blocks with lore-keeper-ingest patterns **plus** common bible dialects the chunker currently misses (Porcelain one-liners, Wings compact lists).
- Full report JSON: `tools/launch-readiness/reports/bible-monster-coverage.json`

### Library-wide numbers (filesystem, all 303 Completed bibles)

| Metric | Value |
|--------|------:|
| Campaigns scanned | 303 |
| With ≥1 extractable monster block | 261 |
| Perfect full parse (all monsters full) | 46 |
| Total monster blocks | 1641 |
| Full / partial / none | 464 (28.3%) / 2 / 1175 |

**Structural finding:** Most “0% full” bestiaries already have numbers but use **`HP 30, AC 14` (no colon)** or narrative-only lines. The parser requires labelled `HP:` / `AC:`. That is a content format job, not a missing-design job.

**Genre hole:** **Post-Apocalyptic** has **zero** campaigns at full parser coverage. Completed packages are thin (~1.8k words) and often film-IP heavy (e.g. Cordyceps Crown = Last of Us). Not launch-ten material without a dedicated content wave.

---

## 3. Ranked ten (proposed)

| Rank | Campaign | Genre | Parser (full/n) | Length (author) | Why this rank |
|-----:|----------|-------|----------------:|-----------------|---------------|
| 1 | **the-eternal-feast** | Intrigue | **10/10** | Long (~35 sess) | Unique product identity (interdimensional restaurant). Already in combat/parser playtest lore. Flagship. **PI renames required** (Beholder Cork, Yuan-Ti / Kuo-Toa / Blink Dog staff rows). |
| 2 | **the-porcelain-court** | Horror | **10/10** | Long (~30 sess) | Strong cold open (new dolls, Protocols, Basement). Dark social flagship; pilot-migration package. Clean PI scan. |
| 3 | **abyssal-descent** | Horror | **10/10** | Short (10–15) | Survival trial campaign; parser dialect reference. Distinct from Porcelain (claustrophobia vs court). **PI nips:** Beholder eye graft secret; Carrion Crawler sample quest. |
| 4 | **seven-swords-for-hire** | Adventure | **10/10** | Medium (12–18) | Classic “hire blades, defend village” open; clear reason to act session 1. Full stats. Seven Samurai *structure* (public-domain pattern), not a named IP dump. |
| 5 | **the-impossible-vault** | Intrigue | **0/8** (loose HP/AC present) | Short (8–10) | Best **trial conversion** length: stylish heist, session 1 pitch. Needs colon/format normalization only — **not** invented stats. |
| 6 | **academy-of-arcane-gastronomy** | Fantasy | **10/10** | Long (~35 / “4 years”) | Original magical cooking school; marketable without being a film remake. Complements Feast without duplicating the restaurant premise. |
| 7 | **the-crimson-thread-of-silverport** | Urban | **10/10** | Epic multi-gen | Only urban package that is both complete **and** full-parse. Opening is strong (boomtown job / corrupt foreman). Long — flagship urban, not trial. |
| 8 | **murder-on-the-astral-express** | Mystery | **9/9** | Long multi-case | Full parse mystery with a cold-openable locked-train case. **Caveat:** overview leans hard Agatha Christie / Poirot names — flag for PO rename of detective IP if player-facing. Bible history mentions **githyanki** (PI rename). |
| 9 | **the-weather-weavers** | Historical | **10/10** | Short/medium package | Full 4-file package + full parse. Prefer over silk-and-shadow-road (bible-only, incomplete for ingest) and way-of-the-fading-blade (Last Samurai pastiche risk). |
| 10 | **wings-of-the-void** | Sci-Fi | **0/10** (HP/AC present, **no colons**) | Long (~24) | Only strong **original** sci-fi with a real bestiary + hook (Fallers, Skyrift). Avoided **see-you-space-cowboy** despite 10/10 parse (Cowboy Bebop pastiche). Format fix only. |

**Genres covered:** Intrigue, Horror×2, Adventure, Fantasy, Urban, Mystery, Historical, Sci-Fi = **8**.  
**Missing from ten:** Post-Apocalyptic (no ready package).  
**Length mix:** 2 short (Abyssal, Impossible Vault), mid (Seven Swords, Silk Road), rest long/flagship.

---

## 4. Five alternates (swap freely)

| Alt | Campaign | Genre | Parser | Swap when… |
|-----|----------|-------|-------:|------------|
| A1 | **clash-of-olympus** | Fantasy | 10/10 | You want traditional demigod/labors fantasy instead of food academy |
| A2 | **ascension-protocol** | Adventure | 10/10 | You want combat/Titan-hunt forward adventure instead of Seven Swords |
| A3 | **way-of-the-fading-blade** | Historical | 10/10 | Prefer samurai tragedy — **flag Last Samurai pastiche** for PO |
| A4 | **the-silk-and-shadow-road** | Historical | 10/10 monsters | Original metaphysical road — **bible only** (no brief/overview/world-building); needs package completion before ingest |
| A5 | **dust-devils-due** | Post-Apocalyptic | 0 (thin) | Only if you **must** show post-apoc at launch — needs bestiary + stats authored; **do not** pick Cordyceps Crown (Last of Us names) |

Other near-misses intentionally **not** alternates:  
- **winters-ambassadors** — full parse but **direct Le Guin** (Ekumen, Gethen, Karhide, Estraven).  
- **see-you-space-cowboy** — full parse but Bebop.  
- **the-watchmen-protocol** / **the-white-wolfs-hunt** — named IP risk.  
- **jazz-noir-city** — prior slate pick; **no bestiary**, ~1.6k words.

---

## 5. Opening judgements (preview — full Phase 2 still pending)

| Campaign | Opening cold-run? | Note |
|----------|-------------------|------|
| Eternal Feast | **Strong** | Hired as staff; first service chaos. |
| Porcelain Court | **Strong** | New dolls, Protocols, wrongness. |
| Abyssal Descent | **Strong** | Expedition starts descending. |
| Seven Swords | **Strong** | Village hires desperate blades. |
| Impossible Vault | **Strong** | Mastermind pitch. |
| Arcane Gastronomy | **Strong** | First day / sorting / disaster. |
| Crimson Thread | **Adequate** | Boomtown job works; multi-gen framing is heavy for a trial. |
| Astral Express | **Strong case, IP caution** | Train murder works; Poirot branding may need PO edit. |
| Weather Weavers | **TBD in Phase 2** | Package complete; opening not yet cold-read for weakness report. |
| Wings of the Void | **Strong** | First jump initiation is cinematic. |

---

## 6. What I will **not** do until you approve

- No PI renames, trademark sweeps, or stat-line rewrites on the ten.  
- No work on the other ~153.  
- No edits in `infinite-realms-production`.  
- No inventing stats for creatures that have none.

---

## 7. Approve / swap

Please reply with:

1. **Approve as ranked**, or  
2. **Swap list** (e.g. “drop Astral Express for Clash of Olympus; force a post-apoc slot”), and  
3. Any campaigns you know are **must-include** or **never**.

Then Phase 2 runs only on the approved ten: full parse verification, PI renames, trademark fixes, asset existence check, ingest structure check, weak-opening report — staged commits as specified.
