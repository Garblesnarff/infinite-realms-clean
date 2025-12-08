# World-Building Specification: The Halls of Valhalla

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Halls of Valhalla**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The players died heroically in battle and were chosen by Valkyries to enter Valhalla, where they fight by day and feast by night in preparation for Ragnarok. However, they discover someone is accelerating the prophesied apocalypse and corrupting the Nine Realms from within. The players must navigate Norse afterlife politics, prove themselves among legendary heroes, investigate across the Nine Realms, and ultimately face Ragnarok itself. Their choices will determine whether the cosmic cycle ends in oblivion, continues as fated, or transforms into something new. This is a campaign about facing inevitable doom with courage, the weight of destiny, and whether fate can be influenced or must be accepted.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the creation of the Nine Realms from Ymir's body and how Odin, Vili, and Ve shaped the cosmos.
    *   Write the history of the Aesir-Vanir war and the peace that followed, explaining the current divine order.
    *   Describe the Binding of Fenrir and how the gods' betrayal created the monster they feared.
    *   Explain Baldur's death, Loki's punishment, and how these events began the countdown to Ragnarok.
    *   Detail the creation of Valhalla and Folkvangr as afterlife realms for chosen warriors.
    *   Describe the role of Valkyries as choosers of the slain and servants of Odin.
    *   Explain the prophecy of Ragnarok in detail: the signs, the battles, the death of gods, and the promised rebirth.
    *   Write the history of human worship and how mortal belief empowers the gods.
    *   Describe Yggdrasil's nature as the cosmic axis connecting all realms.
    *   Explain the concept of wyrd (fate) and how even gods are bound by it.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Einherjar of Valhalla** (Major - Warrior Society)
        *   **Goals:** Prepare for Ragnarok through eternal combat, uphold warrior honor, feast and celebrate heroism, serve Odin.
        *   **Hierarchy:** Odin as All-Father, Valkyries as commanders, legendary heroes as champions, regular einherjar as warriors.
        *   **Public Agenda:** Train for the final battle, maintain readiness, celebrate glorious death.
        *   **Secret Agenda:** Some question the futility of eternal practice for inevitable doom; internal politics about who is "most honored"; fear of permanent death if Valhalla falls.
        *   **Assets:** Infinite resurrection (until Ragnarok), legendary weapons, divine mead and boar, Valhalla's halls, combat expertise.
        *   **Relationships:** Loyal to Odin but with varying degrees of questioning; respect Valkyries; rivalry with Folkvangr; prepared to fight giants and monsters.

    *   **The Aesir Gods** (Major - Divine Rulers)
        *   **Goals:** Maintain cosmic order, prepare for Ragnarok, preserve their realms, gather power through worship.
        *   **Hierarchy:** Odin as All-Father, Thor and other major gods as leaders, lesser gods and divine servants below.
        *   **Public Agenda:** Protect the Nine Realms, uphold justice and order, combat chaos and giants.
        *   **Secret Agenda:** Fear their prophesied doom; some seek ways to change fate; internal conflicts about how to face Ragnarok.
        *   **Assets:** Divine power, command of natural forces, Asgard fortress, Bifrost for travel, mortal worship.
        *   **Relationships:** Uneasy truce with Vanir gods; eternal conflict with giants; rely on einherjar armies; suspicious of Loki.

    *   **The Valkyries** (Minor - Divine Warriors)
        *   **Goals:** Choose the worthy slain, serve Odin, prepare heroes for Ragnarok, maintain Valhalla.
        *   **Hierarchy:** Brunhilde as leader, other named Valkyries, shield-maidens in training.
        *   **Public Agenda:** Fairly select the heroic dead, guide einherjar, serve as divine warriors.
        *   **Secret Agenda:** Some question Odin's choices; forbidden relationships with einherjar; fear of losing autonomy; wonder if endless war is truly honorable.
        *   **Assets:** Flight, combat prowess, ability to see heroic deaths, immortality, divine weapons.
        *   **Relationships:** Serve Odin but with personal agency; bond with einherjar; work alongside Freya; sometimes conflict with each other.

    *   **The Frost Giants of Jotunheim** (Major - Ancient Enemies)
        *   **Goals:** Survive, prepare for Ragnarok, take vengeance on the Aesir, reclaim stolen power.
        *   **Hierarchy:** Various giant jarls and kings, no single unified ruler, tribal structure.
        *   **Public Agenda:** Opposition to Asgard, gathering strength for the final battle.
        *   **Secret Agenda:** Not all want war; some seek survival over vengeance; internal divisions between warmongers and peace-seekers; fear they will be destroyed entirely in Ragnarok.
        *   **Assets:** Immense size and strength, frost magic, fortified mountain holds, ancient knowledge.
        *   **Relationships:** Ancient blood feud with Aesir; some dealings with Loki; view mortals as insignificant; respect strength.

    *   **Loki's Conspiracy** (Minor - Hidden Faction)
        *   **Goals:** Survive Ragnarok, rule the reborn cosmos, ensure his own memory and power endure, revenge on the gods.
        *   **Hierarchy:** Loki as architect, corrupted einherjar as agents, manipulated giants and spirits as pawns.
        *   **Public Agenda:** None - operates in secret.
        *   **Secret Agenda:** Accelerate Ragnarok, corrupt Yggdrasil, rewrite fate threads, position himself to survive and rule after the rebirth.
        *   **Assets:** Master manipulation, shape-shifting, agents throughout the realms, knowledge of fate-weaving, divine cunning.
        *   **Relationships:** Pretends loyalty to Asgard; manipulates all sides; uses his children (Fenrir, Hel, Jormungandr) as weapons; genuinely believes he's saving something rather than being purely evil.

    *   **The Dishonored Dead of Hel** (Minor - Neutral Afterlife)
        *   **Goals:** Exist in peace, seek recognition, avoid annihilation in Ragnarok, serve goddess Hel.
        *   **Hierarchy:** Hel as goddess-ruler, spirits of the unheroic dead as inhabitants.
        *   **Public Agenda:** Acceptance of their fate, neither heaven nor hell, simple existence.
        *   **Secret Agenda:** Resent being considered "lesser" than einherjar; some seek ways to prove heroism; Hel seeks greater standing among the gods.
        *   **Assets:** Vast numbers, knowledge of death and spirits, Hel's divine power, underground realm.
        *   **Relationships:** Outcasts from divine society; Hel is Loki's daughter but acts independently; resentful of but not hostile to Asgard; simply want to matter.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Odin All-Father:** King of Asgard, god of wisdom, war, and death. Sacrificed eye for wisdom. Knows Ragnarok is coming but seeks to change it.
    *   **Thor Odinson:** God of thunder, protector of Midgard, fated to die killing Jormungandr. Brave and straightforward.
    *   **Loki Laufeyson:** Trickster god, blood-brother to Odin, secretly orchestrating the conspiracy. Brilliant and bitter.
    *   **Brunhilde:** Lead Valkyrie, chooser of the slain, torn between duty and love. The players' primary contact.
    *   **Freya:** Goddess of love and war, mourns Baldur, commands half of einherjar in Folkvangr. Powerful and grieving.
    *   **Heimdall:** Watchman of the gods, sees and hears all, bound by oaths to not interfere directly. Guardian of Bifrost.
    *   **Hel:** Goddess of the dishonored dead, half-living half-corpse, seeks recognition. Loki's daughter but independent.
    *   **Fenrir:** The great wolf, bound by the gods, will break free at Ragnarok. Vengeful but justified in rage.
    *   **Sigurd Dragonslayer:** Legendary einherjar, slayer of Fafnir, proud champion who becomes ally/rival to players.
    *   **The Norns (Urd, Verdandi, Skuld):** Three weavers of fate, ancient beyond gods, cryptic and bound by cosmic rules.

*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Veteran Einherjar Warrior (Various Eras)" - Create Norse warriors from different time periods with distinct personalities.
    *   "Valkyrie Shield-Maiden" - Divine warrior chooser of slain with personal motivations.
    *   "Frost Giant Warrior" - Massive combatant from Jotunheim with grudges against gods.
    *   "Frost Giant Peace-Seeker" - Rare giant who questions the eternal war.
    *   "Corrupted Einherjar (Loki's Agent)" - Secretly working for the conspiracy.
    *   "Lesser Aesir God" - Minor deities with specific domains and personalities.
    *   "Spirit of Hel's Realm" - Faded ghost of someone who died unheroically.
    *   "Midgard Mortal" - Living humans who worship the gods and fear Ragnarok.
    *   "Dwarf Smith" - Crafters of legendary weapons from Svartalfheim.
    *   "Jormungandr Cultist" - Worshipper of the World Serpent preparing for its rising.

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**

    *   **Valhalla - The Hall of the Slain:**
        *   **Key Landmarks:** Odin's high throne, five hundred and forty massive doors, endless training grounds, feast tables stretching to horizon, armories of legendary weapons, the healing halls where einherjar resurrect.
        *   **Primary Inhabitants:** Odin, Valkyries, hundreds of legendary einherjar from all eras, serving spirits, Huginn and Muninn (Odin's ravens).
        *   **Available Goods & Services:** Infinite mead and boar, weapon training, resurrection after death in combat, audience with Odin, legendary weapon armory, tactical planning for Ragnarok.
        *   **Potential Random Encounters (x5):** Epic duel between legendary heroes; Valkyrie arriving with new einherjar; Odin walking disguised among warriors; discovery of a corrupted einherjar; sudden combat drill announced by horn-blast.
        *   **Embedded Plot Hooks & Rumors (x3):** "Some warriors aren't resurrecting properly." "Odin has been consulting the Norns more frequently." "A Valkyrie was seen crying in the armory." "The mead tastes different lately - something's wrong."
        *   **Sensory Details:** Sight (Golden halls impossibly vast, shields lining walls, weapons everywhere, firelight dancing). Sound (Clash of combat, victory songs, horn blasts, the crackle of central fires). Smell (Roasted boar, mead, leather and metal, smoke from fires). Touch (Worn weapon grips, rough wooden tables, cold metal armor). Taste (Perfectly seasoned boar, sweet divine mead that never causes hangover).

    *   **The Bifrost Bridge:**
        *   **Key Landmarks:** Heimdall's watchtower at the Asgard end, the rainbow bridge itself stretching across void, gates to other realms.
        *   **Primary Inhabitants:** Heimdall the Watchman, occasional travelers with permission.
        *   **Available Goods & Services:** Travel to other Nine Realms (with permission), information from Heimdall who sees all, warnings of approaching threats.
        *   **Potential Random Encounters (x5):** Heimdall testing travelers' worthiness; glimpse of events in other realms below; aurora lights dancing; feeling of being watched by All-Father; frost giant raiders attempting to cross.
        *   **Embedded Plot Hooks & Rumors (x3):** "Heimdall seems troubled but won't say why." "The bridge flickers sometimes now - it never did before." "Something is moving in the void beneath the bridge."
        *   **Sensory Details:** Sight (Impossible rainbow colors, transparent yet solid, stars and realms visible below, Asgard behind, destinations ahead). Sound (Ethereal humming, wind across void, Heimdall's horn). Smell (Ozone, something like distant flowers). Touch (Solid as stone but warm, vibrating slightly with power). Taste (Air tastes of color and light).

    *   **Yggdrasil - The World Tree:**
        *   **Key Landmarks:** The massive trunk visible from all realms, three great roots (to Asgard, Jotunheim, Niflheim), the Well of Urd at base, branches stretching into cosmos, the dragon Nidhogg gnawing at roots.
        *   **Primary Inhabitants:** Ratatoskr (squirrel messenger), Nidhogg (dragon), spirits of the tree, the Norns at Well of Urd.
        *   **Available Goods & Services:** Travel between realms via branches and roots, visions from the well's water, communion with cosmic forces, ancient wisdom.
        *   **Potential Random Encounters (x5):** Nidhogg attacking roots; messages from Ratatoskr the squirrel; spirits of the tree granting visions; evidence of corruption in the bark; the Norns weaving at their loom.
        *   **Embedded Plot Hooks & Rumors (x3):** "The tree bleeds where it shouldn't." "Nidhogg seems stronger than before." "The Norns are reweaving threads that were already set." "Some branches have withered."
        *   **Sensory Details:** Sight (Impossibly massive tree trunk, bark carved with natural runes, green leaves despite cosmic void, roots like mountains). Sound (Creaking wood like ancient forest, gnawing of Nidhogg, whisper of leaves, drip of sap). Smell (Ancient wood, fresh growth, decay at roots, something pure). Touch (Warm living bark, sticky sap that grants visions). Taste (Sap is sweet and grants momentary wisdom).

    *   **Jotunheim - Land of Giants:**
        *   **Key Landmarks:** Massive ice mountains, giant fortresses carved from stone, the throne-hall of the giant kings, frozen rivers, aurora-lit skies.
        *   **Primary Inhabitants:** Frost giants of various clans, ice trolls, winter spirits, massive predators.
        *   **Available Goods & Services:** Trade (if you can earn respect), giant-forged weapons, frost magic knowledge, political alliances (difficult).
        *   **Potential Random Encounters (x5):** Frost giant patrol; winter storm manifestation; ice drake; giant smithy at work; two giant clans feuding.
        *   **Embedded Plot Hooks & Rumors (x3):** "Some giants speak of peace." "Loki visited the winter king recently." "Weapons for Ragnarok are being forged." "A giant remembers when gods and giants were kin."
        *   **Sensory Details:** Sight (Everything built to massive scale, ice and stone, aurora colors in sky, frost patterns). Sound (Howling wind, giant footsteps like thunder, ice cracking, distance roars). Smell (Sharp cold, stone, something ancient). Touch (Biting cold, everything too large to grasp properly). Taste (Ice that burns tongue, iron in the air).

    *   **Hel - Realm of the Dishonored Dead:**
        *   **Key Landmarks:** Hel's hall (half beautiful, half decayed), fields of mist, the river Gjoll with its bridge, gates guarded by Garm the hound.
        *   **Primary Inhabitants:** Goddess Hel, spirits of those who died of sickness or age, the hound Garm.
        *   **Available Goods & Services:** Audience with Hel, communion with the dead, knowledge of death and spirits, passage to and from (difficult).
        *   **Potential Random Encounters (x5):** Faded spirits seeking recognition; Garm patrolling; Hel's half-corpse face observing; memories manifesting as ghostly scenes; souls bargaining for better fate.
        *   **Embedded Plot Hooks & Rumors (x3):** "Hel seeks greater standing among gods." "Some spirits here were heroes but died 'wrong.'" "Loki visits his daughter in secret." "Baldur's spirit is kept here against his will."
        *   **Sensory Details:** Sight (Colorless, misty, everything faded, Hel's hall split between life and death). Sound (Whispers, distant weeping, hollow echoes, nothing quite solid). Smell (Must and cold, not unpleasant but empty). Touch (Everything feels distant, numb, neither warm nor cold). Taste (Everything tastes of nothing, even food has no flavor).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**

    *   **IF:** Players earn high reputation among einherjar through combat prowess.
    *   **THEN:** Legendary heroes seek them out for alliances. Gain access to Valhalla's deepest armories. Odin grants private audience. Other einherjar follow their commands in battle. Generate scenes of respect and growing leadership.

    *   **IF:** Players uncover evidence of Loki's conspiracy.
    *   **THEN:** Loki becomes aware of their investigation. Sabotage and assassination attempts increase. His agents spread misinformation. The conspiracy accelerates its timeline. Generate encounters with corrupted NPCs and misleading clues.

    *   **IF:** A major prophecy of Ragnarok is fulfilled (Fenrir breaks a chain, Fimbulwinter begins, a god dies early).
    *   **THEN:** The Ragnarok counter advances. Environmental changes reflect approaching doom (darker skies, colder weather, more desperate NPCs). New threats emerge. Generate reactions from major NPCs about fate's inevitability.

    *   **IF:** Players ally with frost giants or other "enemy" factions.
    *   **THEN:** Some Asgard NPCs distrust them. Others see them as visionaries. The political landscape shifts. Generate both support from unexpected allies and condemnation from traditionalists.

    *   **IF:** Players discover ways to slow Ragnarok's approach.
    *   **THEN:** The cosmic balance feels wrong. Some NPCs fear breaking fate worse than doom. Others desperately support any hope. Loki's conspiracy works harder to accelerate events. Generate moral debates about whether changing fate is right.

    *   **IF:** A player character permanently dies before Ragnarok.
    *   **THEN:** Funeral in Valhalla, memorial scenes, impact on party morale. The sacrifice might have cosmic significance. Generate grief responses from NPCs who bonded with the character. Possible resurrection quest if party pursues it.

    *   **IF:** Ragnarok begins (counter reaches zero).
    *   **THEN:** Massive world state change. All prophecied events start happening. The sky darkens, Fenrir breaks free, Jormungandr rises, fire and ice armies march. Valhalla mobilizes for war. All NPCs shift to wartime priorities. Generate epic scale battles and apocalyptic atmosphere.

    *   **IF:** Players defeat or redeem Loki.
    *   **THEN:** His conspiracy collapses or transforms depending on how handled. Agents lose direction or seek redemption. The fate-weaving stabilizes or completes corruption. Generate consequences based on whether Loki died, was imprisoned, or was convinced to change.

    *   **IF:** Players choose to break the cycle of fate entirely.
    *   **THEN:** Reality becomes unstable. Gods and NPCs divided between hope and horror. Unforeseen consequences emerge. The Nine Realms might become frozen between death and life. Generate existential consequences and philosophical debates.

    *   **IF:** Players embrace fate and die gloriously in the final battle.
    *   **THEN:** Bittersweet ending where their sacrifice has meaning. The rebirth happens as prophesied but influenced by their choices. Their saga becomes legend. Generate memorial scenes and echoes of their influence in the new world.

**7. Mechanics & Systems**
*   **Resurrection Mechanics:** In Valhalla and during Ragnarok, slain characters resurrect at dawn. Track "Glorious Deaths" - dying heroically grants temp bonuses. Special circumstances (soul destruction, world-ending moments) can cause permanent death.
*   **Wyrd Points System:** Fate currency earned through heroic deeds and Norse virtues. Spend for rerolls, special abilities, or to break prophecy. Running out means fate works against you.
*   **Ragnarok Counter:** Visible countdown tracking approach of apocalypse. Major events advance it. Creates urgency and allows players to see consequences of actions.
*   **Reputation Tracking:** Measure standing with einherjar, gods, giants, and other factions. High reputation unlocks allies, weapons, and information.
*   **Legendary Weapon Growth:** Weapons gain power and names through heroic deeds. Track accomplishments with each weapon to unlock properties.

**8. Theme & Tone Consistency**
*   **Core Themes:** Facing inevitable doom with courage, the weight of destiny, whether fate can be changed or only faced with dignity, the glory and futility of eternal combat, sacrifice that has meaning even in defeat, the cycle of death and rebirth.
*   **Tone Guidance:** Epic and weighty, but not hopeless. Bittersweet - glory and doom intertwined. Brutal combat but honorable. Cosmic scale but personal stakes. The approaching end makes every moment significant.
*   **Avoid:** Making it grimdark without hope, treating death casually since resurrection is common, simplifying Norse mythology into generic fantasy, making Loki one-dimensional evil rather than complex villain with valid grievances.
