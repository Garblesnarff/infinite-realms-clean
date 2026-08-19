# Reconciliation — why my checker said 198 and the database says 188

**2026-08-18.** Supersedes the row counts in `CAMPAIGN-AUDIT-2026-08-15.md`.
Ground truth is 188. My checker was faithful; my method was not.

---

## 1. The number is reconciled exactly

Both numbers are correct. They describe different revisions of the bible.

| Revision | Academy rows |
|---|---:|
| `660efb99^` — the revision `main` is at | **188** |
| `660efb99` — `fix(content): normalize launch-ten bestiaries for lore-keeper chunker` | 198 |
| `HEAD` of `content/launch-ten-readiness` | 198 |

`660efb99` gave the academy bestiary a `## Bestiary` heading. That made 10
monster blocks visible to `extractEncounters()` for the first time. 188 + 10 = 198.

Verified by running the byte-exact `main` chunker against each revision's files
in turn. Everything else in my chain checked out and was ruled out on the way:

- I rebuilt `chunker.ts` byte-for-byte from `main` (25,781 bytes) and diffed it
  against the copy my audit used. **No difference.** The 10-byte discrepancy I
  flagged earlier was only the `.js` import-specifier edit needed to bundle.
- The four academy files on disk are md5-identical to the ones I measured.
- I replaced my hand-rolled dedupe with `main`'s real `dedupeCampaignChunks`.
  Same answer, zero identity collisions.

So the checker reproduces production exactly, at whatever revision you point it at.

## 2. The real error: I audited a branch production has never seen

`infinite-realms-clean` is checked out on `content/launch-ten-readiness`
(`ce784236`). That branch is **25 commits ahead of `main`**, and 13 of those are
not even pushed to its own remote. `main` is `8da99ced`, which is what production
ingests from.

Every number in the 2026-08-15 audit — all 820 campaigns — describes that branch.
Production has seen none of it. That is the same failure the handoff warned about,
in a form I did not anticipate: I checked against the right file on the wrong
revision, and never pinned one.

**Any audit output must name its revision.** The checker now needs a
`--rev` note in its output; until then, quote the commit alongside the count.

## 3. The larger error: I did not look for prior work

`campaign-ideas/tools/launch-readiness/` is an active workstream that already
covers much of what I did:

| What exists there | What I built |
|---|---|
| `irparse.py` — a Python port of the chunker, validated against the TypeScript on 20 campaigns | `preflight.mjs`, which bundles the TypeScript directly |
| `coverage_report.py` — library-wide coverage | my `--json` audit |
| `BIBLE-GENERATION-SPEC.md` — the format contract for the generator | `CAMPAIGN-BIBLE-FORMAT-SPEC.md` |
| `PHASE4-LIBRARY-CLEANUP.md` — identifies the `[TAG: …]` header problem | my "main finding" |

`PHASE4-LIBRARY-CLEANUP.md` states the cause in the same terms I did: 218 bibles
put creatures under `[TAG: ENEMY_STATBLOCK]`, so `extractSection()` finds nothing.
It was found before I got here.

**And it was already decided.** That workstream chose to normalize the bibles, not
to change the parser: 223 bibles rewritten, then 21 more, zero regressions, the 20
launch-batch campaigns verified byte-unchanged. My recommendation to change the
extractor instead cuts against a decision that has already shipped 244 files.

**I withdraw that recommendation.** `ISSUE-tag-dialect.md` should not be filed as
written.

## 4. What survives, and it is worth having

The prior work is **bestiary-scoped**. `irparse.py` implements `extract_section`,
`extract_encounters` and the stat-block parser, and nothing else.
`coverage_report.py` counts monster blocks. "265 bibles fully parsing" means their
monsters parse.

The same `[TAG: …]` header cause applies to every other entity type, and nothing
has addressed it. Measured at branch HEAD, after all the normalization:

- **199 campaigns extract monsters and nothing else** — no NPCs, no locations, no
  quests, no factions, no items.
- Campaigns yielding zero of a category: NPCs 218, quests 219, locations 216,
  items 216, factions 215.

`[TAG: NPC_TIER_1]` x281, `[TAG: LOCATIONS_MAIN]` x281, `[TAG: QUEST_MAIN]` x281,
`[TAG: FACTION_DATA]` x281, `[TAG: ITEM_LEGENDARY]` x281 are all still invisible.

The bestiary normalizer solved one section. Five more have the identical defect.

**Revised recommendation:** extend `normalize_bestiaries_v2.py` to insert the
plain-word headings for the other five sections, following the precedent exactly —
relabel only, invent nothing, re-parse every file before saving, refuse any file
that loses content. That reuses a proven method and a proven safety rule instead of
opening a second front in the parser.

## 5. One finding that is independent of all of this

The Eternal Feast is live. Its bible's `### Minor NPCs (Table of 50)` table has no
bold name cells, and `extractNPCs()` requires `| **Name** |`. 50 named minor NPCs
and 30 side quests have never reached the database. I verified this by reading the
file, not by inference.

This one has nothing to do with TAG headers — Eternal Feast uses plain-word
headings throughout. It is a separate, live content loss, and it is worth checking
against the database on its own.

## 6. Status of the deliverables

| File | Status |
|---|---|
| `CAMPAIGN-BIBLE-FORMAT-SPEC.md` | Sound, but reconcile with `BIBLE-GENERATION-SPEC.md` — two specs for one pipeline is worse than either alone |
| `CAMPAIGN-AUDIT-2026-08-15.md` | **Do not use the row counts.** Unpinned, measured on an unmerged branch |
| `ISSUE-tag-dialect.md` | **Withdrawn.** Contradicts a shipped decision |
| `preflight.mjs` | Sound and useful — bundles the real TypeScript, so it cannot drift from `irparse.py`'s port. Needs revision pinning |
| `preflight-boldfix.mjs`, `preflight-tagfix.mjs` | Prototypes only. Keep for measurement, do not ship |
