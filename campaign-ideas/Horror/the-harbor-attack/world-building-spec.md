# World-Building Specification Brief: The Harbor Attack

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Harbor Attack**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The party is in the bustling port city of Harbordeep when a massive, unknown creature emerges from the ocean and begins destroying the harbor district. As panic spreads and the creature advances into the city, the party must navigate collapsing buildings, stampeding crowds, and a military response that only seems to make things worse. Complicating matters, smaller parasitic creatures fall from the main beast, hunting anyone they encounter. The party must reach an evacuation point while helping those they can—knowing they cannot save everyone.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the founding of Harbordeep as a major port city, its economy based on trade and fishing, and its population of ~50,000.
    *   Write about the Heart of the Deep: an ancient relic stolen from the Abyssal Rift centuries ago by treasure hunters, believed to grant dominion over the ocean.
    *   Describe Thalos the Deep-Born: an ancient guardian creature from the Abyssal Rift, tasked with protecting the Heart.
    *   Explain why Thalos has awoken now: the Heart's seal has weakened, allowing Thalos to sense its location.
    *   Detail the spawn creatures: parasites that live on Thalos's hide, falling off when it enters shallow water. They are mindless hunters.
    *   Write about the Lantern Festival: Harbordeep's annual celebration, which tragically coincides with Thalos's attack.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Survivors** (Major)
        *   **Goals:** Escape the city, protect loved ones, survive at any cost.
        *   **Hierarchy:** No formal structure; informal leaders emerge (Captain Rhysa, the party).
        *   **Public Agenda:** Get to the evacuation point. Help who you can.
        *   **Secret Agenda:** Many survivors are willing to abandon others to save themselves.
        *   **Assets:** Numbers, local knowledge, desperation.
        *   **Relationships:** Trust the party as potential leaders; panicked and prone to stampedes.
    *   **The City Guard** (Minor)
        *   **Goals:** Evacuate civilians, fight the spawn creatures, stop Thalos (futile).
        *   **Hierarchy:** Led by Captain Rhysa, divided into squads scattered across the city.
        *   **Public Agenda:** We are here to protect you. Follow our orders.
        *   **Secret Agenda:** High command has ordered a full retreat, leaving civilians behind.
        *   **Assets:** Weapons, armor, magical artillery (ineffective against Thalos).
        *   **Relationships:** Overwhelmed and understaffed; view the party as allies or liabilities depending on their actions.
    *   **The Cathedral Order** (Minor)
        *   **Goals:** Protect the Heart of the Deep (not knowing it's causing the disaster).
        *   **Hierarchy:** Led by High Priest Davron, includes priests and temple guards.
        *   **Public Agenda:** The cathedral is sacred ground. We will not abandon it.
        *   **Secret Agenda:** The Order knows the Heart is dangerous but believes it's too valuable to return.
        *   **Assets:** Knowledge of the Heart, temple defenses, religious authority.
        *   **Relationships:** Will resist the party if they try to take the Heart; may be convinced with evidence.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Thalos the Deep-Born:** Ancient sea guardian, colossal and unstoppable, seeking the Heart of the Deep.
    *   **Captain Rhysa Coldan:** Military officer organizing evacuations, brave but grief-stricken.
    *   **Scholar Viresh:** Historian who knows about the Heart, guilt-ridden over the disaster.
    *   **Kellen:** A young boy separated from his family, innocent and vulnerable.
    *   **High Priest Davron:** Leader of the Cathedral Order, stubborn and protective of the Heart.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Panicked Civilian"
    *   "City Guard Soldier"
    *   "Injured Survivor"
    *   "Looter Taking Advantage"
    *   "Parent Searching for Child"
    *   "Spawn Creature"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Harbor District:** The initial attack site, now devastated.
        *   **Key Landmarks:** The docks (collapsed), the Festival Square (underwater), overturned ships, flooded streets.
        *   **Primary Inhabitants:** Dead or fled. Spawn creatures nest in wrecked ships.
        *   **Available Goods & Services:** None—pure destruction.
        *   **Potential Random Encounters (x5):** Spawn creature ambush, collapsing building, tidal wave, discovery of corpses, lone survivor.
        *   **Embedded Plot Hooks & Rumors (x3):** "Someone saw Thalos heading inland." "The military's bombardment only made it angrier." "There are spawn nests in the wrecked ships."
        *   **Sensory Details:** Sight (Water, rubble, fires, capsized ships), Sound (Creaking metal, distant roars, water lapping), Smell (Saltwater, smoke, death).
    *   **The Middle City:** Residential and commercial districts under siege.
        *   **Key Landmarks:** Market Square, residential towers (partially collapsed), military checkpoint, abandoned tavern.
        *   **Primary Inhabitants:** Fleeing civilians, spawn creatures, scattered guards.
        *   **Available Goods & Services:** Scavenged supplies, medical aid at checkpoint (limited).
        *   **Potential Random Encounters (x5):** Stampeding crowd, spawn attack, building collapse, injured NPC, looters.
        *   **Embedded Plot Hooks & Rumors (x3):** "The creature is heading toward the cathedral." "Captain Rhysa is at the checkpoint organizing evacuations." "A scholar at the archives might know what this thing is."
        *   **Sensory Details:** Sight (Leaning buildings, fires, crowds), Sound (Screams, Thalos's roar, distant explosions), Smell (Smoke, dust, panic sweat).
    *   **The Cathedral District:** The heart of the city, Thalos's destination.
        *   **Key Landmarks:** The Grand Cathedral (partially destroyed), the vault (underground), the archives, rubble-filled streets.
        *   **Primary Inhabitants:** Cathedral Order, spawn creatures, Scholar Viresh.
        *   **Available Goods & Services:** Knowledge, the Heart of the Deep (if accessed).
        *   **Potential Random Encounters (x5):** Cathedral guard confrontation, spawn swarm, Thalos's arrival, collapsing vault, High Priest's plea.
        *   **Embedded Plot Hooks & Rumors (x3):** "The cathedral holds an ancient relic from the ocean." "Thalos is searching for something specific." "The Order will die before giving up the Heart."
        *   **Sensory Details:** Sight (Stone ruins, stained glass shards, Thalos looming), Sound (Thalos's footsteps, crumbling stone, prayers), Smell (Incense, dust, ocean brine).
    *   **The Evacuation Point:** The city gates, the last chance to escape.
        *   **Key Landmarks:** The gates (fortified), the refugee camp, military transports, spawn-infested ruins nearby.
        *   **Primary Inhabitants:** Thousands of refugees, guards, Captain Rhysa.
        *   **Available Goods & Services:** Evacuation (if the party arrives in time), medical triage.
        *   **Potential Random Encounters (x5):** Spawn attack on camp, refugee panic, transport leaving, NPC begging for help, military standoff.
        *   **Embedded Plot Hooks & Rumors (x3):** "The last transport leaves in an hour." "There's a spawn nest blocking the main route." "Captain Rhysa is holding the line, but she can't hold forever."
        *   **Sensory Details:** Sight (Crowded camp, military transports, distant Thalos), Sound (Crying children, orders shouted, engines), Smell (Sweat, fear, exhaust).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The party returns the Heart of the Deep to Thalos.
    *   **THEN:** Thalos takes the Heart and retreats into the ocean. The spawn creatures die or flee. The city is saved but heavily damaged. High Priest Davron is furious and denounces the party.
    *   **IF:** The party destroys the Heart of the Deep.
    *   **THEN:** Thalos goes berserk, unleashing a final, catastrophic rampage. The cathedral district is leveled. The Evacuation Clock advances by 3.
    *   **IF:** The party ignores the Heart and focuses only on evacuation.
    *   **THEN:** Thalos destroys the cathedral, finds the Heart on its own, and retreats—but the delay costs thousands more lives.
    *   **IF:** The Evacuation Clock reaches 12 before the party arrives.
    *   **THEN:** The final transport leaves without them. The party must survive in the ruined city or find another escape route (dangerous).
    *   **IF:** The party destroys multiple spawn nests.
    *   **THEN:** Spawn encounters decrease by 25% per nest destroyed. Civilian casualties drop. Captain Rhysa commends the party.
    *   **IF:** The party saves Kellen and reunites him with surviving family (if any).
    *   **THEN:** Morale among refugees improves. Kellen becomes a symbol of hope. The party gains reputation as heroes.
    *   **IF:** Thalos reaches the evacuation point before the party escapes.
    *   **THEN:** The campaign enters a desperate final stand. The party must hold the line while transports flee. High casualties.
