> **WITHDRAWN 2026-08-18 — DO NOT FILE.** This proposes a parser change. The
> project already decided the opposite and shipped it: 244 bibles normalized
> via `tools/launch-readiness/normalize_bestiaries_v2.py`, zero regressions.
> The measurements below are still valid and still useful, but the remedy
> should be to extend that normalizer to the five sections it has not yet
> covered. See `RECONCILIATION-2026-08-18.md`.

# Lore-keeper chunker cannot see `[TAG: …]` section headers — 219 of 303 finished bibles ingest almost empty

## Summary

`extractSection()` in `tools/lore-keeper-ingest/src/chunker.ts` matches section
headers by plain word (`NPC`, `Faction`, `Location`, …). 219 of the 303 finished
campaign bibles head their sections with a TAG marker instead:

```markdown
## [TAG: NPC_TIER_1]
## [TAG: FACTION_DATA]
## [TAG: LOCATIONS_MAIN]
## [TAG: QUEST_MAIN]
## [TAG: ITEM_LEGENDARY]
## [TAG: ENEMY_STATBLOCK]
```

Those sections are never found, so their contents are never chunked. The bibles
themselves are well formed and consistent. The failure is silent: ingest reports
success and writes a campaign row with a handful of chunks.

This is the reason campaign #4 onward cannot launch as a pure data operation.

## Evidence

Measured on 2026-08-15 across the whole `campaign-ideas/` tree with a checker that
bundles the real `chunker.ts` and `parser.ts` rather than re-implementing them.
Excludes `_to_delete`, `Tools`, `Ideas-To-Expand`.

The tell is a bimodal yield. A campaign either produces 120–240 rows or it
produces almost none. There is nothing in between, because the difference is one
header convention, not content quality.

`Completed/gold-and-vengeance` produces 26 rows today. Its bible holds 10 factions,
11 tier-1 NPCs, 30 tier-2 NPCs, 5 zones with 25 locations, 11 main-quest beats,
6 side quests and 5 legendary items. The only rows that survive are 10 monsters,
because that one section happens to carry a second plain `## Bestiary` heading
below the TAG marker.

TAG vocabulary and frequency across finished bibles:

| Tag | Count | Section it should feed |
|---|---|---|
| `NPC_TIER_1`, `NPC_TIER_2` | 281 each | NPCs |
| `FACTION_DATA` | 281 | Factions |
| `LOCATIONS_MAIN` | 281 | Locations |
| `QUEST_MAIN` | 281 | Main quest |
| `ITEM_LEGENDARY` | 281 | Items |
| `ENEMY_STATBLOCK` | 280 | Bestiary |
| `QUEST_SIDE` | 81 | Side quests |
| `ITEM_LOOT` | 81 | Items |
| `RULES_CUSTOM` | 80 | Mechanics |
| `ENCOUNTER_TABLE` | 73 | Encounters |
| `DM_GUIDE` | 80 | Campaign roadmap |

The TAG dialect also differs inside its sections, in two consistent ways:

1. **Tier-1 NPCs carry no numbering.** `**Name** (Type) - description`, where the
   supported dialect uses `1.  **Name** (Type) - description`.
2. **Table cells are not bold.** `| Barnaby | Ship's Cook | …` where the supported
   dialect uses `| **Barnaby** | Ship's Cook | …`. Both `extractNPCs()` and
   `extractQuests()` require the bold span, so entire tables are dropped.

## Proposed change

Four edits to `chunker.ts`, in order of value:

1. **`extractSection()`** — add a `TAG_ALIASES` map from section name to tag
   names, and append TAG header patterns to the existing pattern list.
2. **`extractSection()`** — skip a pattern whose captured body is blank instead of
   returning it. A TAG marker with an empty body currently shadows a real plain
   heading further down. This one line is what makes the change safe.
3. **`extractNPCs()`** — add a third split pattern for unnumbered
   `**Name** (Type) - desc` entries.
4. **Table extractors** — make the `**` around a name cell optional, and reject
   markdown alignment rows (`---`, `:---`, `:---:`) and header cells by name.

A working prototype is attached as `preflight-tagfix.mjs`. It is a measurement
tool, not a patch. It is not production-ready — see Caveats.

## Measured effect

Across the 303 finished campaigns:

| Measure | Today | With the prototype |
|---|---|---|
| NEEDS REWRITE | 250 | 33 |
| Campaigns with 5+ of 7 entity categories populated | 55 | 271 |
| Total rows written to `campaign_chunks` | 11,566 | 20,889 |
| Campaigns that lose rows | — | 1 |

Campaigns going from zero entities to some, by category: NPCs 218, quests 219,
locations 216, items 216, factions 215.

The three live campaigns:

| Campaign | Rows today | With prototype |
|---|---|---|
| `abyssal-descent` | 206 | 206 |
| `academy-of-arcane-gastronomy` | 198 | 198 |
| `the-eternal-feast` | 124 | **204** |

Abyssal Descent and Academy are byte-identical before and after. Eternal Feast
gains 80 rows, and that needs a decision rather than a merge — see below.

## Caveats — please read before implementing

1. **The Eternal Feast is live and would change.** The 80 new rows are 50 tier-2
   NPCs and 30 side quests that its bible has always contained, in unbolded
   tables. If this is real recovered content, it should ship. If it is noise, edit
   #4 needs narrowing. Someone should read a sample of those 50 names first, and
   confirm against the database that `the-eternal-feast` currently has zero
   `npc_tier2` rows.
2. **One regression.** `beast-of-skull-isle` goes 199 → 197 rows: `quest_side`
   drops from 30 to 28 under the loosened table pattern. Small, but it is a real
   behaviour change in a currently-clean campaign and should be understood, not
   waved through.
3. **Session outlines are not fixed.** The `DM_GUIDE` mapping does not rescue any
   roadmaps, because those bibles use `### Session-by-Session Breakdown` as a
   container and the per-session lines do not match
   `**Session N: Title**`. Out of scope here; worth a follow-up.
4. **Measurement fidelity.** The prototype was measured on a reconstruction of
   `main`'s `chunker.ts` that differs from `main` by 10 bytes not yet accounted
   for. It reproduces production row counts exactly for two of the three live
   campaigns, so the reconstruction is behaviourally faithful, but please
   re-measure against `main` before trusting the totals to the row.
5. **`_to_delete/` is walked by `listCampaignDirectories()`.** It holds 139
   directories. Any real ingest run over the whole tree would pick them up. Worth
   an exclusion in the walker regardless of this issue.

## Alternative considered and rejected

Rewriting the 219 bibles to plain-word headers. Rejected: it is 219 hand edits
against a machine-generated, already-consistent format, it risks lore loss, and it
leaves the parser just as brittle for the next generator that emits a new dialect.
The TAG markers are in fact a better parsing target than prose headings — they are
unambiguous and closed-vocabulary.

## Related

- Epic #1798 — 160 campaigns must go live as a pure data operation.
- `campaign-ideas/CAMPAIGN-BIBLE-FORMAT-SPEC.md` — the format contract, derived
  from this parser.
- `campaign-ideas/CAMPAIGN-AUDIT-2026-08-15.md` — the full per-campaign audit.
