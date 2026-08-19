# Campaign Bible Audit — Full Library

> **SUPERSEDED IN PART, 2026-08-18.** Every row count below was measured on
> `content/launch-ten-readiness` (`ce784236`), which is **25 commits ahead of
> `main`** and which production has never ingested. Treat the counts as
> describing that branch, not the library. The recommendation to change the
> parser is **withdrawn** — this project already chose normalization and has
> shipped 244 repaired bibles. See `RECONCILIATION-2026-08-18.md`.
> What survives: the finding that normalization has only covered the bestiary,
> and that five other sections have the same defect.

**2026-08-15** · measured with `preflight.mjs`, which bundles the real chunker and parser from `main`.

Nothing here is from a manifest. Every number is what the ingestion pipeline produces from the files on disk today.


---


## Headline

- `campaign-ideas/` holds **820 directories** the ingester would treat as campaigns, not 163. `_to_delete`, `Tools` and `Ideas-To-Expand` are already excluded from this count.
- **303** sit under `Completed/`. That is the real working set.
- **517** sit in the loose genre folders. These are idea stubs: 514 of them have no campaign bible at all. They are out of scope until someone writes the bible.

Of the 303 finished campaigns, **as the parser stands today**:

| Verdict | Count |
|---|---|
| CONFORMING | 11 |
| FIXABLE | 42 |
| NEEDS REWRITE | 250 |

That 250 is misleading, and it is the main finding of this audit. Read the next section before you plan any rewriting.


---


## The 219: one parser gap, not 219 broken bibles

219 of the 303 finished bibles use `## [TAG: NPC_TIER_1]` style section headers. `extractSection()` matches on plain words, so it never finds those sections. The content inside them is well formed and consistent. It is simply never read.

A prototype extractor change was built and measured against the whole library:

| Measure | Parser today | With the change |
|---|---|---|
| NEEDS REWRITE | 250 | 33 |
| Campaigns with 5+ of 7 entity categories populated | 55 | 271 |
| Total rows the database would receive | 11,566 | 20,889 |
| Campaigns that lose rows | — | 1 |

Per entity category, campaigns going from zero entities to some: NPCs 218, quests 219, locations 216, items 216, factions 215.

**Recommendation: file the parser change, do not rewrite the bibles.** The details and the caveats are in `ISSUE-tag-dialect.md`.


---


## Per genre, finished campaigns

| Genre | Conforming | Fixable | Needs rewrite | Rows today | Rows after fix |
|---|---|---|---|---|---|
| Adventure | 5 | 6 | 10 | 2,053 | 3,070 |
| Fantasy | 1 | 17 | 140 | 4,341 | 9,075 |
| Historical | 1 | 2 | 10 | 1,002 | 1,329 |
| Horror | 1 | 4 | 14 | 1,160 | 1,867 |
| Intrigue | 1 | 3 | 14 | 544 | 1,088 |
| Mystery | 1 | 4 | 14 | 995 | 1,767 |
| Post-Apocalyptic | 0 | 0 | 17 | 128 | 572 |
| Sci-Fi | 0 | 3 | 18 | 701 | 1,108 |
| Urban | 1 | 3 | 13 | 642 | 1,013 |


---


## CONFORMING — ingest clean today, no edits needed

| Rows | Campaign |
|---|---|
| 201 | `Completed/Adventure/ghost-who-walks` |
| 200 | `Completed/Adventure/blades-of-glory` |
| 199 | `Completed/Adventure/beast-of-skull-isle` |
| 197 | `Completed/Horror/arkham-investigations` |
| 193 | `Completed/Adventure/court-of-redemption` |
| 177 | `Completed/Historical/arc-of-orleans` |
| 173 | `Completed/Mystery/the-watchmen-protocol` |
| 126 | `Completed/Intrigue/the-seekers-trial` |
| 124 | `Completed/Urban/the-coffee-and-tragedy` |
| 122 | `Completed/Fantasy/the-prophesied-child` |
| 106 | `Completed/Adventure/seven-swords-for-hire` |

These eleven are the launch runway. Any of them can go to a dry run now.


---


## FIXABLE — mechanical edits only

Every one of these already yields a full entity set. The findings are overview labels, sidecar files, or a single empty extractor. None needs new lore.

| Rows | Campaign | Blockers |
|---|---|---|
| 236 | `Fantasy/a-midsummer-nights-chaos` | _warnings only_ |
| 206 | `Horror/abyssal-descent` | _warnings only_ |
| 205 | `Horror/the-porcelain-court` | OV_GENRE_LABEL, OV_LEVEL_LABEL, OV_TONE_LABEL |
| 203 | `Adventure/impossible-heist-protocol` | OV_GENRE_LABEL, OV_LEVEL_LABEL, OV_TONE_LABEL |
| 203 | `Fantasy/alchemical-insurgence` | OV_GENRE_LABEL, OV_LEVEL_LABEL, OV_TONE_LABEL |
| 201 | `Sci-Fi/see-you-space-cowboy` | _warnings only_ |
| 200 | `Adventure/against-the-titans` | _warnings only_ |
| 200 | `Fantasy/academy-of-legends` | _warnings only_ |
| 200 | `Fantasy/children-of-the-stars` | OV_GENRE_LABEL, OV_LEVEL_LABEL, OV_TONE_LABEL |
| 199 | `Fantasy/atomic-dawn` | OV_GENRE_LABEL, OV_TONE_LABEL |
| 198 | `Adventure/ascension-protocol` | OV_GENRE_LABEL, OV_LEVEL_LABEL, OV_TONE_LABEL |
| 198 | `Fantasy/academy-of-arcane-gastronomy` | OV_GENRE_LABEL, OV_LEVEL_LABEL, OV_TONE_LABEL |
| 198 | `Fantasy/baba-yagas-bargain` | _warnings only_ |
| 197 | `Fantasy/beyond-the-wall` | _warnings only_ |
| 197 | `Horror/calypsos-death-derby` | _warnings only_ |
| 196 | `Fantasy/ash-and-remembrance` | _warnings only_ |
| 196 | `Fantasy/battle-of-the-bands` | _warnings only_ |
| 195 | `Historical/the-weather-weavers` | OV_GENRE_LABEL, OV_LEVEL_LABEL, OV_TONE_LABEL |
| 194 | `Fantasy/beneath-the-grassblade` | OV_GENRE_LABEL, OV_LEVEL_LABEL, OV_TONE_LABEL |
| 194 | `Fantasy/blood-of-the-einherjar` | OV_GENRE_LABEL, OV_LEVEL_LABEL, OV_TONE_LABEL |
| 192 | `Mystery/murder-on-the-astral-express` | OV_GENRE_LABEL, OV_LEVEL_LABEL, OV_TONE_LABEL |
| 163 | `Mystery/the-white-wolfs-hunt` | _warnings only_ |
| 155 | `Mystery/the-verdant-codex` | OV_GENRE_LABEL, OV_LEVEL_LABEL, OV_TONE_LABEL |
| 154 | `Urban/the-chosen-slayer` | _warnings only_ |
| 152 | `Adventure/the-spire-ascendant` | _warnings only_ |
| 150 | `Fantasy/the-ghost-of-midgard` | _warnings only_ |
| 137 | `Sci-Fi/wings-of-the-void` | OV_GENRE_LABEL, OV_LEVEL_LABEL, OV_TONE_LABEL |
| 130 | `Fantasy/classical-symphony-kingdom` | OV_GENRE_LABEL, OV_LEVEL_LABEL, OV_TONE_LABEL |
| 130 | `Historical/war-of-the-elements` | OV_GENRE_LABEL, OV_LEVEL_LABEL, OV_TONE_LABEL |
| 124 | `Fantasy/the-hermits-pilgrimage` | OV_GENRE_LABEL, OV_LEVEL_LABEL, OV_TONE_LABEL |
| 124 | `Intrigue/the-eternal-feast` | OV_GENRE_LABEL, OV_LEVEL_LABEL, OV_TONE_LABEL |
| 121 | `Urban/the-crimson-thread-of-silverport` | _warnings only_ |
| 116 | `Urban/the-village-of-quiet-seasons` | OV_GENRE_LABEL, OV_TONE_LABEL |
| 113 | `Horror/xenomorph-protocol` | _warnings only_ |
| 111 | `Fantasy/chronicles-of-the-somnolent-oracle` | OV_GENRE_LABEL, OV_LEVEL_LABEL, OV_TONE_LABEL |
| 105 | `Intrigue/the-impossible-vault` | _warnings only_ |
| 99 | `Mystery/thieves-of-the-cognitive-palace` | _warnings only_ |
| 95 | `Sci-Fi/who-knows-what-evil` | _warnings only_ |
| 94 | `Fantasy/clash-of-olympus` | _warnings only_ |
| 88 | `Adventure/the-lightning-runner` | _warnings only_ |
| 88 | `Intrigue/the-revolutionaries-anthem` | _warnings only_ |
| 84 | `Adventure/the-crimson-spire` | _warnings only_ |

The commonest fix by far is the overview label block. 26 of these need the same four lines added to `<slug>.md`:

```markdown
**Campaign Type / Genre:** <genre> / <sub-genre>
**Tone Keywords:** <word>, <word>, <word>
**Player Level Range:** Start **1**, Finish **10**
**Difficulty:** <easy|low-medium|medium|hard|deadly>
```


---


## NEEDS REWRITE — with the parser change, most of these are not rewrites

250 campaigns today. **217** of them stop being rewrites the moment the extractor change lands.

The genuine rewrites are the remainder. Listed here are the finished campaigns that still yield almost nothing even with the prototype change applied:

| Rows today | Rows after fix | Campaign | Blockers |
|---|---|---|---|
| 2 | 2 | `Horror/wrath-of-achilles` | NOFILE_BIBLE, YIELD0_LOCATIONS, YIELD0_MAIN_QUEST, YIELD0_NPCS |
| 2 | 2 | `Horror/wrath-of-the-phoenix` | NOFILE_BIBLE, YIELD0_LOCATIONS, YIELD0_MAIN_QUEST, YIELD0_NPCS |
| 4 | 4 | `Urban/fates-warning` | NOFILE_BIBLE, YIELD0_LOCATIONS, YIELD0_MAIN_QUEST, YIELD0_NPCS |
| 5 | 5 | `Fantasy/children-of-the-planet` | SECTION_MISSING_LOCATIONS, SECTION_MISSING_MAIN_QUEST, SECTION_MISSING_NPCS, YIELD0_LOCATIONS, YIELD0_MAIN_QUEST, YIELD0_NPCS |
| 7 | 7 | `Intrigue/rank-and-deception` | OVERVIEW_GENRE_LABEL, OVERVIEW_LEVEL_LABEL, OVERVIEW_TONE_LABEL, SECTION_MISSING_LOCATIONS, SECTION_MISSING_MAIN_QUEST, SECTION_MISSING_NPCS, YIELD0_LOCATIONS, YIELD0_MAIN_QUEST, YIELD0_NPCS |
| 7 | 7 | `Sci-Fi/winds-of-fortune` | NOFILE_BIBLE, OVERVIEW_GENRE_LABEL, OVERVIEW_LEVEL_LABEL, OVERVIEW_TONE_LABEL, YIELD0_LOCATIONS, YIELD0_MAIN_QUEST, YIELD0_NPCS |
| 8 | 8 | `Historical/tides-of-the-trident-throne` | NOFILE_BIBLE, OVERVIEW_GENRE_LABEL, OVERVIEW_LEVEL_LABEL, OVERVIEW_TONE_LABEL, YIELD0_LOCATIONS, YIELD0_MAIN_QUEST, YIELD0_NPCS |
| 8 | 8 | `Sci-Fi/shadows-of-the-precursors` | OVERVIEW_GENRE_LABEL, OVERVIEW_LEVEL_LABEL, OVERVIEW_TONE_LABEL, SECTION_MISSING_MAIN_QUEST, YIELD0_MAIN_QUEST, YIELD0_NPCS |
| 8 | 8 | `Sci-Fi/steel-prophets` | OVERVIEW_GENRE_LABEL, OVERVIEW_LEVEL_LABEL, OVERVIEW_TONE_LABEL, SECTION_MISSING_MAIN_QUEST, YIELD0_MAIN_QUEST, YIELD0_NPCS |
| 9 | 9 | `Intrigue/operation-family-deception` | OVERVIEW_GENRE_LABEL, OVERVIEW_LEVEL_LABEL, OVERVIEW_TONE_LABEL, SECTION_MISSING_LOCATIONS, SECTION_MISSING_MAIN_QUEST, SECTION_MISSING_NPCS, YIELD0_LOCATIONS, YIELD0_MAIN_QUEST, YIELD0_NPCS |
| 9 | 9 | `Sci-Fi/sons-of-ares` | SECTION_MISSING_MAIN_QUEST, YIELD0_MAIN_QUEST, YIELD0_NPCS |
| 9 | 9 | `Urban/lagoon-company-chronicles` | SECTION_MISSING_MAIN_QUEST, YIELD0_MAIN_QUEST, YIELD0_NPCS |
| 10 | 10 | `Fantasy/checkmate-protocol` | OVERVIEW_GENRE_LABEL, OVERVIEW_LEVEL_LABEL, OVERVIEW_TONE_LABEL, SECTION_MISSING_LOCATIONS, SECTION_MISSING_MAIN_QUEST, SECTION_MISSING_NPCS, YIELD0_LOCATIONS, YIELD0_MAIN_QUEST, YIELD0_NPCS |
| 10 | 10 | `Sci-Fi/serenity-rising` | SECTION_MISSING_MAIN_QUEST, YIELD0_MAIN_QUEST, YIELD0_NPCS |
| 10 | 10 | `Sci-Fi/songstress-and-the-valkyrie` | SECTION_MISSING_MAIN_QUEST, YIELD0_MAIN_QUEST, YIELD0_NPCS |
| 11 | 11 | `Urban/most-wanted-blacklist` | SECTION_MISSING_MAIN_QUEST, YIELD0_MAIN_QUEST, YIELD0_NPCS |
| 11 | 11 | `Urban/no-day-but-today` | SECTION_MISSING_MAIN_QUEST, YIELD0_MAIN_QUEST, YIELD0_NPCS |
| 13 | 13 | `Urban/grind-city-prophets` | OVERVIEW_GENRE_LABEL, OVERVIEW_LEVEL_LABEL, OVERVIEW_TONE_LABEL, SECTION_MISSING_MAIN_QUEST, YIELD0_MAIN_QUEST, YIELD0_NPCS |
| 13 | 13 | `Urban/hip-hop-street-empire` | OVERVIEW_GENRE_LABEL, OVERVIEW_LEVEL_LABEL, OVERVIEW_TONE_LABEL, SECTION_MISSING_MAIN_QUEST, YIELD0_MAIN_QUEST, YIELD0_NPCS |
| 14 | 14 | `Sci-Fi/starfire-rebellion` | OVERVIEW_GENRE_LABEL, OVERVIEW_LEVEL_LABEL, OVERVIEW_TONE_LABEL, SECTION_MISSING_MAIN_QUEST, YIELD0_MAIN_QUEST, YIELD0_NPCS |
| 15 | 15 | `Urban/jazz-noir-city` | OVERVIEW_GENRE_LABEL, OVERVIEW_LEVEL_LABEL, OVERVIEW_TONE_LABEL, SECTION_MISSING_MAIN_QUEST, YIELD0_MAIN_QUEST, YIELD0_NPCS |
| 16 | 16 | `Sci-Fi/steam-war-chronicles` | OVERVIEW_GENRE_LABEL, OVERVIEW_LEVEL_LABEL, OVERVIEW_TONE_LABEL, SECTION_MISSING_MAIN_QUEST, YIELD0_MAIN_QUEST, YIELD0_NPCS |
| 16 | 16 | `Urban/the-dark-lords-day-job` | NOFILE_OVERVIEW, SECTION_MISSING_LOCATIONS, SECTION_MISSING_MAIN_QUEST, YIELD0_LOCATIONS, YIELD0_MAIN_QUEST |
| 17 | 17 | `Sci-Fi/street-samurai-legacy` | OVERVIEW_GENRE_LABEL, OVERVIEW_LEVEL_LABEL, OVERVIEW_TONE_LABEL, SECTION_MISSING_MAIN_QUEST, YIELD0_MAIN_QUEST, YIELD0_NPCS |
| 10 | 40 | `Adventure/ong-bak-sacred-guardian` | SECTION_MISSING_LOCATIONS, SECTION_MISSING_MAIN_QUEST, SECTION_MISSING_NPCS, YIELD0_LOCATIONS, YIELD0_MAIN_QUEST, YIELD0_NPCS |
| 10 | 40 | `Mystery/the-wires-game` | OVERVIEW_GENRE_LABEL, OVERVIEW_LEVEL_LABEL, OVERVIEW_TONE_LABEL, SECTION_MISSING_LOCATIONS, SECTION_MISSING_MAIN_QUEST, SECTION_MISSING_NPCS, YIELD0_LOCATIONS, YIELD0_MAIN_QUEST, YIELD0_NPCS |
| 31 | 47 | `Horror/the-timelords-companion` | SECTION_MISSING_LOCATIONS, YIELD0_LOCATIONS, YIELD0_NPCS |
| 62 | 62 | `Adventure/above-the-cloudline` | OVERVIEW_GENRE_LABEL, OVERVIEW_LEVEL_LABEL, OVERVIEW_TONE_LABEL, SECTION_MISSING_LOCATIONS, SECTION_MISSING_MAIN_QUEST, YIELD0_LOCATIONS, YIELD0_MAIN_QUEST |
| 57 | 87 | `Historical/way-of-the-fading-blade` | SECTION_MISSING_LOCATIONS, SECTION_MISSING_NPCS, YIELD0_LOCATIONS, YIELD0_NPCS |
| 110 | 171 | `Sci-Fi/wings-of-the-crows` | YIELD0_LOCATIONS |
| 74 | 185 | `Mystery/winters-ambassadors` | SECTION_MISSING_LOCATIONS, SECTION_MISSING_MAIN_QUEST, YIELD0_LOCATIONS, YIELD0_MAIN_QUEST |
| 196 | 196 | `Historical/the-silk-and-shadow-road` | NOFILE_CREATIVE_BRIEF, NOFILE_OVERVIEW, NOFILE_WORLD_BUILDING |
| 198 | 259 | `Historical/tides-of-fortune` | SECTION_MISSING_LOCATIONS, YIELD0_LOCATIONS |


---


## Two claims that need a database check before anyone acts

Rule zero: the database is the source of truth. Neither of these is confirmed.

1. **Academy of Arcane Gastronomy computes as 198 rows against a reported 188.** Two of the three live campaigns reproduce exactly (Abyssal Descent 206, The Eternal Feast 124), so the checker is faithful. The Academy gap is real arithmetic but an unknown cause. It could be a bible edit made after the re-ingestion.

2. **The Eternal Feast appears to be missing 80 rows it has always had in its bible** — 50 minor NPCs and 30 side quests, in tables whose name cells are not bold. This is a live campaign. If the database confirms zero `npc_tier2` rows for it, that is content the game has never been able to reach.

Both are answered by one dry run each on Hetzner:

```
bun run reingest -- --campaign academy-of-arcane-gastronomy --repo-path ../../../infinite-realms-clean
bun run reingest -- --campaign the-eternal-feast --repo-path ../../../infinite-realms-clean
```


---


## Housekeeping found along the way

- **15 campaign directories carry exFAT `._*` sidecar files.** `find campaign-ideas -name "._*" -delete`.
- **No ambiguous slugs.** Every campaign directory name is unique across genre folders, so `reingest --campaign <slug>` is safe today. Keep it that way.
- **`_to_delete/` holds 139 directories that the ingester would walk into.** It is excluded here by hand. Any tool that touches this tree must exclude it too, or a real run will ingest deleted campaigns.
- **10 campaigns have entity names over 60 characters**, where an extractor swallowed a sentence.
- **5 finished campaigns are missing a bible**, and 2 are missing another required file.

