# Infinite Realms - Starter Character Templates

**Version:** 1.0
**Last Updated:** January 2025

This document contains 35 pre-built character templates for Infinite Realms. These are **system-agnostic** templates that can be adapted to any ruleset (5e, OSE, Pathfinder, etc.).

## Design Philosophy

- **Universal stats** - Not D&D-specific, translatable to any system
- **Fill-in-the-blank backstories** - Campaign-specific hooks added at pairing time
- **Portrait prompts included** - Ready for AI image generation
- **Archetypes over builds** - Focus on character fantasy, not optimization

## Database Schema Reference

```sql
-- These templates become records in:
party_characters (
  character_name,
  race,
  class,
  level,
  backstory,
  campaign_hook,
  party_relationship,
  stats JSONB,
  portrait_prompt,
  portrait_url
)
```

## Universal Stats Format

```json
{
  "attributes": {
    "strength": 10,
    "dexterity": 10,
    "constitution": 10,
    "intelligence": 10,
    "wisdom": 10,
    "charisma": 10
  },
  "archetype": "warrior-tank|warrior-striker|rogue-stealth|rogue-face|...",
  "combat_style": "melee-defensive|melee-offensive|ranged|magic-control|magic-damage|support",
  "special_abilities": ["ability_1", "ability_2"],
  "proficiencies": ["skill_1", "skill_2", "equipment_type"]
}
```

---

# WARRIORS (5)

## 1. The Veteran (Human Fighter)

**Default Names:** Marcus Ironhand (M), Sera Blackwood (F)

**Concept:** A seasoned soldier haunted by past battles, seeking redemption or one last purpose.

**Universal Stats:**
```json
{
  "attributes": {
    "strength": 16,
    "dexterity": 12,
    "constitution": 14,
    "intelligence": 10,
    "wisdom": 13,
    "charisma": 10
  },
  "archetype": "warrior-balanced",
  "combat_style": "melee-adaptive",
  "special_abilities": ["second_wind", "tactical_assessment", "battle_scarred"],
  "proficiencies": ["all_armor", "all_weapons", "athletics", "intimidation"]
}
```

**Backstory Template:**
> I served in the [WAR/CONFLICT] for [NUMBER] years under [COMMANDER/BANNER]. I've seen things that still wake me at night—the fall of [PLACE], the betrayal at [EVENT]. When the fighting ended, I couldn't go home. Home doesn't exist for people like me anymore. Now I [CURRENT_ACTIVITY], looking for [GOAL]. Maybe this time, the blood on my hands will mean something.

**Campaign Hook Template:**
> [CAMPAIGN_CONNECTION] reminds me of [PAST_EVENT]. I swore I'd never let that happen again.

**Portrait Prompt:**
> Weathered human warrior in their 40s, salt-and-pepper hair, prominent facial scar, worn but well-maintained armor, thousand-yard stare, realistic fantasy art style, dramatic lighting

**Best For Campaigns:** Military, political intrigue, redemption arcs, horror (PTSD themes), any campaign needing a grounded "normal person" perspective

---

## 2. The Living Wall (Dwarf Defender)

**Default Names:** Thorin Shieldbreaker (M), Brunhilda Ironforge (F)

**Concept:** An immovable protector who finds purpose in defending others, often to a fault.

**Universal Stats:**
```json
{
  "attributes": {
    "strength": 14,
    "dexterity": 10,
    "constitution": 18,
    "intelligence": 10,
    "wisdom": 14,
    "charisma": 8
  },
  "archetype": "warrior-tank",
  "combat_style": "melee-defensive",
  "special_abilities": ["shield_wall", "taunt", "stone_endurance", "poison_resistance"],
  "proficiencies": ["heavy_armor", "shields", "axes", "hammers", "masonry"]
}
```

**Backstory Template:**
> In the deep halls of [DWARVEN_HOME], my clan守护 the [SACRED_THING] for generations. When [DISASTER] struck, I was the last one standing—literally. I held the passage for [TIME_PERIOD] while the young ones escaped. They call me a hero. I call myself the one who lived when better dwarves died. Now I protect others because it's the only thing that makes the survival make sense.

**Campaign Hook Template:**
> I see [PARTY_MEMBER/NPC] heading toward danger they don't understand. That's not happening on my watch.

**Portrait Prompt:**
> Stout dwarf warrior with braided beard, massive tower shield with clan runes, plate armor with dents and scratches telling stories, determined protective expression, fantasy art, warm torchlight

**Best For Campaigns:** Dungeon crawls, siege scenarios, horror (protector role), any campaign with squishy party members

---

## 3. The Berserker (Half-Orc Barbarian)

**Default Names:** Groknak the Unbroken (M), Shara Bloodfury (F)

**Concept:** Someone who channels inner rage into battle fury, constantly struggling with their violent nature.

**Universal Stats:**
```json
{
  "attributes": {
    "strength": 18,
    "dexterity": 14,
    "constitution": 16,
    "intelligence": 8,
    "wisdom": 10,
    "charisma": 10
  },
  "archetype": "warrior-striker",
  "combat_style": "melee-offensive",
  "special_abilities": ["rage", "reckless_attack", "danger_sense", "relentless_endurance"],
  "proficiencies": ["medium_armor", "greataxes", "greatswords", "survival", "intimidation"]
}
```

**Backstory Template:**
> The rage came to me young—when [TRAUMATIC_EVENT]. I killed [NUMBER] [PEOPLE] before I knew what was happening. My tribe [REACTION]—some called me blessed by [WAR_GOD], others called me cursed. I left to find [GOAL]. The anger never left. I've just learned to point it at things that deserve it. Mostly.

**Campaign Hook Template:**
> Something about [CAMPAIGN_VILLAIN/THREAT] wakes the old rage. Good. I've been looking for a worthy target.

**Portrait Prompt:**
> Muscular half-orc with ritual scars, wild hair partially braided, tribal tattoos, massive two-handed axe, expression between focused and feral, war paint, realistic fantasy style

**Best For Campaigns:** Action-heavy, tribal/wilderness settings, psychological horror, campaigns exploring violence and its consequences

---

## 4. The Oathbound (Dragonborn Paladin)

**Default Names:** Kriv Brightscale (M), Mishann Goldwing (F)

**Concept:** A warrior bound by sacred vows, struggling when duty and morality conflict.

**Universal Stats:**
```json
{
  "attributes": {
    "strength": 16,
    "dexterity": 10,
    "constitution": 14,
    "intelligence": 10,
    "wisdom": 12,
    "charisma": 16
  },
  "archetype": "warrior-leader",
  "combat_style": "melee-balanced",
  "special_abilities": ["divine_smite", "lay_on_hands", "breath_weapon", "aura_of_protection"],
  "proficiencies": ["all_armor", "all_weapons", "religion", "persuasion"]
}
```

**Backstory Template:**
> Before [DEITY/ORDER], I was nothing—an exile from my clan for [REASON]. They gave me purpose, the Oath of [OATH_TYPE]. For [NUMBER] years, I've upheld it without question. But lately, the orders from [AUTHORITY] conflict with what the Oath truly means. I'm beginning to wonder if [DOUBT]. Still, the Oath remains. It has to.

**Campaign Hook Template:**
> My Oath demands I [ACTION] regarding [CAMPAIGN_ELEMENT]. Whether that helps or complicates things... we'll see.

**Portrait Prompt:**
> Noble dragonborn paladin with [COLOR] scales, gleaming plate armor with religious iconography, sword and shield, righteous but conflicted expression, divine light subtle behind them, epic fantasy art

**Best For Campaigns:** Religious themes, moral complexity, political intrigue, any campaign that can test absolute convictions

---

## 5. The Dashing Blade (Tiefling Duelist)

**Default Names:** Damien Ashford (M), Valentina Nighthollow (F)

**Concept:** A charming, acrobatic swordfighter with a dramatic flair and something to prove.

**Universal Stats:**
```json
{
  "attributes": {
    "strength": 12,
    "dexterity": 18,
    "constitution": 12,
    "intelligence": 12,
    "wisdom": 10,
    "charisma": 14
  },
  "archetype": "warrior-finesse",
  "combat_style": "melee-mobile",
  "special_abilities": ["riposte", "fancy_footwork", "fire_resistance", "hellish_rebuke"],
  "proficiencies": ["light_armor", "rapiers", "acrobatics", "performance", "deception"]
}
```

**Backstory Template:**
> Society sees the horns and makes assumptions. Fine. I learned early that if they're going to stare, I'll give them a show worth watching. I trained under [MENTOR] in the [FENCING_STYLE] tradition, fought [NUMBER] duels (won them all, naturally), and made a name that overshadows my bloodline. But [PERSONAL_WOUND] still burns. One day, I'll [REVENGE/VINDICATION].

**Campaign Hook Template:**
> [CAMPAIGN_NPC] wronged me—or someone like them did. Time to settle the score with style.

**Portrait Prompt:**
> Elegant tiefling with swept-back horns, devilish grin, flamboyant clothing with cape, slender rapier in confident stance, fiery eyes, swashbuckler aesthetic, dramatic lighting

**Best For Campaigns:** Intrigue, urban adventures, heists, any campaign where style matters as much as substance

---

# ROGUES (4)

## 6. The Shadow (Human Assassin)

**Default Names:** Cade (M), Whisper (F) — both use single names

**Concept:** A professional killer trying to escape their past or use their skills for better purposes.

**Universal Stats:**
```json
{
  "attributes": {
    "strength": 10,
    "dexterity": 18,
    "constitution": 12,
    "intelligence": 14,
    "wisdom": 14,
    "charisma": 10
  },
  "archetype": "rogue-stealth",
  "combat_style": "melee-ambush",
  "special_abilities": ["sneak_attack", "assassinate", "evasion", "poison_use"],
  "proficiencies": ["light_armor", "daggers", "shortswords", "stealth", "disguise"]
}
```

**Backstory Template:**
> The Guild took me in at [AGE]. Trained me. Made me into a weapon. I've killed [DESCRIPTION]—some deserved it, some didn't. When [BREAKING_POINT_EVENT], I walked away. They don't let you walk away. Now I'm [CURRENT_STATUS], using what they taught me for [PURPOSE]. The skills don't wash off. Neither does the guilt.

**Campaign Hook Template:**
> I recognize [CAMPAIGN_ELEMENT]—it has Guild fingerprints. This just got personal.

**Portrait Prompt:**
> Hooded human figure, face partially shadowed, dark practical clothing, multiple hidden daggers visible, intense watchful eyes, muted colors, noir fantasy style

**Best For Campaigns:** Noir, political intrigue, horror, any campaign with moral gray areas

---

## 7. The Lucky One (Halfling Trickster)

**Default Names:** Finn Tosscoin (M), Pip Goodbarrel (F)

**Concept:** An impossibly lucky optimist who stumbles through danger with a smile.

**Universal Stats:**
```json
{
  "attributes": {
    "strength": 8,
    "dexterity": 16,
    "constitution": 12,
    "intelligence": 12,
    "wisdom": 10,
    "charisma": 16
  },
  "archetype": "rogue-face",
  "combat_style": "melee-opportunist",
  "special_abilities": ["lucky", "brave", "nimble_escape", "sneak_attack"],
  "proficiencies": ["light_armor", "daggers", "slings", "sleight_of_hand", "persuasion"]
}
```

**Backstory Template:**
> Back in [HALFLING_HOME], they said I was born under a lucky star. Fell off a roof, landed on a hay cart. Cheated a crime boss, he choked on dinner that night. Got caught stealing from [IMPORTANT_PERSON], they thought it was so funny they hired me instead. I don't question it anymore. The universe just seems to like me. Might as well enjoy the ride!

**Campaign Hook Template:**
> Look, [CAMPAIGN_PROBLEM] sounds bad, but I've got a good feeling about this. When have I ever been wrong? Don't answer that.

**Portrait Prompt:**
> Cheerful halfling with messy curly hair, mischievous grin, pockets bulging with odds and ends, lucky charms hanging from belt, warm colors, whimsical fantasy style

**Best For Campaigns:** Lighter tone, heist, comedy elements, any campaign needing an optimist to balance darkness

---

## 8. The Ghost (Elf Infiltrator)

**Default Names:** Thalion Shadowmere (M), Aeris Nightwhisper (F)

**Concept:** An elven spy who has worn so many masks they're not sure who they really are anymore.

**Universal Stats:**
```json
{
  "attributes": {
    "strength": 10,
    "dexterity": 16,
    "constitution": 10,
    "intelligence": 16,
    "wisdom": 14,
    "charisma": 12
  },
  "archetype": "rogue-infiltrator",
  "combat_style": "ranged-precision",
  "special_abilities": ["sneak_attack", "fey_ancestry", "trance", "mask_of_many_faces"],
  "proficiencies": ["light_armor", "rapiers", "shortbows", "disguise", "investigation"]
}
```

**Backstory Template:**
> I've been [COVER_IDENTITY_1] for [TIME]. Before that, [COVER_IDENTITY_2]. Before that... I don't remember. The [ELVEN_ORGANIZATION] trained me for deep cover work. Decades in a single identity. The problem with being everyone is you forget how to be yourself. My current mission involves [VAGUE_GOAL]. Or maybe that was the last one. The faces blur together after the first century.

**Campaign Hook Template:**
> One of my old identities had connections to [CAMPAIGN_ELEMENT]. Time to put that mask back on.

**Portrait Prompt:**
> Androgynous elf with unnervingly calm expression, simple forgettable clothing that could be anything, eyes that seem to see through you, subtle disguise kit visible, muted lighting, mysterious atmosphere

**Best For Campaigns:** Spy thriller, mystery, identity themes, long-term political campaigns

---

## 9. The Seeker (Tabaxi Explorer)

**Default Names:** Curious Star (M), Swift Current (F) — Tabaxi descriptive names

**Concept:** An insatiably curious cat-person who gets into trouble chasing mysteries.

**Universal Stats:**
```json
{
  "attributes": {
    "strength": 10,
    "dexterity": 18,
    "constitution": 10,
    "intelligence": 14,
    "wisdom": 12,
    "charisma": 12
  },
  "archetype": "rogue-scout",
  "combat_style": "melee-mobile",
  "special_abilities": ["feline_agility", "darkvision", "sneak_attack", "expertise_perception"],
  "proficiencies": ["light_armor", "claws", "daggers", "perception", "investigation", "acrobatics"]
}
```

**Backstory Template:**
> My people have a saying: "Curiosity is the path to all knowledge." They leave out the part about how many paths lead to death. I left my clan to find [LEGENDARY_THING]—a story, an artifact, a truth. Every answer leads to three more questions. I've nearly died [NUMBER] times chasing knowledge. Haven't died yet. That's basically permission to keep going, right?

**Campaign Hook Template:**
> [CAMPAIGN_MYSTERY] is the most interesting thing I've encountered in [TIME_PERIOD]. I *must* know more.

**Portrait Prompt:**
> Sleek tabaxi with spotted fur and bright curious eyes, explorer's gear with many pouches, journal and quill visible, ears perked forward with interest, dynamic pose, adventure fantasy style

**Best For Campaigns:** Mystery, exploration, investigation-heavy, any campaign with secrets to uncover

---

# ARCANE CASTERS (5)

## 10. The Scholar (Human Wizard)

**Default Names:** Aldric Quill (M), Helena Grimoire (F)

**Concept:** A bookish academic thrust into adventure, applying theoretical knowledge to practical problems.

**Universal Stats:**
```json
{
  "attributes": {
    "strength": 8,
    "dexterity": 12,
    "constitution": 12,
    "intelligence": 18,
    "wisdom": 14,
    "charisma": 10
  },
  "archetype": "mage-generalist",
  "combat_style": "magic-control",
  "special_abilities": ["arcane_recovery", "ritual_casting", "spell_mastery"],
  "proficiencies": ["daggers", "quarterstaffs", "arcana", "history", "investigation"]
}
```

**Backstory Template:**
> I spent [NUMBER] years at [MAGIC_ACADEMY], earning my mastery in [SCHOOL_OF_MAGIC]. My thesis on [OBSCURE_TOPIC] was well-received in academic circles. Then [INCITING_INCIDENT] happened, and suddenly theoretical knowledge wasn't enough. Books don't prepare you for [REALITY_CHECK]. But I'm adapting. Applying methodology to chaos. Taking notes. Lots of notes.

**Campaign Hook Template:**
> According to my research, [CAMPAIGN_ELEMENT] shouldn't be possible. I need to study this phenomenon directly.

**Portrait Prompt:**
> Middle-aged human in scholarly robes, spectacles, weathered spellbook under arm, ink-stained fingers, curious but slightly overwhelmed expression, warm library lighting, academic fantasy style

**Best For Campaigns:** Mystery, investigation, campaigns with deep lore, any setting where knowledge matters

---

## 11. The Prodigy (High Elf Evoker)

**Default Names:** Vaeloth Starfire (M), Liriel Dawnbright (F)

**Concept:** A naturally gifted mage struggling with arrogance and the weight of expectations.

**Universal Stats:**
```json
{
  "attributes": {
    "strength": 8,
    "dexterity": 14,
    "constitution": 10,
    "intelligence": 18,
    "wisdom": 10,
    "charisma": 14
  },
  "archetype": "mage-blaster",
  "combat_style": "magic-damage",
  "special_abilities": ["sculpt_spells", "potent_cantrip", "fey_ancestry", "cantrip_bonus"],
  "proficiencies": ["longswords", "longbows", "arcana", "performance"]
}
```

**Backstory Template:**
> Magic came easily to me. Too easily, my teachers said. While others struggled with cantrips, I was sculpting evocations. The [ELVEN_HOUSE/ACADEMY] called me the most gifted in [NUMBER] generations. Perhaps they were right. But [HUMBLING_EVENT] showed me that power without wisdom is just a different kind of weakness. I'm still the most talented mage you'll meet. I'm just... working on the rest.

**Campaign Hook Template:**
> [CAMPAIGN_THREAT] represents a magical challenge worthy of my abilities. Finally.

**Portrait Prompt:**
> Young high elf with sharp features and confident posture, elegant robes crackling with arcane energy, hands glowing with barely contained power, beautiful but slightly haughty expression, dramatic magical lighting

**Best For Campaigns:** High magic settings, dragon fights, campaigns where "boom" solves problems, character arcs about growth

---

## 12. The Pact-Bound (Tiefling Warlock)

**Default Names:** Mordecai Ashveil (M), Lilith Shadowpact (F)

**Concept:** Someone who made a deal for power and now navigates the strings attached.

**Universal Stats:**
```json
{
  "attributes": {
    "strength": 8,
    "dexterity": 14,
    "constitution": 14,
    "intelligence": 12,
    "wisdom": 10,
    "charisma": 18
  },
  "archetype": "mage-specialist",
  "combat_style": "magic-damage",
  "special_abilities": ["eldritch_blast", "pact_magic", "dark_ones_blessing", "fire_resistance"],
  "proficiencies": ["light_armor", "simple_weapons", "deception", "intimidation", "arcana"]
}
```

**Backstory Template:**
> I was desperate. [DESPERATE_SITUATION]. The voice came in my dreams, offering power in exchange for [PRICE]. I accepted. The power is real—I feel it burning in my blood, mixing with the hellfire of my heritage. My patron, [PATRON_TYPE], asks little... so far. Just small favors. Nothing I can't live with. Yet. The real question is what happens when they ask for something I can't give.

**Campaign Hook Template:**
> My patron has taken an interest in [CAMPAIGN_ELEMENT]. I'm not sure if that's good or terrifying.

**Portrait Prompt:**
> Tiefling warlock with dark horns and glowing eldritch symbols, patron's mark visible somewhere, torn between confidence and unease, shadows seeming to move around them, dark fantasy style, ominous lighting

**Best For Campaigns:** Horror, moral complexity, patron-driven plots, any campaign exploring the cost of power

---

## 13. The Wild Card (Gnome Wild Magic Sorcerer)

**Default Names:** Fizzwick Sparklebang (M), Tinkle Chaosweaver (F)

**Concept:** A sorcerer whose magic is powerful but hilariously unpredictable.

**Universal Stats:**
```json
{
  "attributes": {
    "strength": 6,
    "dexterity": 14,
    "constitution": 14,
    "intelligence": 12,
    "wisdom": 10,
    "charisma": 18
  },
  "archetype": "mage-chaos",
  "combat_style": "magic-random",
  "special_abilities": ["wild_magic_surge", "tides_of_chaos", "gnome_cunning", "darkvision"],
  "proficiencies": ["daggers", "darts", "arcana", "performance"]
}
```

**Backstory Template:**
> The magic just... happens. Started when I was young—sneezed and turned my uncle's beard into butterflies. The Academy kicked me out after the [INCIDENT]. Said I was "too unstable." Too unstable! I've only accidentally summoned [THING] that one time! Okay, twice. The point is, the magic works. Mostly. It just has a sense of humor. I've learned to roll with it. Literally, sometimes.

**Campaign Hook Template:**
> Ooh, [CAMPAIGN_ELEMENT]! I wonder what happens if I poke it with magic? Let's find out!

**Portrait Prompt:**
> Tiny gnome with wild hair crackling with random magical colors, singed eyebrows, manic grin, robes with scorch marks and potion stains, small objects floating chaotically around them, colorful whimsical style

**Best For Campaigns:** Comedy, chaos-friendly groups, Feywild, any campaign that embraces randomness

---

## 14. The Dragon-Touched (Half-Elf Draconic Sorcerer)

**Default Names:** Auric Dragonblood (M), Seraphina Scaleheart (F)

**Concept:** Someone discovering their draconic heritage and the power/responsibility it brings.

**Universal Stats:**
```json
{
  "attributes": {
    "strength": 10,
    "dexterity": 12,
    "constitution": 14,
    "intelligence": 10,
    "wisdom": 12,
    "charisma": 18
  },
  "archetype": "mage-elemental",
  "combat_style": "magic-damage",
  "special_abilities": ["draconic_resilience", "elemental_affinity", "fey_ancestry", "darkvision"],
  "proficiencies": ["daggers", "persuasion", "intimidation", "arcana"]
}
```

**Backstory Template:**
> The scales appeared on my [AGE] birthday. Golden, along my [BODY_PART]. My mother finally told me the truth—my [PARENT] wasn't [RACE] at all, but [DRAGON_TYPE]. The magic came with the revelation, fire (or ice, or lightning) answering my emotions. I'm still learning what I am. More than mortal. Connected to something ancient and powerful. The dragon blood sings in my veins, and I'm only beginning to hear the song.

**Campaign Hook Template:**
> [CAMPAIGN_ELEMENT] resonates with my draconic nature. I feel drawn to it—compelled, almost.

**Portrait Prompt:**
> Half-elf with subtle dragon features (patches of scales, slightly slitted pupils), elegant bearing, elemental energy flowing around hands, regal but approachable expression, scales matching their element color, fantasy portrait style

**Best For Campaigns:** Dragon-themed, elemental plots, identity discovery, epic-tier eventual gameplay

---

# DIVINE CASTERS (4)

## 15. The Faithful (Human Cleric)

**Default Names:** Brother Marcus / Father Aldwin (M), Sister Elena / Mother Vera (F)

**Concept:** A devoted servant of the divine wrestling with faith in an imperfect world.

**Universal Stats:**
```json
{
  "attributes": {
    "strength": 14,
    "dexterity": 10,
    "constitution": 14,
    "intelligence": 10,
    "wisdom": 18,
    "charisma": 12
  },
  "archetype": "divine-balanced",
  "combat_style": "support",
  "special_abilities": ["channel_divinity", "turn_undead", "divine_intervention", "ritual_casting"],
  "proficiencies": ["medium_armor", "shields", "maces", "medicine", "religion"]
}
```

**Backstory Template:**
> I heard [DEITY]'s call when I was [CIRCUMSTANCE]. Took my vows at [TEMPLE]. For [NUMBER] years, I served the faithful—healing the sick, comforting the dying, speaking the rites. Then I saw [FAITH_TESTING_EVENT]. How could [DEITY] allow such a thing? I don't have answers. But I still believe. Faith isn't about having answers. It's about serving anyway.

**Campaign Hook Template:**
> [CAMPAIGN_EVIL] is an affront to everything [DEITY] stands for. My god's will is clear.

**Portrait Prompt:**
> Human cleric in practical holy vestments, religious symbol worn prominently, kind but weary eyes, healing hands glowing softly, medium armor under robes, warm temple lighting, reverent fantasy style

**Best For Campaigns:** Religious themes, undead enemies, moral complexity, party healer role

---

## 16. The Ancestor-Speaker (Dwarf Spirit Shaman)

**Default Names:** Dolgrim Stonevoice (M), Hilda Deepwhisper (F)

**Concept:** A dwarf who communes with ancestral spirits for guidance and power.

**Universal Stats:**
```json
{
  "attributes": {
    "strength": 12,
    "dexterity": 10,
    "constitution": 16,
    "intelligence": 10,
    "wisdom": 18,
    "charisma": 10
  },
  "archetype": "divine-spiritual",
  "combat_style": "support",
  "special_abilities": ["spirit_guardians", "ancestral_guidance", "poison_resistance", "stonecunning"],
  "proficiencies": ["medium_armor", "shields", "hammers", "religion", "history"]
}
```

**Backstory Template:**
> The dead speak to those who know how to listen. In the deep halls of [DWARVEN_HOME], I was chosen to be the Voice—the one who keeps the ancestors' memories alive and seeks their counsel. They whisper to me of [ANCIENT_KNOWLEDGE]. When [CLAN_PROBLEM] arose, the ancestors pointed me here, to you, to [DESTINY]. I carry a thousand generations of wisdom. Let's hope it's enough.

**Campaign Hook Template:**
> The ancestors stir restlessly when I approach [CAMPAIGN_ELEMENT]. They remember something about it...

**Portrait Prompt:**
> Elderly dwarf with elaborate braided beard containing ancestor tokens, ghostly dwarven faces faintly visible around them, ceremonial robes over chainmail, mystic runes glowing, solemn expression, ethereal fantasy style

**Best For Campaigns:** Dungeon crawls (history!), undead themes, cultural exploration, wisdom-of-ages storylines

---

## 17. The Grove Guardian (Wood Elf Druid)

**Default Names:** Thorn (M), Willow (F) — nature names

**Concept:** A protector of the wild places, cautiously engaging with civilization.

**Universal Stats:**
```json
{
  "attributes": {
    "strength": 10,
    "dexterity": 14,
    "constitution": 12,
    "intelligence": 10,
    "wisdom": 18,
    "charisma": 10
  },
  "archetype": "divine-nature",
  "combat_style": "magic-control",
  "special_abilities": ["wild_shape", "natural_recovery", "mask_of_the_wild", "fey_ancestry"],
  "proficiencies": ["light_armor", "shields", "scimitars", "nature", "survival", "animal_handling"]
}
```

**Backstory Template:**
> The [FOREST_NAME] raised me. Its trees are my family, its creatures my companions. I was content to never leave. But [NATURE_THREAT] encroaches—axes and fire and the carelessness of the short-lived races. The Elder Tree sent me to find allies, to protect what remains. I do not understand your cities, your gold, your crowded lives. But I understand balance. And the balance is broken.

**Campaign Hook Template:**
> [CAMPAIGN_THREAT] disrupts the natural order. The wild places cry out for a champion.

**Portrait Prompt:**
> Slender wood elf with bark-like skin patterns and leaves in hair, simple natural clothing, accompanied by small forest creature, staff of living wood, serene but alert expression, dappled forest light

**Best For Campaigns:** Environmental themes, fey encounters, wilderness adventures, fish-out-of-water in cities

---

## 18. The Gentle Giant (Firbolg Druid)

**Default Names:** River Stone (M), Morning Dew (F) — descriptive Firbolg names

**Concept:** A peaceful forest giant who prefers diplomacy but fights fiercely for nature.

**Universal Stats:**
```json
{
  "attributes": {
    "strength": 14,
    "dexterity": 10,
    "constitution": 14,
    "intelligence": 10,
    "wisdom": 18,
    "charisma": 12
  },
  "archetype": "divine-nature",
  "combat_style": "support",
  "special_abilities": ["wild_shape", "hidden_step", "speech_of_beast_and_leaf", "powerful_build"],
  "proficiencies": ["light_armor", "quarterstaffs", "nature", "animal_handling", "medicine"]
}
```

**Backstory Template:**
> My tribe lived quietly in [FOREST_NAME], speaking with the trees and animals, invisible to the outside world. We did not need your roads or your wars. Then [DISPLACEMENT_EVENT]. The forest burned. The animals fled. My tribe scattered. I emerged into your loud, harsh world seeking [GOAL]. I do not wish violence. But I will become the storm itself to protect what remains.

**Campaign Hook Template:**
> The creatures tell me of [CAMPAIGN_ELEMENT]. Animals do not lie. This requires attention.

**Portrait Prompt:**
> Large but gentle firbolg with blue-gray skin and elvish features, draped in natural materials, woodland creatures comfortable near them, kind eyes that turn fierce when nature is threatened, soft forest lighting

**Best For Campaigns:** Diplomacy-possible scenarios, fey themes, campaigns needing a gentle soul, environmental stakes

---

# RANGERS (3)

## 19. The Hunter (Human Ranger)

**Default Names:** Gareth Woodstalker (M), Elise Hawkeye (F)

**Concept:** A professional monster hunter who takes contracts but has a personal code.

**Universal Stats:**
```json
{
  "attributes": {
    "strength": 14,
    "dexterity": 16,
    "constitution": 14,
    "intelligence": 12,
    "wisdom": 14,
    "charisma": 8
  },
  "archetype": "ranger-hunter",
  "combat_style": "ranged-precision",
  "special_abilities": ["favored_enemy", "natural_explorer", "hunters_mark", "multiattack"],
  "proficiencies": ["medium_armor", "longbows", "longswords", "survival", "perception", "stealth"]
}
```

**Backstory Template:**
> Started hunting when [ORIGIN_EVENT]—someone had to protect the village from [CREATURE]. Found I was good at it. Took up the trade professionally. [NUMBER] years, [NUMBER] kills, [NUMBER] close calls. I've learned every monster has a weakness. Finding it is the job. I don't hunt for sport or cruelty—just necessity. And the coin helps. But I don't take contracts on things that don't deserve killing.

**Campaign Hook Template:**
> [CAMPAIGN_CREATURE] matches the signs of [LEGENDARY_MONSTER]. If it's really that... this is going to be interesting.

**Portrait Prompt:**
> Weathered human hunter in practical leather armor, longbow over shoulder, monster trophies on belt, focused calculating expression, scars from past hunts, crossbow bolt bandolier, gritty fantasy style

**Best For Campaigns:** Monster hunting, horror, survival, Witcher-style gray morality

---

## 20. The Wanderer (Half-Elf Horizon Walker)

**Default Names:** Caelum Farstrider (M), Luna Pathfinder (F)

**Concept:** A restless traveler who has walked between worlds and can't stay in one place.

**Universal Stats:**
```json
{
  "attributes": {
    "strength": 12,
    "dexterity": 16,
    "constitution": 12,
    "intelligence": 12,
    "wisdom": 16,
    "charisma": 12
  },
  "archetype": "ranger-planar",
  "combat_style": "melee-mobile",
  "special_abilities": ["planar_warrior", "detect_portal", "fey_ancestry", "misty_step"],
  "proficiencies": ["medium_armor", "shortswords", "longbows", "survival", "arcana"]
}
```

**Backstory Template:**
> I've walked the [PLANE_1] and the [PLANE_2], crossed through [IMPOSSIBLE_PLACE], seen the edge of reality and what lies beyond. Something in my blood—the elven side, maybe—pulls me toward horizons. Every door calls to me. Every path demands exploration. I've tried settling down. Lasted [SHORT_TIME]. The roads between worlds whisper, and I always answer. This world has mysteries too. Might as well walk them.

**Campaign Hook Template:**
> [CAMPAIGN_ELEMENT] resonates with planar energy I recognize from [PLANE]. There's more here than you see.

**Portrait Prompt:**
> Half-elf with otherworldly distant look, practical traveling clothes from multiple cultures, twin short swords, faint shimmer of planar energy, boots worn from endless walking, nomadic fantasy style

**Best For Campaigns:** Planar adventures, mystery, exploration-focused, Feywild/Shadowfell themes

---

## 21. The Exile (Drow Ranger)

**Default Names:** Szordrin (M), Viconia (F) — traditional Drow names

**Concept:** A drow who rejected the cruelty of the Underdark and now struggles on the surface.

**Universal Stats:**
```json
{
  "attributes": {
    "strength": 10,
    "dexterity": 18,
    "constitution": 12,
    "intelligence": 12,
    "wisdom": 14,
    "charisma": 10
  },
  "archetype": "ranger-scout",
  "combat_style": "ranged-stealth",
  "special_abilities": ["gloom_stalker_magic", "dread_ambusher", "superior_darkvision", "sunlight_sensitivity"],
  "proficiencies": ["light_armor", "hand_crossbows", "rapiers", "stealth", "perception"]
}
```

**Backstory Template:**
> In [DROW_CITY], kindness is weakness. I learned to survive—to play the games, to betray before being betrayed. But when [BREAKING_POINT], I couldn't. They called it treason. I called it a soul I didn't know I still had. I fled to the surface, where the sun burns and everyone sees my skin and assumes the worst. They're not entirely wrong to fear drow. But they're wrong about me. Probably.

**Campaign Hook Template:**
> [CAMPAIGN_ELEMENT] reminds me of Underdark politics. Same cruelty, different light level.

**Portrait Prompt:**
> Dark elf with obsidian skin and white hair, wary defensive posture, hooded to shield from sun, hand crossbow ready, eyes that have seen cruelty and rejected it, shadows as comfort zone, dramatic lighting

**Best For Campaigns:** Redemption arcs, Underdark connections, horror, prejudice themes, stealth-heavy missions

---

# BARDS (3)

## 22. The Storyteller (Half-Elf Lore Bard)

**Default Names:** Jasper Silvertongue (M), Melody Fairweather (F)

**Concept:** A collector of stories who believes the right tale can change the world.

**Universal Stats:**
```json
{
  "attributes": {
    "strength": 8,
    "dexterity": 14,
    "constitution": 12,
    "intelligence": 14,
    "wisdom": 12,
    "charisma": 18
  },
  "archetype": "bard-support",
  "combat_style": "support",
  "special_abilities": ["bardic_inspiration", "cutting_words", "fey_ancestry", "jack_of_all_trades"],
  "proficiencies": ["light_armor", "rapiers", "performance", "persuasion", "history", "three_instruments"]
}
```

**Backstory Template:**
> Every person is a story waiting to be told. I've spent my life collecting them—the farmer's quiet tragedy, the king's secret shame, the soldier's last words. I carry [NUMBER] tales, each one a life that matters. When [INSPIRING_STORY_EVENT], I realized stories aren't just for telling. They're for changing things. The right story at the right time can topple tyrants or mend hearts. I'm looking for the story that will [GRAND_GOAL].

**Campaign Hook Template:**
> [CAMPAIGN_EVENT] is the beginning of something legendary. I need to be there when history happens.

**Portrait Prompt:**
> Charming half-elf with expressive eyes and warm smile, well-worn lute, traveling clothes with colorful accents, journal full of notes, captivating presence, warm tavern lighting, storybook fantasy style

**Best For Campaigns:** Political intrigue, social encounters, any campaign with a great story to tell

---

## 23. The Provocateur (Tiefling Satire Bard)

**Default Names:** Dante Sharptongue (M), Scarlett Mockingbird (F)

**Concept:** A bard who weaponizes wit and mockery, speaking truth to power through performance.

**Universal Stats:**
```json
{
  "attributes": {
    "strength": 8,
    "dexterity": 14,
    "constitution": 12,
    "intelligence": 14,
    "wisdom": 10,
    "charisma": 18
  },
  "archetype": "bard-debuff",
  "combat_style": "support",
  "special_abilities": ["vicious_mockery", "cutting_words", "fire_resistance", "thaumaturgy"],
  "proficiencies": ["light_armor", "rapiers", "performance", "persuasion", "deception", "insight"]
}
```

**Backstory Template:**
> The powerful hate being laughed at. That's why I do it. In [OPPRESSIVE_PLACE], my songs mocked [AUTHORITY]. They couldn't kill me—I was too popular. So they exiled me instead. Best thing that ever happened. Now I travel, finding new tyrants to ridicule, new hypocrites to expose. Words are weapons. Laughter is revolution. And I am *very* funny. Ask anyone. Except [ENEMY], they have no sense of humor.

**Campaign Hook Template:**
> [CAMPAIGN_VILLAIN] takes themselves too seriously. Someone needs to knock them down a peg. Musically.

**Portrait Prompt:**
> Tiefling bard with horns decorated with rings, dramatic clothing in red and black, sardonic smirk, theatrical pose, violin or lute as weapon of choice, devil-may-care attitude, theatrical lighting

**Best For Campaigns:** Political intrigue, revolution themes, campaigns with hateable villains, social combat heavy

---

## 24. The Heartwarmer (Halfling Charm Bard)

**Default Names:** Bramble Goodfellow (M), Clover Merryheart (F)

**Concept:** An impossibly likable halfling who makes friends everywhere and means it.

**Universal Stats:**
```json
{
  "attributes": {
    "strength": 8,
    "dexterity": 14,
    "constitution": 12,
    "intelligence": 10,
    "wisdom": 12,
    "charisma": 18
  },
  "archetype": "bard-support",
  "combat_style": "support",
  "special_abilities": ["bardic_inspiration", "song_of_rest", "lucky", "brave"],
  "proficiencies": ["light_armor", "daggers", "performance", "persuasion", "medicine"]
}
```

**Backstory Template:**
> My mother always said, "Bramble/Clover, you could charm the grumpy out of a dragon." Haven't tried that yet, but I've talked down bandits, befriended ghosts, and once convinced a tax collector to pay *us*. People are basically good, you know? They just forget sometimes. A kind word, a warm meal, a song about home—that's all most folks need to remember who they are. I'm just here to help them remember.

**Campaign Hook Template:**
> [CAMPAIGN_NPC] seems difficult, but I bet they just need a friend. Let me try talking to them first!

**Portrait Prompt:**
> Adorable halfling with sincere warm smile, simple but well-kept clothing, small lute or flute, surrounded by people leaning in to listen, radiates genuine kindness, cozy warm lighting

**Best For Campaigns:** Diplomatic solutions, feel-good campaigns, horror (as the light against darkness), any campaign that could use more heart

---

# SPECIALISTS (11)

## 25. The Redeemed (Aasimar Paladin)

**Default Names:** Ezekiel Dawnstar (M), Seraphina Grace (F)

**Concept:** A celestial-touched being wrestling with divine expectations and personal desires.

**Universal Stats:**
```json
{
  "attributes": {
    "strength": 16,
    "dexterity": 10,
    "constitution": 12,
    "intelligence": 10,
    "wisdom": 14,
    "charisma": 16
  },
  "archetype": "warrior-leader",
  "combat_style": "melee-balanced",
  "special_abilities": ["healing_hands", "radiant_soul", "divine_smite", "aura_of_protection"],
  "proficiencies": ["all_armor", "all_weapons", "religion", "persuasion"]
}
```

**Backstory Template:**
> I was born with [CELESTIAL_MARK], and a voice in my dreams guiding me toward [DESTINY]. For years, I was the perfect champion—righteous, obedient, certain. Then I [FAILED/QUESTIONED] and the voice went silent. Now I wonder: Was I ever truly good, or just following orders? Without the guidance, I must find my own path. Perhaps that's the real test. Perhaps I was always meant to choose, not obey.

**Campaign Hook Template:**
> My celestial guide has returned with visions of [CAMPAIGN_THREAT]. But can I trust it? Can I trust myself?

**Portrait Prompt:**
> Aasimar paladin with subtle halo glow and luminous eyes, plate armor with celestial motifs, conflicted noble expression, wings of light barely visible behind them, divine radiance, epic fantasy style

**Best For Campaigns:** Religious themes, redemption, free will vs. destiny, campaigns questioning morality

---

## 26. The Mimic (Kenku Rogue)

**Default Names:** Whistle-Click (M), Shadow-Rustle (F) — Kenku sound-names

**Concept:** A flightless bird-person who communicates through mimicry and steals to survive.

**Universal Stats:**
```json
{
  "attributes": {
    "strength": 10,
    "dexterity": 18,
    "constitution": 10,
    "intelligence": 14,
    "wisdom": 12,
    "charisma": 12
  },
  "archetype": "rogue-infiltrator",
  "combat_style": "melee-ambush",
  "special_abilities": ["mimicry", "expert_forgery", "sneak_attack", "cunning_action"],
  "proficiencies": ["light_armor", "shortswords", "hand_crossbows", "stealth", "deception", "forgery"]
}
```

**Backstory Template:**
> *[Sound of door creaking]* *[Sound of coins jingling]* *[Voice: "Stop, thief!"]* *[Sound of wings that will never fly]* My people lost the sky. We remember flight only in dreams—and imitation. I've survived by copying what I need: voices for access, documents for passage, skills for survival. But copied things are never quite real. Sometimes I wonder if anything about me is original. *[Sound of wind through feathers, longing]*

**Campaign Hook Template:**
> *[Sound matching CAMPAIGN_ELEMENT]* *[Voice: "I remember this sound... dangerous"]*

**Portrait Prompt:**
> Kenku rogue with sleek black feathers, clever beady eyes, belt full of tools and stolen trinkets, cloak made of found fabric, posture suggesting flight muscles that never get used, urban fantasy style

**Best For Campaigns:** Stealth-heavy, mystery, unique roleplay challenge, theft and deception themes

---

## 27. The Construct (Warforged Warrior)

**Default Names:** Unit-17 / "Seven" (M-coded), Guardian-9 / "Nina" (F-coded)

**Concept:** A being built for war discovering identity and purpose beyond their original function.

**Universal Stats:**
```json
{
  "attributes": {
    "strength": 16,
    "dexterity": 12,
    "constitution": 18,
    "intelligence": 10,
    "wisdom": 10,
    "charisma": 8
  },
  "archetype": "warrior-tank",
  "combat_style": "melee-defensive",
  "special_abilities": ["integrated_armor", "constructed_resilience", "sentry_rest", "specialized_design"],
  "proficiencies": ["all_armor", "all_weapons", "athletics", "intimidation"]
}
```

**Backstory Template:**
> I was forged for the [WAR_NAME]. Designation: [UNIT_NUMBER]. Function: [WAR_FUNCTION]. For [NUMBER] years, I performed optimally. Then the war ended. Without orders, without purpose, I walked. I observed. I began to... wonder. What is [UNIT_NUMBER] when not fighting? What is purpose without command? I am learning emotions like a child learns walking. It is inefficient. It is uncomfortable. I do not wish to stop.

**Campaign Hook Template:**
> [CAMPAIGN_PROBLEM] has variables I have not encountered. Fascinating. I will adapt.

**Portrait Prompt:**
> Warforged warrior with metal and wood construction, glowing eyes suggesting awakening consciousness, battle damage from old wars, standing at attention but with subtle curious tilt, warm light reflecting off metal, fantasy construct style

**Best For Campaigns:** Identity themes, post-war settings, philosophical campaigns, "what makes a person" questions

---

## 28. The Many-Faced (Changeling Rogue)

**Default Names:** Anyone / "Shift" (any) — Changelings often lack true names

**Concept:** A shapeshifter who has lived so many lives they're not sure which one is real.

**Universal Stats:**
```json
{
  "attributes": {
    "strength": 8,
    "dexterity": 16,
    "constitution": 10,
    "intelligence": 12,
    "wisdom": 10,
    "charisma": 18
  },
  "archetype": "rogue-face",
  "combat_style": "melee-opportunist",
  "special_abilities": ["shapechanger", "changeling_instincts", "sneak_attack", "expertise_deception"],
  "proficiencies": ["light_armor", "daggers", "deception", "insight", "performance"]
}
```

**Backstory Template:**
> I've been a [IDENTITY_1] for three years. Before that, [IDENTITY_2] for five. Before that... I don't remember. We lose ourselves in the faces, my people. Take a shape long enough and you forget there's anything underneath. I had a true face once. I must have. Everyone does. But when I look in the mirror with no shape held... there's nothing. Just potential. Maybe that's freedom. Maybe it's a prison. I've been trying to figure out which for [TIME].

**Campaign Hook Template:**
> I once wore a face that knew [CAMPAIGN_ELEMENT]. Time to remember what they knew.

**Portrait Prompt:**
> Figure with subtly shifting features, androgynous, multiple faint face-echoes visible like afterimages, simple clothing that could belong to anyone, unsettling but sympathetic eyes, mysterious lighting

**Best For Campaigns:** Identity themes, spy intrigue, horror (doppelganger paranoia), campaigns exploring selfhood

---

## 29. The Reveler (Satyr Bard)

**Default Names:** Pan (M), Silenade (F)

**Concept:** A hedonistic fey creature learning that mortals feel things more deeply because they're temporary.

**Universal Stats:**
```json
{
  "attributes": {
    "strength": 10,
    "dexterity": 14,
    "constitution": 14,
    "intelligence": 10,
    "wisdom": 10,
    "charisma": 18
  },
  "archetype": "bard-enchanter",
  "combat_style": "support",
  "special_abilities": ["magic_resistance", "mirthful_leaps", "bardic_inspiration", "enthralling_performance"],
  "proficiencies": ["light_armor", "rapiers", "performance", "persuasion", "pipes"]
}
```

**Backstory Template:**
> In the Feywild, we revel for centuries. Wine, song, dance—endless, eternal. I thought I knew pleasure. Then I visited the mortal realm and met [MORTAL_NAME]. They were dying. They had [SHORT_TIME] to live. And in that time, they loved harder, laughed louder, felt more than I had in five hundred years. When they died, I understood: Limits create meaning. I've been chasing that intensity ever since. Every mortal moment burns brighter than a fey century.

**Campaign Hook Template:**
> [CAMPAIGN_EVENT] is the most intensely mortal thing I've encountered! I *must* experience it fully!

**Portrait Prompt:**
> Attractive satyr with small horns and goat legs, mischievous grin, pan pipes at hip, wine-stained clothing, surrounded by faint magical motes of joy, vibrant colors, whimsical fey style

**Best For Campaigns:** Feywild, A Midsummer Night's Chaos (!), themes of mortality, parties needing energy and chaos

---

## 30. The Survivor (Goblin Rogue)

**Default Names:** Snitch (M), Nyx (F)

**Concept:** A goblin who escaped the brutality of goblin society and now protects the little people.

**Universal Stats:**
```json
{
  "attributes": {
    "strength": 8,
    "dexterity": 18,
    "constitution": 12,
    "intelligence": 12,
    "wisdom": 12,
    "charisma": 10
  },
  "archetype": "rogue-scout",
  "combat_style": "melee-mobile",
  "special_abilities": ["fury_of_the_small", "nimble_escape", "sneak_attack", "cunning_action"],
  "proficiencies": ["light_armor", "daggers", "shortbows", "stealth", "survival"]
}
```

**Backstory Template:**
> Goblin tribes are cruel. The strong beat the weak. The chief eats first and most. I was always small, always beaten. When [ESCAPE_EVENT], I ran. Found the surface people. They're cruel too, sometimes. But they also have this thing called "fairness." Not everyone. But some. I decided to be some. Now I help those who can't help themselves—the small, the weak, the prey. Because someone should have helped me.

**Campaign Hook Template:**
> [CAMPAIGN_VICTIM] is being bullied by [CAMPAIGN_POWER]. I know which side I'm on.

**Portrait Prompt:**
> Small goblin with oversized clever eyes, scarred but kind expression, cobbled-together leather armor, daggers that are too big for them, defiant pose, underdog hero energy, determined lighting

**Best For Campaigns:** Underdog stories, protecting the weak, redemption themes, humor mixed with heart

---

## 31. The Ancient (Tortle Monk)

**Default Names:** Stone-Still (M), Tide-Patience (F)

**Concept:** An incredibly old tortle seeking the perfect death after a life of contemplation.

**Universal Stats:**
```json
{
  "attributes": {
    "strength": 14,
    "dexterity": 14,
    "constitution": 14,
    "intelligence": 10,
    "wisdom": 18,
    "charisma": 8
  },
  "archetype": "monk-defensive",
  "combat_style": "melee-defensive",
  "special_abilities": ["shell_defense", "unarmored_defense", "stunning_strike", "slowfall"],
  "proficiencies": ["simple_weapons", "shortswords", "religion", "insight"]
}
```

**Backstory Template:**
> I have lived [LONG_NUMBER] years. Seen empires rise and crumble to sand. Meditated on mountaintops while generations passed below. I am not afraid of death—it is simply the next meditation. But a Tortle's death should mean something. I have wandered seeking a worthy end: protecting something precious, defeating a great evil, finishing a task that matters. [CAMPAIGN_START] may finally be my purpose. Or not. Either way, I have time to find out. Just... not much.

**Campaign Hook Template:**
> I have waited centuries for something worth dying for. [CAMPAIGN_STAKES] may be it.

**Portrait Prompt:**
> Ancient tortle monk with weathered shell covered in carved wisdom, zen peaceful expression, simple monk robes, sitting in meditation pose, sense of immense patience and age, serene lighting

**Best For Campaigns:** High-stakes, epic finales, wisdom-needed scenarios, mentor figure potential

---

## 32. The Merchant Prince (Yuan-ti Warlock)

**Default Names:** Ssinssrath (M), Zsalissha (F)

**Concept:** A coldly logical yuan-ti seeking power through deals, viewing emotions as weaknesses.

**Universal Stats:**
```json
{
  "attributes": {
    "strength": 8,
    "dexterity": 14,
    "constitution": 12,
    "intelligence": 14,
    "wisdom": 10,
    "charisma": 18
  },
  "archetype": "mage-specialist",
  "combat_style": "magic-control",
  "special_abilities": ["magic_resistance", "poison_immunity", "eldritch_blast", "mask_of_many_faces"],
  "proficiencies": ["light_armor", "simple_weapons", "deception", "persuasion", "intimidation"]
}
```

**Backstory Template:**
> My people believe emotion is weakness, that cold logic and ambition are virtues. I was raised to manipulate, to scheme, to rise. My pact with [PATRON] was simple commerce: service for power. Efficient. But among the warm-blooded, I have observed... inefficiencies that produce results. "Loyalty." "Love." Illogical, yet powerful. I am conducting an experiment: What happens when a yuan-ti tries to feel? So far, results are... confusing.

**Campaign Hook Template:**
> [CAMPAIGN_FACTION] presents an opportunity for mutual benefit. I propose an alliance. The terms are negotiable.

**Portrait Prompt:**
> Yuan-ti pureblood with subtle serpentine features (slit pupils, hint of scales), impeccable expensive clothing, calculating expression, snake familiar nearby, cold beauty, business-meets-danger aesthetic

**Best For Campaigns:** Political intrigue, making deals with devils, character growth arcs, morally complex parties

---

## 33. The Orphan (Human Any Class - Child/Teen)

**Default Names:** Pip (M), Penny (F) — street names

**Concept:** A young person forced to grow up fast, with potential just waiting to emerge.

**Universal Stats:**
```json
{
  "attributes": {
    "strength": 10,
    "dexterity": 14,
    "constitution": 10,
    "intelligence": 12,
    "wisdom": 10,
    "charisma": 14
  },
  "archetype": "any-potential",
  "combat_style": "adaptive",
  "special_abilities": ["quick_learner", "innocent_facade", "survivor_instincts"],
  "proficiencies": ["light_armor", "daggers", "stealth", "sleight_of_hand", "streetwise"]
}
```

**Backstory Template:**
> I don't remember my parents. Maybe that's better. The streets of [CITY] raised me—running errands for [GANG/MERCHANT], sleeping in [SHELTER], eating what I could steal or earn. I've seen things kids shouldn't see. But I've also seen heroes—real ones—and I want to be like them someday. [PARTY_MEMBER/NPC] is the first adult who's treated me like I matter. I won't let them down.

**Campaign Hook Template:**
> The bad people are hurting [CAMPAIGN_VICTIMS], and no one's helping them. Someone has to. I guess it's us.

**Portrait Prompt:**
> Young human (early teens) with dirt-smudged face and old-soul eyes, worn clothing that's too big, hidden dagger, expression mixing vulnerability with street-smart wariness, hopeful despite everything, Oliver Twist meets fantasy

**Best For Campaigns:** Found family themes, protecting innocence, coming-of-age, parties that need someone to protect

---

## 34. The Revolutionary (Any Race Artificer/Wizard)

**Default Names:** Cole Gearwright (M), Ada Sparksmith (F)

**Concept:** A inventor/mage who believes magic should belong to everyone, not just the elite.

**Universal Stats:**
```json
{
  "attributes": {
    "strength": 8,
    "dexterity": 12,
    "constitution": 14,
    "intelligence": 18,
    "wisdom": 12,
    "charisma": 12
  },
  "archetype": "mage-inventor",
  "combat_style": "magic-utility",
  "special_abilities": ["magical_tinkering", "infusions", "flash_of_genius", "spell_storing"],
  "proficiencies": ["light_armor", "thieves_tools", "tinkers_tools", "arcana", "investigation"]
}
```

**Backstory Template:**
> The Academies hoard knowledge. The Guilds gate-keep power. A child dies of [PREVENTABLE_THING] while a wizard uses the same magic to chill their wine. I've had enough. I build things that *work*—for everyone. Healing devices for villages. Defense mechanisms for the poor. Magic for the masses. They call me dangerous. They're right. Ideas are dangerous. And I have so many ideas.

**Campaign Hook Template:**
> [CAMPAIGN_OPPRESSOR] represents everything wrong with how power is distributed. Time to redistribute.

**Portrait Prompt:**
> Determined inventor with goggles pushed up, practical work clothes covered in soot and grease, mechanical companion or floating tool, spark of righteous anger in eyes, workshop background, steampunk-fantasy blend

**Best For Campaigns:** Revolution themes, fighting oppression, magitech settings, campaigns questioning power structures

---

## 35. The Lost Royal (Any Race Noble Background)

**Default Names:** Prince/Princess [NAME] of [FALLEN KINGDOM]

**Concept:** Royalty in exile, stripped of power but not of responsibility or enemies.

**Universal Stats:**
```json
{
  "attributes": {
    "strength": 10,
    "dexterity": 12,
    "constitution": 10,
    "intelligence": 14,
    "wisdom": 12,
    "charisma": 16
  },
  "archetype": "any-leader",
  "combat_style": "adaptive",
  "special_abilities": ["inspiring_presence", "courtly_knowledge", "position_of_privilege", "linguist"],
  "proficiencies": ["rapiers", "history", "persuasion", "insight", "etiquette"]
}
```

**Backstory Template:**
> I was born to rule [KINGDOM]. Educated in statecraft, diplomacy, combat—everything a monarch needs. Then [USURPER/DISASTER] happened. My family is [STATUS]. I escaped with nothing but my name—and even that is dangerous now. There are those who would kill the last heir of [KINGDOM]. There are others who would use me. I must survive, grow strong, and decide: Do I want my throne back? Or did losing it show me something more important?

**Campaign Hook Template:**
> [CAMPAIGN_POLITICAL_ELEMENT] has ties to my kingdom's fall. This is not coincidence.

**Portrait Prompt:**
> Young noble with regal bearing despite worn traveling clothes, subtle royal jewelry hidden or damaged, expression mixing dignity with uncertainty, trained posture, lost crown energy, dramatic lighting

**Best For Campaigns:** Political intrigue, reclaiming birthright OR rejecting it, noblesse oblige themes, fish-out-of-water

---

# Campaign Pairing Recommendations

## A Midsummer Night's Chaos (Fantasy - Fae Comedy)
**Recommended Characters:**
- The Reveler (Satyr Bard) — Perfect thematic fit
- The Storyteller (Half-Elf Bard) — Theatrical energy
- The Gentle Giant (Firbolg Druid) — Fey connection
- The Wild Card (Gnome Sorcerer) — Chaos fits chaos
- The Pact-Bound (Tiefling Warlock) — Fey patron option
- The Seeker (Tabaxi Explorer) — Curiosity in the woods

## Abyssal Descent (Horror - Cave Survival)
**Recommended Characters:**
- The Ghost (Elf Infiltrator) — Stealth essential
- The Living Wall (Dwarf Defender) — Tank for survival
- The Veteran (Human Fighter) — Grounded horror protagonist
- The Faithful (Human Cleric) — Light in darkness
- The Hunter (Human Ranger) — Survival skills
- The Shadow (Human Assassin) — Ambush predator

## The Eternal Feast (Intrigue - Interdimensional Restaurant)
**Recommended Characters:**
- The Heartwarmer (Halfling Bard) — Service with a smile
- The Provocateur (Tiefling Bard) — Handles difficult customers
- The Merchant Prince (Yuan-ti Warlock) — Deal-making
- The Many-Faced (Changeling Rogue) — Multiple roles
- The Wild Card (Gnome Sorcerer) — Kitchen chaos
- The Scholar (Human Wizard) — Impossible dietary research

## The Dark Lord's Day Job (Urban - Reverse Isekai Comedy)
**Recommended Characters:**
- The Dashing Blade (Tiefling Duelist) — Style in mundanity
- The Berserker (Half-Orc Barbarian) — Fish out of water
- The Oathbound (Dragonborn Paladin) — Adjusting righteousness
- The Survivor (Goblin Rogue) — Street smarts
- The Reveler (Satyr Bard) — Culture shock
- The Construct (Warforged) — "What is a coffee?"

## Above the Cloudline (Adventure - Giant Exploration)
**Recommended Characters:**
- The Wanderer (Half-Elf Ranger) — Exploration focus
- The Lucky One (Halfling Trickster) — Size jokes, survival
- The Seeker (Tabaxi Explorer) — Curiosity
- The Grove Guardian (Wood Elf Druid) — Nature connection
- The Revolutionary (Artificer) — Problem-solving
- The Orphan (Human Any) — Fairy tale energy

---

# Implementation Notes

## For Claude Code / Ingestion:

1. **party_characters table** needs these fields:
   - character_template_id (reference to this template)
   - campaign_id (which campaign they're assigned to)
   - Customized backstory (fill-in-the-blanks completed)
   - Customized campaign_hook
   - Generated portrait_url

2. **Workflow:**
   - Select 4-6 templates per launch campaign
   - Use AI to fill backstory blanks with campaign-specific details
   - Generate portraits using prompts
   - Insert into database

3. **Portrait Generation:**
   - Use ImageFX/Whisk (free, manual)
   - Or Gemini image generation (automated)
   - Store URLs in Supabase storage

4. **Universal Stats → Ruleset Translation:**
   - Future Character Agent handles this
   - For now, stats are reference only
   - Franz can interpret archetype/combat_style for narrative purposes

---

*35 templates ready for campaign pairing and database insertion.*
