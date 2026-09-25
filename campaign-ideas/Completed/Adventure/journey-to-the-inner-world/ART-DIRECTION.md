# Journey to the Inner World — Art Direction & Asset List

**For:** Campaign Claude. Use this document to write the Muse generation doc.
**From:** Asset Claude, 2026-09-24
**Source of truth:** `journey-to-the-inner-world-campaign-bible.md`. All line numbers refer to that file.

---

## 0. Read first — 4 blockers before any generation

1. **The creative brief is for a different draft. Rewrite it.**
   - `creative-brief.md`, `world-building-spec.md` and `journey-to-the-inner-world.md` describe an old draft: Serpent Men, Abolethic Sovereignty, Crystal Heart, "Professor" Alistair Finch, dinosaurs.
   - The bible has a different cast: Great Wyrm egg cosmology, 10 factions, "Baron" Alistair Finch.
   - If Muse reads the old brief, it will generate dinosaurs and serpent men. Replace the brief's style section with Section 2 below.
2. **Do the IP renames before art.** Names drive filenames and slugs.
   - "Myconid": 14 uses on 13 lines (74, 120, 130, 145, 155, 184, 213, 233×2, 295, 304, 335, 386, 438). Affects the faction, 4 Tier-2 NPCs, 1 location, 1 monster, 2 items.
   - Use the app's race names: **Kenku → Ravenfolk** (The Silent, l.95). **Tabaxi → Catfolk** (The Echo-Hunter, l.105). These match `src/data/races/` on main.
   - **Artificer** (Progenitor Prime, l.91): the app has no rename for it. The SRD gate rejects it (`srd-gate.test.ts`), and starter seeding throws `Unsupported SRD class "Artificer"`. Change the class to an SRD class, for example Wizard. Or drop the class label. The design does not change.
   - **Pregens must use SRD classes only.** A non-SRD class breaks starter seeding.
3. **Write the starter characters.** The bible has **0 pre-generated PCs**. The storefront needs `starter_character_templates` with portraits. Midsummer had 6. Suggested cast: a 4–6 person expedition party that fits the Delvers' Guild descent.
4. **Clean the names for ingestion.** Do this before ingest, not after.
   - Strip parentheticals from monster names: `Fungal-Zombie (Myconid)`, `Grafted Horror (Flesh-Weaver)`, `Chaos-Mutant (Yolk-Embracer)`. Move the tag to the type line.
   - Bestiary headings `### 1. Yolk-Spawn (CR 2)` carry a leading number and a CR tag. Both can leak into `entity_name`.
   - Tier-1 NPCs, items and loot are numbered lists. That is the "16. The Recipe Hunter" bug.
   - `Grak, the "Tame" Troglodyte` slugs to `grak-the-tame-troglodyte`. That is fine, but keep the name stable.
   - Cross-campaign names: **Dr. Aris Thorne** also exists in Abyssal Descent. **Warden-Unit 734** echoes Eternal Feast's "Unit 734". Recommend renaming both. It is not a DB clash, but it looks like reuse in the storefront.

**Order:** renames → pregens → name cleanup → ingest → style bake-off → Muse doc → generate → manifest from `entity_name` → upload.

---

## 1. Style decision — graphic novel vs anime

**LOCKED 2026-09-24: graphic novel "Ink & Glow".** It won the bake-off 2 of 3 (Rostova and Grafted Horror; anime won the River of Light). Use only the Ink & Glow style block from §2.1. Do not mix styles. Results are in `STYLE-BAKE-OFF-PROMPTS.md`.

Rob wanted one of two styles. Both work. **Recommendation: graphic novel ("Ink & Glow").** Confirm it with a 6-image bake-off (Section 1.3).

### 1.1 Why a stylized look at all

- All 4 live campaigns are dark and painterly. A stylized look stands out in the storefront.
- Most assets show at small sizes: 96px thumbnails and 48px and 32px combat circles. Bold lines and flat shapes read at these sizes. Painterly detail turns to mud.
- AI generators hold a stylized look more consistently across 100+ images than a painterly look.

### 1.2 Trade-off

| | **Graphic novel — "Ink & Glow"** (recommended) | **Anime — "Luminous Expedition"** |
|---|---|---|
| Genre fit | Verne's original books used engraved illustrations. Inks with hatching are a direct descendant of them. | Classic adventure anime is also a strong fit for expeditions, airships and drills. |
| Glow | Black ink with neon spot colour gives maximum contrast. Glow is the signature. | Bloom, light particles and floating spores. Soft and beautiful. |
| Grotesque cast | Handles the Flesh-Weavers, the grafted horrors and the worm-in-a-suit well. Stays unsettling. | Tends to soften or cute-ify horror. There is a risk to the tone. |
| Faces at 96px | Good. Needs strong silhouettes. | Excellent. Anime faces read at any size. |
| Consistency | Good. Line weight drifts between generators. | Best. Most generators know anime well. |
| Audience | Comic and TTRPG crowd. Feels "premium module". | Broadest appeal, especially with younger players. |

**Why the graphic novel wins by a small margin:** a third of the cast is body-horror, and the black-ink-and-neon look gives the campaign one signature that is easy to repeat. Anime wins if the bake-off shows that faces or consistency are much better.

### 1.3 Bake-off (do this before writing the Muse doc)

Generate the same 3 subjects in both styles, which is 6 images in total. Compare them at 96px and at 32px.

1. **Captain Eva Rostova** (l.98). Tests a human face at thumbnail size.
2. **Grafted Horror** (l.341). Tests the grotesque cast.
3. **The River of Light** (l.183). Tests glow in a wide 4:3 location.

Pick the style that wins 2 of 3. Then lock the style block. Do not mix styles after the lock.

**Result (2026-09-24):** Ink & Glow won Rostova and the Grafted Horror. Anime won the River of Light. **Ink & Glow is locked.**

---

## 2. Locked style rules (Ink & Glow)

### 2.1 Style blocks (paste into every prompt)

**Graphic novel — Ink & Glow:**
> Graphic novel illustration. Bold black ink linework with variable line weight. Cross-hatched shadows in the manner of 19th-century engraving. Flat colour fills with 2–3 value steps, no painterly blending, no photoreal texture. Deep dark base palette. The only saturated colours are glowing light sources, which rim-light the subject. Realistic adult proportions, expressive faces.

**Anime — Luminous Expedition (not chosen, kept for reference only; do not use):**
> Anime illustration. Clean cel-shaded characters, crisp line, two-tone shading. Detailed painted backgrounds with atmospheric depth. Grounded adult proportions, about 7 heads tall, no chibi. Deep dark base palette. Glowing light sources with soft bloom and drifting light particles. The only saturated colours are glowing light sources.

**Negative (both):** no text, no letters, no captions, no speech bubbles, no panel borders, no logos, no watermarks, no signatures, no frame. Do not name real studios or artists in prompts. Describe traits only.

### 2.2 Palette

- **Base (the dark):** ink-black, midnight blue, deep teal, moss green, bruised purple.
- **Glow (light sources only):** electric cyan, acid green, sulphur yellow, hot magenta.
- **Surface warmth:** brass, copper, lantern amber, coal-smoke grey. Only for surface-world people and gear, mostly the Delvers' Guild.

### 2.3 Colour script — "the deeper you go, the brighter it gets"

The Core is a sun, so the descent inverts normal cave logic. Each zone has one colour key.

| Zone | Key | Light source |
|---|---|---|
| 1. Great Chasm of Al-Ghor | amber, brass, soot grey | grey daylight from above, lanterns, furnace glow |
| 2. Labyrinth of Echoes | cold grey-violet | faint crystal light. Show sound as visible ripple lines. |
| 3. Bioluminescent Jungle | teal and green | cyan, magenta and gold glows from plants, fungi and fruit |
| 4. Sea of Chaos | oily black, iridescent, flesh pink | glowing primordial sea, maelstrom light |
| 5. Core's Corona | white-gold, overexposed | the Core. Black glass throws hard reflections. |

### 2.4 Faction visual keys (proposals, adopt or edit)

Use these for NPC costume accents and for the faction emblems.

| Faction | Colour | Emblem motif |
|---|---|---|
| The Delvers' Guild | brass, amber | drill bit inside a gear |
| The Surface Sentinels | slate grey, sky blue | keystone under a closed dome |
| The Geode-Gnostics | cyan, violet | faceted hexagonal crystal |
| The Flesh-Weavers of the Yolk | flesh pink, bone | stitched spiral |
| The Children of the Core | sunfire orange | handprint over a sun |
| The Remnant of the Shell-Wardens | grey stone, gold light | scarab inside a hexagonal seal |
| The Descendants of the Yolk-Embracers | oil-slick iridescent | broken egg leaking light |
| The Echo-Thieves | magenta | concentric sound rings around an open mouth |
| [renamed fungal faction] | acid green | mushroom cap with a spore ring |
| The Society of the Blind Worm | umber, pale worm-white | eyeless worm eating its tail |

### 2.5 Recurring motifs

- Egg and hatching: cracks, shell fragments, seals.
- Crystal growth and resonance.
- Visible sound (Labyrinth of Echoes, Echo-Thieves).
- Patchwork biology with visible stitches (Flesh-Weavers).
- Everything that glows is alive, or was alive.

---

## 3. Asset list

### 3.1 Formats (verified against the app code)

| Asset | Ratio | Size | Framing |
|---|---|---|---|
| Cover | 4:5 | 1200×1500 | Subject centred. Nothing important in the outer 10%. |
| Banner | 21:9 | ≥ 2352×1008 | Wide vista. Key subject in the centre third. It is also the fallback header. |
| Starter portrait | 1:1 | ≥ 1024² | Face in the upper-middle. Shown as 96, 64 and 16px circles and as a wide header crop. |
| NPC / monster / item | 1:1 | ≥ 1024² | Subject fills the centre 70%. Must survive a 32px circle crop. Strong silhouette. |
| Location | 4:3 | 1600×1200 | Focal point in the centre. The lightbox is square on mobile. |
| Faction emblem | 1:1 | ≥ 1024² | Centred emblem, plain dark background. **Does not render yet (#2198).** |
| Scenes | — | — | **Do not generate.** They do not render. |

### 3.2 What to generate

**P0 — needed to ship the storefront listing**

| Asset | Count | Notes |
|---|---|---|
| Cover | 1 | Suggest: the party on a rope bridge over the Great Chasm, looking down into a glow far below. Uses the zone 1 → zone 3 colour shift in one frame. |
| Banner | 1 | Suggest: the Bioluminescent Jungle vista with the Core-sun on the horizon and the party in silhouette. |
| Starter portraits | 4–6 | Blocked until the pregens are written (Blocker 3). |

**P1 — core play assets (these show in chat and combat)**

| Asset | Count | Bible lines |
|---|---|---|
| Tier-1 NPCs | 20 | 88–107 |
| Monsters | 10 | 311–369 |
| Locations (sub-locations) | 25 | 164–202 |

**P2 — nice to have**

| Asset | Count | Bible lines |
|---|---|---|
| Items (5 legendary + 20 custom loot) | 25 | 258–306 |
| Tier-2 NPCs | 49 | 112–160. Generate only if ingest creates `npc_tier2` chunks for them. |

**P3 — hold**

| Asset | Count | Notes |
|---|---|---|
| Faction emblems | 10 | Hold until #2198 ships. |
| Zone establishing shots | 5 | Only if ingest creates chunks for the 5 zones. Otherwise use them as trailer b-roll. |

**Totals:** P0+P1 = 57 + pregens. All tiers = 146 + pregens.

### 3.3 Design notes for hard subjects

These entities have no fixed look in the bible. Lock one design before generating.

- **Yolk-Spawn** (l.311): it has no fixed body. Pick one mid-mutation form, for example an egg-yolk mass sprouting a wing, a claw and an extra eye.
- **The Great Mind-Spore** (l.96): it is continent-sized. Show one vast glowing fungal "face" or brain-cap in a cavern, with a human figure for scale.
- **The Worm-That-Walks** (l.97) and **Kael** (l.121): a formal suit with worms at the collar and cuffs. Keep it unsettling, not gory.
- **The Surface of the Core** (l.202): it is not physical. Show an abstract "event horizon" of white-gold light with shapes forming at the edge.
- **Progenitor Prime** (l.91): an amalgam of mismatched limbs. Give it one clear focal face so it reads at 32px.
- **The Silent** (l.95): a Ravenfolk in a sound-dampening suit, with a playback device. Show the beak and feathers at the collar so the species reads.
- **The Echo-Hunter** (l.105): a Catfolk mercenary. Quiet and lean.
- **Warden-Unit 734** vs **Warden-Scarab**: both are Shell-Warden constructs. Give them a shared material (grey stone with gold light seams) so they read as one faction.

---

## 4. Rules for Muse's output (same as Midsummer)

- **Filenames = slug of the final `entity_name`**, as the uploader computes it: lowercase, strip diacritics and apostrophes, turn every other non-alphanumeric run into `-`, trim hyphens. Example: `grak-the-tame-troglodyte.png`.
- Take the names from the **ingested** `entity_name`, not from bible headings. Do not use fuzzy matching.
- Folders: `<campaign-slug>/{npc,monster,location,item,faction,portrait,card,banner}/`.
- Manifest: include `entity_name` verbatim, type, slug, real file format and pixel size.
- Save as PNG. Record the real format; do not rename a JPEG to `.png`.
- One file per entity. If there are variants, keep the chosen one and move the others to `_alts/`.
- Muse does not upload and does not write SQL. Asset Claude runs QA, then builds the manifest and uploads.
