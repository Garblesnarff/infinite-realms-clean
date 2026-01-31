### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Glassflame Tower**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** During a lavish gala at the Glassflame Tower—a 40-story magical skyscraper—the party is trapped when the Crimson Hand mercenary company seizes the building. Led by Vorak Ironscale, the mercenaries seek an ancient artifact in the tower's vault. Separated from their gear and outnumbered twenty-to-one, the party must use improvisation, the tower's magical infrastructure, and guerrilla tactics to save hostages and stop the heist before the tower's magical core explodes.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the construction of the Glassflame Tower and its significance as a marvel of modern magical architecture.
    *   Write the history of the Crimson Hand mercenary company, from elite military unit to mercenary organization.
    *   Describe the Shard of Eternity—its origin, powers, and why it's hidden in the tower's vault.
    *   Explain the tower's magical infrastructure: how it's powered, what the core does, and what happens when it fails.
    *   Detail the betrayal that destroyed Vorak's original military unit and how the tower's owner was responsible.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Party (Reluctant Heroes)** (Minor)
        *   **Goals:** Survive, save the hostages, stop the theft, prevent the tower's destruction.
        *   **Hierarchy:** An impromptu group thrown together by circumstance.
        *   **Public Agenda:** Gala attendees or security personnel caught in the siege.
        *   **Secret Agenda:** Each member must decide if they're willing to become heroes or just survivors.
        *   **Assets:** Their skills, knowledge of the party layout, improvisation, and eventually control of tower systems.
        *   **Relationships:** Allied with surviving staff; opposed to the Crimson Hand; trying to rescue the hostages.
    *   **The Crimson Hand** (Major)
        *   **Goals:** Steal the Shard of Eternity, escape with minimal losses.
        *   **Hierarchy:** Military-style command structure led by Vorak, with specialized units for different tasks.
        *   **Public Agenda:** Professional mercenaries taking a high-value job.
        *   **Secret Agenda:** This is Vorak's personal revenge against the tower's owner; his troops don't know this could be a suicide mission.
        *   **Assets:** Superior numbers (50+ mercenaries), military training, prepared explosives and magical countermeasures, control of entry/exit points.
        *   **Relationships:** The antagonists, but professional rather than sadistic; some may desert if they learn the truth.
    *   **Tower Security & Staff** (Minor)
        *   **Goals:** Survive, protect their employer's property, assist the hostages.
        *   **Hierarchy:** Scattered survivors from the security force and maintenance staff.
        *   **Public Agenda:** Do their jobs and go home alive.
        *   **Secret Agenda:** Some security personnel feel guilty for failing to stop the takeover.
        *   **Assets:** Knowledge of the tower's systems, maintenance access, security protocols.
        *   **Relationships:** Natural allies to the party; fearful of the Crimson Hand; protective of civilian hostages.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Vorak Ironscale:** A brilliant, cold tactician with a tragic backstory and a revenge plot that's consuming him.
    *   **Lady Silviana Crystalwind:** A diplomat-mage who's more capable than she first appears, knows the truth about the Shard.
    *   **Griswold "Gris" Fixit:** The nervous but brave maintenance chief who becomes an unlikely hero.
    *   **Kesh the Silent:** Vorak's honorable but deadly lieutenant who can potentially be turned or reasoned with.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Crimson Hand Elite Soldier"
    *   "Crimson Hand Mage-Breaker (Anti-magic specialist)"
    *   "Terrified Gala Guest"
    *   "Wounded Security Guard"
    *   "Tower Maintenance Worker with Useful Knowledge"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Grand Ballroom (Floor 35):** Where hostages are kept, opulent and now fortified by mercenaries.
        *   **Key Landmarks:** Crystal chandeliers, the main stage, the floor-to-ceiling windows, the service entrance.
        *   **Primary Inhabitants:** Hostages (nobles, merchants, diplomats), Crimson Hand guards.
        *   **Available Goods & Services:** Improvised weapons from furniture, food and drink from the buffet.
        *   **Potential Random Encounters (x5):** Guard shift change, hostage causing a distraction, mercenary arguing about orders, VIP hostage attempting negotiation, discovery of hidden magical item in decoration.
        *   **Embedded Plot Hooks & Rumors (x3):** "Lady Silviana is not what she seems." "One of the hostages is a Crimson Hand spy." "The head of security is still alive somewhere."
        *   **Sensory Details:** Sight (Shattered crystal, overturned tables, city lights far below), Sound (Whispered conversations, boots on marble, distant magical hums), Smell (Spilled wine, smoke, fear-sweat).
    *   **The Service Corridors:** Hidden passages throughout the tower known mainly to staff.
        *   **Key Landmarks:** The main maintenance shaft, magical conduit junctions, the service elevator, Gris's workshop.
        *   **Primary Inhabitants:** Party members, Gris, other surviving staff, occasional mercenary patrols.
        *   **Available Goods & Services:** Tools, cleaning supplies that can be weaponized, access to tower systems.
        *   **Potential Random Encounters (x5):** Mercenary patrol searching corridors, magical conduit surge, structural damage blocking path, hidden stash of security equipment, survivor in hiding.
        *   **Embedded Plot Hooks & Rumors (x3):** "There's a secret route to the vault level." "The core is already unstable from poor maintenance." "Someone sabotaged the tower's defenses from inside."
        *   **Sensory Details:** Sight (Bare concrete, glowing magical conduits, tool racks), Sound (Hum of machinery, dripping water, echoing footsteps), Smell (Ozone from magic, industrial cleaners, dust).
    *   **The Vault Level (Basement 3):** Ancient architecture housing priceless artifacts.
        *   **Key Landmarks:** The main vault door, the Shard's containment chamber, the runic defense grid, the emergency exit.
        *   **Primary Inhabitants:** Crimson Hand specialists, magical guardians, eventually Vorak himself.
        *   **Available Goods & Services:** Ancient magical items (dangerous to use), the Shard of Eternity.
        *   **Potential Random Encounters (x5):** Specialist team cracking vault, magical trap activation, guardian construct activating, structural tremor from magical feedback, discovery of other vault contents.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Shard is more dangerous than the theft." "Vorak plans to use it here, not escape with it." "The vault's defenses are alive."
        *   **Sensory Details:** Sight (Ancient stone, modern magical security, crackling energy barriers), Sound (Drilling/cutting sounds, arcane humming, stone grinding), Smell (Aged stone, ozone, burnt magic).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The party gains access to the tower security center.
    *   **THEN:** They can monitor mercenary positions, lock/unlock doors, and control elevators. Generate specific tactical advantages this provides for upcoming encounters.
    *   **IF:** The party successfully rescues a group of hostages.
    *   **THEN:** Those hostages can provide information, resources, or assistance. One might be a mage who can help with magical problems. Mercenaries become more aggressive in response.
    *   **IF:** The tower's stability drops below 5.
    *   **THEN:** Generate progressive environmental hazards: tremors that require DEX saves, magical surges that cause wild magic effects, sections of floors collapsing, elevator failures.
    *   **IF:** The party kills or captures Kesh the Silent.
    *   **THEN:** Vorak becomes emotionally compromised, making tactical errors but also becoming more dangerous and unpredictable. Generate specific changes to his final encounter.
    *   **IF:** The party discovers Vorak's true revenge motive.
    *   **THEN:** They can potentially exploit this information to turn some of his mercenaries against him, or use it in negotiation. Generate NPC reactions and potential defector scenarios.
    *   **IF:** The party uses improvised explosives excessively.
    *   **THEN:** Accelerate the tower's structural instability. Generate additional collapse events and reduce the time available in the final act.
    *   **IF:** In the finale, the party chooses to stabilize the tower instead of pursuing Vorak immediately.
    *   **THEN:** Vorak escapes with the Shard, but hundreds of lives are saved. Generate an epilogue where the party must deal with the consequences of the Shard being in the world and Vorak still at large.
