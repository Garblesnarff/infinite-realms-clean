### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**Threads of the Pattern**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** In a world where the Dark One strains against his prison and the Wheel of Time turns toward the Last Battle, the players discover they are Ta'veren—individuals around whom the Pattern itself bends, forcing probability and destiny to converge. As channelers of the One Power divided into male Saidin (tainted with madness) and female Saidar (pure), they must navigate prophecy, unite fractured nations, battle Shadowspawn and Forsaken, and face the Dark One himself while deciding whether to fulfill destiny or defy it.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the Breaking of the World—when Lews Therin and male Aes Sedai went mad and shattered civilization.
    *   Write the history of the Age of Legends, its wonders, and how the Dark One was freed and re-imprisoned.
    *   Describe the Prophecies of the Dragon and signs of the Dragon's Rebirth.
    *   Explain the One Power: Saidin and Saidar, the five elements, weaving, and why Saidin is tainted.
    *   Detail the formation and structure of the White Tower and the seven Ajahs of Aes Sedai.
    *   Write about the Forsaken—their identities, powers, and what they want in the Third Age.
    *   Describe the Dark One's prison, how it was made, and why the seals are failing.
    *   Explain Tel'aran'rhiod, the World of Dreams, and its role in the Pattern.
    *   Detail the concept of Ta'veren and how the Pattern uses them to correct its course.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The White Tower (Aes Sedai)** (Major)
        *   **Goals:** Guide the world to the Last Battle, find and control the Dragon Reborn, preserve knowledge and order.
        *   **Hierarchy:** Amyrlin Seat leads, seven Ajahs (Blue, Red, Green, Gray, White, Brown, Yellow) each with their own focus. Hall of the Tower legislates.
        *   **Public Agenda:** We serve all, guiding humanity and fighting the Shadow with the One Power.
        *   **Secret Agenda:** Deeply divided by Ajah politics, infiltrated by the Black Ajah (Darkfriends), many schemes to control rather than serve.
        *   **Assets:** Most powerful channelers, vast library, political influence across nations, Warders, Eyes and Ears (spy network).
        *   **Relationships:** Respected and feared by nations; opposed by Children of the Light; hunting male channelers; manipulating rulers.

    *   **The Children of the Light (Whitecloaks)** (Major - Antagonist to channelers)
        *   **Goals:** Destroy all Darkfriends and channelers, impose their version of Light through military force.
        *   **Hierarchy:** Lord Captain Commander leads, divided into legions, includes the Questioners (torturers and inquisitors).
        *   **Public Agenda:** We are the pure warriors of Light, cleansing the world of Shadow without tainted magic.
        *   **Secret Agenda:** Infiltrated by actual Darkfriends at high levels; many are zealots who cause more harm than good.
        *   **Assets:** Large military force, fanatical devotion, political power in Amadicia, network of informants.
        *   **Relationships:** Hostile to Aes Sedai and all channelers; oppose many rulers; actually infiltrated by the Shadow they claim to fight.

    *   **The Aiel** (Major)
        *   **Goals:** Follow ji'e'toh (honor/obligation system), seek the Car'a'carn prophesied to lead them, hold toh (obligation) for the past.
        *   **Hierarchy:** Led by clan chiefs and Wise Ones (female channelers), organized by clan and sept, complex honor-based society.
        *   **Public Agenda:** We are the deadliest warriors in the world, holding to our honor code in the Three-fold Land (Aiel Waste).
        *   **Secret Agenda:** Carrying deep shame—they abandoned the Way of the Leaf and their service to Aes Sedai, building their culture on broken oaths.
        *   **Assets:** Unmatched warriors, Wise Ones who channel, knowledge of the Waste, prophecy of the Car'a'carn.
        *   **Relationships:** Hostile to "wetlanders" historically; will follow the Car'a'carn; Wise Ones coordinate with some Aes Sedai.

    *   **The Forsaken** (Major - Antagonist)
        *   **Goals:** Serve the Dark One, gain power in the new world order, achieve immortality and dominance.
        *   **Hierarchy:** Thirteen Forsaken freed from prison, nominally serving the Dark One but constantly scheming against each other. Nae'blis (highest servant) promised to one.
        *   **Public Agenda:** None—they operate through manipulation, disguise, and proxies.
        *   **Secret Agenda:** Each wants to be Nae'blis. Most serve from ambition or nihilism rather than pure evil. Some could be turned.
        *   **Assets:** Age of Legends knowledge, immense Power, immortality, Shadowspawn armies, Darkfriend networks.
        *   **Relationships:** Manipulate all sides; war among themselves; create False Dragons and chaos; hunt the true Dragon.

    *   **The Black Tower** (Minor - Emerges later)
        *   **Goals:** Train male channelers before they go mad, prove men can channel safely, support the Dragon Reborn.
        *   **Hierarchy:** Led by Mazrim Taim, organized into ranks (Soldier, Dedicated, Asha'man—guardian).
        *   **Public Agenda:** We are weapons for the Last Battle, male channelers finally organized and trained.
        *   **Secret Agenda:** Infiltrated by Darkfriends at leadership level; Taim may be training male channelers for the Shadow.
        *   **Assets:** Growing number of male channelers, aggressive combat training, lack of political entanglements.
        *   **Relationships:** Opposed by Aes Sedai; supported cautiously by the Dragon; feared by everyone; some want to bond Aes Sedai as weapons.

    *   **The Seanchan Empire** (Minor - Invaders)
        *   **Goals:** Conquer the westlands and return them to the Empire, enslave all channelers as damane (property).
        *   **Hierarchy:** Imperial family descended from Artur Hawkwing, rigid caste system, sul'dam (leash-holders) control damane.
        *   **Public Agenda:** We bring order to chaos, reclaiming our ancestor Hawkwing's lands.
        *   **Secret Agenda:** Their entire society is built on the lie that sul'dam cannot channel (they can, they just don't know it).
        *   **Assets:** Vast armies, exotic creatures (raken, grolm, corlm), enslaved channelers in a'dam, superior organization.
        *   **Relationships:** At war with westland nations; see Aes Sedai as marath'damane (must be leashed); some prophecy suggests alliance.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Moiraine Damodred:** Blue Ajah Aes Sedai, seeker of the Dragon, devoted to the Light, foresees her own sacrifice.
    *   **Lan Mandragoran:** Warder, last king of Malkier, weapon-master, death-wish battling duty.
    *   **Ishamael/Ba'alzamon:** Chief Forsaken, nihilistic philosopher, Dragon's eternal enemy, insane from partial imprisonment.
    *   **Lanfear:** Most powerful female Forsaken, manipulator of dreams, obsessed with the Dragon she loved as Lews Therin.
    *   **Padan Fain:** Darkfriend twisted by the Dark One and Shadar Logoth, hound tracking the Dragon, embodiment of dual corruption.
    *   **Rand al'Thor (potential):** The Dragon Reborn, shepherd bearing impossible destiny, containing Lews Therin's memories, fracturing under pressure.
    *   **Siuan Sanche:** Amyrlin Seat, secretly guiding toward Last Battle, fallen from power but still fighting.
    *   **Mazrim Taim:** False Dragon or ally? Leader of the Black Tower, powerful and ambiguous, possibly Darkfriend.

*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Aes Sedai of [Ajah] with political agenda"
    *   "Warder devoted to their Aes Sedai"
    *   "Child of the Light zealot"
    *   "Aiel Clan Chief or Wise One"
    *   "Male channeler on the edge of madness"
    *   "Darkfriend hidden in plain sight"
    *   "Noble playing Daes Dae'mar (political game)"
    *   "Wolfbrother connected to Tel'aran'rhiod"
    *   "Ogier Treesinger seeking Stedding"
    *   "Seanchan sul'dam and her damane"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **Tar Valon and the White Tower:**
        *   **Key Landmarks:** The White Tower (impossible white spire), Hall of the Tower, Ajah quarters, Warder yards, harbors, Shining Walls.
        *   **Primary Inhabitants:** Aes Sedai of all Ajahs, Warders, Accepted and Novices in training, servants, supplicants.
        *   **Available Goods & Services:** Healing (Yellow Ajah), political mediation (Gray), legal advice, access to the library, Warder training.
        *   **Potential Random Encounters (x5):** Ajah politics turning deadly; Black Ajah operating in secret; Accepted's testing going wrong; male channeler captured; dragon-omen appearing in sky.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Black Ajah is real and runs deeper than anyone knows." "The Amyrlin is secretly guiding the Dragon Reborn." "The Tower itself is ter'angreal (magic item) of unknown function."
        *   **Sensory Details:** Sight (white Tower reaching impossible heights, colored Ajah shawls, Warder cloaks that shift color), Sound (novices reciting catechisms, swords clashing in yards, powerful weaves humming), Smell (perfumed Aes Sedai, leather from Warder yards, age and power).

    *   **The Aiel Waste (Three-fold Land):**
        *   **Key Landmarks:** Rhuidean (sacred city), Alcair Dal (meeting ground), holds (Aiel dwellings), Dragonwall mountains.
        *   **Primary Inhabitants:** Aiel warriors and Wise Ones, Jenn Aiel remnant in Rhuidean, ji'e'toh society.
        *   **Available Goods & Services:** Water (precious), training in spear and hand-fighting, Wise One wisdom, access to prophecy.
        *   **Potential Random Encounters (x5):** Challenge to honor (ji'e'toh); Bleakness (Aiel who learn the truth and break); Wise One channeling; trial to enter Rhuidean; vision of the past.
        *   **Embedded Plot Hooks & Rumors (x3):** "Rhuidean contains prophecy and terrible truth about Aiel past." "The Car'a'carn will unite the clans." "The Shaido clan serves the Shadow."
        *   **Sensory Details:** Sight (endless desert, Aiel in cadin'sor, distant heat shimmer), Sound (wind, silence, spear-clashing), Smell (dry dust, sweat, distant rain that never comes).

    *   **Shayol Ghul and the Blight:**
        *   **Key Landmarks:** Shayol Ghul (mountain prison), the Pit of Doom, Thakan'dar (Trolloc forges), corrupted landscape.
        *   **Primary Inhabitants:** Shadowspawn (Trollocs, Myrddraal, Draghkar), Forsaken, Darkfriends, corrupted wildlife.
        *   **Available Goods & Services:** None for servants of Light—only death and corruption.
        *   **Potential Random Encounters (x5):** Trolloc raid; Myrddraal hunt; plants attacking; reality corruption; the Dark One's voice.
        *   **Embedded Plot Hooks & Rumors (x3):** "The seals on the prison are failing." "The Forsaken gather here for dark councils." "The Dark One can remake reality at the Pit of Doom."
        *   **Sensory Details:** Sight (wrong-colored plants, sky like bruise, mountain of Shayol Ghul smoking), Sound (screams, Trolloc grunts, unnatural silence), Smell (rot, corruption, something sweet and terrible).

    *   **Tel'aran'rhiod (World of Dreams):**
        *   **Key Landmarks:** Dream-versions of every physical location, nightmare realms, Wise One meeting places, Hero's realm.
        *   **Primary Inhabitants:** Dreamers, Dreamwalkers, Wolfbrothers, Heroes of the Horn (waiting), Forsaken hunters.
        *   **Available Goods & Services:** Information (spy on anyone), instant travel, practice with power, communion with wolves or Heroes.
        *   **Potential Random Encounters (x5):** Nightmare manifesting; Wise One teaching; Forsaken ambush; Hero appearing; reality shifting based on belief.
        *   **Embedded Plot Hooks & Rumors (x3):** "Death here is death in reality." "The Forsaken hunt Dreamers here." "Heroes wait here to answer the Horn."
        *   **Sensory Details:** Sight (locations slightly wrong, shifting based on perception, vibrant colors), Sound (echoes that don't match, thought made audible), Smell (varies with belief—can smell anything if you believe it).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** A male channeler accumulates too much taint corruption.
    *   **THEN:** They begin showing madness—paranoia, hearing voices (Lews Therin), violent outbursts. Eventually they will go completely mad and must be gentled or killed. Generate descent into madness arc.

    *   **IF:** The players cleanse Saidin of the taint.
    *   **THEN:** Male channelers stop going mad. The Black Tower becomes a true force for good. The balance of power shifts dramatically. The Dark One's long-term plan is disrupted. Generate world reaction and new faction alignments.

    *   **IF:** A player is revealed as the Dragon Reborn.
    *   **THEN:** Nations seek to control or kill them. Prophecy begins fulfilling. Forsaken hunt them specifically. Pattern tightens around them. Generate diplomatic, combat, and prophecy-related challenges.

    *   **IF:** The players unite the Aiel clans as the Car'a'carn.
    *   **THEN:** Gain powerful military force. Many Aiel break from "Bleakness" learning their true past. Shaido clan rebels. Generate Aiel war host and internal Aiel conflict.

    *   **IF:** An Aes Sedai bonds a male channeler as Warder (reversed bond).
    *   **THEN:** Scandal and revolutionary concept. If it works, it changes gender power dynamics. Black Tower and White Tower relationships shift. Generate political upheaval.

    *   **IF:** The players ally with or oppose the Seanchan.
    *   **THEN:** Major military alliance or devastating war. If allied, access to sul'dam and damane but moral horror of slavery. If opposed, brutal warfare. Generate Seanchan campaign.

    *   **IF:** The players break or preserve the Dark One's seals.
    *   **THEN:** Breaking frees the Dark One for final battle. Preserving delays but doesn't solve. Either choice has cosmic consequences. Generate Last Battle or prolonged conflict.

    *   **IF:** Players show the Dark One that free will is worth suffering.
    *   **THEN:** Philosophical victory, Dark One cannot be killed but is imprisoned with new understanding. The Wheel continues but wiser. Generate new age dawning.
