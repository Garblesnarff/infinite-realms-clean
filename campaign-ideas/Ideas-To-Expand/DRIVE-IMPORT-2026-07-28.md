# Drive Idea Import — Original Concepts Not Yet in the Library

**Source:** Google Drive, `Campaign Ideas - Full` spreadsheet and `campaign ideas - first run`.
**Imported:** 2026-07-28.
**Why these matter:** the library's problem is not volume, it is originality. 206 of
305 bibles are template clones and 13 carry third-party pastiche. Everything below
is an original premise with no Wizards and no third-party IP attached.

Cross-checked against all 820 campaign directories. **195 of 198 ideas are unused.**

| Source | Ideas | Already used |
|---|---:|---:|
| `Campaign Ideas - Full` (spreadsheet, 4 blocks of 20) | 80 | 0 |
| `campaign ideas - first run` (tiered doc) | 118 | 3 |

The three already used: The Unwritten War, The Unwritten World, The Chronomancer's
Debt (as `the-chronomancers-gambit`).

---

## Priority A — fills a genre with zero shippable campaigns

Sci-Fi, Post-Apocalyptic, Intrigue and Urban currently have **no** campaign with
authored depth. These ten fill all four. Each already carries a logline, tone,
core concept, locus, sensory anchor and an expansion hook, which is more than most
framework packages in the repo have.

### Sci-Fi

**The Color from Between** — *Tier S*
A new, indescribable colour from a crashed meteor is rewriting life into alien
forms. The party enters a quarantined village to find a missing scholar amidst the
transfigured but placid townsfolk.
Tone: hypnotic, body horror. Core concept: reality infected by alien physics.
Locus: the crystalline meteor. Verbs: contain, research, purge.
Hook: the colour is the sensory organ of a dimension-bleeding intelligence.

### Urban

**The Hour of Rust** — *Tier A*
In the city of Cogsworth, decay accelerates until metal rusts in minutes. The party
must reach the Clockwork Core, which now ticks backwards, before the city collapses.
Tone: frantic, tense. Core concept: entropy weaponised and localised.
Hook: the rust is a temporal disease now reaching living things.

**The Symbiotic City** — *Tier A*
A fleshy architectural fungus is reshaping the slums and bonding with residents. The
party must retrieve a noble's scion, now a willing leader of the new gestalt.
Tone: grotesque, alluring. Core concept: parasitic hive-mind architecture.
Hook: the fungus is terraforming the region to match its home dimension.

**The Masquerade of Faces** — *Tier B*
Nobody in the city can recognise faces any more, seeing only shifting masks. The
immune party infiltrates the Mask-Maker's Guild, whose leader now controls identity.
Tone: paranoid, intriguing. Core concept: identity as a removable object.
Hook: the masks are the true faces of Fey who swapped places with the populace.

### Intrigue

**The Consensus Engine** — *Tier S*
Magic now works only for those connected to a device enforcing one version of
reality. The party, users of old magic, are relics of a reality voted out of
existence.
Tone: conspiratorial, defiant. Core concept: reality is a democracy.
Hook: the Engine is failing, bleeding through dozens of failed realities.

**The Map that Eats the World** — *Tier A*
A perfect map of the kingdom is found, and damage to the map damages the real place.
A saboteur tears off a corner, destroying a port city during the party's first watch.
Tone: high-stakes, paranoid. Core concept: the representation is the reality.
Hook: the map is charting lands beyond the border, threatening to create them.

**The Memory Garden** — *Tier A*
Flowers have bloomed that hold tangible memories. The party is sent after the King's
spymaster is found catatonic, his secrets blooming for anyone to pluck.
Tone: nostalgic, dangerous. Core concept: memory as a physical commodity.
Hook: someone has learned to plant false memories and rewrite histories.

**The Tyranny of Dreams** — *Tier B*
Everyone in a barony dreamt the same obsidian citadel, and now it is physically real.
The party enters the shared dreamscape to dethrone the Dream Monarch who rules by night.
Tone: surreal, oppressive. Core concept: a dream conquering waking reality.
Hook: the Monarch is the suppressed subconscious of a comatose child.

### Post-Apocalyptic

**The Appetites of the Road** — *Tier C*
A stretch of highway has turned sentient and predatory, rearranging itself to trap
and digest travellers' belongings. The party escorts a caravan and finds the road
gone behind them.
Tone: unsettling, disorienting. Core concept: predatory sentient geography.
Hook: the road is one tendril of a continent-spanning entity now waking.

**The Salt Perpetual** — *Tier C*
In Brinehollow, water can no longer evaporate and the town is drowning slowly. The
party investigates a lighthouse projecting a beam of damp darkness.
Tone: gloomy, damp. Core concept: a broken physical process.
Hook: the keeper bargained with an elemental power to make the region its home.

---

## Priority B — strongest remaining concepts

Genre-flexible, all Tier S or A, all original:

| Idea | Tier | Core concept |
|---|---|---|
| The Cacophony of Stillness | S | Sound as a finite resource; new sound is only born in living lungs |
| The Theorem of Flesh | S | A mathematical, viral god; comprehension is the infection vector |
| The Gravity Well of Regret | S | Emotional weight is literal gravity |
| The Grammar of Creation | B | A language that creates objects but erases a concept per use |
| The Lie of Gravity | A | Gravity as a belief system; a monastery floats a mile up |
| The Chronal Mire | B | Time as a physical landscape in an unstable swamp |
| The Law of Averages | A | Narrative causality fraying; heroism becoming statistically impossible |
| The World in the Painting | B | A painting of a duchy becoming more real than the duchy |
| The Echoes of a Dead Language | C | Hieroglyphs that imprint a dead person's skills and personality |

---

## Priority C — the stranded package

**The Godskin Atlas** sits complete on the unmerged branch
`origin/agent/add-godskin-atlas-campaign-package`: four files, 55 KB, no Product
Identity names, no trademark references, and a genuinely original bestiary
(Gilded Phagocyte, Scar Shepherd, Pore Hound, Nerve Kite).

It cannot ship as-is. **The bestiary is prose only — no HP, AC or CR anywhere**, so
the chunker extracts zero monsters. It needs stats authored, not reformatted.

Decision needed: author the stats and merge, or drop the branch.

---

## What is not worth taking

- **The `Stories` folder** is a 2024 book-generator experiment — chapter drafts,
  crew code dumps, Colab notebooks. Prose fiction, not campaign material.
- **`Story Idea Generation`** (Macabre Monday, Sci-Fi Saturday and so on) is horror
  YouTube channel prompts. Different product.
- **The other two blocks of 20** in the spreadsheet are title-and-tone only, with no
  logline. They read as generated variations on one sensory gimmick — scent, echo,
  flavour, texture, silence repeated across many entries. Low value; the same
  template problem that produced the 114 clones.

---

## Caution

`campaign ideas - first run` contains at least one Wizards item reference: *The City
Ruled by Whim* is built on a Deck of Many Things. Rename it before expanding —
the deck is not open content.

Apply `tools/launch-readiness/BIBLE-GENERATION-SPEC.md` to anything expanded from
this file, so new bibles arrive parser-ready instead of needing another repair pass.
