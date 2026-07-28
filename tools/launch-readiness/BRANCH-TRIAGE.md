# Stale Branch Triage

**Repo:** `infinite-realms-clean`
**Reviewed from:** `content/launch-ten-readiness` @ `8dfa1c5c`
**Date:** 2026-07-28
**Method:** read-only (`git show`, `git log`, `git diff`, `git ls-tree`). Nothing merged,
moved, or written outside this file.

Answers the open question left in `PHASE4-LIBRARY-CLEANUP.md` §5 ("4 stale branches on
origin — all behind, none merged") and in `DRIVE-IMPORT-2026-07-28.md` Priority C
("author the stats and merge, or drop the branch").

---

## Verdicts

| Branch | Verdict | Action |
|---|---|---|
| `agent/add-godskin-atlas-campaign-package` | **Partially valuable — finish it** | Cherry-pick all 4 files, author 8 stat blocks, reformat bestiary headers |
| `chore/campaign-catalog-and-reorganization` | **Partially valuable** | Cherry-pick 2 files (`ip-review.md`, length data out of `campaigns.csv`). Drop the other 13 |
| `chore/campaign-pilot-migration` | **Superseded — drop** | Delete the branch. Its content is a stale copy; its layout contradicts CLAUDE.md |
| `claude/improve-dnd-campaign-agent-…` | **Superseded — drop** | Zero files not already on HEAD (pre-confirmed) |

All three unmerged branches fork from the same commit, `8da99ced`. The pilot-migration
branch is stacked on top of the catalog branch, so "drop pilot, keep part of catalog" is
coherent — pilot adds only 5 files of its own.

---

## 1. `agent/add-godskin-atlas-campaign-package`

### What is on it

4 files, 1127 lines, 55 KB, in one directory —
`campaign-ideas/Fantasy/the-godskin-atlas/`:

| File | Words |
|---|---:|
| `the-godskin-atlas.md` (overview) | 1720 |
| `creative-brief.md` | 1350 |
| `world-building-spec.md` | 1943 |
| `the-godskin-atlas-campaign-bible.md` | 3192 |

Premise: a continent rises from an uncharted sea and turns out to be the sleeping body of
a god named Orison. Every road is anatomy. 15 sessions, five acts, level 3 → 13–14,
high difficulty. 7 factions, 7 major NPCs + a minor table, 17 named locations across 5
anatomical zones, 15-step main quest, 12 side quests, 8 artifacts + 10 field loot
entries, 4 custom mechanics (Awakening Clock, Somatic Reputation, Living Atlas Folios,
Ichor Resonance), a 15-session guide, and a RAG index.

### Legal and originality status: clean

Scanned the whole package for the Product Identity and trademark lists in
`BIBLE-GENERATION-SPEC.md` §2.3 — **zero hits**. No beholder/modron/mind flayer, no
`D&D`, no Waterdeep/Sigil/Planescape/Ravenloft. Also no hits against `depth_score.py`'s
eleven pastiche families. The creature names are invented, not borrowed: Gilded
Phagocyte, Scar Shepherd, Pore Hound, Nerve Kite, Ossuary Mite, Dream Hart, Violet
Lacuna, Marked Expeditioner. This is one of the few genuinely original packages
available, and originality is the library's stated shortage.

### Why it cannot ship today — verified, not assumed

Ran the production-equivalent parser against the bible:

```
irparse.extract_section(text, 'Bestiary')  -> found  (## 7. BESTIARY matches, re.I)
irparse.coverage(text)                     -> []     (zero creatures extracted)
```

The section heading is fine. The failure is per-creature: entries are written as
`### Gilded Phagocyte` followed by two sentences of prose. `MONSTER_PATTERNS` requires
`### <n>. <Name> (CR <x>)`, and `parse_stat_block` requires labelled `**HP:**` /
`**AC:**`. There is no number anywhere in the bestiary — not a mislabelled one, an
absent one. Per PHASE1's hard rule this is a **missing-design job, not a format job**;
`normalize_bestiaries.py` cannot touch it.

### How much work the stat blocks actually are

**8 creatures.** That is the whole job, and it lands exactly inside the spec's
"8 to 12 creatures per campaign" requirement — no creatures need inventing, and none
need cutting.

The campaign antagonist, **The Starved Thought**, is explicitly a persuasive idea, not a
body ("A private conclusion that feels self-generated… Power: it simplifies choices by
removing the emotional capacity to value alternatives"). The finale is a negotiation with
Orison, not a boss fight. So there is no ninth stat block hiding in the design.

**The prose implies power level clearly enough to author from.** Three independent
signals:

1. The overview states **Start level 3 → Finish 13–14**, which is a CR ~1 to CR ~15
   ladder over 15 sessions.
2. The bible's five zones (Outer Skin → Handlands → Face → Ribcage → Interior) are a
   linear progression, and each creature's prose ties it to a zone or an act.
3. Each entry already specifies role, tactics and a non-combat resolution — which is the
   hard part of monster design. "Removing the mark without violence can convince it a
   threat has been resolved" (Phagocyte); "may be rescued through recognition rather than
   damage" (Marked Expeditioner). Only the numbers are missing.

A defensible ladder, derived from zone placement and the stated level curve:

| Creature | Role in the design | Suggested CR band |
|---|---|---|
| Ossuary Mite | swarm scavenger, tunnel complexes | 1/2–1 |
| Pore Hound | pack hunter, redirectable | 2–3 |
| Nerve Kite | caster disruptor | 3–4 |
| Marked Expeditioner | tragic humanoid, rescuable | 4–5 |
| Dream Hart | non-hostile lure | 5 (avoid-not-fight) |
| Scar Shepherd | terrain/entombment threat | 7–8 |
| Gilded Phagocyte | immune-response elite, marks targets | 9–10 |
| Violet Lacuna | act-capstone, removes properties | 13–15 |

**Effort: roughly 50 added lines.** Compare a shipped flagship: `the-eternal-feast` has 10
creatures in ~6 lines each. Eight entries at that density plus renumbered headers is a
single focused authoring pass — call it one to two hours by hand, or one LLM pass against
the §3 prompt block in `BIBLE-GENERATION-SPEC.md` followed by an `irparse.coverage()`
check that must return 8 × `full`. That is small next to the 8205 words already written,
and it is the *only* thing standing between this package and the shelf.

### Recommendation: **finish it, then merge**

Evidence: it is IP-clean where 114 campaigns are not; it is original where 206 of 305
bibles are template clones; its bestiary is eight distinct creatures where the clone
cluster is three; it is a complete four-file package; and the remaining work is bounded
at eight stat blocks with the power level already implied. Dropping this to avoid a
two-hour authoring task would be the wrong trade.

At 21.9 KB the bible is smaller than the depth-score leaders (~50 KB), so expect it to
land mid-table on `depth_score.py` rather than at the top. It earns its place on
originality and genre-fit, not on bulk.

### Migration steps

1. Cherry-pick the four files as-is into `campaign-ideas/Fantasy/the-godskin-atlas/`
   (the branch already uses the correct genre-root path for a package awaiting a bible).
2. Rewrite the eight bestiary headers to `### <n>. <Name> (CR <x>)`.
3. Add `(CR x). <Type>. **HP:** <n>, **AC:** <n>.` plus an `**Abilities:**` block to each
   entry, keeping the existing prose as flavour and the existing non-combat outs as
   stated abilities. Vary HP/AC off round numbers; never reproduce 30/13, 80/16, 180/18.
4. Confirm no `[TAG: ...]` marker sits between the Bestiary heading and the last creature.
5. Verify: `irparse.coverage()` returns 8 entries, all `full`.
6. Move the whole package to `campaign-ideas/Completed/Fantasy/the-godskin-atlas/` in one
   move — all four files together, per CLAUDE.md.
7. Update `DRIVE-IMPORT-2026-07-28.md` Priority C to record the decision.

---

## 2. `chore/campaign-catalog-and-reorganization`

### What is on it

15 files: 13 under `catalog/` plus `tools/build_catalog_reports.py` and
`tools/validate_campaigns.py`. No campaign files are moved or edited — the branch is
explicitly inventory-only (`catalog/repository-migration.md`: "performs **no**
campaign-directory moves, merges, renames, or deletions").

The core artifact is `catalog/campaigns.json` / `campaigns.csv`: 1098 rows (958 GitHub
packages + 140 ideas-sheet concepts), 16 columns including `normalized_length`,
`session_min/max`, `ip_status`, `readiness_score`, `audit_confidence`.

### Does its schema still describe the current layout? No.

`catalog/campaign.schema.json` is not a directory-layout schema at all — it is a
*metadata* schema for a per-package `campaign.yaml`, and it deliberately encodes state in
fields rather than in a directory name. Its own `metadata.md` says so: the schema exists
"instead of encoding all state in a directory name." That is a direct philosophical
conflict with the current main line, where `Completed/` vs genre-root *is* the state
marker, freshly re-affirmed in CLAUDE.md and `BIBLE-GENERATION-SPEC.md` §2.5.

The `documents` field is also path-shaped and assumes the pilot's flat filenames
(`campaign.md`, `campaign-bible.md`) rather than the live `<slug>.md` /
`<slug>-campaign-bible.md` convention. Adopting the schema unchanged would require the
pilot migration, which is rejected below.

### What the 135-campaign merge did to the data

Measured, not estimated: of the 958 GitHub rows, **135 `github_path` values no longer
exist on HEAD and 823 still resolve.** That 135 is exactly the split-campaign count that
commit `897910eb` merged, and the branch's own `duplicate-review.md` lists exactly 135
duplicate groups. I re-ran the split check against HEAD: **zero campaigns now exist in
two places.**

So `duplicate-review.md` (678 lines) is fully discharged — main already picked the
richer copy in every group, which is the same resolution the branch recommended.
`campaign-audit.md` and `campaign-index.md` report pre-merge counts (958 packages,
303 Completed / 655 outside) that are now wrong; HEAD has 824 packages, 303 / 521.

Worse for reuse: **there is no script on the branch that regenerates `campaigns.json`.**
`build_catalog_reports.py` only *reads* the pre-built JSON. The catalog is a frozen
snapshot with no way to refresh it against the current tree.

### What is still genuinely valuable

**`catalog/ip-review.md` — keep this.** 66 flagged campaigns. Only 9 are Wizards-related
(Planescape); the other **57 flag third-party franchises that HEAD has no detector for.**
`depth_score.py`'s `PASTICHE` dict covers eleven families (Demon Slayer, Cowboy Bebop,
My Hero Academia, Le Guin, Harry Potter, Tolkien, Star Wars, Warhammer, Princess Bride,
named Lovecraft, Percy Jackson). The catalog flags franchises entirely outside that dict:

> Alien, Watchmen (2), Marvel, Doctor Who, Pirates of the Caribbean (2), Hades (2),
> Chrono Trigger (2), The Witcher (4), Inheritance Cycle (2), Persona 4, Uzumaki,
> Sherlock Holmes, King Kong, The Last of Us, Ip Man, Ong-Bak, Enter the Dragon (2),
> Crouching Tiger Hidden Dragon (2), Firefly/Serenity (6), The Stormlight Archive (19)

Spot-checked on HEAD: `xenomorph-protocol`, `the-watchmen-protocol`,
`curse-of-the-black-pearl`, `escape-from-zagreus`, `echoes-of-lavos`,
`beast-of-skull-isle`, `riders-of-alagaesia`, `the-timelords-companion`,
`spiral-of-uzumaki`, `shadows-of-inaba`, `deductions-of-baker-street` — **all still
present, all still carrying the franchise in the slug.** The main line's trademark sweep
removed Wizards marks only; this exposure is live and unaddressed.

Caveat on quality: the flags are automated triage and the confidence is uneven. The
19-campaign "Stormlight Archive" cluster is a keyword heuristic and clearly
over-triggers — a Joan of Arc historical (`the-maid-of-orleans`) and a Macedonian
campaign are not Stormlight pastiche. Treat the ~25 flags where the franchise is in the
campaign's own title as indisputable and the rest as leads to verify.

**Length metadata in `campaigns.csv` — worth extracting.** 732 of 958 rows carry
`session_min` / `session_max` / `normalized_length`. HEAD has no length metadata for
storefront filtering. 823 of 958 paths still resolve, so the join is mostly mechanical.

**`launch-readiness.md` — superseded, but it validates the method.** Its 3/3/3 slate
predates shipping, and 5 of its 9 picks (Impossible Vault, Ascension Protocol, Eternal
Feast, Porcelain Court, Wings of the Void) are in `depth_score.py`'s `SHIPPED` set today.
Two picks it did not anticipate matter: it recommends `combat-healer-chronicles` as an
alternate and `see-you-space-cowboy` is not on its list at all — the latter shipped and
carries a Cowboy Bebop flag. The judgement was directionally right; the document itself
adds nothing HEAD does not already know.

### Recommendation: **cherry-pick two things, drop the other thirteen**

Merge:

- `catalog/ip-review.md` — re-home as
  `tools/launch-readiness/IP-THIRD-PARTY-REVIEW.md`, since HEAD has no `catalog/`
  directory and this is a launch-gating document.
- The `session_min` / `session_max` / `normalized_length` / `readiness_score` columns of
  `campaigns.csv` for the 823 rows whose path still resolves.

Drop: `campaign.schema.json`, `examples/`, `metadata.md`, `repository-migration.md`
(describes the rejected move), `duplicate-review.md` (discharged), `campaign-audit.md`,
`campaign-index.md` (stale counts), `asset-coverage.md` (one campaign, Drive-side),
`sheet-only-ideas.md` (140 rows, superseded by `DRIVE-IMPORT-2026-07-28.md`'s 195 with
tier ratings and expansion hooks), `launch-readiness.md`, `campaigns.json`,
`campaigns.csv` as a tracked artifact, `build_catalog_reports.py`,
`validate_campaigns.py` (both operate on a snapshot that cannot be regenerated).

### Migration steps

1. `git show origin/chore/campaign-catalog-and-reorganization:catalog/ip-review.md >
   tools/launch-readiness/IP-THIRD-PARTY-REVIEW.md`.
2. Rewrite its paths: 135 entries point at pre-merge duplicate paths. Every merged
   campaign now lives at `campaign-ideas/Completed/<Genre>/<slug>/`. Collapse the
   entries that appear twice (`crouching-tiger-hidden-dragon`, `echoes-of-lavos`,
   `enter-the-dragon`, `escape-from-zagreus`, `factions-of-sigil`, `oaths-of-the-radiant`,
   `riders-of-alagaesia`, `the-bioluminescent-expanse`, `curse-of-the-black-pearl`,
   `hearts-of-the-dragon-and-tiger`).
3. Drop the 9 Planescape rows — `depth_score.py`'s `KNOCKOFFS` set and PHASE4 §4 already
   cover those.
4. Verify each remaining flag by reading the campaign; mark the Stormlight cluster
   "unverified heuristic" rather than importing it as fact.
5. Optionally fold the confirmed non-Wizards franchises into `depth_score.py`'s
   `PASTICHE` dict as distinctive-name regexes, so the check runs on every future pass
   instead of living in a static list.
6. Join the length columns onto whatever storefront metadata store is chosen. Do not
   re-add `catalog/` as a directory; it has no generator and would rot again.

---

## 3. `chore/campaign-pilot-migration`

### What is on it

40 files, but only 5 are its own: `catalog/path-migrations.csv`,
`catalog/pilot-migration.md`, `tools/validate_pilot_migration.py`,
`ideas/expansion-queue/the-godskin-atlas/{campaign.yaml,concept.md}`. The other 35 are
the catalog branch it is stacked on, plus 20 campaign files that are pure `git mv`
renames of four packages into `campaigns/<slug>/`.

### Does the layout conflict with CLAUDE.md? Directly.

The branch proposes:

```
campaigns/<slug>/{campaign.yaml,campaign.md,campaign-bible.md,world-building-spec.md,creative-brief.md,supporting/,assets/}
```

CLAUDE.md's "Package layout rule (important)" and `BIBLE-GENERATION-SPEC.md` §2.5 both
mandate:

```
campaign-ideas/Completed/<Genre>/<slug>/{<slug>.md,creative-brief.md,world-building-spec.md,<slug>-campaign-bible.md}
```

Three incompatibilities, not one:

1. **Genre disappears.** The pilot flattens to a single `campaigns/` root. Every current
   tool assumes genre directories: `depth_score.py` iterates a hardcoded `GENRES` list
   over `Completed/<g>` and `<g>`; `coverage_report.py` and `stats.sh` do the same.
   Adopting it breaks all of them.
2. **`Completed/` disappears.** The pilot replaces the has-a-bible signal with a
   `status:` field in `campaign.yaml`. Main just spent a commit (`897910eb`) re-asserting
   the directory convention and merging 135 campaigns back into it, and then wrote the
   rule into CLAUDE.md. The two models cannot both be the source of truth.
3. **Filenames change.** `<slug>.md` → `campaign.md`, `<slug>-campaign-bible.md` →
   `campaign-bible.md`, which the generation spec explicitly contradicts.

### The content on it is stale, not just relocated

`git diff --stat HEAD...<branch>` shows the campaign files as 0-line changes, which reads
like "nothing new" — but that is a merge-base artifact. Comparing blobs against HEAD
directly, every bible differs:

| File | vs HEAD |
|---|---|
| `the-eternal-feast/campaign-bible.md` | 6 insertions / 6 deletions |
| `the-porcelain-court/campaign-bible.md` | 40 / 10 |
| `combat-healer-chronicles/campaign-bible.md` | 138 / 513 |

The Eternal Feast diff is the trademark sweep: the branch still contains `Modron Chef`,
`Unit 734 (Modron Waiter)`, `Cork (A one-eyed Beholder)`, `Kuo-Toa`, `Yuan-Ti`,
`Blink Dog` — all of which HEAD has already renamed to Cogwright, a sentient wine-cask
spirit, Deepfin fishfolk, Scalebound humanoid and Flickerhound. **Merging this branch
would reintroduce Product Identity names into a shipped launch campaign.**

The combat-healer bible on the branch is byte-identical (modulo one line) to HEAD's
`combat-healer-chronicles-campaign-bible.OLD.md` — i.e. the pre-normalisation copy that
main deliberately superseded.

### Its one real insight has already been acted on

`pilot-migration.md` correctly identified that combat-healer-chronicles had a rich
package outside `Completed/` and a distinct thin RAG bible inside it, and preserved both.
Main reached the same conclusion for all 135 groups, keeping the richer copy and
retaining the other as `*-campaign-bible.OLD.md`. The pilot's `supporting/` folder idea
is a marginally tidier home for those `.OLD.md` files, but it is not worth a layout
change.

`ideas/expansion-queue/the-godskin-atlas/concept.md` is a 21-line stub of a campaign that
exists in full (1127 lines) on the Godskin branch. Strictly worse.

### Recommendation: **drop the branch entirely**

Evidence: zero unique campaign content (every file is a rename of something already on
HEAD, in an older state); the layout is mutually exclusive with a convention main
re-affirmed four commits ago and wrote into CLAUDE.md; it would break `depth_score.py`,
`coverage_report.py` and `stats.sh`; and merging it would silently regress the trademark
cleanup on a shipped campaign.

### Migration steps

None. Delete the remote branch. If a per-package metadata file is wanted later, design it
*inside* `campaign-ideas/Completed/<Genre>/<slug>/` so the directory convention and the
metadata coexist rather than compete — the field list in `campaign.schema.json` is a
reasonable starting point even though its layout assumptions are not.

---

## Summary of actions

**Do:**
1. Author 8 stat blocks for The Godskin Atlas, verify with `irparse.coverage()`, merge
   the package into `campaign-ideas/Completed/Fantasy/`.
2. Port `catalog/ip-review.md` to `tools/launch-readiness/IP-THIRD-PARTY-REVIEW.md`,
   fix the 135 stale paths, verify the flags, and consider folding the confirmed
   franchises into `depth_score.py`'s `PASTICHE` dict.
3. Extract length metadata for the 823 still-resolving rows of `campaigns.csv`.

**Do not:**
4. Do not merge `chore/campaign-pilot-migration` — it regresses trademark fixes and
   contradicts CLAUDE.md.
5. Do not adopt `campaigns/<slug>/` or `campaign.yaml` as the package layout.
6. Do not re-add `catalog/` as a tracked directory; it has no generator.

**Then:** all four origin branches can be deleted.
