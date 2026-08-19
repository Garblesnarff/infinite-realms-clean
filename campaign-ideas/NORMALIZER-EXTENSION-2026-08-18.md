# Section normalizer — extending the bestiary work to the other five sections

**2026-08-18.** Dry-run result and proposal. **Nothing has been written to the
repository.** All figures below come from applying the tool to a throwaway copy of
`content/launch-ten-readiness` (`ce784236`) extracted with `git archive`.

---

## 1. Why this exists

`normalize_bestiaries_v2.py` fixed the bestiary: 295 → 41 campaigns with zero
extractable monsters. Confirmed independently — their `coverage_report.py` reports
305 → 42 zero-monster bibles across the same two revisions, and my checker agrees.

That work covered one section. Five more have the identical defect and were never
touched. Measured at `ce784236`, campaigns under `Completed/` yielding **zero** of
a category:

| Category | Zero-yield campaigns |
|---|---:|
| NPCs | 244 |
| Items | 244 |
| Quests | 243 |
| Locations | 234 |
| Factions | 231 |
| Monsters | 41 (already fixed) |

## 2. What the tool does

`normalize-sections.mjs`, three passes, each edit judged on its own:

**Pass 0 — unbold headings.** `## **3. NPC ROSTER**` → `## 3. NPC ROSTER`.
Removes markup, no text.

**Pass 1 — give each TAG marker a visible heading.** The marker is kept:

```diff
-## [TAG: NPC_TIER_1]
+## NPC Roster
+[TAG: NPC_TIER_1]
```

Level matters. `ITEM_LOOT` and `NPC_TIER_2` become `###`, not `##`, or they would
fall outside their parent section.

**Pass 2 — entry markup.** Adds list numbering and bold spans around text the
author already wrote:

```diff
-**"One-Eyed" Jacquotte** (Human Swashbuckler) - Cunning, ruthless...
+1.  **"One-Eyed" Jacquotte** (Human Swashbuckler) - Cunning, ruthless...
```

```diff
-| Pinch | Line Cook | Crab-Person | Kitchen | Only walks sideways. |
+| **Pinch** | Line Cook | Crab-Person | Kitchen | Only walks sideways. |
```

## 3. Safety, following the v2 precedent exactly

- **Relabel only.** No word is added, removed or altered.
- **Every candidate is judged by the real parser.** The tool bundles the actual
  `chunker.ts` and `parser.ts`, so verification cannot drift from production.
  This is the one deliberate departure from `irparse.py`: covering five more
  extractors by porting would mean five more ports to keep in step.
- **Word/number multiset guard** (`no_content_loss` from v2) on every edit and
  again on the whole file.
- **An edit is kept only if it gains and regresses nothing.** Two were refused on
  exactly that basis: one would have reduced `monster`, one `item`.
- A campaign whose category already works is not touched.

Verification after applying to 250 files: **0 files lost an authored word or
number. 0 campaigns lost a row.**

## 4. Result

303 finished campaigns, before and after:

| | Before | After |
|---|---:|---:|
| NEEDS REWRITE | 250 | **33** |
| FIXABLE | 38 | 255 |
| CONFORMING | 15 | 15 |
| Rows reaching `campaign_chunks` | 11,566 | **20,711** |
| Row regressions | — | **0** |

Zero-yield campaigns by category: NPCs 244 → 27, locations 234 → 18, quests
243 → 25, factions 231 → 16, items 244 → 29.

Entities recovered: NPCs +3,373, quests +2,119, locations +1,584, factions +1,170,
items +1,015.

**The three live campaigns:**

| Campaign | Before | After |
|---|---:|---:|
| `abyssal-descent` | 206 | 206 |
| `academy-of-arcane-gastronomy` | 198 | 198 |
| `the-eternal-feast` | 124 | **204** |

Two are byte-identical. The Eternal Feast gains the 50 minor NPCs and 30 side
quests its bible has always held in unbolded tables — the live loss reported
earlier. That is the only change to a published campaign, and it is the one thing
here that needs your decision rather than a review.

## 5. What this does not fix

- **Session outlines: 236 campaigns still yield zero.** Giving `[TAG: DM_GUIDE]`
  a `## Campaign Roadmap` heading is not enough. Those bibles use
  `### Session-by-Session Breakdown` as a container, and the chunker needs each
  session on its own line as `**Session N: Title**`. Fixable by the same method,
  but it is a distinct edit and I have not written it.
- **33 campaigns still need real work.** Six are missing a required file
  outright. The rest are thin or stub bibles. That list is short enough to read.
- Monsters are unchanged at 41 zero-yield, as expected — that is the prior work,
  and this tool leaves it alone.

## 6. To run it

```
node campaign-preflight/normalize-sections.mjs --repo-path <tree>            # headings only
node campaign-preflight/normalize-sections.mjs --repo-path <tree> --entries  # + entry markup
node campaign-preflight/normalize-sections.mjs --repo-path <tree> --entries --write
```

Run it against a `git archive` extract first, as here, not against the working
tree. Re-measure with `preflight.mjs` before and after.

## 7. Open question for you

This branch is 25 commits ahead of `main` and production has ingested none of it.
Merging the branch and re-ingesting is a separate decision from whether to run
this tool. I would sequence it: run the normalizer on the branch, review the
diff, merge, then re-ingest — so production picks up the bestiary work and this
in one pass rather than two.
