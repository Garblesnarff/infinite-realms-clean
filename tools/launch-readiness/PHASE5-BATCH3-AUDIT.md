# Batch 3 — Shortlist Audit (Ten Candidates)

**Branch:** `content/launch-ten-readiness`
**Date:** 2026-07-28
**Scope:** Audit only. No campaign content was rewritten. Every finding below is a
recommendation for the product owner.
**Method:** `coverage_report.py` + the verified `irparse` port for mechanics;
manual read of every overview, creative brief, world-building spec and bible
opening for everything else.

---

## 0. Headline

**Mechanically, all ten are perfect. Editorially, six of the ten are other
people's intellectual property reproduced with the character names intact.**

The depth scorer ranked eight of these ten in the library's top eleven, with
`pi: []` and `pastiche: []` on every one. That is correct as far as the scorer
goes and useless as a launch gate. Its `PASTICHE` dictionary knows about Demon
Slayer, Cowboy Bebop and Tolkien. It does not know about Doc Savage, Tarzan,
Initial D, Trails in the Sky, Into the Woods, The Da Vinci Code or True
Detective — which is what these ten actually are.

| Verdict | Count | Campaigns |
|---------|------:|-----------|
| **Ship** | 2 | journey-to-the-inner-world, curse-of-the-jersey-devil |
| **Ship after edits** | 2 | tides-of-the-trident-throne, careful-what-you-wish |
| **Salvage the bible, bin the package** | 3 | lord-of-the-jungle, man-of-bronze, mountain-pass-legends |
| **Drop** | 3 | bracers-of-liberl, symbols-of-the-divine, sins-of-the-city |

---

## 1. Parser coverage

Verified two ways: `python3 tools/launch-readiness/coverage_report.py`, and
directly against the verified port
(`sys.path.insert(0,'tools/launch-readiness'); import irparse; irparse.coverage(text)`).
Both agree exactly.

| Campaign | Monsters extracted | Grading FULL | Bible KB |
|----------|-------------------:|-------------:|---------:|
| lord-of-the-jungle | 10 | 10 (100%) | 54.6 |
| journey-to-the-inner-world | 10 | 10 (100%) | 53.3 |
| man-of-bronze | 10 | 10 (100%) | 53.3 |
| mountain-pass-legends | 10 | 10 (100%) | 52.9 |
| bracers-of-liberl | 10 | 10 (100%) | 51.6 |
| symbols-of-the-divine | 10 | 10 (100%) | 51.2 |
| sins-of-the-city | 10 | 10 (100%) | 50.8 |
| careful-what-you-wish | 10 | 10 (100%) | 50.6 |
| curse-of-the-jersey-devil | 10 | 10 (100%) | 50.5 |
| tides-of-the-trident-throne | 10 | 10 (100%) | 27.4 |

**100/100 FULL.** No stat blocks are missing HP or AC. No normalization needed
on any of the ten — the Phase 4 sweep already did the work.

Two mechanical notes:

- `parse_stat_block` returns `challengeRating: None` for **all 100** blocks
  across all ten. CR is carried in the `### N. Name (CR x)` header and in the
  body prose, but not in a labelled field the parser reads. This is a
  **parser-side** gap, not a content gap — it is identical on batch 1 and 2 —
  but if production ever uses CR for encounter budgeting, it is reading nothing.
- `tides-of-the-trident-throne` is half the length of the others (27.4 KB vs
  ~52 KB) and its session outline is one-line stubs where the others are full
  paragraphs. It is a different, thinner generation tier. It parses fine; it is
  less content for the same shelf price.

---

## 2. Package completeness

All ten have overview + creative-brief + world-building-spec + campaign-bible in
one directory, and all ten carry the full twelve-tag bible structure.

| Campaign | Overview | Brief | World-building | Bible | Notes |
|----------|:--------:|:-----:|:--------------:|:-----:|-------|
| lord-of-the-jungle | ✓ | ✓ | ✓ | ✓ | |
| journey-to-the-inner-world | ✓ | ✓ | ✓ | ✓ | |
| man-of-bronze | ✓ | ✓ | ✓ | ✓ | |
| mountain-pass-legends | ✓ | ✓ | ✓ | ✓ | |
| bracers-of-liberl | ✓ | ✓ | ✓ | ✓ | |
| symbols-of-the-divine | ✓ | ✓ | ✓ | ✓ | |
| sins-of-the-city | ✓ | ✓ | ✓ | ✓ | |
| careful-what-you-wish | ✓ | ✓ | ✓ | ✓ | **no `[TAG: ENCOUNTER_TABLE]`** |
| curse-of-the-jersey-devil | ✓ | ✓ | ✓ | ✓ | |
| tides-of-the-trident-throne | ✓ | ✓ | ✓ | ✓ | **bible filename is `tide-…`, slug is `tides-…`** |

No image references (`![…]`, `.png`, `.jpg`) anywhere in the ten, so no broken
asset paths. No in-repo art under `campaign-assets/` for any of them.

### The completeness check is hiding the real problem

"Four files present" is passing these packages when **six of the ten contain two
different campaigns**. The bible is one story; the overview, brief and
world-building spec are a *different* story, lifted from a film, novel, anime or
game. A subscriber reading the storefront blurb and then playing session 1 would
be playing something else entirely.

| Campaign | Overview / brief / spec are… | Bible is… | Coherent? |
|----------|------------------------------|-----------|:---------:|
| lord-of-the-jungle | Tarzan (ERB) | *Veridia*, a sentient continent-jungle choosing a new avatar | ✗ |
| man-of-bronze | Doc Savage | *Arion and the Fulcrum*, Logic vs Instinct made flesh | ✗ |
| mountain-pass-legends | Initial D | *Janus and Terminus*, gods of Passage and Walls; tolls paid in memory | ✗ |
| careful-what-you-wish | Into the Woods | *The Law of Narrative Conservation*, wishes as cosmic accounting | ✗ |
| symbols-of-the-divine | The Da Vinci Code | Cosmic Glyph dreaming reality | ✗ |
| sins-of-the-city | True Detective S1 | Urban God dreaming reality | ✗ |
| bracers-of-liberl | Trails in the Sky | **also** Trails in the Sky | ✓ (badly) |
| journey-to-the-inner-world | generic hollow-earth | Great Wyrm / Shell / Yolk | ✓ |
| curse-of-the-jersey-devil | Jersey Devil folklore | Pine Barrens as psychic wound | ✓ |
| tides-of-the-trident-throne | Atlantean succession crisis | same | ✓ |

**The bibles are the good half.** In five cases the bible is genuinely original,
well-structured, ten authored monsters deep — and is being marketed as a
knock-off of something else. That is a fixable problem, and it is the single
highest-value piece of work available in this batch.

---

## 3. Legal — Wizards Product Identity and trademarks

### Clean on the explicit list

Scanned all ten packages for: beholder, spectator, death tyrant, mind flayer,
illithid, githyanki, githzerai, yuan-ti, kuo-toa, slaad, umber hulk, displacer
beast, carrion crawler, modron, intellect devourer, flumph, froghemoth.

**One hit, a false positive:**
`mountain-pass-legends/world-building-spec.md:26` — `"Racing Spectator"
(mountain culture participants)`. Ordinary English. Leave it.

Also scanned for waterdeep, ravenloft, strahd, planescape, sigil, eberron,
spelljammer, dark sun, undermountain, zariel, vecna, D&D, Dungeons & Dragons,
DnD, Forgotten Realms, Faerûn, Asmodeus, Elminster, Icewind Dale, Red Wizards,
Menzoberranzan, Tiamat, Mordenkainen, Bigby, Tasha. **Zero hits across all ten.**
This is the cleanest batch yet on the trademark sweep.

### Three PI creatures the scorer's list does not cover

The `PI` list in `depth_score.py` is sixteen names. These three are not on it,
are not in SRD 5.1 to my knowledge, and are in the batch:

| Term | Campaign | Hits | Note |
|------|----------|-----:|------|
| **Myconid** | journey-to-the-inner-world | 16 | An entire faction — "The Myconid Sovereignty" — plus 5 NPCs, a location, a quest, and a stat block reading `(CR 6). Myconid.` |
| **Myconid** | lord-of-the-jungle | 2 | NPC "Spore-Tech Gix (Myconid Artificer)" + a stat block |
| **Warforged** | man-of-bronze | 1 | "The Prime Calculator (Warforged Wizard)" — Eberron PI |
| **duergar** | tides-of-the-trident-throne | 1 | world-building-spec population line |

`drider`, `blink dog`, `rakshasa`, `otyugh`, `owlbear`, `drow`, `sahuagin`,
`aboleth`, `mimic`, `tiefling`, `dragonborn` are all fine (SRD 5.1) and appear
in this batch without concern.

**Recommendation:** get these three verified against SRD 5.1 and add whatever
survives to the `PI` list in `depth_score.py`. Myconid in particular is a
whole-faction rename in journey-to-the-inner-world — the campaign I am otherwise
recommending for launch. It is a straight find-and-replace ("Sporefolk
Concordance" or similar), roughly twenty lines.

---

## 4. Third-party pastiche — the actual failure mode

This is where the batch falls apart. These are not "inspired by". In every case
below the package reproduces the source's **named characters**.

### 4.1 `lord-of-the-jungle` — Tarzan (Edgar Rice Burroughs)

You asked me to check this one specifically. It is true, and it is worse than a
pastiche.

Named in the overview and the world-building spec:

> **Korak the Jungle Lord**, **Jane Porter**, **Professor Archimedes Porter**,
> **La of Opar**, the **Lost City of Opar**, the **Temple of the Flaming God**,
> **Captain Clayton**, **Chief Mbonga**, **Rokoff** the ivory hunter, the
> Elephant Graveyard, degenerate Atlantean descendants.

Every one of those is Burroughs. Korak is Tarzan's son (*The Son of Tarzan*,
1915); La and Opar are from *The Return of Tarzan* (1913); Rokoff is Nikolas
Rokoff, ERB's recurring villain; Clayton is Tarzan's own family name; Mbonga is
the chief from *Tarzan of the Apes*. The early novels are US public domain, but
Edgar Rice Burroughs, Inc. holds and actively enforces trademarks on **Tarzan**,
**Korak**, **Opar**, **La of Opar**, and — note the campaign title —
**"Lord of the Jungle"** is itself an ERB registered mark.

Separately: the overview's framing ("colonial Africa", "primitive peoples",
"noble savagery", "tribal peoples in authentic traditional garb") is a
content-sensitivity problem independent of the legal one, and would be a poor
look on a storefront in 2026.

**The bible is not Tarzan at all** and is excellent — Veridia, a
continent-spanning sentient plant whose animals are its antibodies, holding a
brutal audition for its next avatar because the current one is dying and the
jungle is infected with a crystalline blight.

**Verdict: bin the overview, brief and spec. Keep the bible. Relaunch under a
new title.**

### 4.2 `man-of-bronze` — Doc Savage

Also true, also verbatim. Named in the overview and world-building spec:

> **Doc Savage (Clark Savage Jr.)**, **The Fabulous Five**, **Monk Mayfair**,
> **Ham Brooks**, **Long Tom Roberts**, **Renny Renwick** ("Holy cow!"),
> **Johnny Littlejohn**, **John Sunlight**, **Patricia Savage**, the
> **Fortress of Solitude**, the **86th Floor Headquarters**, plus three actual
> Doc Savage novel titles used as act names — *Land of Terror*, *The Phantom
> City*, *The Devil Genghis*.

"Doc Savage" and "Man of Bronze" are live trademarks (Condé Nast / licensees).
"Fortress of Solitude" is separately associated with DC. Renny's catchphrase and
the reform-by-brain-surgery premise are lifted straight from the pulps.

**The bible is not Doc Savage at all** — it is Arion, the vanished Man of Bronze,
and the Fulcrum between the Architect (logic) and the Beast (instinct).
Original, and good.

**Verdict: same as above. Bin three files, keep the bible, retitle.**

### 4.3 `mountain-pass-legends` — Initial D

> **Gunma**, **Mount Akina**, **Mount Akagi**, **Myogi**, **Usui**, tofu
> delivery, the **Red Suns**, **Akina Speed Stars**, **Night Kids**, **Emperor**,
> **Impact Blue**, the **"White Comet of Akagi"**, **Takeshi**, **Keisuke**,
> **Mako**, gutter running, inertia drift, blind attacks, the AE86 and RX-7 in
> the art brief, and `## Art Style: Anime Racing Realism (Initial D-inspired)`
> stated outright.

Beyond the IP: this is a **modern Japanese street-racing campaign** filed under
Adventure in a 5E-compatible fantasy library, with a bestiary of wisps, golems
and wraiths that has nothing to do with cars.

The bible is a completely unrelated and rather beautiful original: Janus, God of
Passage, and Terminus, God of Walls; travellers pay a toll in memory to cross;
the discarded tolls have become sentient "Legends" that hunt the pass. One stray
flag inside it — **"The Ragged Flagon Tavern"** is a Skyrim (Bethesda) location
name and should be changed.

**Verdict: bin the overview, brief and spec. Keep the bible. This is a strong
Adventure campaign wearing someone else's jacket.**

### 4.4 `bracers-of-liberl` — Trails in the Sky (Nihon Falcom)

The worst of the six, because unlike the others **the bible is IP too**. There
is nothing to salvage.

> **Liberl**, **Zemuria**, **Bracers** / the **Bracer Guild**, **Orbments** /
> **Orbal** energy / **Septium**, **Ouroboros**, **Enforcers**, the
> **Grandmaster**, the **Gospel Plan**, **Sept-Terrion**, the **Aureole**,
> **Professor Epstein**, the **Septian Church**, **Jaeger** mercenaries, the
> **Erebonian Empire**, the floating city **Glorious**, and the towns
> **Rolent**, **Bose**, **Ruan**, **Zeiss**, **Grancel** — every real Liberl
> region in order.

Named characters: **Cassius Bright**, **Schera** (the overview literally says
"Estelle archetype"), **Joshua** (former Ouroboros child assassin), **Olivier
Lenheim** (secret prince of the neighbouring empire), **Colonel Richard**,
**Professor Alba**. Mechanics: **Orbment/Quartz crafting**, the **S-Break**
system, **Bracer Points**. The creative brief names the game.

That is the entire plot of *Trails in the Sky FC/SC* with no filing off. Falcom
is a live rights holder. There is no rename that fixes this, because after you
rename everything there is no campaign left.

**Verdict: drop from the batch and shelf the package.**

### 4.5 `symbols-of-the-divine` — The Da Vinci Code (Dan Brown)

> **Robert Langdon**, **Sophie Neveu**, **Jacques Saunière**, **Leigh Teabing**,
> **Bishop Aringarosa**, **Silas**, **Bezu Fache**, **André Vernet**, **Rémy
> Jean**, **Sister Sandrine** — the complete cast, unchanged.
>
> Plus: the **Louvre**, the **Priory of Sion**, **Opus Dei**, the **Knights
> Templar**, the **Rose Line**, *sang real*, **Vitruvian Man**, **Rosslyn
> Chapel**, **Mary Magdalene's tomb**.

The world-building spec instructs the generator to write "the Divine Figure's
true history (**fantasy equivalent of Jesus**)". The creative brief asks the art
model for "**Tom Hanks's** intelligent everyman quality". Several nouns have the
word "equivalent" appended — *"Opus Dei equivalent"*, *"the Louvre equivalent"* —
which is not a rename, it is a confession.

**Verdict: drop. If the concept is wanted, it needs writing from scratch.**

### 4.6 `sins-of-the-city` — True Detective S1 (HBO)

The single worst legal item in the batch, because it names living actors.

> Overview tagline: *"Time is a flat circle. We've done this before. We'll do it
> again."* — Rust Cohle's line, verbatim.
>
> Characters: **Rust** Blackburn, **Martin** Redwood, **Reggie Ledoux**,
> Sheriff **Billy Tuttle**, Reverend Theodore **Childress**, **Errol
> Childress**, **Maggie Hart**, the **Yellow King**, **Carcosa**.
>
> Locations: Ledoux's meth lab, the Tuttle compound, Errol's fortress, Bayou
> Parish.
>
> Creative brief: *"**Reference:** Matthew McConaughey's Rust Cohle, True
> Detective"*; *"**Reference:** Woody Harrelson's Marty Hart"*; *"**Reference:**
> Charles Halford's Ledoux"*; *"**Reference:** Glenn Fleshler's Errol"*;
> *"Reference: T Bone Burnett's True Detective score, 'Far From Any Road'"*.
> Also the opening victim posed with antlers in a cypress grove, and Errol's
> "This is Carcosa" mantra.

Four named actors and their roles, in a shipping asset-generation brief.
**Verdict: drop.**

### 4.7 `careful-what-you-wish` — Into the Woods (Sondheim & Lapine)

The Grimm source tales are public domain. The **combination** is not.

> **The Baker and His Wife**, the **Witch's curse for the father's theft**, the
> **Giant's Widow** descending for revenge, **Cinderella's unfaithful prince**,
> the **Two Princes** (the "Agony" pair), **Little Red** traumatized after the
> wolf, **Jack** who does not understand consequences, the **Mysterious Man**,
> the **Narrator**, the **Steward**, the Woods.
>
> Structure: everyone gets their wish by the midpoint, then the consequences and
> the Giant. That is Act I / Act II of the musical, exactly.

The Baker, the Baker's Wife, the Mysterious Man, the Narrator, the Steward and
the Giant's Widow are Lapine's inventions, in copyright until the 2080s. The
creative brief names the musical.

**The bible is original and strong** — the Law of Narrative Conservation, wishes
as a loophole in cosmic bookkeeping, the Court of Consequences, a kingdom
wished into permanent hollow happiness. The bestiary is genuinely inventive
("A Legal Precedent", "A Blank Page", "A Cautionary Tale", The Cosmic
Accountant).

**Verdict: keep the campaign, rewrite the overview/brief/spec off the bible.**
The Grimm characters can stay if the Lapine-specific ones go; this is the
lightest lift of the six.

### 4.8 `tides-of-the-trident-throne` — moderate flag only

Atlantis is Plato's; tritons, merfolk, sahuagin, dragonborn and kraken are SRD.
No named characters from anything. But:

- The creative brief lists `**Inspiration**: Aquaman, Game of Thrones, Lord of
  the Rings underwater` and `Visual: Aquaman (2018)`, `Audio: Game of Thrones
  OST, Lord of the Rings OST, Pirates of the Caribbean`.
- The overview's themes section says `**Political Intrigue:** Game of Thrones
  beneath the waves`.
- "Seven Kingdoms" + trident + Atlantean succession + surface-vs-deep is
  uncomfortably close to the 2018 Aquaman film's structure.

These are comp titles in an internal brief, not lifted characters. **Strip the
named comps from anything customer-facing, rename "the Seven Kingdoms" to
something else, and it ships.**

### 4.9 `journey-to-the-inner-world` and `curse-of-the-jersey-devil` — clean

- **journey-to-the-inner-world**: hollow-earth exploration. Verne's *Journey to
  the Center of the Earth* (1864) is public domain and no character or place
  name is borrowed from it — the brief cites it as an art comp alongside Avatar
  and Subnautica, which is normal. The bible (Great Wyrm, Shell, Yolk, Core,
  Progenitors) is entirely original. **Only issue is the Myconid rename.**
- **curse-of-the-jersey-devil**: the Jersey Devil, Mother Leeds, the thirteenth
  child and Leeds Point are genuine 18th-century American folklore with no
  rights holder. The Pine Barrens is a real place. The bible's reading of the
  Devil as a psychic wound made of un-said things is original. **Clean.**

---

## 5. Template cloning the scorer missed

`sins-of-the-city` and `symbols-of-the-divine` **share a single bible** with a
find-and-replace applied. Identical stat signature across all ten monsters
(40/13, 40/16, 60/14, 70/15, 80/16, 90/17, 110/18, 140/17, 150/18, 200/18),
428 vs 427 lines, and normalising City↔Symbol and Dream↔Meaning collapses most
of the document to zero diff:

| sins-of-the-city | symbols-of-the-divine |
|------------------|-----------------------|
| Whispering Streets Drone | Whispering Texts Drone |
| Architect of the Dream | Architect of Meaning |
| Urban God (Dream-Avatar) | Cosmic Glyph (Meaning-Avatar) |
| The City's Voice | The Symbol's Voice |
| The City Guard | The Sacred Guard |
| The Somnambulist / Professor Anya Sharma / the Debug-Master | *identical* |

The scorer reported `clone_peers: 1` for each and still scored them 97.4 and
97.6 — one clone peer is not enough signal to sink a campaign, but two campaigns
in the *same shortlist* sharing one bible is a storefront embarrassment.

`curse-of-the-jersey-devil` is a lighter third member of the same family: same
session-1 skeleton (missing person → minor manifestation attacks → investigate
the family → recover a lost object), same session-2 line verbatim ("A
terrifying, psychological battle against a creature that is a reflection of
themselves"), same Reality-Glitcher faction, same Professor Anya Sharma NPC. It
diverges enough after that to stand alone, and the Jersey Devil material is
genuinely its own — but **do not ship it in the same batch as either of the
other two.**

`Professor Anya Sharma` also appears in `man-of-bronze` and (outside the batch)
`rank-and-deception`. It is a shared NPC name pool, not a clone in those cases.

---

## 6. Opening runnability — cold read

Judged on: does a trial player get a **place**, a **situation**, and a **reason
to act** in the first ten minutes? Where the overview and the bible disagree
(see §2), both are judged.

| Campaign | Rating | Why |
|----------|--------|-----|
| curse-of-the-jersey-devil | **Strong** | Named place (Pine Barrens), hired to investigate livestock killings, witnesses describe the creature, tracks lead to Leeds properties, a child goes missing. Place, situation and reason all land cold. |
| tides-of-the-trident-throne | **Strong** | The High King is assassinated in front of you at the Coral Summit and deputises you with his dying breath. Impossible to fumble. Bible version is terse but identical. |
| journey-to-the-inner-world | **Strong** | Two good openings that agree: hired to find a vanished explorer, cave-in forces you forward (overview); or the quake opens the Great Chasm in your town and you dig survivors out (bible). Either works. |
| bracers-of-liberl | **Strong** *(unusable)* | Guild exam, then "find my lost cat" — and the cat has been eaten by the thing you now have to fight. Textbook onboarding. Wasted on a package that cannot ship. |
| careful-what-you-wish | **Adequate–strong** | Superb image — a town festival where every laugh sounds like weeping, and a sentient "Bad Joke" attacks. Loses a point for an unnamed town and no stated reason you're there. |
| lord-of-the-jungle | **Adequate** | Bible: your transport crashes at the jungle's edge, hostile wildlife immediately. Fine, but "airship/boat/caravan" is an unresolved GM choice at the single most important moment, and the overview's opening is a *different* scene from a different campaign. |
| man-of-bronze | **Adequate** | Bible: a city street turns into jungle for sixty seconds and something half-machine half-beast comes out of it. Strong image, but the party has no reason to act beyond proximity, and the payoff (a Patron recruits you) is deferred to session 2. |
| mountain-pass-legends | **Adequate** *(bible)* | Arrive at the pass, negotiate the Toll-Takers, brawl in a tavern, pay a memory. Concrete, but never says why you are crossing. The overview's opening (pre-dawn tofu run, a Red Suns scout passes you on the downhill) is **strong** — and is Initial D. |
| symbols-of-the-divine | **Weak** | *"The players are in a town where a loved one has gone missing."* No named town, no named person, no named relationship, then a generic drone attacks. Nothing for a cold player to hold. The overview opening (Louvre murder) is strong and is Dan Brown's. |
| sins-of-the-city | **Weak** | Byte-identical to the above. The overview opening (Amaryllis Devereaux posed with antlers in a cypress grove) is very strong and is True Detective's. |

---

## 7. Genre spread

Batch 3 as shortlisted covers **5 of 9**: Adventure ×4, Fantasy ×2, Mystery ×2,
Horror ×1, Historical ×1.

**Missing: Sci-Fi, Intrigue, Urban, Post-Apocalyptic.**

After the recommended drops it is worse — Adventure ×1, Fantasy ×1, Horror ×1,
Historical ×1, **4 of 9**, with three more campaigns pending a rewrite before
they can be counted.

Running totals across all three batches, if batch 3 ships as recommended:

| Genre | B1 | B2 | B3 (recommended) | Total |
|-------|---:|---:|-----------------:|------:|
| Fantasy | 1 | 2 | 1 | 4 |
| Adventure | 1 | 2 | 1 | 4 |
| Horror | 2 | 1 | 1 | 4 |
| Mystery | 1 | 1 | 0 | 2 |
| Historical | 1 | 1 | 1 | 3 |
| Intrigue | 2 | 1 | 0 | 3 |
| Urban | 1 | 1 | 0 | 2 |
| Sci-Fi | 1 | 1 | 0 | 2 |
| **Post-Apocalyptic** | **0** | **0** | **0** | **0** |

Post-Apocalyptic has now been empty for three batches. The scorer's best
Post-Apoc candidate is `after-the-starfall` at 36.0 — a three-monster template
clone. **There is no shippable Post-Apocalyptic campaign in this library.** It
has to be authored, not selected.

### Backfill candidates (not audited beyond a premise read — treat as leads)

| Genre | Candidate | Score | Caution |
|-------|-----------|------:|---------|
| Intrigue | `the-seekers-trial` | 87.7 | 10 monsters, complete, no obvious source. Shares "The Somnambulist" NPC name with the sins/symbols cluster — check for template overlap first. |
| Urban | `the-coffee-and-tragedy` | 77.9 | Only 9 monsters, 23.8 KB bible. Thin but original-looking. |
| Adventure | `gold-and-vengeance` | 97.3 | Highest unshipped score in the library. Revenge heist. Reads original. |
| Historical | `arc-of-orleans` | 90.4 | Joan of Arc. Historical figure, public domain. |
| Fantasy | `breath-of-the-wilds` | 96.0 | Title is Zelda-adjacent; verify the interior before committing. |
| Sci-Fi | — | — | **Nothing above 35.6.** Every Sci-Fi package is a three-monster clone. |

**Do not shortcut these onto the shelf on score alone.** Names already visible in
the top-40 that will not survive a read: `brick-by-brick` (LEGO — minifigures,
Master Builder, all live trademarks, and LEGO litigates), `cloverfield-emergence`
(Paramount), `ghost-who-walks` (The Phantom, King Features), `beast-of-skull-isle`
(King Kong), `just-one-more-thing` (Columbo), `project-mayhem-rising` (Fight
Club), `aldnoah-drive-conspiracy` (Aldnoah.Zero), `breath-of-the-slayer-corps`
(Demon Slayer — the scorer does catch this one), `arkham-investigations`
(Lovecraft is PD; "Arkham" is also a DC mark).

---

## 8. Recommended batch 3

### Ship now (2)

| Campaign | Genre | Work required |
|----------|-------|---------------|
| `curse-of-the-jersey-devil` | Horror | None. Ship as is. |
| `journey-to-the-inner-world` | Adventure | Rename **Myconid** → original term (1 faction, 5 NPCs, 1 location, 1 quest, 1 stat block, ~20 lines). Pending SRD verification. |

### Ship after light edits (2)

| Campaign | Genre | Work required |
|----------|-------|---------------|
| `tides-of-the-trident-throne` | Historical | Strip "Aquaman / Game of Thrones / Pirates of the Caribbean" from the brief and the overview themes; rename "the Seven Kingdoms"; rename **duergar**; rename the bible file `tide-…` → `tides-…`. Accept that it is a thinner package (27 KB) than the rest of the shelf. |
| `careful-what-you-wish` | Fantasy | Rewrite overview + brief + world-building spec from the bible's own material. Remove the Baker and His Wife, the Giant's Widow, the Two Princes, the Mysterious Man, the Narrator, the Steward, and the "Into the Woods" citation. Grimm characters may stay. Add an `[TAG: ENCOUNTER_TABLE]` section. Bible is untouched. |

### Salvage — bible is good, package is not (3)

Each needs the overview, creative brief and world-building spec **rewritten from
the bible**, and a new title. This is roughly a day of authoring each and yields
three genuinely original campaigns.

| Campaign | Working title suggestion | Bible premise |
|----------|--------------------------|---------------|
| `lord-of-the-jungle` | *The Gardener's Audition* | Veridia, a sentient continent-jungle whose dying avatar has triggered a brutal succession; a crystalline blight is driving its antibodies mad. Also rename **Myconid**. |
| `man-of-bronze` | *The Fulcrum* | The Architect (logic) and the Beast (instinct); the last living balance-point vanished a decade ago and the world is tipping. |
| `mountain-pass-legends` | *The Toll of Passage* | Janus, God of Passage, vs Terminus, God of Walls. Cross the pass by paying a memory; the discarded memories have become predators. Also rename **the Ragged Flagon**. |

### Drop (3)

| Campaign | Reason |
|----------|--------|
| `bracers-of-liberl` | *Trails in the Sky* reproduced in full — setting, plot, named characters, mechanics — in **all four files**, bible included. Nothing to salvage. |
| `symbols-of-the-divine` | *The Da Vinci Code* with the complete cast list intact and the word "equivalent" appended to a few nouns. Bible is a clone of sins-of-the-city. |
| `sins-of-the-city` | *True Detective S1* with character names unchanged, a quoted line as the tagline, and four named actors cited in a shipping asset brief. Bible is a clone of symbols-of-the-divine. |

**Net: 4 launch-ready after edits, 3 salvageable with authoring, 3 dropped.**
This does not fill a batch of ten. Batch 3 should either ship short at four, or
four fresh candidates should be selected and audited to this standard before the
batch closes.

---

## 9. Remaining for the product owner

1. **Legal call on Myconid, Warforged and duergar.** Not on the current PI list;
   I believe all three are absent from SRD 5.1. Myconid gates
   `journey-to-the-inner-world`, which is otherwise the cleanest campaign here.
2. **Decide on the three salvage packages.** Rewriting three overviews yields
   three original campaigns from bibles that already exist and already parse.
   The alternative is shelving 160 KB of good writing because of the marketing
   copy wrapped around it.
3. **Batch 1 and 2 need a re-audit under this standard.** The batch-2 report
   already flagged Cowboy Bebop, Buffy, The Last Samurai, Hamilton and Twisted
   Metal as "commercial risk, not auto-rewritten" and shipped them anyway. Given
   what this audit found — actors named in briefs, character rosters copied
   whole — that decision deserves revisiting. `see-you-space-cowboy` in
   particular ships with a ship named *Bebop*.
4. **Teach the scorer this failure mode, or accept it cannot learn it.** Adding
   Doc Savage, Tarzan, Initial D, Trails in the Sky, Into the Woods, Da Vinci
   Code and True Detective to `PASTICHE` catches these seven and nothing else.
   The general signal is cheaper and more reliable: **flag any package whose
   creative brief contains "Inspired by *Title*", "Reference: <Actor>" or
   "-inspired", and any world-building spec whose Tier 1 NPC roster is a list of
   proper names that do not appear in the bible.** Every one of the six offenders
   in this batch trips both.
5. **Add a coherence check to the completeness gate.** "Four files present" is
   currently passing packages that contain two unrelated campaigns. Comparing the
   overview's Tier 1 NPC names against the bible's `[TAG: INDEX_KEYWORDS]` line
   would have caught six of these ten automatically.
6. **CR is not being parsed.** All 100 blocks in this batch return
   `challengeRating: None`. Content has the CR in the header; the parser reads
   only labelled fields. Worth a look if production budgets encounters by CR.
7. **Post-Apocalyptic remains empty after three batches.** Nothing in the library
   scores above 36. It needs authoring.
8. **Two campaigns in one shortlist shared a bible.** Add a same-batch clone
   check before the next shortlist is approved.
