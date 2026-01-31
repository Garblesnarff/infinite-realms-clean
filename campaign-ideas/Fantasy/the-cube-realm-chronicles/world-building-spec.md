### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Cube Realm Chronicles**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The party awakens in the Cube Realm, a strange dimension where everything exists in perfect geometric forms and reality itself can be reshaped by those who understand its laws. To survive and escape, they must master the art of material harvesting and crafting, delve into progressively dangerous dimensional layers (the Nether-Below and the Void-Beyond), and ultimately face the Ender Tyrant, an ancient dragon that guards the only portal home. The world operates on strange rules: night brings terrible creatures, resources must be gathered and transmuted, and the deeper you delve, the more reality itself begins to unravel.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the origin of the Cube Realm as a prison dimension created by ancient archmages to contain the Ender Tyrant.
    *   Write the history of how the geometric laws of this realm came to be and why everything exists in perfect cubic forms.
    *   Describe the nature of the Ender Tyrant: an ancient dragon of void and entropy that once threatened to consume entire planes.
    *   Explain the origins of the Villagers, the native humanoid inhabitants, and their simple, trade-based society.
    *   Detail the discovery of the Eyes of Ending, artifacts crafted from the essence of slain Ender creatures that can locate the Stronghold.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Villager Communes** (Major)
        *   **Goals:** To live peaceful, simple lives, trade with outsiders, and avoid the dangers of the Cube Realm.
        *   **Hierarchy:** Each village has an Elder (like Hroon). Villagers have specialized professions (farmers, blacksmiths, librarians).
        *   **Public Agenda:** We welcome trade and mutual protection, but please don't bring trouble to our doors.
        *   **Secret Agenda:** They know far more about the Cube Realm's true nature than they reveal, fearing that sharing this knowledge will only bring more danger.
        *   **Assets:** Safe villages with farms, basic crafting knowledge, rare trade goods.
        *   **Relationships:** Neutral to friendly with adventurers; hostile to Pillagers and Illagers.
    *   **The Piglin Warbands** (Minor)
        *   **Goals:** To accumulate wealth (especially gold), dominate the Nether-Below, and engage in brutal combat.
        *   **Hierarchy:** Led by powerful Warlords like Grakk. Strength and gold determine status.
        *   **Public Agenda:** Pay us in gold, and we won't kill you. Fight us, and we'll take everything you own.
        *   **Secret Agenda:** To overthrow the Blaze Sovereign and claim the Nether Fortress, gaining control of the most valuable Nether resources.
        *   **Assets:** Fire resistance, knowledge of Nether geography, access to Bastion Remnants (treasure-filled ruins).
        *   **Relationships:** Hostile to all unless bribed with gold; at war with the Blaze Sovereign.
    *   **The Pillagers** (Minor)
        *   **Goals:** To raid, pillage, and destroy. They thrive on chaos and conquest.
        *   **Hierarchy:** Organized into raiding parties led by Captains. Serve powerful Illager sorcerers.
        *   **Public Agenda:** We take what we want. Resistance is futile.
        *   **Secret Agenda:** To serve the Illagers in a grand plan to overthrow the Villagers and claim their lands.
        *   **Assets:** Outposts, crossbows, Ravagers (massive, rideable beasts).
        *   **Relationships:** Hostile to Villagers and adventurers; serve the Illagers.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **The Wandering Trader:** A mysterious, eternally cursed merchant who appears randomly, offering rare trades and cryptic advice.
    *   **Elder Villager Hroon:** The wise leader of a hidden village, knowledgeable about the Cube Realm's history and the truth of its nature.
    *   **Piglin Warlord Grakk:** The brutal, gold-obsessed ruler of a Nether warband, a potential enemy or uneasy ally.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Novice Crafter Adventurer"
    *   "Paranoid Villager Farmer"
    *   "Scarred Nether Explorer"
    *   "Greedy Piglin Trader"
    *   "Fanatical Pillager Captain"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Party's Base Camp:** A player-constructed fortified base that evolves throughout the campaign.
        *   **Key Landmarks:** The Main Hall, Crafting Workshops, Farms, Mine Entrance, Defensive Walls.
        *   **Primary Inhabitants:** The player characters, any rescued NPCs or hired help.
        *   **Available Goods & Services:** Crafting, storage, farming, safe rest.
        *   **Potential Random Encounters (x5):** A trader arrives with rare goods, a Creeper sneaks close to the walls at night, a Dimensional Rift opens nearby, a Villager seeks refuge, a distant roar from the Nether portal.
        *   **Embedded Plot Hooks & Rumors (x3):** "Strange noises come from the deep mines at night." "A Villager mentioned an ancient temple to the east." "The Wandering Trader spoke of a Stronghold deep underground."
        *   **Sensory Details:** Sight (Blocky stone walls, glowing furnaces, organized chests of resources), Sound (Hammering of crafting, crackling torches, distant monster groans), Smell (Wood smoke, fresh-tilled earth, the metallic tang of iron).
    *   **The Ancient Temple:** A jungle temple filled with traps, lore, and treasure.
        *   **Key Landmarks:** The Trapped Entrance, The Mural Chamber, The Hidden Vault.
        *   **Primary Inhabitants:** Traps, possibly leftover guardians (enchanted armor stands).
        *   **Available Goods & Services:** Loot (treasure, rare crafting recipes, lore).
        *   **Potential Random Encounters (x5):** A pressure plate trap, a arrow dispenser, a hidden chest, a wandering jungle creature, an Illager scout.
        *   **Embedded Plot Hooks & Rumors (x3):** "The murals show a dragon imprisoned in a void." "A journal mentions the Eyes of Ending." "A map fragment points to a Nether portal location."
        *   **Sensory Details:** Sight (Overgrown stone blocks, intricate redstone mechanisms, faded murals), Sound (Clicking of traps, dripping water, rustling vines), Smell (Damp stone, jungle rot, ancient dust).
    *   **The Nether Fortress:** A massive obsidian stronghold in the Nether-Below, home to the Blaze Sovereign.
        *   **Key Landmarks:** The Blaze Spawner Chamber, The Lava Moat, The Nether Wart Garden, The Throne of Embers.
        *   **Primary Inhabitants:** Blazes, Wither Skeletons, Magma Cubes, the Blaze Sovereign (boss).
        *   **Available Goods & Services:** None. Pure combat zone and resource gathering (Blaze Rods, Nether Wart).
        *   **Potential Random Encounters (x5):** A patrol of Wither Skeletons, a Blaze ambush, a lava flow blocks the path, a Ghast attacks from above, a treasure chest in a hidden alcove.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Blaze Sovereign guards the most Blaze Rods." "Wither Skeletons carry rare Wither Skulls." "A secret room holds ancient Nether lore."
        *   **Sensory Details:** Sight (Black obsidian walls, rivers of lava, floating Blazes wreathed in flame), Sound (Roaring fire, the hiss of lava, the rattle of Wither Skeleton bones), Smell (Sulfur, burning stone, acrid smoke).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The players successfully build a fully fortified base with farms, workshops, and defenses.
    *   **THEN:** The base becomes a safe haven, attracting wandering Villagers and traders. Generate new NPCs who offer quests and services. The base can withstand a major Pillager raid without collapsing.
    *   **IF:** The players activate a Nether Portal without proper preparation (fire-resistant gear, strong weapons).
    *   **THEN:** Generate a scenario where they are immediately overwhelmed by Nether mobs. They must retreat or face a deadly encounter. The portal remains active, and Nether creatures may begin appearing in the Overworld.
    *   **IF:** The players ally with Piglin Warlord Grakk and help him overthrow the Blaze Sovereign.
    *   **THEN:** Grakk becomes the new ruler of the Nether Fortress and offers the party exclusive trading rights for Nether resources. However, he is fickle and may betray them if a better offer comes along.
    *   **IF:** The players close multiple Dimensional Rifts, stabilizing an area.
    *   **THEN:** That region becomes safer, with fewer monster spawns. Villagers may establish a new settlement there, creating a new trading hub.
    *   **IF:** The players defeat the Ender Tyrant.
    *   **THEN:** The Void-Beyond begins to destabilize. The party must quickly claim the Egg of Returning and activate the portal home before the entire dimension collapses, creating a tense, time-limited final escape sequence.
