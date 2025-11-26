### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Wendigo Hunger**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** A harsh winter has trapped a remote northern settlement in snow and ice, cutting them off from the outside world. As supplies dwindle and desperation grows, something ancient awakens in the frozen wilderness—the Wendigo, a spirit of insatiable hunger and cannibalism. The players must survive the brutal winter, resist the growing temptation of forbidden hungers, and discover which among the survivors has already been possessed by the Wendigo spirit before it spreads and consumes everyone. The hunger is inside them all.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the founding of Fort Winterhold as a northern trading post and military outpost.
    *   Write the history of the indigenous peoples of the region and their sacred taboos against cannibalism.
    *   Describe the legend of the first Wendigo: a shaman who consumed his entire tribe during a terrible winter 500 years ago.
    *   Explain the nature of the Wendigo curse: how it spreads, how it corrupts, and why it cannot be killed by conventional means.
    *   Detail past Wendigo outbreaks in the region and how they were (temporarily) stopped.
    *   Write about the Ancient Burial Mound and the frozen heart that sustains the Wendigo spirit.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Survivors** (Major)
        *   **Goals:** To survive the winter and escape the fort when the snows clear.
        *   **Hierarchy:** Officially led by Commander Bjorn Ironhand. Includes soldiers, traders, trappers, and indigenous guides.
        *   **Public Agenda:** We stick together, ration supplies, and wait for spring.
        *   **Secret Agenda:** As starvation sets in, fractures appear. Some hoard food, others consider desperate measures, and a few are already possessed.
        *   **Assets:** The fort's defenses, dwindling food supplies, winter survival skills, weapons and ammunition.
        *   **Relationships:** Internal paranoia and distrust growing; some look to Elder Miksa for spiritual guidance; others rely on the players for leadership.
    *   **The Possessed** (Major - Hidden Faction)
        *   **Goals:** To feed the endless hunger and spread the Wendigo corruption to all survivors.
        *   **Hierarchy:** No formal structure. The Wendigo spirit coordinates through psychic connection to those it possesses. Commander Bjorn is the first secretly possessed.
        *   **Public Agenda:** Unknown. They appear as normal survivors experiencing hardship.
        *   **Secret Agenda:** To isolate victims, encourage cannibalism, destroy food supplies, and ultimately transform everyone into Wendigo thralls.
        *   **Assets:** Superhuman strength and speed when revealed, ability to survive in the cold, psychic communication with the Wendigo spirit.
        *   **Relationships:** Actively sabotaging survival efforts; targeting the weak and isolated; opposing Elder Miksa and the players.
    *   **The Spirit Keepers** (Minor)
        *   **Goals:** To uphold the old ways and prevent the Wendigo's return through ritual and tradition.
        *   **Hierarchy:** Led by Elder Miksa. Includes a few indigenous guides and believers in the old traditions.
        *   **Public Agenda:** We must maintain the taboos and resist the hunger.
        *   **Secret Agenda:** Miksa knows a ritual to destroy the Wendigo permanently but it requires a willing sacrifice from someone already corrupted.
        *   **Assets:** Knowledge of ancient rituals, spiritual protections, understanding of the Wendigo's nature.
        *   **Relationships:** Trying to guide the players; distrusted by some survivors as superstitious; hunted by the possessed.
    *   **The Pragmatists** (Minor)
        *   **Goals:** Survival by any means necessary, including breaking taboos if required.
        *   **Hierarchy:** Informal alliance of survivors who prioritize practical survival over morality. May include the cook, some trappers, and desperate civilians.
        *   **Public Agenda:** We do what we must to survive.
        *   **Secret Agenda:** Some are considering cannibalism of the dead as a survival strategy. They don't realize this invites the Wendigo's corruption.
        *   **Assets:** Practical skills, willingness to make hard choices, food that may be hoarded.
        *   **Relationships:** Opposed to the Spirit Keepers' restrictions; may seek the players' support for controversial decisions; unknowingly vulnerable to possession.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **The Wendigo Spirit:** An ancient evil that possesses cannibals. Manifests as a towering skeletal creature covered in ice with a frozen heart. Cannot be permanently killed while its heart remains.
    *   **Elder Miksa:** Wise keeper of indigenous lore, knows the Wendigo's nature and how to fight it. Possesses the purification ritual.
    *   **Commander Bjorn Ironhand:** The fort's military leader, secretly one of the first to be possessed. Uses his authority to isolate victims.
    *   **Sasha Brightclaw:** The fort's best hunter, carrying guilt from past survival cannibalism. The Wendigo's presence is reawakening her trauma.
    *   **Doctor Henrik Frost:** The fort's physician, desperately trying to understand the strange illness affecting survivors. May discover the possession.
    *   **Yura the Cook:** Practical and resourceful, but increasingly willing to consider taboo food sources as supplies run out.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Starving Civilian"
    *   "Paranoid Soldier"
    *   "Partially Possessed Survivor (early transformation)"
    *   "Indigenous Guide Who Knows the Old Ways"
    *   "Trader with Hoarded Supplies"
    *   "Child Separated from Parents"
    *   "Fully Transformed Wendigo Thrall"
    *   "Desperate Parent Willing to Do Anything"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **Fort Winterhold:** A remote trading post and military outpost, now snowbound and isolated.
        *   **Key Landmarks:** The Great Hall (central gathering and rationing point), Commander's Office, Barracks, Food Storehouse (burned), Walls and Gates, Medical Ward.
        *   **Primary Inhabitants:** ~40 survivors including soldiers, traders, trappers, indigenous guides, and civilians. Several are secretly possessed.
        *   **Available Goods & Services:** Rationed food (dwindling), medical care (limited supplies), shelter, warmth from central fires.
        *   **Potential Random Encounters (x5):** Finding evidence of food theft, witnessing a survivor exhibiting strange behavior, a possessed individual attacking someone in secret, a desperate survivor proposing cannibalism, discovering a frozen corpse with bite marks.
        *   **Embedded Plot Hooks & Rumors (x3):** "Commander Bjorn has been acting strange." "Food is disappearing faster than rationing accounts for." "Elder Miksa knows something she's not sharing."
        *   **Sensory Details:** Sight (Wooden walls caked with snow and ice, dim firelight through windows, frost on every surface), Sound (Howling wind, crackling fires, whispered conversations, distant screams), Smell (Wood smoke, unwashed bodies, desperation).
    *   **The Frozen Wastes:** The surrounding wilderness—endless snow, frozen forests, and howling winds.
        *   **Key Landmarks:** The Frozen Lake, the Dead Forest (bare trees), Snow Drifts (some hiding horrors), Hunting Grounds (now devoid of game).
        *   **Primary Inhabitants:** The Wendigo spirit, transformed thralls, dying wildlife, frozen corpses from previous hunting parties.
        *   **Available Goods & Services:** None. This is a place of death and danger.
        *   **Potential Random Encounters (x5):** A blizzard reducing visibility to zero, finding tracks of something massive and inhuman, discovering a hunting party's frozen corpses, being stalked by the Wendigo, experiencing hypothermia and frostbite.
        *   **Embedded Plot Hooks & Rumors (x3):** "The wildlife fled weeks before the first snow." "There's a cave system where the Wendigo drags its victims." "The burial mound is three days' journey north."
        *   **Sensory Details:** Sight (Endless white, skeletal trees, blood on snow, northern lights), Sound (Wind howling, branches cracking from ice, distant screams, silence), Smell (Nothing—the cold kills all scent, frost in nostrils).
    *   **The Bone Cave:** A cave system where the Wendigo drags victims, filled with centuries of remains.
        *   **Key Landmarks:** The entrance (a dark mouth in a snow drift), tunnels lined with bones, the feeding chamber (gnawed corpses), ice formations like frozen blood.
        *   **Primary Inhabitants:** The Wendigo (when it lairs here), partially transformed thralls, the spirits of the consumed.
        *   **Available Goods & Services:** None. Only horror and death.
        *   **Potential Random Encounters (x5):** Finding a recent victim still barely alive, being ambushed by thralls, discovering evidence of the Wendigo's centuries-long existence, experiencing visions of past victims, direct confrontation with the Wendigo.
        *   **Embedded Plot Hooks & Rumors (x3):** "The cave goes deep into the mountain." "The bones tell a story of hundreds of victims." "Something guards this place."
        *   **Sensory Details:** Sight (Darkness broken only by dim light, bones everywhere, ice gleaming), Sound (Dripping water, crunching bones underfoot, distant growling, echoes), Smell (Decay, ancient blood, cold stone).
    *   **The Ancient Burial Mound:** The site where the original shaman consumed his tribe. The Wendigo's frozen heart is buried here.
        *   **Key Landmarks:** The mound itself (a hill covered in ancient markers), a ritual circle carved into ice, the burial chamber beneath, the frozen heart (glowing with malevolent energy).
        *   **Primary Inhabitants:** The Wendigo spirit's essence, protective spirits of the consumed tribe, Wendigo thralls guarding the site.
        *   **Available Goods & Services:** None. This is the final confrontation site.
        *   **Potential Random Encounters (x5):** Visions of the original tribe's destruction, waves of Wendigo thralls attacking, the spirit manifesting in full form, spiritual guardians testing the party's worthiness, Elder Miksa performing the purification ritual.
        *   **Embedded Plot Hooks & Rumors (x3):** "The heart must be destroyed to end the curse." "A willing sacrifice is required." "The spirits of the original tribe still linger here."
        *   **Sensory Details:** Sight (Ancient stone markers, ice-covered mound, glowing heart visible through ice, spectral figures), Sound (Ancient chanting echoing, wind screaming, heartbeat rhythm), Smell (Ancient death, ozone, spiritual energy).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** A player character commits cannibalism or fails to stop another from doing so.
    *   **THEN:** That player gains Corruption Points. The Wendigo's presence becomes stronger. More survivors begin to succumb to the temptation.
    *   **IF:** The players successfully identify and eliminate a possessed individual before they spread the corruption.
    *   **THEN:** The Wendigo's influence temporarily weakens. Survivors' morale improves. However, paranoia increases as people realize the threat is among them.
    *   **IF:** The players fail to maintain adequate food supplies and rationing breaks down.
    *   **THEN:** Starvation sets in rapidly. Hunger levels increase across all characters. Desperate survivors turn to cannibalism. Wendigo possessions multiply.
    *   **IF:** Commander Bjorn's possession is exposed.
    *   **THEN:** The fort's leadership collapses into chaos. The possessed reveal themselves and attack openly. The players must take command or the survivors will be picked off one by one.
    *   **IF:** A player character reaches 10 Corruption Points and transforms fully.
    *   **THEN:** That character becomes an NPC Wendigo thrall under the DM's control. The other players must decide whether to try to save them or destroy them. The transformation is traumatic for the group.
    *   **IF:** The players successfully perform the purification ritual at the Ancient Burial Mound.
    *   **THEN:** The Wendigo's frozen heart is destroyed. All possessed individuals either die or are freed from the curse. The winter immediately begins to break. Those with Corruption Points are purified but scarred by the experience. The region is safe—for now.
