# House Stat Curve (HP / AC by CR)

**Status:** derived, validated, **not yet applied to any campaign bible.**
Applying it to a bible is a separate, human-approved step.

`PHASE1-SELECTION.md` recorded that no house curve existed for supplying missing
creature stats, and that gaps should therefore be reported rather than filled.
This document removes that blocker. The curve below is **not** a design opinion
and **not** SRD 5.1 — it is the median of what the library's own authors already
wrote, across 589 authored stat blocks.

Machine-readable form: `tools/launch-readiness/cr_curve.py`
(`hp_for_cr(cr)`, `ac_for_cr(cr)`, `python3 cr_curve.py --table`).

---

## 1. Method

**Extraction.** Every campaign bible under `campaign-ideas/` (305 bibles with a
`*-campaign-bible.md`) was passed through `irparse.py`, the verified port of the
production `authored-stat-block-parser.ts` plus the lore-keeper chunker's
`extractEncounters`. HP and AC come from `parse_stat_block()` unmodified.

One deviation, and it is the only one: the production chunker's monster regexes
match the CR in the block header but **discard it** (it falls between two capture
groups). The harvest re-ran those exact regexes with the CR value captured rather
than thrown away. No other pattern was loosened, so every block counted here is a
block the production pipeline also recognises.

Result: **1021 blocks with a complete (CR, HP, AC) triple**, from 243 bibles.
Fractional CRs (`1/2`, `1/4`, `1/8`) are normalised to floats and reported with
their original labels.

**Clone correction.** ~206 of the 305 bibles are generator template clones. Two
families dominate: 114 campaigns share the exact stat signature
`(30/13, 80/16, 180/18)` and another 22 share `(30/13, 80/15, 180/18)`; smaller
families of 8 and 4 exist. Left in, these blocks are 42% of the dataset and
concentrate entirely at CR 2, 5 and 12.

The correction used is **campaign-level exclusion**, not row-level dedup: any
campaign that `depth_score.py --json` reports with `clone_peers >= 4` was dropped
whole. This is stricter than deduping identical rows — a clone campaign's *other*
monsters are equally generator output and equally unearned as evidence, even
where their numbers happen to differ. The published curve therefore rests on
**589 blocks from 99 campaigns**.

For comparison, a row-level dedup (collapse identical `name/CR/HP/AC` tuples to
one vote) retains 950 blocks and produces **identical HP medians at every CR**;
AC medians differ by at most half a point, at CR 5 and 6 only. Both approaches
agree; the strict one is published because it is the harder test.

**Statistic.** Median, not mean. The library contains authored extremes that are
correct as written but ruinous to an average — a CR 3 "Apollo's Plague Arrow"
with HP 1 / AC 22, a CR 30 kaiju with HP 5000. These were verified against source
and left in the dataset; the median absorbs them.

---

## 2. The curve

Medians of the clone-corrected cohort. `srcs` = distinct campaigns contributing.

| CR   | HP  | HP IQR    | AC | AC range | blocks | srcs | confidence |
|------|-----|-----------|----|----------|--------|------|------------|
| 0    | 1   | 1–1       | 10 | 10–10    | 1      | 1    | **thin**       |
| 1/8  | 5   | 5–5       | 12 | 12–12    | 1      | 1    | **thin**       |
| 1/4  | 12  | 10–15     | 10 | 10–12    | 4      | 4    | **thin**       |
| 1/2  | 15  | 12–15     | 12 | 11–18    | 19     | 19   | observed   |
| 1    | 18  | 15–20     | 12 | 10–18    | 31     | 27   | observed   |
| 2    | 30  | 30–40     | 13 | 5–18     | 74     | 61   | observed   |
| 3    | 45  | 45–50     | 14 | 10–22    | 84     | 69   | observed   |
| 4    | 60  | 55–65     | 15 | 8–20     | 58     | 44   | observed   |
| 5    | 80  | 75–80     | 16 | 9–18     | 94     | 75   | observed   |
| 6    | 90  | 90–96     | 16 | 8–18     | 44     | 38   | observed   |
| 7    | 110 | 105–118   | 17 | 7–20     | 27     | 27   | observed   |
| 8    | 120 | 120–150   | 18 | 13–20    | 44     | 44   | observed   |
| 9    | 140 | 139–142   | 17 | 12–20    | 12     | 12   | observed   |
| 10   | 150 | 150–180   | 18 | 10–22    | 33     | 33   | observed   |
| 11   | 165 | —         | 18 | —        | 0      | 0    | *interpolated* |
| 12   | 180 | 180–180   | 18 | 16–22    | 27     | 27   | observed   |
| 13   | 205 | —         | 19 | —        | 0      | 0    | *interpolated* |
| 14   | 225 | —         | 19 | —        | 0      | 0    | *interpolated* |
| 15   | 250 | 250–250   | 20 | 18–25    | 25     | 25   | observed   |
| 16   | 280 | —         | 20 | —        | 0      | 0    | *interpolated* |
| 17   | 310 | —         | 21 | —        | 0      | 0    | *interpolated* |
| 18   | 340 | —         | 21 | —        | 1      | 1    | *interpolated* |
| 19   | 370 | —         | 22 | —        | 0      | 0    | *interpolated* |
| 20   | 400 | 400–400   | 22 | 20–25    | 7      | 7    | observed   |
| 21–24| 440–560 | —     | 22 | —        | 0      | 0    | *interpolated* |
| 25   | 600 | 600–600   | 22 | 22–22    | 2      | 2    | **thin**       |
| 26+  | —   | —         | —  | —        | 0      | 0    | **no data — refuse** |

`confidence` is thresholded at 5 distinct source campaigns. `cr_curve.py` exposes
this as `confidence_for_cr()`, interpolates the gaps linearly between observed
anchors, and raises `ValueError` above CR 25 rather than inventing a number.

CR 18 has a single authored observation (HP 250) which the curve deliberately
does **not** follow — one campaign is not evidence, and 250 at CR 18 would make
the curve non-monotonic against CR 15's 250. `cr_curve.py` reports the overridden
sample in `curve_row(18)['overridden_sample']` so the choice is visible.

**The underlying rule the authors were following** is worth stating plainly,
because it is much simpler than the table suggests:

> **HP ≈ 15 × CR** for CR 2 through 12, then accelerating: ~17×CR at CR 15,
> 20×CR at CR 20, 24×CR at CR 25.
> **AC ≈ 12 + CR/2**, flattening around AC 18 from CR 8 to CR 12, reaching 20 at
> CR 15 and 22 at CR 20.

Observed HP medians are 30/45/60/80/90/110/120/140/150/180 at CR 2–12. Those are
round numbers on a 15×CR line. This is a deliberate, consistent house convention,
not noise — which is the single strongest argument that a curve is derivable here
at all.

---

## 3. Clone contamination: before and after

| CR | blocks (all) | blocks (clone-corrected) | median HP all → corrected | mean HP all → corrected | HP IQR all → corrected |
|----|--------------|--------------------------|---------------------------|-------------------------|------------------------|
| 2  | 210          | 74                       | 30 → **30** (0%)          | 31.5 → 34.3 (+8.9%)     | 30–30 → **30–40**      |
| 5  | 238          | 94                       | 80 → **80** (0%)          | 79.5 → 78.8 (−0.9%)     | 80–80 → **75–80**      |
| 12 | 171          | 27                       | 180 → **180** (0%)        | 180.9 → 185.6 (+2.6%)   | 180–180 → 180–180      |

All other CRs are unaffected (clone bibles contain only three monsters each).

**The honest finding: clone contamination did not shift the medians at all.**
It shifted three other things, and each matters:

1. **Sample size, badly.** CR 5 looked like 238 observations; it is 94. CR 12
   looked like 171; it is 27. Any confidence claim built on the raw counts would
   have been inflated 2–6×.
2. **Spread, badly.** Clones collapse the IQR to a single point (CR 2: 30–30,
   CR 5: 80–80), making the convention look far tighter than authors actually
   write it. The corrected IQRs (30–40, 75–80) are the real variation.
3. **Nothing else.** The template values sit exactly on the non-clone median.
   The generator was, in effect, trained on the same house convention the human
   authors follow. That is why the medians are stable — and it is a reason for
   *more* confidence in the curve's central values, not less.

The mean does move (CR 2: +8.9%), which is why the curve is built on medians.

---

## 4. Out-of-sample validation

28 bibles contain authored HP/AC in a layout the production chunker cannot read
(e.g. `1. **Name** (CR 3 Beast). HP: 60, AC: 14.`). Those blocks contributed
**nothing** to the curve above. Re-harvested with a separate windowed scan they
yield 204 blocks from 21 campaigns — an independent cohort, different authors,
different formatting, never seen by the primary derivation.

| CR | curve HP | holdout HP | curve AC | holdout AC | holdout n |
|----|----------|-----------|----------|-----------|-----------|
| 1  | 18       | 20        | 12       | 13        | 9   |
| 2  | 30       | **30**    | 13       | 12        | 22  |
| 3  | 45       | **45**    | 14       | **14**    | 34  |
| 4  | 60       | **60**    | 15       | 16        | 15  |
| 5  | 80       | 75        | 16       | 15        | 20  |
| 6  | 90       | **90**    | 16       | 17        | 17  |
| 7  | 110      | **110**   | 17       | 18        | 16  |
| 8  | 120      | **120**   | 18       | 16        | 16  |
| 10 | 150      | **150**   | 18       | 17        | 18  |
| 12 | 180      | 200       | 18       | 19        | 5   |
| 15 | 250      | **250**   | 20       | 19        | 14  |
| 20 | 400      | **400**   | 22       | **22**    | 10  |

HP medians match **exactly** at CR 2, 3, 4, 6, 7, 8, 10, 15 and 20, and are
within 7% at CR 1, 5 and 12. AC agrees within ±2 everywhere. This is the
strongest evidence in this document that the curve describes a real, shared
convention rather than an artefact of one extraction path.

---

## 5. Comparison against SRD 5.1

Reference: 322 SRD monsters from Open5e (`document__slug=wotc-srd`), medians by CR.

| CR  | house HP | SRD HP | ΔHP  | house AC | SRD AC | ΔAC | SRD n |
|-----|----------|--------|------|----------|--------|-----|-------|
| 1/2 | 15       | 22     | −32% | 12       | 12     | 0   | 33 |
| 1   | 18       | 26     | −31% | 12       | 12     | 0   | 25 |
| 2   | 30       | 45     | −33% | 13       | 13     | 0   | 41 |
| 3   | 45       | 58     | −22% | 14       | 14     | 0   | 20 |
| 4   | 60       | 85     | −29% | 15       | 12     | +3  | 11 |
| 5   | 80       | 95     | −16% | 16       | 15     | +1  | 25 |
| 6   | 90       | 112    | −20% | 16       | 14     | +2  | 10 |
| 7   | 110      | 126    | −13% | 17       | 17     | 0   | 6  |
| 8   | 120      | 136    | −12% | 18       | 15     | +3  | 9  |
| 9   | 140      | 154    | −9%  | 17       | 18     | −1  | 8  |
| 10  | 150      | 157    | −4%  | 18       | 18     | 0   | 6  |
| 12  | 180      | 126    | +43% | 18       | 15     | +3  | 2  |
| 15  | 250      | 210    | +19% | 20       | 18     | +2  | 4  |
| 20  | 400      | 300    | +33% | 22       | 20     | +2  | 3  |

**Shape of the divergence.** The house curve is a **steeper line** than SRD's.
It sits ~30% *below* SRD at CR 1/2–2, crosses over around CR 10–11, and sits
19–33% *above* SRD at CR 15–20. AC tracks SRD closely at low CR and runs 2–3
points high from CR 12 up.

**Read on whether this is intentional.** It is consistent with a library tuned
for a party of four, and the pattern is too orderly to be accidental:

- *Low CR below SRD.* Four PCs delete low-CR mobs regardless of HP. Cutting a
  CR 2 from 45 HP to 30 makes trash fights end in one round instead of two —
  the correct call if low-CR creatures are being used as texture and pacing
  rather than as threats.
- *High CR above SRD, with AC +2–3.* A four-PC party concentrates its action
  economy on a single boss. SRD's CR 20 at 300 HP evaporates against a
  focused tier-4 party; 400 HP and AC 22 buys the boss the rounds its
  legendary actions and lair effects need to matter. This is the same
  correction most published adventures apply by hand.

Caveats on this comparison: the SRD sample is itself thin above CR 10 (n = 2–6
per CR), so the CR 12 comparison in particular (SRD n=2, medians 99 and 153) is
not a stable reference point. Treat the CR ≤ 10 rows as the meaningful ones.

I did not find written design documentation stating this intent. The "party of
four" reading is inference from the shape of the data, not a sourced claim.

---

## 6. Confidence

**High confidence (use it):** CR 2–10, and CR 12, 15, 20.
Every one of these rests on 25+ distinct campaigns (except CR 9 at 12 and CR 20
at 7), survives strict clone exclusion without moving, and is reproduced
independently by the 204-block holdout cohort. The HP medians here are as solid
as this library can make them.

**Moderate confidence:** CR 1/2 and CR 1 (19 and 27 sources). Well sampled, but
the HP spread is proportionally wide (CR 1 ranges 5–30 for a median of 18) —
low-CR creatures in this library are written loosely.

**Low confidence — do not lean on these:** CR 0, 1/8, 1/4, 18, 25. One to four
observations each. The values in the table are recorded for completeness;
`cr_curve.py` flags them `thin` and, at CR 18, overrides the single observation
with interpolation.

**No data at all:** CR 11, 13, 14, 16, 17, 19, 21, 22, 23, 24, and everything
above 25. The library simply never wrote a creature at these ratings.
`cr_curve.py` interpolates 11–24 and **refuses CR 26+ with a ValueError**.

**The main structural caveat.** These 589 blocks come from a library that a
generator helped write. The medians are real and self-consistent, but they are
the medians of a *convention*, not of playtested encounters. Nothing in this
repo shows that a CR 5 creature at 80 HP plays correctly at a table. The curve
answers "what does this library consider a CR 5?" — it does not answer "is that
right?". Treat every number as a defensible default that a designer should be
free to overrule without justifying it.

**One known artefact:** AC is non-monotonic at CR 8→9 (18 then 17). CR 9 has
only 12 observations. The curve reports the observed values rather than
smoothing, so this wrinkle is visible rather than hidden.

---

## 7. Where this curve must NOT be used

1. **Do not apply it to any campaign bible without human approval.** That is a
   separate step. This document produces the curve; it does not authorise its
   use.

2. **Do not use it to "fix" bibles whose stats merely fail to parse.** This is
   the most important restriction, and it inverts the assumption behind the
   task. Of the 62 bibles with no fully-parsed monster:
   - **28 already have complete authored HP and AC** in a layout the chunker
     cannot read. These need **reformatting**, not invented numbers. Overwriting
     an author's 60 HP with the curve's 60 HP is lucky; overwriting their 30 HP
     is data loss.
   - **25 have no bestiary section at all** — a structural gap, not a stat gap.
   - **3 have neither CR nor stats** — nothing to hang a curve on.
   - **Only 6 bibles are genuine stat gaps** (creatures with CR and abilities but
     no HP/AC anywhere): `a-midsummer-nights-chaos`, `the-prophesied-child`,
     `winds-of-fortune`, `wings-of-the-crows`, `war-of-the-elements`,
     `the-coffee-and-tragedy`. Their CR demand falls almost entirely in CR 1–8,
     which is exactly where this curve is strongest. **These six are the only
     candidates for curve-supplied stats.**

3. **Do not use it above CR 25 or below CR 0.** `cr_curve.py` raises. Do not
   work around this by extrapolating; there is no evidence up there.

4. **Do not use it for the thin CRs (0, 1/8, 1/4, 18, 25) without a designer
   signing off on each value.** One observation is an anecdote.

5. **Do not use it for boss or set-piece creatures.** The curve is a median of
   ordinary creatures. Named antagonists, legendary creatures and kaiju in this
   library are written well off the line (the CR 30 entry has 5000 HP — 7× what
   SRD's CR 30 carries). A boss deserves a hand-set number.

6. **Do not treat it as SRD-compatible.** A creature statted from this curve is
   deliberately not an SRD-equivalent creature of that CR (−30% HP at low CR,
   +30% at high CR). Do not mix curve-statted and SRD-statted creatures in one
   encounter and expect the CR budget to hold.

7. **Do not back-fill it into bibles that already ship.** The 243 bibles with
   authored stats are the evidence for this curve. Rewriting them to match it
   would be circular and would destroy the source data.

8. **Do not use it to derive anything else.** It supplies HP and AC only. Attack
   bonus, save DCs, damage output and proficiency were not analysed here, and
   nothing in this document supports inventing them.

---

## 8. Reproducing this

The harvest, clone analysis and holdout scripts were written as throwaway
tooling under `tools/launch-readiness/_work/` and are not part of the shipped
toolchain. The two durable artefacts are this document and `cr_curve.py`.
The inputs needed to redo the work from scratch:

- `irparse.py` — extraction (capture the header CR the chunker discards)
- `depth_score.py --json` — `clone_peers` per campaign; exclude `>= 4`
- `campaign-ideas/**/{Completed/,}*/**-campaign-bible.md` — 305 bibles
- Open5e `https://api.open5e.com/v1/monsters/?document__slug=wotc-srd&limit=100`
  paged with `&page=N` (note: `&offset=` is ignored by that endpoint)

Derived 2026-07-28.
