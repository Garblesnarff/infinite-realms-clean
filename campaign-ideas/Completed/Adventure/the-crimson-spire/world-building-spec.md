### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Crimson Spire**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** Elite city guard members raid a 30-story tower controlled by crime lord Tama. When the tower is sealed and a bounty placed on their heads, they must fight upward through escalating waves of gang members. Each floor brings deadlier enemies in tighter spaces, with no backup and dwindling resources, culminating in facing Tama's legendary enforcers and the crime lord himself.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the history of the Crimson Spire tenement and how it became a gang fortress.
    *   Write Tama's rise to power in the criminal underworld and why the city guard finally moved against him.
    *   Describe the elite guard force the party belongs to—their training, reputation, and code.
    *   Explain the tower's defensive capabilities and how Tama can seal it completely.
    *   Detail the gang hierarchy within the tower—different territories, lieutenants, and the three elite enforcers.
    *   Describe the corruption in the city guard that led to the party walking into a trap.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Elite City Guard** (Minor - Party)
        *   **Goals:** Arrest Tama, uphold the law, survive.
        *   **Hierarchy:** Chain of command with the party as a specialized unit.
        *   **Public Agenda:** Protect the city from organized crime.
        *   **Secret Agenda:** Some guard leaders are corrupt; the party may be expendable pawns.
        *   **Assets:** Elite combat training, institutional support (usually), mandate of law.
        *   **Relationships:** At war with Tama's organization; betrayed by corrupt elements; the party is trapped and alone.
    *   **Tama's Criminal Organization** (Major)
        *   **Goals:** Maintain control of territory, protect the boss, eliminate threats.
        *   **Hierarchy:** Tama at top, three elite enforcers, floor lieutenants, rank-and-file gang members.
        *   **Public Agenda:** Control drug trade, protection rackets, and illegal operations.
        *   **Secret Agenda:** Tama is building toward something bigger—possibly a coup or takeover of city government.
        *   **Assets:** The fortified tower, hundreds of gang members, drug production, the three enforcers.
        *   **Relationships:** Opposed to city guard; paying off corrupt officials; ruthless to civilians.
    *   **The Corrupt Officials** (Background)
        *   **Goals:** Profit from both sides, maintain power, eliminate idealistic guards.
        *   **Hierarchy:** Scattered individuals in positions of power.
        *   **Public Agenda:** Serve justice.
        *   **Secret Agenda:** Profit from crime while appearing clean; set up the party to be eliminated.
        *   **Assets:** Authority to order operations, ability to withhold backup, insider information.
        *   **Relationships:** Secret alliance with Tama; view party as threat to their arrangement.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Tama:** The cultured, dangerous crime lord who's also a master martial artist.
    *   **Mad Dog:** The berserker enforcer who fights with brutal close-quarters combat.
    *   **The Assassin:** The elegant knife specialist treating killing as art.
    *   **The Hammer:** The massive, loyal enforcer with overwhelming strength.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Gang Thug (Low-level members, numbers over skill)"
    *   "Gang Enforcer (Mid-level, coordinated tactics)"
    *   "Drugged Berserker (Enhanced strength, feels no pain)"
    *   "Floor Lieutenant (Mini-boss for each sector)"
    *   "Elite Guard (Tama's personal protection on top floors)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **Lower Floors (1–10):** Residential tenements turned gang housing.
        *   **Key Landmarks:** The main entrance (now sealed), central stairwell, various cramped apartments, the first safe room.
        *   **Primary Inhabitants:** Low-level gang members, drug users, prisoners.
        *   **Available Goods & Services:** Scavenged weapons and supplies from defeated enemies.
        *   **Potential Random Encounters (x5):** Ambush from apartment, trap in stairwell, hostage situation, discover gang drug stash, floor lieutenant appears.
        *   **Embedded Plot Hooks & Rumors (x3):** "Tama has magical wards sealing the building." "There are non-combatants trapped here." "A corrupt guard warned Tama about the raid."
        *   **Sensory Details:** Sight (Worn walls, graffiti, blood stains, flickering lights), Sound (Shouts, footsteps echoing, distant combat), Smell (Sweat, fear, chemicals).
    *   **Drug Labs (21–26):** Manufacturing floors filled with hazards.
        *   **Key Landmarks:** The main production lab, storage rooms filled with volatile chemicals, testing chambers, overseer's office.
        *   **Primary Inhabitants:** Berserker guards high on combat drugs, chemists defending their operation.
        *   **Available Goods & Services:** Combat stimulants (with side effects), alchemical supplies.
        *   **Potential Random Encounters (x5):** Chemical explosion, berserker wave attack, accidental fire, trapped lab worker, Mad Dog's dramatic entrance.
        *   **Embedded Plot Hooks & Rumors (x3):** "The drugs make you stronger but cost you sanity." "Tama tests the products on his own guards." "There's an antidote formula hidden here."
        *   **Sensory Details:** Sight (Industrial equipment, chemical barrels, workers in protective gear), Sound (Bubbling liquids, industrial hum, incoherent shouting), Smell (Acrid chemicals, burning, toxic fumes).
    *   **The Penthouse (27–30):** Tama's luxurious headquarters.
        *   **Key Landmarks:** The throne room, training dojo, armory, viewing balcony, the sealed magical ward controls.
        *   **Primary Inhabitants:** Tama, his remaining elite enforcers, personal guards.
        *   **Available Goods & Services:** The truth about the betrayal, Tama's personal armory.
        *   **Potential Random Encounters (x5):** Enforcer battles, elite guard squads, magical traps, final standoff with Tama.
        *   **Embedded Plot Hooks & Rumors (x3):** "Tama was once a city guard himself." "He knows martial arts techniques no one else does." "The ward controls are here—break them to escape."
        *   **Sensory Details:** Sight (Luxury contrasting with violence outside, art and culture, weapons on display), Sound (Quiet after chaos, Tama's calm voice, the city outside), Smell (Incense, quality wood, expensive alcohol).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The party attempts to rest without finding a safe room.
    *   **THEN:** Generate an ambush scenario. Exhaustion forces mistakes, and enemies capitalize.
    *   **IF:** The party discovers and uses combat stimulant drugs.
    *   **THEN:** Grant temporary combat bonuses but track addiction and withdrawal. Generate side effects and moral dilemmas.
    *   **IF:** The party defeats Mad Dog through cunning rather than direct combat.
    *   **THEN:** He respects them and reveals information about Tama's past before dying. Generate this exchange.
    *   **IF:** The party splits up to face multiple threats.
    *   **THEN:** Generate separate encounter chains, with potential for one group to be overwhelmed and need rescue.
    *   **IF:** The party reaches the penthouse with minimal resources remaining.
    *   **THEN:** Tama offers a deal—single combat with him, winner takes all. Generate this negotiation.
    *   **IF:** In the finale, the party exposes the corruption rather than just defeating Tama.
    *   **THEN:** Generate an epilogue where the guard is reformed but the party faces political consequences for revealing the truth.
