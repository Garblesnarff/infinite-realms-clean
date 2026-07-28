# Campaign Bible Generation Spec

**Status:** authoritative. Use this for every new bible.
**Written:** 2026-07-28, after the library-wide cleanup.

The generator that produced the current library is not in this repository. This
file is the corrected specification. Paste the prompt block below into whatever
runs the generation.

---

## 1. Why this file exists

Three faults in the current library all came from generation, not from authors:

| Fault | Scale | Cost |
|---|---|---|
| Bestiaries in a shape the chunker cannot read | 292 of 314 bibles | Every monster fought as an 11 HP generic |
| The same three creatures with new names | 206 of 305 bibles | Four genres have no shippable campaign |
| Bible written into `Completed/`, package left at the genre root | 135 campaigns | No ingest path saw a whole campaign |

Each was repaired by hand. None will stay repaired if generation keeps its
current behaviour.

---

## 2. Hard requirements

### 2.1 Bestiary format

Production reads monsters in two steps. Both must succeed.

**Step 1 — the chunker finds the section.** The bible must contain a heading
matching `## Bestiary` (a leading number is allowed: `## 7. Bestiary`).
`[TAG: ENEMY_STATBLOCK]` alone is not enough. The chunker looks for the word
Bestiary or Encounter and nothing else.

**Step 2 — the chunker finds each creature.** Every entry must use this exact
header form, ending with the CR in brackets:

```
### <n>. <Name> (CR <x>)
```

**Step 3 — the parser reads the stats.** Every field needs its label and a
colon. A number without a label is invisible to production. This is deliberate:
a wrong stat cannot be seen in play, but a failed parse gets logged.

Write each entry exactly like this:

```
### 1. Sorrow-Demon (CR 2)
(CR 2). Fiend. **HP:** 45, **AC:** 13.
**Abilities:**
*   **Passive: Aura of Grief:** Any creature starting its turn within 20 feet
    has its speed halved.
*   **Action: Weeping Touch:** Melee attack. 2d6 psychic damage, WIS save or
    the target weeps for one turn.
```

Accepted label spellings: `HP`, `Hit Points`, `Health`; `AC`, `Armor Class`,
`Armour Class`. Emphasis is optional, the colon is not. `HP 45, AC 13` fails.

AC must be 1 to 30. HP must be above 0.

Do not put a `[TAG: ...]` marker between the Bestiary heading and the last
creature. The parser cuts everything after the first marker it sees.

### 2.2 Creature variety

This is the rule the current generator broke.

- Write **8 to 12** creatures per campaign.
- Every creature must be specific to this campaign's world.
- **Never** produce the Standard / Elite / Mastermind ladder.
- **Never** reuse the stat line `HP 30 / AC 13`, `HP 80 / AC 16`,
  `HP 180 / AC 18`. 114 campaigns already share it.
- Vary HP and AC across the campaign. A bestiary where every entry sits on a
  round number is a template, not a design.
- Do not reuse ability names between campaigns. "Ordered Discipline",
  "Reality-Warping Pulse" and "The Final Move" are burned — they appear in
  over a hundred bibles.

Self-check before output: if two creatures in this bible could swap names
without anyone noticing, rewrite them.

### 2.3 Names that cannot ship

Verified against the full 322-entry SRD 5.1 monster list (Open5e,
`document__slug=wotc-srd`, CC-BY-4.0).

**Never use — absent from the SRD:**

beholder, spectator, death tyrant, mind flayer, illithid, githyanki, githzerai,
yuan-ti, kuo-toa, slaad, umber hulk, displacer beast, carrion crawler, modron,
intellect devourer, flumph, froghemoth

**Safe — these are in the SRD, do not "fix" them:**

drider, blink dog, rakshasa, otyugh, owlbear, drow, and the plane names
Feywild, Shadowfell, Underdark, Nine Hells, Mechanus

**Never use — Wizards trademarks and settings:**

D&D, Dungeons & Dragons, Wizards of the Coast, Player's Handbook, Monster
Manual, Dungeon Master's Guide, Forgotten Realms, Faerûn, Waterdeep, Baldur's
Gate, Ravenloft, Strahd, Barovia, Menzoberranzan, Drizzt, Red Wizards, Thay,
Planescape, Sigil, Eberron, Sharn, Spelljammer, Dark Sun, Athas, Dragonlance,
Krynn, Greyhawk, Undermountain, Zariel, Xanathar, Mordenkainen, Elminster,
Vecna, Icewind Dale, Neverwinter

Say **5E** or **5E-compatible** instead of D&D.

### 2.4 Third-party pastiche

A campaign may take inspiration from a film, anime or novel. It may not carry
that work's proper nouns. Rename every character, place and named technique
before output. Campaigns already in the library that need this pass include
Demon Slayer, Cowboy Bebop, My Hero Academia and Le Guin material.

If the premise cannot survive renaming, the premise is the problem.

### 2.5 File layout

A campaign is **one directory** with four files:

```
campaign-ideas/Completed/<Genre>/<slug>/
    <slug>.md                      overview
    creative-brief.md
    world-building-spec.md
    <slug>-campaign-bible.md
```

Before the bible exists, the first three live in
`campaign-ideas/<Genre>/<slug>/`. When the bible is written, **move the whole
package** into `Completed/<Genre>/`. Never write a bible into `Completed/`
while the other files stay behind. That split 135 campaigns.

---

## 3. Prompt block

> You are writing a campaign bible for Infinite Realms, a 5E-compatible solo
> tabletop platform. Follow every rule below. A bible that breaks any hard rule
> is rejected.
>
> **Bestiary format.** Include a section headed `## Bestiary`. Inside it write 8
> to 12 creatures. Each creature uses this header exactly, with the CR in
> brackets at the end:
> `### <number>. <Creature Name> (CR <rating>)`
> On the next line give the stats with labels and colons:
> `(CR <rating>). <Type>. **HP:** <number>, **AC:** <number>.`
> Then `**Abilities:**` and two or three bullet points.
> A number without a label cannot be read by the platform. AC must be 1 to 30.
>
> **Variety.** Every creature belongs to this campaign's world and nowhere else.
> Do not write a Standard / Elite / Mastermind ladder. Do not use the stat lines
> HP 30 AC 13, HP 80 AC 16, or HP 180 AC 18. Vary the numbers. Do not reuse
> ability names across campaigns.
>
> **Names.** Never use: beholder, spectator, death tyrant, mind flayer,
> illithid, githyanki, githzerai, yuan-ti, kuo-toa, slaad, umber hulk,
> displacer beast, carrion crawler, modron, intellect devourer, flumph,
> froghemoth. Never use Wizards trademarks or setting names, including D&D,
> Dungeons & Dragons, Forgotten Realms, Waterdeep, Ravenloft, Barovia, Strahd,
> Planescape, Sigil, Eberron, Spelljammer, Dark Sun, Undermountain, Zariel or
> Vecna. Write 5E or 5E-compatible instead of D&D. Drider, blink dog, rakshasa
> and owlbear are open content and may be used.
>
> **Pastiche.** If the premise draws on a film, anime or novel, rename every
> character, place and named technique. Keep the structure, drop the names.
>
> **Sections.** Use the tag headings the platform already expects:
> LORE_CORE, FACTION_DATA, NPC_TIER_1, NPC_TIER_2, LOCATIONS_MAIN, QUEST_MAIN,
> QUEST_SIDE, ITEM_LEGENDARY, ENEMY_STATBLOCK, INDEX_KEYWORDS. Put the
> `## Bestiary` heading directly under the ENEMY_STATBLOCK tag, and do not place
> any other tag marker between that heading and the last creature.

---

## 4. Verify before commit

```bash
python3 tools/launch-readiness/coverage_report.py --failing   # must list nothing new
python3 tools/launch-readiness/depth_score.py --top 20        # clones must not appear
./campaign-ideas/stats.sh                                     # totals must not jump
```

A new bible is acceptable when it reports 8 or more monsters, all grading FULL,
with zero clone peers.
