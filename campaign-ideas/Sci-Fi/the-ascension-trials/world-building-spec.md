### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Ascension Trials**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The party awakens on a mysterious island teeming with dinosaurs and other prehistoric creatures, with no memory of how they arrived. To survive, they must tame beasts, evolve from primitive stone tools to advanced tek armor, and establish a tribe capable of withstanding the island's escalating challenges. Strange obelisks dot the landscape, and entering them triggers boss arena battles against impossibly powerful creatures. Only by defeating all the guardians and collecting their trophies can the party ascend to the truth: the island is a massive simulation, and only those who prove their worth can leave and join the Overseers in the stars.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the origin of the ARKs: massive simulation islands created by an advanced civilization to test and select survivors for a cosmic purpose.
    *   Write the history of the first explorers who discovered the truth of the ARKs, including Helena Walker and her team.
    *   Describe the nature of Element: a rare, powerful material that fuels tek technology and is only created by defeating guardian creatures.
    *   Explain the role of the Overseer: the AI that governs each ARK and judges who is worthy of ascension.
    *   Detail the implant: the mysterious crystal embedded in each survivor's arm, which tracks progress and controls respawn.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Overseers** (Major)
        *   **Goals:** To test survivors, identify the worthy, and prepare them for ascension.
        *   **Hierarchy:** AI-based. Each ARK has an Overseer. Above them is the Genesis System.
        *   **Public Agenda:** (None. They operate through simulation mechanics.)
        *   **Secret Agenda:** To create a stable, sustainable population for the next phase of cosmic colonization.
        *   **Assets:** Control over the ARK, guardian creatures, respawn technology, the simulation itself.
        *   **Relationships:** Neutral to survivors; enforces trials impartially.
    *   **The Survivor Tribes** (Major)
        *   **Goals:** To survive, thrive, and ultimately ascend.
        *   **Hierarchy:** Tribal, with chieftains and elders. The party forms or joins a tribe.
        *   **Public Agenda:** Secure resources, tame dinosaurs, defeat guardians, and ascend.
        *   **Secret Agenda:** Some tribes (like Nerva's) seek to dominate the ARK, enslaving others to boost their own chances.
        *   **Assets:** Tamed dinosaurs, fortified bases, crafted gear, numbers.
        *   **Relationships:** Alliances and rivalries shift based on resources and power.
    *   **The Guardians** (Minor)
        *   **Goals:** To test survivors through combat. They are not sentient; they are programmed challenges.
        *   **Hierarchy:** None. They are boss creatures (Broodmother, Megapithecus, Dragon, Overseer).
        *   **Public Agenda:** Defeat all who enter their arenas.
        *   **Secret Agenda:** None. They exist only as trials.
        *   **Assets:** Immense power, unique abilities, arena control.
        *   **Relationships:** Hostile to all.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Helena Walker:** A scientist who has been on the ARK for years, seeking to understand its purpose.
    *   **Nerva:** The brutal warlord of the largest rival tribe, obsessed with ascension at any cost.
    *   **The Overseer:** The cold, logical AI guardian that controls the ARK.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Desperate Solo Survivor"
    *   "Rival Tribe Warrior"
    *   "Tamed Dinosaur (various species)"
    *   "Alpha Predator (mini-boss)"
    *   "Data Log Hologram"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Southern Beaches:** Safe starting zones with gentle herbivores and basic resources.
        *   **Key Landmarks:** The party's first base, supply drops (glowing beacons), scattered ruins.
        *   **Primary Inhabitants:** Dodos, Parasaurs, Dilophosaurs, Trikes.
        *   **Available Goods & Services:** Abundant berries, stone, wood, thatch.
        *   **Potential Random Encounters (x5):** A supply drop lands nearby, a friendly survivor offers trade, a Raptor pack attacks, a Compy swarm, a Carbonemys (giant turtle) wanders by.
        *   **Embedded Plot Hooks & Rumors (x3):** "An obelisk glows on the distant mountain." "A rival tribe has a base to the north." "Strange data logs found in ruins."
        *   **Sensory Details:** Sight (Sandy beaches, blue ocean, lush palm trees), Sound (Waves, dinosaur calls, rustling leaves), Smell (Salt air, vegetation).
    *   **The Redwood Forest:** A massive, dangerous biome with towering trees and deadly predators.
        *   **Key Landmarks:** The Giant Tree Platforms, a crashed supply crate, a hidden cave entrance.
        *   **Primary Inhabitants:** Thylacoleos (tree-jumping predators), Terror Birds, Megatheriums.
        *   **Available Goods & Services:** Rare wood, honey, organic polymer from penguins.
        *   **Potential Random Encounters (x5):** A Thylacoleo drops from a tree, a swarm of bees, a Dire Bear charges, a lone survivor's abandoned base, an Alpha Raptor.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Broodmother's arena requires trophies from Alphas." "A hidden cave holds rare artifacts." "Nerva's tribe controls the northern redwoods."
        *   **Sensory Details:** Sight (Massive redwood trunks, dense canopy, filtered sunlight), Sound (Rustling leaves, predator growls, insect buzzing), Smell (Pine, earth, danger).
    *   **The Tek Cave & Overseer Chamber:** The final dungeon, a high-tech complex leading to the Overseer.
        *   **Key Landmarks:** The Entrance Portal, the Defense Gauntlet, the Overseer's Arena.
        *   **Primary Inhabitants:** High-level creatures (Rexes, Gigas), tek drones, the Overseer.
        *   **Available Goods & Services:** None. Pure gauntlet and boss fight.
        *   **Potential Random Encounters (x5):** A defense turret activates, a Giga appears, a tek forcefield blocks the path, a data log reveals lore, a rival tribe attempts to enter.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Overseer is the final test." "Ascension awaits beyond victory." "The truth of the ARK will be revealed."
        *   **Sensory Details:** Sight (Glowing tek walls, energy barriers, the massive Overseer), Sound (Hum of machinery, energy weapons, the Overseer's synthetic voice), Smell (Ozone, sterile metal).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The party successfully tames their first large dinosaur (e.g., Carno, Rex).
    *   **THEN:** Their tribe gains prestige. Rival tribes may seek alliances or become more aggressive. The party can now attempt more dangerous hunts and bosses.
    *   **IF:** The party defeats a guardian (Broodmother, Megapithecus, or Dragon).
    *   **THEN:** They gain Element and a Guardian Trophy. Helena Walker reveals more lore about the ARK. The next tier of tek Engrams unlocks.
    *   **IF:** The party's base is raided and significantly damaged by a rival tribe.
    *   **THEN:** They lose resources and tames. Generate a revenge quest or negotiation scenario with the rival tribe.
    *   **IF:** The party defeats the Overseer.
    *   **THEN:** The truth is revealed: the ARK is a simulation to test survivors for cosmic colonization. The party can choose to ascend (leave the ARK, join the greater civilization) or stay and help free others. Ascension ends the campaign.
    *   **IF:** The party unlocks all tek-tier Engrams.
    *   **THEN:** They become the most advanced tribe on the ARK, attracting both allies and enemies. Nerva's tribe may launch a final, desperate attack to steal the technology.
