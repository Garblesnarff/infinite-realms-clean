# World-Building Specification Brief: Beneath the Sands

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**Beneath the Sands**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The party arrives in Dusthaven, a remote desert mining town, just as strange tremors begin shaking the ground. Soon, massive worm-like creatures burst from beneath the sand, hunting by vibration and devouring anything that moves on the surface. Trapped in the town with dwindling supplies and no way to call for help, the party must organize the survivors, fortify defensible locations, and discover the creatures' weaknesses—all while the monsters evolve into deadlier forms with each passing day.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the founding of Dusthaven as a mining outpost and its economic dependence on the Deepshaft Mine.
    *   Write the history of the Deepshaft Mine: what it produced, how deep it went, and the warnings from old prospectors about "digging too greedily."
    *   Describe the Sandwyrms: their biology, lifecycle, evolutionary adaptability, and how they have survived deep underground for millennia.
    *   Explain the legend of "The Beneath"—old desert tales of monsters that live in the deep places, waiting to devour the greedy.
    *   Detail the isolation of Dusthaven: no telegraph, no nearby settlements, weeks from the nearest city. Why help won't come in time.
    *   Write about past mining disasters and the hubris that led to breaking into the Sandwyrm nest.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Survivors of Dusthaven** (Major)
        *   **Goals:** Survive the siege, protect each other, escape if possible.
        *   **Hierarchy:** Informally led by Sheriff Kord, with Doc Mira as moral authority and various NPCs contributing skills (miners, hunters, merchants).
        *   **Public Agenda:** We stick together, we survive.
        *   **Secret Agenda:** Sub-groups have conflicting goals—some want to hoard supplies, others want to flee, some want revenge on those who caused the disaster.
        *   **Assets:** The town's buildings, limited supplies, weapons (mostly hunting rifles and mining tools), knowledge of the mine.
        *   **Relationships:** United by crisis but fracturing under pressure; trust the party initially but morale can shift.
    *   **The Hoarders** (Minor)
        *   **Goals:** Secure resources for themselves at the expense of others.
        *   **Hierarchy:** Led by Gregor the Merchant, includes a few selfish townsfolk.
        *   **Public Agenda:** We're just being practical. Everyone should look out for themselves.
        *   **Secret Agenda:** Plan to flee with supplies and leave others to die.
        *   **Assets:** Control of the General Store, hidden caches of food and water.
        *   **Relationships:** Distrusted by most survivors; will betray the party if it means survival.
    *   **The Sandwyrm Collective** (Major - Antagonist)
        *   **Goals:** Protect the nest, eliminate threats, expand territory.
        *   **Hierarchy:** Led by the Alpha Wyrm (the mother), with juveniles and evolved variants as her "soldiers."
        *   **Public Agenda:** None—they are animals (albeit intelligent ones).
        *   **Secret Agenda:** The Alpha is protecting her young; she will not stop until the threat (Dusthaven) is eliminated or she is dead.
        *   **Assets:** Numbers, evolutionary adaptability, control of the underground, vibration-based hunting.
        *   **Relationships:** View all surface-dwellers as threats; cannot be negotiated with.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Sheriff Kord Ironhand:** Pragmatic dwarf leader, guilt-ridden over the mine disaster.
    *   **Doc Mira Sunstone:** Compassionate elven healer, secretly ill, refuses to abandon anyone.
    *   **Old Val:** Grizzled prospector with knowledge of the mine and creatures, paranoid but brave.
    *   **Gregor the Merchant:** Selfish store owner who hoards supplies and attempts to flee.
    *   **Elara Sandborn:** Panicked mother with a young child, desperate for the party's help.
    *   **The Alpha Wyrm:** The colossal matriarch of the Sandwyrms, ancient and protective of her nest.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Veteran Miner"
    *   "Desperate Townsperson"
    *   "Injured Survivor"
    *   "Opportunistic Scavenger"
    *   "Brave Volunteer Defender"
    *   "Juvenile Sandwyrm"
    *   "Evolved Climber Sandwyrm"
    *   "Spitter Sandwyrm Variant"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **Dusthaven (Town Surface):** The main area under siege, now a fortress of elevated walkways.
        *   **Key Landmarks:** Main Street (now empty and dangerous), Sheriff's Office (refuge), General Store (supply hub), Water Tower (lookout), Saloon (secondary refuge), Livery Stable (collapsed).
        *   **Primary Inhabitants:** ~200 survivors (dwindling as casualties mount), Sandwyrms prowling beneath the sand.
        *   **Available Goods & Services:** Limited food and water, ammunition, medical supplies (rationed), repairs (if materials are available).
        *   **Potential Random Encounters (x5):** Sandwyrm attack, supply dispute, NPC panic, structural collapse of walkway, rescue mission for trapped survivor.
        *   **Embedded Plot Hooks & Rumors (x3):** "Old Val says he knows where the creatures came from." "Gregor is hoarding twice the supplies he admits." "Someone heard noises from the sealed mine entrance last night."
        *   **Sensory Details:** Sight (Dusty streets, elevated walkways, rippling sand), Sound (Wind, distant tremors, survivor whispers, sudden silence before an attack), Smell (Dust, sweat, fear, blood).
    *   **The Sheriff's Office:** The primary safe house, a two-story stone building.
        *   **Key Landmarks:** Ground floor (barricaded), second floor (bunks and supplies), rooftop (lookout post), the jail cells (now storage).
        *   **Primary Inhabitants:** Sheriff Kord, Doc Mira, ~30 survivors.
        *   **Available Goods & Services:** Medical care, ammunition storage, strategy planning.
        *   **Potential Random Encounters (x5):** Morale check among survivors, injured person brought in, argument over resources, sighting of Sandwyrm variant, Kord shares guilt about the mine.
        *   **Embedded Plot Hooks & Rumors (x3):** "Kord was one of the miners who broke into the nest." "There's a hidden armory in the basement." "Doc Mira is getting sicker."
        *   **Sensory Details:** Sight (Stone walls, barricaded windows, improvised beds), Sound (Hushed conversations, footsteps on wood, Doc Mira's healing prayers), Smell (Dust, old wood, herbal medicine).
    *   **The Deepshaft Mine:** The source of the Sandwyrms, now a dark and deadly dungeon.
        *   **Key Landmarks:** Mine Entrance (partially collapsed), Upper Tunnels (narrow and unstable), The Junction (where miners broke through), Lower Tunnels (claw-marked walls), The Nest (massive chamber filled with eggs and the Alpha).
        *   **Primary Inhabitants:** Juvenile Sandwyrms, evolved variants, swarms of burrowing grubs, the Alpha Wyrm.
        *   **Available Goods & Services:** None—pure survival and combat.
        *   **Potential Random Encounters (x5):** Juvenile Sandwyrm ambush, tunnel collapse, discovery of dead miners, acid trap (Spitter), swarm of grubs.
        *   **Embedded Plot Hooks & Rumors (x3):** "The miners found something ancient down there before they died." "Old Val sealed a tunnel years ago—he thinks the same creature is back." "The Alpha has been alive for centuries."
        *   **Sensory Details:** Sight (Darkness punctuated by lantern light, claw marks, organic nest structures), Sound (Skittering, distant roars, dripping water, your own breath), Smell (Damp earth, rot, something acrid and alien).
    *   **The Desert (Surrounding Area):** The endless, hostile environment that traps the survivors.
        *   **Key Landmarks:** Sand dunes, rocky outcrops, skeletal remains of wagons and animals, the horizon (shimmering with heat).
        *   **Primary Inhabitants:** Sandwyrms (hunting), carrion birds, scorpions.
        *   **Available Goods & Services:** None—certain death without preparation.
        *   **Potential Random Encounters (x5):** Sandwyrm ambush while traveling, heat exhaustion, discovery of previous victim's corpse, mirage (false hope), dust storm.
        *   **Embedded Plot Hooks & Rumors (x3):** "The nearest settlement is three weeks' travel on foot." "Some survivors want to risk the desert rather than face the Sandwyrms." "There's supposed to be an old caravan route marked by stone cairns."
        *   **Sensory Details:** Sight (Endless dunes, bleached bones, sun glare, distant heat shimmer), Sound (Wind, silence, your own heartbeat), Smell (Hot sand, dry air, death).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The party successfully fortifies key buildings and establishes elevated walkways.
    *   **THEN:** Survivor morale increases. Casualties decrease. However, the Evolution Counter advances—Climber variants emerge within 2 days.
    *   **IF:** The party fails to ration supplies properly.
    *   **THEN:** Morale plummets. Gregor's hoarding is exposed, causing a near-riot. An NPC attempts to flee and is killed by Sandwyrms.
    *   **IF:** The party kills multiple Sandwyrms in quick succession.
    *   **THEN:** The Evolution Counter advances rapidly. A new variant emerges (Spitter or Armored). The Alpha becomes more aggressive.
    *   **IF:** The party attempts to flee Dusthaven into the desert.
    *   **THEN:** Sandwyrms hunt them in the open. Unless they have a solid plan (wagons, distraction, heavy armor), casualties are high. Survivors who stay behind feel betrayed.
    *   **IF:** The party destroys the nest but fails to kill the Alpha.
    *   **THEN:** The Alpha pursues them to the surface in a rage. The final battle occurs in the middle of Dusthaven, causing massive collateral damage.
    *   **IF:** Morale drops below 5.
    *   **THEN:** A group of survivors, led by Gregor, attempts a mutiny. They try to steal supplies and flee, or demand the party leave. This creates internal conflict during the siege.
    *   **IF:** The party successfully kills the Alpha Wyrm.
    *   **THEN:** The remaining Sandwyrms retreat into the deep desert, leaderless. Dusthaven is saved, but the mine is sealed forever, ending the town's economy.
