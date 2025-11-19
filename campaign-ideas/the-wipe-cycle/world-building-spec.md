### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Wipe Cycle**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The party awakens naked on a desolate, post-apocalyptic island with nothing but a rock and a torch. This is the Wipe Cycle, a harsh world where resources are scarce, and other survivor groups will kill on sight to take what you have. To survive, the party must gather materials, craft weapons and armor, build a fortified base, and navigate the treacherous politics of warring factions—all while knowing that other players (rival groups) are doing the same. The island resets every lunar cycle (the "Wipe"), erasing all progress and forcing everyone to start over. The only way to escape the cycle is to find and activate the ancient Bunker Key before the next Wipe, a goal that will pit the party against every other faction on the island.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the origin of the Wipe Cycle: a post-apocalyptic experiment by a defunct civilization to test human resilience and adaptability.
    *   Write the history of the first Wipe survivors, who discovered the Bunker Key pieces but failed to unite them before the next cycle.
    *   Describe the nature of the Bunker: an ancient fallout shelter that doubles as an escape portal, requiring three key pieces to activate.
    *   Explain the role of the Overseers: automated systems that enforce the Wipe and monitor survivor progress.
    *   Detail the factions: how the Iron Fangs, Red Skulls, and Rust Merchants formed and their brutal histories.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Iron Fangs** (Major)
        *   **Goals:** To dominate the island, control all high-value resources, and find the Bunker Key.
        *   **Hierarchy:** Led by Ironclad, with lieutenants commanding raid teams.
        *   **Public Agenda:** Pay tribute, and we won't raid you. Resist, and we take everything.
        *   **Secret Agenda:** Ironclad plans to monopolize the Bunker Key, escaping alone and leaving everyone else to the Wipe.
        *   **Assets:** The largest, most fortified base, the best weapons, control of two major monuments.
        *   **Relationships:** Hostile to all except those who pay tribute; at war with the Red Skulls.
    *   **The Red Skulls** (Major)
        *   **Goals:** To destroy the Iron Fangs and claim the island through sheer brutality.
        *   **Hierarchy:** Decentralized. Led by individual champions like the Berserker.
        *   **Public Agenda:** Raid, kill, and loot. No mercy, no alliances.
        *   **Secret Agenda:** They believe the Wipe is a divine test. Escaping is cowardice; dominance is the only goal.
        *   **Assets:** Superior PvP skills, terror tactics, no fixed base (constantly moving).
        *   **Relationships:** Hostile to everyone, especially the Iron Fangs.
    *   **The Rust Merchants** (Minor)
        *   **Goals:** To profit from the chaos by trading rare items and information.
        *   **Hierarchy:** Led by Ash, with a network of solo traders.
        *   **Public Agenda:** We sell anything to anyone—for the right price.
        *   **Secret Agenda:** Ash knows the Bunker Key locations and is auctioning the information to the highest bidder.
        *   **Assets:** Hidden stashes, knowledge of monument loot, portable trading outposts.
        *   **Relationships:** Neutral to all factions; profits from everyone.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Ironclad:** The ruthless warlord of the Iron Fangs, determined to escape the Wipe Cycle.
    *   **Ash:** The slippery merchant who plays all factions against each other for profit.
    *   **The Red Skull Berserker:** A terrifying construct enforcer, the island's deadliest solo raider.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Desperate Solo Survivor"
    *   "Iron Fang Raider"
    *   "Red Skull Berserker (multiple instances)"
    *   "Neutral Trader"
    *   "Automated Turret (monument guardian)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Beaches (Starting Zone):** Rocky shores with basic resources and frequent PvP conflicts.
        *   **Key Landmarks:** Spawn points, scattered debris, small rock formations.
        *   **Primary Inhabitants:** New survivors, hostile wildlife (boars, wolves).
        *   **Available Goods & Services:** Stone, wood, hemp, basic food.
        *   **Potential Random Encounters (x5):** A rival survivor ambushes the party, a wolf pack attacks, a supply crate washes ashore, a trader passes through, distant gunfire.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Iron Fangs control the forest." "A monument to the north has high-tier loot." "The Wipe is only days away."
        *   **Sensory Details:** Sight (Rocky gray shores, rusted metal debris, the harsh sun), Sound (Waves crashing, distant gunfire, the crunch of boots on gravel), Smell (Salt air, rust, decay).
    *   **The Launch Site (Monument):** A massive, irradiated complex with a Bunker Key piece.
        *   **Key Landmarks:** The Main Building, the Rocket, automated turrets, radiation zones.
        *   **Primary Inhabitants:** Automated defenses, hostile NPCs, radiation.
        *   **Available Goods & Services:** High-tier loot (firearms, explosives, components), the first Bunker Key piece.
        *   **Potential Random Encounters (x5):** A turret activates, a rival faction is raiding, radiation intensifies, a trap is triggered, a scientist NPC (hostile).
        *   **Embedded Plot Hooks & Rumors (x3):** "The Bunker Key piece is in the Main Building's vault." "Radiation suits are required to survive." "The Iron Fangs are planning a raid here."
        *   **Sensory Details:** Sight (Rusted metal structures, the towering rocket, sickly green radiation glow), Sound (Hum of turrets, alarms blaring, Geiger counter clicking), Smell (Ozone, chemical tang, rust).
    *   **The Bunker (Final Location):** The escape portal, requiring all three Bunker Key pieces.
        *   **Key Landmarks:** The sealed door, the Key Slots, the Escape Portal inside.
        *   **Primary Inhabitants:** None, until the party and rival factions converge.
        *   **Available Goods & Services:** Escape from the Wipe Cycle.
        *   **Potential Random Encounters (x5):** The Iron Fangs arrive, the Red Skulls ambush, Ash tries to negotiate, a final PvP battle, the Wipe begins.
        *   **Embedded Plot Hooks & Rumors (x3):** "All factions know the Bunker's location." "The final battle will be here." "Activating the portal takes time—defense is crucial."
        *   **Sensory Details:** Sight (A massive, reinforced door, glowing Key Slots, the shimmering portal beyond), Sound (Footsteps echoing, distant explosions, the hum of the portal), Smell (Sterile metal, ozone, gunpowder).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The party successfully raids another faction's base and loots significant resources.
    *   **THEN:** They gain a reputation as a threat. Rival factions will target them for revenge raids. Generate a counter-attack scenario.
    *   **IF:** The party allies with the Iron Fangs by paying tribute.
    *   **THEN:** They gain temporary protection and access to Iron Fang-controlled monuments. However, the Red Skulls will now attack them on sight.
    *   **IF:** The party acquires a Bunker Key piece.
    *   **THEN:** All factions learn of this through spies or witnesses. The party becomes the top target. Generate escalating PvP encounters.
    *   **IF:** The Wipe Cycle begins before the party activates the Bunker.
    *   **THEN:** All structures and resources are destroyed. The party retains levels but must restart from nothing. This is a tragic, "bad ending" scenario.
    *   **IF:** The party activates the Bunker with all three key pieces.
    *   **THEN:** They escape the island, ending the campaign. A final PvP battle may occur as rival factions attempt to stop them or steal the key.
