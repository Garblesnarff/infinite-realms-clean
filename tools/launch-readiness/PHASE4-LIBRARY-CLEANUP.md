# Campaign Library Cleanup — Session Report

**Repo:** `infinite-realms-clean`
**Branch:** `content/launch-ten-readiness`
**Date:** 2026-07-28

---

## 1. What the library actually contains

`stats.sh` was reporting zeros because of a hardcoded stale path
(`/Users/rob/Claude/workspaces/...`). Real numbers:

| Metric | Count |
|--------|------:|
| Campaign package directories | **955** |
| Complete (overview + brief + world-building + bible) | **175** |
| Framework (3 files, needs a bible) | **643** |
| Bible only, no supporting package | **137** |
| Campaign bibles on disk | **314** |

The 137 bible-only directories are worth a decision: 132 are in `Completed/Fantasy/`
and hold nothing but a bible — no overview, no creative brief, no world-building spec.
They will ingest monsters fine but have no narrative package behind them.

**7 campaigns exist in two places at once** (`Completed/<genre>/<slug>/` *and*
`<genre>/<slug>/`) with **different bible content in each copy** — the genre-root copy
is usually 2–3× larger:

| Campaign | Completed/ copy | genre-root copy |
|----------|----------------:|----------------:|
| classical-symphony-kingdom | 12.0 KB | 27.8 KB |
| clockwork-elemental | 12.3 KB | 28.4 KB |
| colossus-ascent | 11.6 KB | 28.2 KB |
| combat-healer-chronicles | 12.0 KB | 47.1 KB |
| shadow-bureau-protocols | 11.7 KB | 7.7 KB |
| (+2 more) | | |

Ingestion needs to know which copy wins. Right now nothing says.

---

## 2. Bestiary normalization — the main work

### The real blocker

Prior reports framed this as "authors forgot the colons." That is only part of it.
The dominant problem was **structural**: **218 bibles** put their creatures under
a `[TAG: ENEMY_STATBLOCK]` marker, not a `Bestiary` heading. Production's
`extractSection()` looks for `Bestiary` / `Encounter` and finds nothing, so those
creatures were never extracted at all — the colon question never even came up.

Two independent things had to be true for a monster to reach combat at authored stats:

1. the chunker can *find* it — needs a `Bestiary` section and a
   `### <n>. <Name> (CR <x>)` header
2. the parser can *read* it — needs labelled `**HP:**` and `**AC:**`

### Method

I ported production's `authored-stat-block-parser.ts` and the lore-keeper chunker's
`extractEncounters` to Python (`tools/launch-readiness/irparse.py`), then **validated
the port against the TypeScript on all 20 launch-batch campaigns — it reproduces the
results exactly**, so coverage numbers here mean the same thing as production logs.

The existing `sim-chunker-coverage.ts` only walks a hardcoded list of twenty;
`coverage_report.py` walks the whole library.

### Hard rule: no invented stats

An entry missing HP, AC, or CR is left **byte-for-byte untouched** and reported.
The normalizer only relabels numbers the author already wrote. Every rewritten file
was re-parsed before being saved, and any file that did not come back 100% full — or
that lost content — was refused.

### Result

| Metric | Before | After |
|--------|-------:|------:|
| Bibles fully parsing | 22 | **245** |
| Bibles with 0 extractable monsters | 292 | **69** |
| Monster blocks extracted | 213 | **1034** |
| Blocks grading FULL | 213 | **1034** (100%) |

**223 bibles rewritten. Zero regressions. The 20 launch-batch campaigns verified byte-unchanged.**

Four entries were left alone for missing numbers:

| Campaign | Creature | Missing |
|----------|----------|---------|
| ong-bak-sacred-guardian | Mad Dog | CR |
| ong-bak-sacred-guardian | The Shadow Spirit | CR |
| the-hermits-pilgrimage | The Mirror Doppelgänger | HP, AC, CR |
| death-on-the-rails | The Snowstorm (Environmental) | HP, AC |

A representative diff:

```diff
 ## [TAG: ENEMY_STATBLOCK]
-### 1. Solarian Shadow (Standard)
-(CR 2). Humanoid. HP 30, AC 13 (Silk patches).
+
+## Bestiary
+### 1. Solarian Shadow (Standard) (CR 2)
+(CR 2). Humanoid. **HP:** 30, **AC:** 13 (Silk patches).
 **Abilities:**
```

---

## 3. The finding that matters more than the coverage number

Mechanically ready is not the same as launch ready.

**144 of 314 bibles share identical monster stat signatures**, and **200 bibles have
exactly three monsters**. One cluster alone accounts for **114 campaigns**, all using
the same three creatures:

- `HP 30 / AC 13` — "(Standard)"
- `HP 80 / AC 16` — "(Elite)"
- `HP 180 / AC 18` — "'The Mastermind' <name> (Proxy)"

…with the same ability names swapped over a different noun. Compare
`gears-of-deus`, `monopolis-rising`, `hextech-revolution`, `the-crimson-kitchen`:
identical stat lines, identical "Ordered X" / "Reality-Warping Pulse" / "The Final
Move" abilities.

For contrast, the hand-audited launch-20 average **10 authored monsters each** with
genuinely distinct stats.

So the 1034 number is real — those creatures will now fight at authored stats instead
of as 11 HP generics — but roughly **a third of the library is one template with the
names changed**, three encounters deep. That is a content-generation problem the
parser can't fix, and it should probably gate what gets promoted to the storefront.

**Recommendation:** treat "3 monsters + cluster-matched stats" as a disqualifier for
launch selection, and prioritize the ~90 bibles with authored depth.

---

## 4. Product Identity / trademark sweep

Scanned 2,849 markdown files. Dropped `spectator` (20 hits) and bare `sigil` (11) as
generic English after context review — "spectator seating", "the king's sigil".

**114 campaigns carry confirmed risk.**

### PI creature names — must be renamed before shipping (27 campaigns)

| Creature | Campaigns |
|----------|----------:|
| modron | 9 |
| beholder / beholderkin | 7 |
| mind flayer / illithid | 6 |
| blink dog | 4 |
| displacer beast | 3 |
| drider | 3 |
| githyanki / githzerai | 4 |
| kuo-toa, yuan-ti, umber hulk, flumph | 1 each |

Worst single offender: **`wildspace-corsairs`** — githyanki, illithid, mind flayer,
umber hulk in one package.

Three of these are already-shipped launch campaigns and need a second pass:
`murder-on-the-astral-express` (drider, modron), `the-eternal-feast` (drider, modron),
`ascension-protocol` (modron), `see-you-space-cowboy` (modron).

### Trademarks and settings (100 campaigns)

- **76 campaigns** contain a bare `D&D` reference; 13 spell out "Dungeons & Dragons".
  Mostly in marketing/positioning prose — mechanical find-and-replace to "5E-compatible".
- Setting proper nouns: waterdeep (5), asmodeus (4), planescape (2), spelljammer (2),
  strahd (2), plus single hits on zariel, elminster, vecna, ravenloft, icewind dale,
  dark sun, eberron, red wizards.

### Structural knockoffs — renaming won't save these

The whole premise is a WotC setting, not a stray creature name:

| Campaign | Setting |
|----------|---------|
| `factions-of-sigil` | Planescape |
| `domains-of-dread` | Ravenloft |
| `sharn-city-of-towers` | Eberron |
| `wasteland-of-athas` | Dark Sun |
| `wildspace-corsairs` | Spelljammer |
| `goldport`, `deductions-of-baker-street` | Waterdeep |

These need a rewrite or a shelf, and that is a judgment call, not a script.

---

## 5. Repo hygiene

- **`stats.sh` fixed** — now derives its own location and additionally reports parser
  coverage. Previously reported 0 across every genre.
- **AppleDouble `._*` files** — already gitignored, none tracked. 25 on disk, harmless.
- **`__pycache__`** added to `.gitignore`.
- **8 stray loose overview files** at genre roots that duplicate a folder elsewhere —
  e.g. `Fantasy/the-ember-rebellion.md` (6.5 KB, High Fantasy) vs
  `Sci-Fi/the-ember-rebellion/` (9.3 KB, full package). **Left in place** — the
  contents genuinely differ, so which one survives is your call, not a script's.
  Note the folder copy is also filed under the wrong genre.
- **4 stale branches on origin** (`agent/add-godskin-atlas-campaign-package`,
  `chore/campaign-catalog-and-reorganization`, `chore/campaign-pilot-migration`,
  `claude/improve-dnd-campaign-agent-…`) — all behind, none merged.

---

## 6. New tooling

| File | Purpose |
|------|---------|
| `tools/launch-readiness/irparse.py` | Python port of the production parser + chunker, verified against the TS on all 20 launch campaigns |
| `tools/launch-readiness/coverage_report.py` | Coverage across the whole library, not a hardcoded ten |
| `tools/launch-readiness/normalize_bestiaries.py` | The mechanical reshape, with the never-invent rule |

```bash
python3 tools/launch-readiness/coverage_report.py --summary
python3 tools/launch-readiness/coverage_report.py --failing
./campaign-ideas/stats.sh
```

---

## 7. Open items

1. **Decide the duplicate-copy rule** for the 7 split campaigns before ingest.
2. **PI second pass on 4 already-shipped campaigns** (modron/drider slipped through).
3. **Gate launch selection on authored depth**, not just parse coverage — the
   114-campaign template cluster is the real constraint.
4. **Legal call** on Blink Dog and Drider (carried over from Phase 2).
5. **69 bibles still have no extractable monsters** — 24 have no stat region at all,
   24 have creature lists with abilities but no HP/AC numbers, and filling those means
   authoring stats, not reformatting.
6. **Post-Apocalyptic** still has no launch-ready campaign.
