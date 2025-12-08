### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Wasteland Run**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** In post-Cataclysm wastelands, the tyrannical Immortan Warlock controls the only water source from his Citadel fortress. The party helps the Five Brides escape, triggering a 500-mile chase across hostile desert pursued by fanatical War Boys. When they discover the fabled Green Place is dead, they must make a desperate choice: keep running or fight back to the Citadel and take it. It's an adrenaline-fueled vehicular campaign about freedom, redemption, and hope in desolation.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the Cataclysm that turned the world into wasteland and why water became the most precious resource.
    *   Write the history of Immortan Warlock's rise to power and the construction of the Citadel fortress.
    *   Describe the War Boys' culture—their religious fervor, obsession with chrome, and desire for glorious death.
    *   Explain the legend of the Green Place and why people believe it still exists.
    *   Detail the vehicle modification culture of the wasteland—how war machines are built from scavenged parts.
    *   Describe the other wasteland settlements: Gas Town (refineries), the Bullet Farm (ammunition), and smaller nomadic tribes.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Citadel / War Boys** (Major)
        *   **Goals:** Serve Immortan Warlock, control water, achieve glorious death in his service.
        *   **Hierarchy:** Immortan at top, his sons as lieutenants, War Boys as fanatical soldiers, workers and slaves at bottom.
        *   **Public Agenda:** Provide order and water (rationed) in exchange for service.
        *   **Secret Agenda:** Immortan's breeding program to produce healthy heirs, his own failing health.
        *   **Assets:** The Citadel fortress, control of water, hundreds of war vehicles, fanatical warriors.
        *   **Relationships:** Allied with Gas Town and Bullet Farm; tyrannize the enslaved population; hunting the party.
    *   **The Convoy (The Party and Allies)** (Minor)
        *   **Goals:** Escape to the Green Place, then liberate the Citadel.
        *   **Hierarchy:** Informal leadership shared by the party and Furiosa.
        *   **Public Agenda:** None—they're fugitives.
        *   **Secret Agenda:** Some seek redemption for past service to Immortan; others seek revenge.
        *   **Assets:** The War Rig, smaller vehicles, skills and determination, the Five Brides' symbolic importance.
        *   **Relationships:** Opposed to Immortan; potential allies in wasteland tribes; hope for the enslaved.
    *   **Wasteland Tribes** (Background)
        *   **Goals:** Survive, maintain their territories, trade.
        *   **Hierarchy:** Various structures—some democratic, some ruled by strongest warriors.
        *   **Public Agenda:** Stay neutral in conflicts between major powers.
        *   **Secret Agenda:** Many would support Immortan's overthrow but fear his power.
        *   **Assets:** Knowledge of the wasteland, hidden settlements, unique resources.
        *   **Relationships:** Wary of Citadel; potential allies or obstacles to the party; some hostile, some helpful.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Immortan Warlock:** The dying tyrant desperate for legacy, seeing himself as a god.
    *   **Furiosa:** The defector war captain seeking redemption and the Green Place.
    *   **Nux:** The War Boy who awakens to free will and chooses redemption.
    *   **The Five Brides:** Each with distinct personality—the warrior, healer, idealist, pragmatist, innocent.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "War Boy (Fanatical raider seeking glorious death)"
    *   "Citadel Worker (Enslaved but potentially sympathetic)"
    *   "Wasteland Nomad (Independent survivor)"
    *   "Gas Town Biker (Hostile territorial raider)"
    *   "Vuvalini Warrior (Elderly survivor from the dead Green Place)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Citadel:** A massive rock formation carved into a fortress with water flowing from deep wells.
        *   **Key Landmarks:** The water platform (where Immortan appears), the lift system, the breeding chambers, the vehicle depot, the worker caves.
        *   **Primary Inhabitants:** Immortan, his sons, War Boys, enslaved workers, the remaining Brides.
        *   **Available Goods & Services:** Water (rationed), fuel, weapons, but all controlled by Immortan.
        *   **Potential Random Encounters (x5):** Water rationing ceremony, War Boys preparing for pursuit, worker rebellion being crushed, vehicle maintenance, breeding program inspection.
        *   **Embedded Plot Hooks & Rumors (x3):** "Immortan is dying and desperate for heirs." "There are secret tunnels from when the Citadel was a mine." "The workers outnumber the War Boys ten to one."
        *   **Sensory Details:** Sight (Towering rock carved with levels, water cascading down, vehicles everywhere), Sound (Echoing chants, rumble of engines, flow of water), Smell (Engine oil, human sweat, the precious scent of water).
    *   **The Open Wasteland:** Endless desert between settlements, the primary setting for the chase.
        *   **Key Landmarks:** The canyon passes, the salt flats, the dune seas, the vehicle graveyard, hidden watering holes.
        *   **Primary Inhabitants:** Nomadic tribes, wasteland predators, the occasional hermit survivor.
        *   **Available Goods & Services:** Scavenging for fuel and parts, potential trade with nomads, natural water sources (rare).
        *   **Potential Random Encounters (x5):** Sandstorm approaching, vehicle breakdown, encounter with nomad traders, discovery of wreckage with supplies, ambush by territorial gang, mirage or heat exhaustion.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Green Place is three days east." "Gas Town controls the canyon passes." "There are things in the deep desert that survived the Cataclysm—changed things."
        *   **Sensory Details:** Sight (Endless orange sand, deep blue sky, heat shimmer, distant rock formations), Sound (Wind howl, engine roar, the crunch of tires on sand), Smell (Hot metal, dust, the complete absence of water).
    *   **The Dead Green Place:** A toxic swamp where paradise once existed.
        *   **Key Landmarks:** The dead trees still standing, the toxic pools, the remnants of the Vuvalini settlement, the crows' nesting grounds.
        *   **Primary Inhabitants:** The last Vuvalini warriors, mutated wildlife, death itself.
        *   **Available Goods & Services:** The Vuvalini can offer alliance and their seed vault—hope for the future.
        *   **Potential Random Encounters (x5):** Discovery of dead vegetation, encounter with Vuvalini elders, toxic pool danger, mutated predator, finding seeds in the vault.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Vuvalini have seeds from before the Cataclysm." "Poison killed the Green Place, but it can be cleansed." "The Citadel has the water needed to restore this land."
        *   **Sensory Details:** Sight (Skeletal trees in toxic water, oil-slick colors on pools, crow flocks), Sound (Eerie wind through dead trees, crow calls, bubbling toxic water), Smell (Decay, chemicals, death of hope).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The party maintains high distance on the Pursuit Clock consistently.
    *   **THEN:** Immortan becomes increasingly desperate and takes greater risks. Generate scenarios where he splits his forces or enters dangerous territory himself.
    *   **IF:** The War Rig is destroyed or abandoned.
    *   **THEN:** The party must acquire new vehicles and adapt tactics. Generate encounters focused on scavenging and rebuilding their convoy.
    *   **IF:** One of the Five Brides dies.
    *   **THEN:** The survivors' motivations shift. Generate emotional consequences and potential party conflict about whether the sacrifice was worth it.
    *   **IF:** Nux joins the party before his redemption arc completes.
    *   **THEN:** Generate trust issues and dramatic moments where he must prove himself, culminating in a self-sacrifice opportunity.
    *   **IF:** The party discovers the Green Place is dead but chooses to keep running east.
    *   **THEN:** Generate an alternate ending where they find other survivors or establish a new settlement, but never confront Immortan—leaving the Citadel's tyranny intact.
    *   **IF:** The party returns to assault the Citadel with the Vuvalini's help.
    *   **THEN:** Generate the siege scenario with specific tactical advantages from the Vuvalini's knowledge and the seeds they carry representing hope for the future.
    *   **IF:** In the finale, the party frees the water without killing Immortan.
    *   **THEN:** Generate an epilogue where Immortan becomes a broken figure worshipped by no one, watching as the people he controlled build something better—living is his punishment, not death.
