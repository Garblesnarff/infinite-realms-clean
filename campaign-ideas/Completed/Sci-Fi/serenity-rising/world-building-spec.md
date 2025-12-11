# World-Building Specification Brief: Serenity Rising

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**Serenity Rising**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The players are the crew of the Serenity, a small transport ship taking odd jobs on the frontier. When they rescue River—a traumatized girl with psychic powers—they become targets of the Alliance totalitarian government. They must stay ahead of Alliance operatives while uncovering the Miranda secret: the Alliance created the Reavers through failed terraforming. To expose this atrocity, they risk everything in a suicide mission that makes them legends and outcasts.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the Unification War between the Alliance (centralized government of core worlds) and the Independents (frontier colonists fighting for autonomy). The Independents lost.
    *   Write the history of terraforming—how humanity left Earth-That-Was and colonized a vast star system with hundreds of terraformed worlds.
    *   Describe the creation of Reavers: the Miranda experiment with the Pax drug that made 99.9% of the population docile until death, and turned 0.1% into savage cannibals.
    *   Explain the social structure: Core worlds are wealthy and controlled by the Alliance, Rim worlds are poor and lawless frontiers where Independents fled.
    *   Detail the Blue Sun Corporation—a mega-corporation with ties to the Alliance that funded River's experimentation and controls much of the economy.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Alliance** (Major)
        *   **Goals:** Maintain order and unity across all colonized worlds through centralized control.
        *   **Hierarchy:** Parliament, military command, intelligence agencies (Hands of Blue, the Operative).
        *   **Public Agenda:** Peace, prosperity, and civilization for all worlds.
        *   **Secret Agenda:** Suppress dissent, cover up the Miranda tragedy, maintain power through propaganda and force.
        *   **Assets:** Massive military fleet, advanced technology, intelligence networks, the law itself.
        *   **Relationships:** Controls Core worlds absolutely. Opposed by Independents. Uses corporations like Blue Sun as proxies.
    *   **The Independents (Browncoats)** (Minor - Defeated)
        *   **Goals:** (Former) Autonomy for frontier worlds. (Current) Survival and resistance.
        *   **Hierarchy:** (Former) Loose coalition of colonial militias. (Current) Scattered veterans and sympathizers.
        *   **Public Agenda:** None—they lost the war and are seen as traitors by the Alliance.
        *   **Secret Agenda:** Some dream of reigniting resistance. Most just want to live free on the Rim.
        *   **Assets:** Surviving soldiers with military training, sympathetic Rim populations, scrappy resourcefulness.
        *   **Relationships:** Hunted by the Alliance. Folk heroes on Rim worlds. Many became smugglers and outlaws.
    *   **Blue Sun Corporation** (Major)
        *   **Goals:** Profit and power through monopolistic control of key industries.
        *   **Hierarchy:** Corporate board, regional directors, research divisions, private security.
        *   **Public Agenda:** Provide goods and services across the 'Verse.
        *   **Secret Agenda:** Fund Alliance black ops projects (like River's academy), control politicians, eliminate competition.
        *   **Assets:** Immense wealth, research facilities, private armies, political influence.
        *   **Relationships:** Alliance partner and puppet master. Ordinary people are consumers or experiments.
    *   **The Reavers** (Minor - Monstrous)
        *   **Goals:** None—they're driven by instinctual rage and cannibalistic urges.
        *   **Hierarchy:** None—they move in packs without leadership or strategy beyond basic hunting.
        *   **Public Agenda:** Unknown—they simply attack, mutilate, and consume.
        *   **Secret Agenda:** (Revealed) They're victims of the Pax experiment on Miranda, transformed into living nightmares.
        *   **Assets:** Stolen ships, no fear of death, savage ferocity, terror they inspire.
        *   **Relationships:** Feared by everyone. The Alliance uses them as the boogeyman of the black.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Malcolm Reynolds:** Captain of Serenity, former Independent sergeant, sarcastic and principled, haunted by the war.
    *   **River Tam:** Psychic weapon created by Alliance experimentation, traumatized genius, speaks in riddles, deadly when triggered.
    *   **The Operative:** Nameless Alliance assassin, believes in perfection he'll never see, philosophical killer.
    *   **Shepherd Book:** Ship's preacher with mysterious Alliance connections, seeks redemption, knows violence.
    *   **Niska:** Sadistic crime lord, tortures for pleasure, holds grudges eternally.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Rim World Sheriff (Frontier lawman, practical justice, suspicious of outsiders)"
    *   "Alliance Officer (Career military, believes in order, underestimates Browncoats)"
    *   "Smuggler/Criminal (Takes illegal jobs, pragmatic, networked with underworld)"
    *   "Reaver (Savage cannibal, mutilated appearance, no negotiation possible)"
    *   "Blue Sun Agent (Corporate operative, cold professionalism, expendable assets)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Serenity (Firefly-class Transport):**
        *   **Key Landmarks:** Cargo bay with loading ramp, common area with kitchen and table, engine room, crew quarters, hidden smuggling compartments, bridge.
        *   **Primary Inhabitants:** The party—this is their home.
        *   **Available Goods & Services:** Transport, smuggling capacity, weapons cache, medical bay (basic), quarters.
        *   **Potential Random Encounters (x5):** N/A—this is the party's safe space.
        *   **Embedded Plot Hooks & Rumors (x3):** "The ship has smuggling compartments that fool most scanners—but Alliance knows they exist." "The engine is held together with prayers and spare parts—it'll fail at the worst time." "Someone left personal belongings from before the war hidden in their bunk."
        *   **Sensory Details:** Sight (Industrial gray metal, warm amber lighting, wooden crates, worn couches, exposed wiring), Sound (Engine hum, metal groaning, footsteps echoing, Wash's toy dinosaurs), Smell (Oil, recycled air, cooking food, metal and rust).
    *   **Persephone (Border World):**
        *   **Key Landmarks:** Eavesdown Docks (spaceport), high-society estates, industrial district, criminal underground.
        *   **Primary Inhabitants:** Mix of wealthy Alliance supporters and poor laborers, criminals, Independents.
        *   **Available Goods & Services:** Legal and illegal cargo, ship repairs, black market, social gatherings, job opportunities.
        *   **Potential Random Encounters (x5):** Alliance patrol questions crew, crime lord offers job, high-society party (social infiltration), pickpocket attempts theft, old war buddy recognizes crew.
        *   **Embedded Plot Hooks & Rumors (x3):** "Badger controls the criminal underworld here—cross him and you're done." "There's an underground network helping Independents escape Alliance attention." "Alliance intelligence operates out of the Governor's estate."
        *   **Sensory Details:** Sight (Mix of elegant manors and grimy docks, ships coming and going, Chinese architecture), Sound (Ship engines, market vendors shouting, music from taverns), Smell (Ship fuel, cooking food, industrial smoke, flowers from estates).
    *   **Miranda (Dead Planet):**
        *   **Key Landmarks:** Silent cities with millions of corpses where they fell, central plaza with recording station, Alliance research facility (abandoned), ships that never launched.
        *   **Primary Inhabitants:** None—entire population is dead. Reavers sometimes pass through.
        *   **Available Goods & Services:** The truth—recordings of what happened.
        *   **Potential Random Encounters (x5):** Discover personal logs from final survivors, Reaver ship lands nearby, Alliance patrol was here first (bodies), holographic message plays on repeat, evidence of how people died peacefully.
        *   **Embedded Plot Hooks & Rumors (x3):** "The last survivor left a recording—she was an Alliance scientist confessing everything." "This planet proves the Alliance created Reavers." "If this information reaches the 'Verse, the Alliance will kill anyone involved."
        *   **Sensory Details:** Sight (Intact buildings, bodies preserved in dry atmosphere, ships ready to launch but empty), Sound (Absolute silence, wind, the crew's breathing), Smell (Dust, desiccated remains, sterile emptiness).
    *   **Mr. Universe's Complex:**
        *   **Key Landmarks:** Broadcast tower capable of reaching entire 'Verse, server rooms, living quarters, memorial to Mr. Universe's robot wife.
        *   **Primary Inhabitants:** Mr. Universe (tech genius), his robot companion.
        *   **Available Goods & Services:** Information brokerage, communication systems, universal signal boost.
        *   **Potential Random Encounters (x5):** Mr. Universe is already dead (killed by the Operative), automated defenses activate, Alliance troops assault the complex, Reavers attack during broadcast, emergency power fails.
        *   **Embedded Plot Hooks & Rumors (x3):** "Mr. Universe can broadcast to every screen in the 'Verse—but the Alliance knows this and will defend it." "The signal must reach the central hub or it'll be filtered out." "Getting here requires flying through Reaver space."
        *   **Sensory Details:** Sight (Walls covered in screens and equipment, blinking lights, dust from abandoned areas), Sound (Electronic hum, news broadcasts playing, alarms), Smell (Electronics, dust, recycled air).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The party betrays River to the Alliance for reward money.
    *   **THEN:** Generate consequences where Simon hunts the party for revenge. River is turned into a fully activated weapon, and the Alliance deploys her against Independents. The crew's reputation is destroyed.
    *   **IF:** The party successfully broadcasts the Miranda recording.
    *   **THEN:** Generate an epilogue where Rim worlds celebrate them as heroes, Core worlds brand them terrorists. The Alliance is weakened but not destroyed. Independent resistance grows.
    *   **IF:** The party refuses to broadcast the truth and keeps Miranda secret.
    *   **THEN:** Generate moral consequences—guilt, nightmares, fractures in the crew. The Alliance continues covering up atrocities. Reavers continue being seen as natural monsters.
    *   **IF:** The Operative learns the truth about Miranda before the final confrontation.
    *   **THEN:** Generate a scenario where he becomes an ally, helping the party broadcast the truth. He then disappears, unable to serve the Alliance or forgive himself.
    *   **IF:** A crew member dies during the final mission.
    *   **THEN:** Generate a funeral scene and lasting impact on the crew. The survivor's guilt drives future choices. Their death proves the cost of defying the Alliance.
    *   **IF:** The party kills Niska permanently.
    *   **THEN:** Generate consequences where his criminal network fractures. Other crime lords fight for territory. Some offer the party alliances; others seek revenge.
    *   **IF:** River's psychic powers are fully stabilized and controlled.
    *   **THEN:** Generate a scenario where she becomes the crew's greatest protector—a warrior who chooses when to fight rather than being triggered involuntarily.
