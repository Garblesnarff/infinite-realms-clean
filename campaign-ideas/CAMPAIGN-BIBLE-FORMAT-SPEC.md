# Campaign Bible Format Spec

**Version 1.0 — 2026-08-15**
Applies to: `infinite-realms-clean/campaign-ideas/**`
Derived from: `ai-adventure-scribe-main/tools/lore-keeper-ingest/src/` on `main`
(`parser.ts`, `chunker.ts`, `entity-name.ts`, `reingest.ts`, `index.ts`)

This document describes what the ingestion pipeline **actually does**. It is not a
style guide. Every rule below comes from a regular expression in the source. If
the source changes, this document is wrong until someone updates it.

---

## 0. Rule zero: the database is the source of truth

Do not report an entity as missing, malformed, or duplicated until you check what
ingestion produced. The `prompts/*.md` manifests are generation aids. They contain
entities the database does not have. Two agents have already reported wrong gap
counts from those manifests.

To check a bible before you touch the database, run the pre-flight checker
(Section 10). To check the database, ask Rob or the Hetzner session to run:

```
bun run reingest -- --campaign <slug> --repo-path ../../../infinite-realms-clean
```

That command is a dry run. It prints added, renamed and unchanged entity counts.
It does not write.

---

## 1. Directory name and slug

### 1.1 How a directory becomes a campaign

`listCampaignDirectories()` walks `campaign-ideas/` from the top. A directory is a
campaign if it holds **any one** of these:

- `overview.md`
- `<directory-name>.md`
- `<directory-name>-campaign-bible.md`
- `creative_brief.md` or `creative-brief.md`

If a directory holds none of them, the walker goes into its subdirectories. This
is why genre folders such as `Completed/Horror/` work. It is also why
`_to_delete/` is scanned. Exclude that folder in every tool you write.

### 1.2 The slug

`dirToSlug()` takes the **last** path part, makes it lowercase, and changes `_` to
`-`. Nothing else. So:

| Rule | Reason |
|---|---|
| The directory name must already be lowercase | The slug is the directory name |
| Use `-` between words, never `_` or a space | `_` is converted, other characters are not |
| Use only `a-z`, `0-9` and `-` | No other character is cleaned |
| The slug must be unique across the whole tree | See 1.3 |
| Do not add or remove a leading `the-` | See 1.4 |

### 1.3 Slugs must be unique across genre folders

`reingest --campaign <slug>` matches the slug against every campaign directory. If
two directories in different genre folders share a name, the command stops with
`Campaign slug is ambiguous`. The current library has no duplicates. Keep it that
way.

### 1.4 The `the-` rule

The folder name, the bible filename and the database slug must be identical. A
mismatch between `the-academy-of-arcane-gastronomy` and
`academy-of-arcane-gastronomy` cost days of work. **The database slug wins.** Never
add or remove a leading `the-` to make a name read better.

---

## 2. Required files

`ingestCampaign()` refuses to ingest a campaign that is missing any of the four
files. It returns `missing <list>` and writes nothing.

For each role the parser tries a list of filenames **in order** and takes the first
that exists:

| Role | Filenames tried, in order |
|---|---|
| Creative brief | `creative_brief.md`, `creative-brief.md` |
| World building | `world_building_spec.md`, `world-building-spec.md` |
| Overview | `overview.md`, `<dir>.md`, `<dir without trailing -campaign>.md` |
| Campaign bible | `campaign_bible.md`, `campaign-bible.md`, `<dir>-campaign-bible.md` |

### 2.1 House convention

All three live campaigns use the hyphenated names and `<dir>.md` for the overview.
That convention ingests correctly. Use it for new work:

```
<slug>/
  creative-brief.md
  world-building-spec.md
  <slug>.md
  <slug>-campaign-bible.md
```

### 2.2 Never keep two files for one role

If both `creative_brief.md` and `creative-brief.md` exist, the parser reads
`creative_brief.md` and ignores the other silently. The same applies to
`overview.md` and `<dir>.md`. Keep exactly one file per role.

### 2.3 Delete AppleDouble sidecars

The T7 drive is exFAT. macOS writes `._<filename>` sidecar files there. Delete them
before you commit. 15 campaign directories currently hold them.

```
find campaign-ideas -name "._*" -delete
```

---

## 3. `<slug>.md` — the overview

`parseOverview()` reads this file with regular expressions. **A label that does not
match does not raise an error. It silently falls back to a default.** This is the
most common defect in the library.

### 3.1 Title

```markdown
# The Eternal Feast
```

The first `# ` heading in the file. If there is none, the title becomes the
directory name in title case.

### 3.2 Genre — required

```markdown
**Campaign Type / Genre:** Intrigue / Culinary Fantasy
```

- The label must be exactly `**Campaign Type / Genre:**`. Spaces around the `/`
  are part of the pattern.
- The value is split on `/` and `,`, and lowercased.
- **Silent default if absent: `["fantasy"]`.**
- A weaker fallback label `Campaign Type:` also matches. Do not rely on it.

### 3.3 Tone — required

```markdown
**Tone Keywords:** decadent, uneasy, absurd
```

- The pattern is `**Tone<anything>:**`, so `**Tone:**` and `**Tone Keywords:**`
  both work.
- The value is split on `,` and lowercased.
- **Silent default if absent: `["adventure"]`.**

### 3.4 Player level range — required

```markdown
**Player Level Range:** Start **1**, Finish **10**
```

- The words `Start` and `Finish` are part of the pattern. Both numbers must be
  wrapped in `**`.
- **If this exact form is absent, a loose fallback takes the first two numbers on
  any line that contains the word "Level".** That fallback is often wrong. It is
  worse than no value, because it looks correct.
- If neither matches, `levelRange` is null.

### 3.5 Difficulty

Put the word `Difficulty` on a line with one of these words:

`easy`, `low-medium`, `medium`, `hard`, `deadly`

```markdown
**Difficulty:** Hard
```

- **Silent default if absent: `medium`.**
- **Known source defect:** `parseDifficulty()` tests `hard` before `medium-hard`,
  so `medium-hard` can never be returned. Do not use that word. Use `hard`.

### 3.6 Core premise

```markdown
**Core Premise:** A restaurant at the end of time serves one guest per century.
The bill has come due.
```

- The block ends at the first blank line that is followed by `---`, `##` or `**`.
- Markdown is stripped. The text is cut at 500 characters.
- **If the label is absent, the premise becomes the first paragraph longer than 50
  characters that does not start with `#`, `*` or `-`.** That is usually the wrong
  text.

### 3.7 Estimated length

```markdown
**Estimated Length:** 10-12 sessions
```

Either `N-M sessions` or `Estimated Length: N-M` matches. If neither is present,
`estimatedSessions` is null.

---

## 4. `<slug>-campaign-bible.md` — sections

The chunker cannot see content that is not under a header it recognises. It calls
`extractSection(content, name)` with a fixed list of names.

### 4.1 Section names the chunker looks for

Each extractor tries its names in order and uses the first section that has a body.

| Extractor | Section names tried |
|---|---|
| NPCs | `NPC`, then `Major NPCs` |
| Factions | `Faction` |
| Locations | `Location`, then `World Map` |
| Main quest | `Main Quest`, then `Quest Architecture` |
| Side quests | `Side Quest` |
| Mechanics | `Mechanic`, then `Unique Mechanic` |
| Items | `Item`, then `Artifact`, then `Loot` |
| Handouts | `Handouts` |
| Bestiary | `Bestiary`, then `Encounter` |
| Session outlines | `Campaign Roadmap`, then `Session` |

The name is matched as a substring of the header text, case-insensitively. So
`## 3. NPC ROSTER` matches the name `NPC`.

### 4.2 Header forms that work

`extractSection()` accepts four header forms:

```markdown
## 3. NPC ROSTER                     <- ## + optional number + name
### Locations                        <- ### + name
## Section 3: NPC ROSTER             <- ## Section N: ... name ...
**NPCs**:                            <- bold label on its own line
```

A `##` section runs to the next `## `. A `###` section runs to the next `###` or
`##`.

### 4.3 Header forms that DO NOT work — read this

These forms are in the library today and are **invisible** to the chunker:

```markdown
## **3. NPC ROSTER**                 <- bold wraps the whole header
## [TAG: NPC_TIER_1]                 <- TAG marker instead of a word
```

The 2026-08-15 audit found **219 of 303 finished bibles use the `[TAG: …]` form.**
Their content is well formed. It is simply never read.

The remedy already chosen for this project is **normalization, not a parser
change**: `tools/launch-readiness/normalize_bestiaries_v2.py` inserts a plain
`## Bestiary` heading, and 244 bibles have been repaired that way with zero
regressions. That work covered the bestiary only. The other five sections
(`NPC_TIER_1`, `LOCATIONS_MAIN`, `QUEST_MAIN`, `FACTION_DATA`, `ITEM_LEGENDARY`)
have the identical defect and are still unaddressed. Extend the normalizer;
do not open a second front in the parser.

Until that change ships, a bible must use a plain-word header from 4.2 to ingest.

### 4.4 Canonical section skeleton

Use this skeleton for new bibles. It satisfies every extractor.

```markdown
# Campaign Bible: <Title>

## 1. Deep Lore and History
## 2. Factions
## 3. NPC Roster
## 4. Locations
## 5. Quest Architecture
## 6. Side Quests
## 7. Item Database
## 8. Bestiary
## 9. Mechanics
## 10. Handouts
## 11. Campaign Roadmap
```

---

## 5. Entity list formats, per type

These are the formats the extractors parse. An entry in any other shape is dropped
without a warning.

### 5.1 NPCs

Inside the NPC section, use a numbered list. The name must be bold.

```markdown
### Major NPCs (20 Profiles)

1.  **Lord Ashworth** (Human Big-Game Hunter) - An eccentric, ruthless aristocrat.
    **Voice:** A crisp, upper-class accent. **Goal:** To capture the Beast.
    **Secret:** He believes the Beast will grant him immortality.
2.  **High Priestess Xylos** (K'tharr Mystic) - A wise, ancient woman.
```

A second form is accepted, where the bold wraps the number:

```markdown
**1. Lord Ashworth** (Human Big-Game Hunter) - ...
```

**Tier is assigned automatically.** `determineTier()` counts the words
`personality`, `voice`, `goal`, `secret`, `motivation` in the block:

| Result | Condition |
|---|---|
| `npc_tier1` | 2 or more of those words, **or** the block is over 500 characters |
| `npc_tier2` | 1 of those words, **or** the block is over 200 characters |
| `npc_tier3` | neither |

To make an NPC tier 1, give it **Voice**, **Goal** and **Secret** lines. Do not
try to control the tier any other way.

### 5.2 Minor NPCs in a table

A four-column table is read as tier 2. **The name cell must be bold.**

```markdown
| Name | Role | Location | Quirk |
|---|---|---|---|
| **Barnaby** | Ship's Cook | The Sea Serpent | Believes fish enjoy being eaten. |
```

An unbolded name cell is dropped. This is a real, current loss: The Eternal Feast
is live with 124 rows, and its bible holds 50 minor NPCs and 30 side quests in
unbolded tables that have never reached the database.

### 5.3 Factions

Two forms work. Use the `###` heading form.

```markdown
### The Drowned Choir
**Type:** Operatic Ghost Pirates
**Leader:** Captain Arioso
**Asset:** The Phantom Fleet.
**Rivals:** The Tide-Speakers.
```

`**Type:**` and `**Leader:**` are read into the chunk metadata. `**Type:**` and
`**Agenda:**` together produce the summary line.

A bracketed form also works: `[The Court of Stolen Breath]` followed by the body.

### 5.4 Locations

Two forms work, and both may be used in one bible.

**Zone form.** The word `Zone` and a number are part of the pattern.

```markdown
### Zone 1: The Root Crown
1.  **The Shattered Plaza:** The city centre, now a crater.
2.  **The Sap-Lake:** A pool of magical sap.
```

The zone becomes a location chunk. Each numbered entry becomes a location chunk
with the zone as its `parentEntity`.

**Bullet form.**

```markdown
*   **Tortuga, the Free Port:** A chaotic city of pirates. **Smell:** Cheap rum.
    **Sound:** Raucous laughter.
```

`**Smell:**` and `**Sound:**` are read into the chunk metadata. Keep them on the
same bullet.

A leading `Loc 3: ` is stripped from the name automatically.

### 5.5 Main quest

Numbered beats with bold names. The beat number becomes `sequenceOrder`.

```markdown
## 5. Quest Architecture

1.  **The Gilded Corpse:** The players find a dead pirate turning to gold.
2.  **The Whispering Coin:** The coin promises wealth and power.
```

### 5.6 Side quests

A four-column table. **The quest name must be bold.** A row whose name is
`Quest Name` is skipped as a header.

```markdown
| Quest Name | Giver | Objective | Reward |
|---|---|---|---|
| **The Singing Ghost** | Captain Arioso | Find the lost sheet music. | Fame. |
```

### 5.7 Items

Numbered entries with bold names.

```markdown
## 6. Item Database

1.  **The Sun-Sliver:** A shard of solidified sunlight.
2.  **The Ocean's Heart:** A pearl the size of a fist.
```

`metadata.isArtifact` is set to true if the section name contains `artifact`, or
if the entry text contains `legendary`.

**A `### 1. The Sun-Sliver` heading does not work.** The name must be bold.

### 5.8 Handouts

The strictest format in the pipeline. **All four labels are required. If any one
is missing the entry is skipped without a warning.**

```markdown
## Handouts

### Balthazar's Recipe Card
Key: `balthazars-recipe`
Title: Balthazar's Recipe Card
Giver: Balthazar
Body:
Fold the saffron into the dough at dawn.

Keep the oven door shut.
```

- `Key:` must be a slug. Runtime delivery validates it.
- `Body:` must be on a line by itself. Everything after it is the body.
- The labels may be prefixed with `- ` or `* `.

### 5.9 Bestiary

Two forms work. The `(CR n)` part is required in both.

```markdown
### 1. Gluten Golem (CR 5)
**HP:** 90, **AC:** 15.
```

```markdown
**1. The Chiropteran Hulk (CR 5)**
**HP:** 90, **AC:** 15.
```

A third form covers old bibles: `### Custom Stat Block: **Name**`.

Encounter tables need a `**D20 <environment>**` heading.

### 5.10 Session outlines

The word `Session`, a number, a colon and the title, all inside one bold span.

```markdown
**Session 1: The Reservation**
The players receive an invitation that names them by a title they do not hold.
```

The number becomes `sequenceOrder`. A heading such as
`### Session-by-Session Breakdown` is only a container; each session still needs
its own bold line.

---

## 6. Entity names

### 6.1 What is cleaned automatically

`normalizeEntityNameForChunkType()` removes:

- Wrapping double quotes, repeatedly
- A leading `Loc 3: ` on location names
- A trailing colon on any name
- A leading `3. ` on faction names

### 6.2 What is rejected

`isSectionMarkerName()` rejects a name that:

- starts with `TAG:`
- is exactly `Concept` or `History`

A rejected name is not a warning. During a safe re-ingest it is a **hard failure**:
`loadReingestCampaign()` throws `Parser emitted section markers for <campaign>`.

### 6.3 Identity and duplicates

A row's identity is `campaign_id + chunk_type + normalized entity_name`. Two
entries with the same identity collapse into one row. So:

- Do not give two NPCs the same name.
- Do not repeat a location in both a zone list and a bullet list.
- An entity may share a name across types. A location and an item may both be
  called `The Ocean's Heart`.

### 6.4 Names must be names

An extractor that swallows a sentence produces a row whose `entity_name` is a
paragraph. Ten campaigns currently have names over 60 characters. Keep the bold
span tight around the name. Put the description after the closing `**`.

---

## 7. `world-building-spec.md`

The whole file becomes one `world_building` chunk. Three named sections become
extra chunks if they are longer than 100 characters:

- `Core Concept`
- `Lore`
- `History` — **but a chunk named exactly `History` is then rejected as a section
  marker.** Name the heading `World History` or `Timeline` instead.

### 7.1 Causality rules

Under a section whose header contains `Causality`, write one rule per line:

```markdown
## Causality Chains

* IF the players return the coin to the sea THEN the Ocean calms for one season
* IF the Sun-Gold is raised above the waves THEN the Long Night ends permanently
```

- `IF` and `THEN` must both be present on the line, in capitals.
- If the effect contains the word `permanent`, the rule is stored as
  irreversible.
- Priority counts down from 5 in file order. Put the most important rule first.

---

## 8. `creative-brief.md`

The brief becomes one chunk, or one chunk per `##` section if the file is over
2000 characters.

### 8.1 The cast agreement rule

**Every named character in the creative brief must exist in the campaign bible,
spelled the same way.**

This rule exists because of the Academy of Arcane Gastronomy. The brief named five
principal NPCs. The bible's 20 major NPCs contained none of them. Three finished
images were orphaned, because art was made from the brief and the database was
built from the bible.

The bible is the cast list. The brief describes how that cast looks and sounds. If
the brief needs a character the bible does not have, add the character to the
bible first.

The pre-flight checker reports brief-only proper nouns as `INFO`. It cannot tell an
orphaned NPC from a real-world reference such as `Gordon Ramsay`, so a person must
read that list.

---

## 9. Pre-flight checklist

Run this before you ask for a dry run.

**Directory**

- [ ] Directory name is lowercase, hyphenated, `a-z0-9-` only
- [ ] No other directory in the tree has the same name
- [ ] No leading `the-` was added or removed
- [ ] No `._*` sidecar files

**Files**

- [ ] All four files exist
- [ ] Exactly one file per role
- [ ] Bible filename is `<slug>-campaign-bible.md`

**Overview**

- [ ] `# Title` heading
- [ ] `**Campaign Type / Genre:**` exact label
- [ ] `**Tone Keywords:**`
- [ ] `**Player Level Range:** Start **N**, Finish **M**`
- [ ] A line with `Difficulty` and one of the five accepted words
- [ ] `**Core Premise:**`
- [ ] `**Estimated Length:** N-M sessions`

**Bible**

- [ ] Section headers use plain words, not `**bold**` and not `[TAG: …]`
- [ ] All eleven canonical sections present
- [ ] NPCs are a numbered list with bold names
- [ ] Each tier-1 NPC has Voice, Goal and Secret
- [ ] Table name cells are bold
- [ ] Locations use the zone form or the bullet form
- [ ] Main quest beats are numbered with bold names
- [ ] Items are numbered with bold names
- [ ] Bestiary entries carry `(CR n)`
- [ ] Handouts carry all four labels
- [ ] Sessions use `**Session N: Title**`
- [ ] No entity name over 60 characters
- [ ] No duplicate names within one type

**Cross-file**

- [ ] Every character named in the brief exists in the bible
- [ ] Causality rules use `IF … THEN …`
- [ ] No world-building heading named exactly `History` or `Concept`

**Measured**

- [ ] `node preflight.mjs --repo-path <repo> --campaign <slug>` reports CONFORMING
- [ ] Row count is in the expected range (a full bible produces 120 to 240 rows)

---

## 10. The pre-flight checker

`preflight.mjs` bundles the real `chunker.ts` and `parser.ts` from `main`. It does
not re-implement them, so it cannot drift from the pipeline.

```
node preflight.mjs --repo-path infinite-realms-clean --campaign <slug>
node preflight.mjs --repo-path infinite-realms-clean --exclude _to_delete,Tools --json
```

It reports, per campaign:

- A verdict: CONFORMING, FIXABLE or NEEDS REWRITE
- Every finding, with the source behaviour it comes from
- The chunk count per type
- The row count after identity dedupe — this is what the database receives
- The list of entities that will need art

Exit code is 1 if any campaign is not CONFORMING.

**Verification status (updated 2026-08-18).** The checker reproduces production
row counts exactly, provided you pin the revision. The Academy of Arcane
Gastronomy gap is fully reconciled: 188 at `main` (`8da99ced`), 198 after
`660efb99`, which gave the bestiary a `## Bestiary` heading and made 10 monster
blocks visible. **188 is ground truth for the database today.**

**Always quote the revision with the count.** The working checkout of
`infinite-realms-clean` sits on `content/launch-ten-readiness`, 25 commits ahead
of `main`. A count taken there does not describe production. See
`RECONCILIATION-2026-08-18.md`.

**Read `tools/launch-readiness/BIBLE-GENERATION-SPEC.md` alongside this document.**
It is the pre-existing contract for the bible generator and it governs the
bestiary format in more detail than Section 5.9 here. Where the two disagree, that
one wins for bestiaries.

---

## 11. Feeding the character-template generator (#1798 item C)

Five starter characters per campaign must eventually come from bible data, not
hand-written SQL. The generator will read the chunks this spec produces. To make a
bible usable by it:

- Give every tier-1 NPC a **Voice**, a **Goal** and a **Secret**. These are the
  only structured personality fields the chunker keeps.
- Put the race and class in the parenthetical after the name:
  `**Lord Ashworth** (Human Big-Game Hunter)`. The parenthetical becomes the chunk
  summary, so it is the one field a generator can read without parsing prose.
- Keep the level range in the overview correct. It sets the starting level.
- Name factions consistently between the faction section and the NPC entries. A
  starter character's allegiance will be resolved by name match.

---

## Appendix A. Silent defaults

Every one of these is applied without a warning.

| Field | Default when the label is missing |
|---|---|
| `title` | Directory name in title case |
| `genre` | `["fantasy"]` |
| `tone` | `["adventure"]` |
| `difficulty` | `medium` |
| `levelRange` | Loose two-number guess, then null |
| `estimatedSessions` | null |
| `premise` | First paragraph over 50 characters |
| Any entity list in an unrecognised format | Dropped entirely |

## Appendix B. Known source defects

Recorded here so nobody rediscovers them. None is fixed as of 2026-08-15.

1. `parseDifficulty()` tests `hard` before `medium-hard`, so `medium-hard` is
   unreachable.
2. The level-range fallback takes the first two numbers on any line containing
   `Level`, which silently produces wrong ranges.
3. `extractSection()` does not accept bold-wrapped or `[TAG: …]` headers, which
   hides 219 of 303 finished bibles. Known since `PHASE4-LIBRARY-CLEANUP.md`;
   being handled by normalization, bestiary first.
4. Table extractors require bold name cells, which drops complete tables in
   otherwise working bibles, including one that is live.
5. A `History` section in the world-building spec is created and then rejected as
   a section marker.
