### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Quiet End**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** A geomagnetic disaster has brought civilization to its knees. All electronics are dead, planes have fallen from the sky, and a strange aurora now dominates the northern skies. The party, survivors of a plane crash in the Canadian wilderness, must trek through the frozen, isolated landscape to reach the rumored safe haven of Perseverance Mills, a remote town that may still have survivors. There are no zombies, no mutants—only the cold, hunger, thirst, wildlife, and the slow, quiet realization that the world as they knew it is gone. Every decision matters: what to carry, when to rest, whether to trust another survivor. This is the quiet end of the world.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the geomagnetic disaster: a solar flare event combined with a magnetic pole shift, rendering all electronics useless and causing widespread infrastructure collapse.
    *   Write the history of the first days: planes fell, power grids failed, cities descended into chaos, and remote areas like the Canadian wilderness became isolated.
    *   Describe the aurora: an eerie, persistent phenomenon caused by the geomagnetic instability, visible even during the day at times.
    *   Explain the slow collapse: there was no single apocalypse moment, just a gradual realization that help was not coming.
    *   Detail Perseverance Mills: a remote town that was already self-sufficient, now rumored to be the only safe haven in the region.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Survivors of Perseverance Mills** (Major)
        *   **Goals:** To survive the winter, maintain order, and protect their dwindling resources.
        *   **Hierarchy:** Led by a council of elders, with roles assigned based on skills (hunters, medics, builders).
        *   **Public Agenda:** We welcome those who can contribute. Freeloaders will not survive.
        *   **Secret Agenda:** Resources are nearly gone. The council is debating whether to turn away newcomers or ration more severely.
        *   **Assets:** A fortified town, food stores (diminishing), wood for heat, a sense of community.
        *   **Relationships:** Cautiously welcoming to the party; hostile to raiders.
    *   **Lone Survivors** (Minor)
        *   **Goals:** To survive alone or in small groups, avoiding conflict and scavenging where possible.
        *   **Hierarchy:** No formal structure. Individuals like Grey Mother, Hobbs, and the Warden are examples.
        *   **Public Agenda:** We survive on our own terms. We help if we can, but survival comes first.
        *   **Secret Agenda:** Many are slowly dying (illness, starvation, isolation). Some are desperate enough to steal.
        *   **Assets:** Wilderness skills, hidden caches, knowledge of the land.
        *   **Relationships:** Vary widely—some friendly, some neutral, some hostile if threatened.
    *   **The Wilderness Itself** (Major — Environmental Faction)
        *   **Goals:** None. Nature is indifferent.
        *   **Hierarchy:** The food chain. Wolves and bears are apex. Deer and rabbits are prey.
        *   **Public Agenda:** None.
        *   **Secret Agenda:** The wilderness is slowly reclaiming human structures, indifferent to the quiet end.
        *   **Assets:** Infinite cold, wildlife, weather, isolation.
        *   **Relationships:** Hostile to those who do not respect it; neutral to those who understand it.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Grey Mother:** The kind, weary matriarch who offers the party their first real shelter.
    *   **Jeremiah Hobbs (The Trapper):** A grizzled wilderness expert hiding a deadly infection.
    *   **The Warden (The Hermit):** A mysterious, silent figure who is revealed to be the party's former pilot.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Desperate Scavenger"
    *   "Perseverance Mills Councilor"
    *   "Injured Traveler"
    *   "Wildlife (Wolf, Bear, Deer, Rabbit)"
    *   "Frozen Corpse (loot and lore)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Crash Site:** The starting point, a wrecked plane in a frozen clearing.
        *   **Key Landmarks:** The plane wreckage, scattered luggage, a makeshift shelter.
        *   **Primary Inhabitants:** None (abandoned quickly).
        *   **Available Goods & Services:** Limited scavenging (clothing, food, a hatchet, matches, a map).
        *   **Potential Random Encounters (x5):** A wolf investigates, a blizzard approaches, frostbite sets in, a flare is found, a survivor's corpse.
        *   **Embedded Plot Hooks & Rumors (x3):** "The map shows Grey Mother's cabin nearby." "The aurora is stronger than normal." "No rescue is coming."
        *   **Sensory Details:** Sight (Twisted metal, snow, the aurora in the sky), Sound (Wind, creaking metal, silence), Smell (Aviation fuel, cold, pine).
    *   **Mystery Lake:** A central hub region with multiple shelters and scavenging locations.
        *   **Key Landmarks:** The Camp Office, the Trapper's Cabin, the Hunting Lodge, the frozen lake.
        *   **Primary Inhabitants:** Hobbs (at the Trapper's Cabin), wildlife, frozen corpses.
        *   **Available Goods & Services:** Scavenging (food, tools, clothing), hunting, fishing.
        *   **Potential Random Encounters (x5):** A wolf pack patrols, a blizzard, a deer is spotted, thin ice cracks, Hobbs offers guidance.
        *   **Embedded Plot Hooks & Rumors (x3):** "Hobbs knows the way to Perseverance Mills." "The lake is dangerous—thin ice." "A bear has claimed the Hunting Lodge."
        *   **Sensory Details:** Sight (Frozen lake, cabins, pine trees, the aurora), Sound (Wind, wolf howls, ice cracking), Smell (Pine, smoke from a distant fire, cold).
    *   **Perseverance Mills:** The destination, a struggling town on the brink of collapse.
        *   **Key Landmarks:** The Community Hall, the General Store, the Church, the Lumber Yard.
        *   **Primary Inhabitants:** The town council, survivors (50-60 people), guards.
        *   **Available Goods & Services:** Trade (limited), shelter (if accepted), tasks (hunting, scavenging).
        *   **Potential Random Encounters (x5):** A council meeting, a desperate survivor begs for food, a raider scout is spotted, a blizzard, the Warden arrives.
        *   **Embedded Plot Hooks & Rumors (x3):** "Resources are nearly depleted." "A coastal settlement is rumored to the east." "The winter will be the harshest yet."
        *   **Sensory Details:** Sight (Weathered buildings, smoke from chimneys, wary faces), Sound (Chopping wood, murmured conversations, wind), Smell (Wood smoke, cooking food, cold).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The party successfully kills a bear.
    *   **THEN:** They gain massive resources (meat for weeks, a bearskin for crafting). Their reputation as capable survivors grows. However, the act may traumatize a character (moral cost of killing such a majestic creature).
    *   **IF:** The party fails to manage warmth during a blizzard.
    *   **THEN:** One or more characters suffer frostbite or hypothermia. Generate a medical crisis requiring immediate treatment or risk permanent injury/death.
    *   **IF:** The party allies with Hobbs and learns of his infection.
    *   **THEN:** They must choose: use precious antibiotics to save him, or let him die and take his supplies. This is a moral dilemma with no easy answer.
    *   **IF:** The party reaches Perseverance Mills and proves their worth.
    *   **THEN:** The council offers them a place in the community. However, they learn resources are so scarce that the town may not survive the winter. The party must choose: stay and risk starvation, or continue to the rumored coastal settlement.
    *   **IF:** The party encounters the Warden and learns the truth (they were the pilot).
    *   **THEN:** Generate a powerful emotional moment. The Warden can offer guidance to the final location, driven by guilt and a desire to ensure the party's survival.
