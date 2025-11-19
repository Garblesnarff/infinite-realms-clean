### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**Depths of Planet 4546B**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The party's skyship crashes on an alien ocean world with no visible land. Stranded in a vast, deep ocean teeming with both beautiful and terrifying alien life, they must survive using scavenged technology, explore increasingly dangerous depths to find resources, and uncover the mystery of an ancient alien civilization that once inhabited this world. Their only hope of escape lies in the deepest, most hostile regions of the ocean, where a plague called the Kharaa Bacterium threatens all life, and an ancient alien facility holds the key to both a cure and a way off this waterlogged planet.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the history of the Precursor civilization: an ancient, highly advanced race that visited this planet seeking a cure for the Kharaa Bacterium.
    *   Write the story of how the Precursors accidentally released Kharaa from a specimen, infecting the planet's ecosystem and forcing them to establish a quarantine.
    *   Describe the Sea Emperor Leviathan and its role in the Precursor research—they discovered it produced an enzyme that could cure Kharaa, but needed its offspring to be born naturally for the enzyme to be viable.
    *   Explain the fate of the Precursors: unable to cure themselves or the Sea Emperor, they eventually died out, leaving behind automated systems to enforce the quarantine.
    *   Detail the history of the Degasi crew, who crashed on 4546B a decade before the party, and their slow, tragic descent into madness and death.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Automated Precursor Systems** (Major)
        *   **Goals:** To maintain the quarantine of Planet 4546B and prevent the spread of Kharaa to other worlds.
        *   **Hierarchy:** No hierarchy. Automated defense platforms, containment facilities, and research stations operate on ancient programming.
        *   **Public Agenda:** Any vessel attempting to leave the planet will be destroyed. Containment is absolute.
        *   **Secret Agenda:** None. The systems are not sentient. They simply execute their programming.
        *   **Assets:** The Quarantine Enforcement Platform (shoots down ships), the Disease Research Facility, the Primary Containment Facility.
        *   **Relationships:** Hostile to any entity attempting to leave the planet; neutral to those exploring, as long as they don't trigger quarantine protocols.
    *   **The Degasi Survivors (Deceased)** (Minor)
        *   **Goals:** (In life) To survive, explore, and find a way off the planet.
        *   **Hierarchy:** Led by Paul Torgal (captain), with Marguerit Maida (security) and Bart Torgal (scientist) as key members.
        *   **Public Agenda:** (None, they are dead. Their bases and logs serve as lore.)
        *   **Secret Agenda:** Paul wanted to build a life on 4546B. Marguerit wanted to escape at any cost. Bart sought to understand the planet.
        *   **Assets:** Three bases (Floating Island, Jellyshroom Cave, Deep Grand Reef), logs, and valuable technology blueprints.
        *   **Relationships:** (None, deceased. Marguerit may still be alive in hiding.)
    *   **The Native Ecosystem** (Major)
        *   **Goals:** Survival and propagation. The ocean's creatures are not organized but represent a constant environmental threat.
        *   **Hierarchy:** Food chain dynamics. Leviathans are apex predators. Smaller creatures are prey or scavengers.
        *   **Public Agenda:** None. They operate on instinct.
        *   **Secret Agenda:** None. They are animals, not factions.
        *   **Assets:** The entire ocean and its biomes. Infinite respawning creatures.
        *   **Relationships:** Predator-prey dynamics. Hostile to the party if provoked or if they enter feeding territories.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **ECHO (Emergency Construct for Habitat Operations):** A clinical, survival-focused AI that guides the party.
    *   **Marguerit Maida:** The last Degasi survivor, a scarred warrior hiding in the deep, infected but resistant to Kharaa.
    *   **The Sea Emperor Leviathan:** A telepathic, ancient creature imprisoned by the Precursors, the key to curing Kharaa.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Scared Fellow Crash Survivor"
    *   "Holographic Precursor Archive"
    *   "Dying Crew Member (Kharaa victim)"
    *   "Automated Precursor Defense Drone"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Safe Shallows:** The starting biome, a shallow, colorful reef teeming with harmless fish and basic resources.
        *   **Key Landmarks:** The Lifepod (starting point), the Party's First Seabase, Kelp Forest border.
        *   **Primary Inhabitants:** Peepers, Boomerangs, Bladderfish (harmless).
        *   **Available Goods & Services:** Abundant copper, titanium, and basic food sources.
        *   **Potential Random Encounters (x5):** A Stalker wanders in from the Kelp Forest, a Gasopod (releases poison gas), a curious Reefback (giant, harmless), a resource-rich wreckage, a Precursor arch glowing mysteriously.
        *   **Embedded Plot Hooks & Rumors (x3):** "Radio signals detected from the Aurora wreck." "Strange energy readings coming from deeper waters." "ECHO suggests building a seabase for long-term survival."
        *   **Sensory Details:** Sight (Bright blue water, colorful coral, schools of small fish), Sound (Gentle water flow, distant whale-like calls, bubbles), Smell (Salty, fresh ocean).
    *   **The Aurora (Crashed Skyship):** A massive, wrecked vessel leaking deadly radiation, filled with valuable salvage.
        *   **Key Landmarks:** The Reactor Room (leaking radiation), the Cargo Bay (tech blueprints), the Drive Core (must be repaired).
        *   **Primary Inhabitants:** Cave Crawlers (hostile insects), automated defense turrets (can be disabled).
        *   **Available Goods & Services:** Advanced tech blueprints, Prawn Suit fragments, valuable materials.
        *   **Potential Random Encounters (x5):** A Cave Crawler ambush, a fire breaks out, a radiation leak intensifies, a supply cache is found, a holographic crew message plays.
        *   **Embedded Plot Hooks & Rumors (x3):** "The reactor must be repaired to stop the radiation." "The black box may reveal why the ship was shot down." "Reaper Leviathans patrol the area."
        *   **Sensory Details:** Sight (Twisted metal, flickering lights, radiation warning signs), Sound (Creaking hull, sparking wires, distant roars), Smell (Burnt metal, ozone, stale air).
    *   **The Primary Containment Facility:** The deepest location, a massive Precursor structure in the Lava Lakes, housing the Sea Emperor.
        *   **Key Landmarks:** The Aquarium Chamber (Sea Emperor's prison), the Enzyme Incubation Room, the Ion Cube Fabricator.
        *   **Primary Inhabitants:** The Sea Emperor Leviathan, Sea Emperor Juveniles (after hatching), automated Precursor systems.
        *   **Available Goods & Services:** The cure enzyme (after helping the Sea Emperor), Ion Cubes (advanced power source).
        *   **Potential Random Encounters (x5):** A telepathic vision from the Sea Emperor, a Warper (Precursor bio-weapon) teleports in, a lava geyser erupts, a data terminal activates, a Sea Dragon Leviathan patrols outside.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Sea Emperor is the key to curing Kharaa." "Its eggs must hatch naturally to produce the enzyme." "Freeing the Sea Emperor will disable the quarantine."
        *   **Sensory Details:** Sight (Massive alien architecture, the Sea Emperor's glowing form, magma visible through reinforced glass), Sound (The Emperor's telepathic hum, bubbling lava, ancient machinery), Smell (Sulfur, alien biology, ancient dust).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The party repairs the Aurora's reactor core.
    *   **THEN:** The radiation zone around the Aurora dissipates, making exploration safer. New areas of the wreck become accessible, and the party can scavenge the most valuable tech.
    *   **IF:** The party enters the territory of a Leviathan-class predator without stealth.
    *   **THEN:** Generate a terrifying chase sequence. The Leviathan pursues the party, forcing them to evade, hide, or use the environment (caves, debris) to escape.
    *   **IF:** The party successfully hatches the Sea Emperor's eggs and obtains the enzyme cure.
    *   **THEN:** All party members are cured of Kharaa. The Sea Emperor thanks them telepathically and shares the location of the quarantine disable switch. The juveniles are released into the ocean, ensuring the species survives.
    *   **IF:** The party attempts to leave the planet without curing Kharaa.
    *   **THEN:** The Quarantine Enforcement Platform detects the infection and shoots down their escape rocket. Generate a scenario where the party must return to the depths to complete the cure before they can escape.
    *   **IF:** The party allies with Marguerit Maida.
    *   **THEN:** She provides valuable knowledge of the deep biomes, warns them of specific dangers, and may aid them in a crucial fight. However, her reckless, aggressive approach may also lead them into unnecessary danger.
