### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Endless Deluge**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The party awakens on a tiny wooden raft drifting in an endless ocean, the result of a cataclysmic flood that has swallowed the world. With only a hook to fish debris from the water, they must expand their raft, gather floating resources, and survive the relentless attacks of Bruce, a massive, territorial shark. As they explore scattered islands, they uncover clues about the Deluge: it was no natural disaster but a magical cataclysm, and the only way to end it is to reach the Tower of Tides, an ancient structure on the farthest island, and reverse the ritual. But the ocean is vast, resources are scarce, and Bruce is always circling.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the origin of the Deluge: a desperate mage named Elowen cast a ritual to flood the world, believing it would cleanse a spreading magical corruption.
    *   Write the history of the world before the Deluge: a thriving civilization with great cities, now lost beneath the waves.
    *   Describe the Tower of Tides: an ancient magical structure built to control the tides, repurposed by Elowen to maintain the flood.
    *   Explain the nature of Bruce: he is not a normal shark but a guardian created by Elowen to prevent anyone from reaching the Tower.
    *   Detail the fate of survivors: most drowned, but some built rafts or reached high islands, creating small, isolated communities.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Drifters** (Minor)
        *   **Goals:** To survive on their rafts, scavenge islands, and find a permanent home.
        *   **Hierarchy:** No formal structure. Solo rafters or small crews. Mira is a notable member.
        *   **Public Agenda:** We survive by scavenging and trading. We mean no harm.
        *   **Secret Agenda:** Some Drifters, like Mira, seek the legendary islands with advanced tech or the Tower of Tides.
        *   **Assets:** Rafts, scavenging skills, knowledge of islands.
        *   **Relationships:** Cautiously friendly to others; wary of Raiders.
    *   **The Raiders** (Minor)
        *   **Goals:** To survive by taking resources from others by force.
        *   **Hierarchy:** Led by Captain Thorne, with a crew of desperate, hardened survivors.
        *   **Public Agenda:** The strong survive. We take what we need.
        *   **Secret Agenda:** Thorne seeks redemption but hides it behind ruthlessness.
        *   **Assets:** Larger, armed rafts, combat skills, numbers.
        *   **Relationships:** Hostile to Drifters and settlers; respect strength.
    *   **The Ocean & Bruce** (Major — Environmental Faction)
        *   **Goals:** None. The ocean is an environment, and Bruce is a guardian.
        *   **Hierarchy:** Bruce is the apex. The ocean has no sentience.
        *   **Public Agenda:** None.
        *   **Secret Agenda:** Bruce is magically bound to prevent anyone from reaching the Tower of Tides.
        *   **Assets:** Infinite water, storms, Bruce's attacks, dwindling debris.
        *   **Relationships:** Hostile to all rafters (via Bruce and hazards).

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Mira (The Drifter):** A veteran rafter who trades and advises the party.
    *   **Captain Thorne (The Raider):** A charismatic but ruthless raider leader seeking redemption.
    *   **The Tidecaller:** The ancient elemental guardian of the Tower of Tides.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Friendly Solo Rafter"
    *   "Desperate Raider"
    *   "Island Hermit"
    *   "Seagull (resource indicator)"
    *   "Bruce the Shark (singular, persistent)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Party's Raft:** The central, evolving location. Starts as 2x2, expands to multi-level fortress.
        *   **Key Landmarks:** Foundation (expandable), storage chests, water purifier, crop plots, sail.
        *   **Primary Inhabitants:** The party.
        *   **Available Goods & Services:** Storage, farming, cooking, rest.
        *   **Potential Random Encounters (x5):** Floating debris, Bruce attacks, a storm, a passing rafter, seagulls land.
        *   **Embedded Plot Hooks & Rumors (x3):** "Debris is getting scarce—we need to find an island." "Bruce seems more aggressive today." "A distant island is on the horizon."
        *   **Sensory Details:** Sight (Wooden planks, blue water, the horizon), Sound (Waves lapping, seagulls, the creak of wood), Smell (Salt air, fish, wood).
    *   **The Research Island (First Island):** A small, rocky island with a research station.
        *   **Key Landmarks:** The Research Station, a small dock, fruit trees, rocky cliffs.
        *   **Primary Inhabitants:** None (abandoned). Possibly wild animals.
        *   **Available Goods & Services:** Metal, vines, fruit, research journals (lore).
        *   **Potential Random Encounters (x5):** A seagull nest, a wild boar, a researcher's ghost (hallucination), Bruce circles offshore, Mira arrives.
        *   **Embedded Plot Hooks & Rumors (x3):** "The journals mention the Deluge and the Tower of Tides." "A map shows other islands." "Bruce seems to guard certain areas."
        *   **Sensory Details:** Sight (Rocky shore, abandoned station, lush greenery), Sound (Waves, wind, bird calls), Smell (Salt, fruit, old paper).
    *   **The Tower of Tides (Final Location):** A massive stone tower on a storm-wracked island.
        *   **Key Landmarks:** The Tower Entrance, the Ritual Chamber, the Eye of the Storm (surrounding the island).
        *   **Primary Inhabitants:** The Tidecaller, elemental guardians, magical traps.
        *   **Available Goods & Services:** None. This is the final challenge.
        *   **Potential Random Encounters (x5):** The Tidecaller appears, elemental guardians attack, a vision of Elowen, a puzzle activates, the storm intensifies.
        *   **Embedded Plot Hooks & Rumors (x3):** "The ritual to end the Deluge is here." "The Tidecaller guards it." "Reversing it may have consequences."
        *   **Sensory Details:** Sight (Massive stone tower, swirling storm clouds, glowing runes), Sound (Thunder, crashing waves, the hum of magic), Smell (Ozone, salt, ancient stone).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The party successfully expands their raft to a multi-level structure with defenses.
    *   **THEN:** Bruce's attacks become less frequent (the defenses work), and the party can focus on exploration. Other rafters may approach, impressed by their progress.
    *   **IF:** The party encounters Captain Thorne's raiders and chooses to fight.
    *   **THEN:** A naval combat scenario. If the party wins, they gain Thorne's resources. If they lose, they must flee or negotiate.
    *   **IF:** The party allies with Mira and helps her reach the legendary tech island.
    *   **THEN:** They gain advanced blueprints (electric purifier, engine for faster travel). Mira becomes a permanent ally.
    *   **IF:** The party navigates through the Eye of the Storm to reach the final island.
    *   **THEN:** Bruce makes his most aggressive attack yet, attempting to destroy the raft. They must fend him off while navigating the storm's hazards.
    *   **IF:** The party reverses the Deluge ritual at the Tower of Tides.
    *   **THEN:** The ocean begins to recede slowly. The campaign ends with the party witnessing the first glimpses of land emerging, and the hope of rebuilding civilization. Bruce vanishes, his purpose fulfilled.
