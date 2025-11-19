### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Color Code Conspiracy: Strangers in Blood**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The players are criminals recruited for a "simple" heist using color-coded aliases to protect their identities: Mr. Ruby, Ms. Emerald, Mr. Sapphire, and so on—strangers thrown together for one job. When the heist goes catastrophically wrong with law enforcement waiting in ambush, the surviving crew members retreat to a safehouse to figure out who betrayed them. Trapped together, bleeding, paranoid, and heavily armed, they must uncover the traitor among them while law enforcement closes in and old grudges surface. As accusations fly and guns are drawn, the campaign becomes a pressure cooker of violence, betrayal, and the desperate mathematics of survival when you can't trust anyone.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the history of color-code operations in the criminal underworld and why aliases protect against betrayal.
    *   Write about "The Boss" and their reputation for assembling perfect crews that never know each other's real identities.
    *   Describe famous heists that went wrong due to betrayal and how they shaped criminal culture.
    *   Explain law enforcement infiltration tactics and how informants operate within criminal organizations.
    *   Detail the warehouse district and its history as a haven for criminal safehouses.
    *   Write about the diamond district and the high-value targets it represents to professional thieves.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Boss's Organization** (Major—possibly compromised)
        *   **Goals:** To execute profitable heists using compartmentalized crews that can't betray the whole organization.
        *   **Hierarchy:** The Boss at the top, with intermediaries who recruit and coordinate but never meet the full crew.
        *   **Public Agenda:** We do not exist.
        *   **Secret Agenda:** Unknown—the Boss's true motives for this job remain mysterious.
        *   **Assets:** Criminal networks, recruitment capabilities, safehouse locations, fencing operations.
        *   **Relationships:** Pays well but abandons compromised crews; may have law enforcement infiltration.
    *   **Major Crimes Task Force** (Major)
        *   **Goals:** To infiltrate and destroy the Boss's organization through informants and stings.
        *   **Hierarchy:** Detective Kross leads a task force with embedded informants and tactical teams.
        *   **Public Agenda:** We protect citizens from organized crime through aggressive prosecution.
        *   **Secret Agenda:** To use infiltration to take down the entire criminal network, with informants at all levels.
        *   **Assets:** Informants within criminal crews, siege capabilities, surveillance technology.
        *   **Relationships:** Antagonistic toward all criminals; may have planted multiple informants in this crew.
    *   **The Criminal Underworld** (Minor)
        *   **Goals:** To profit from crime while avoiding betrayal and law enforcement.
        *   **Hierarchy:** Fragmented groups connected through fences, fixers, and shared resources.
        *   **Public Agenda:** We take care of our own and punish traitors brutally.
        *   **Secret Agenda:** Survival through paranoia—trust no one, especially strangers using fake names.
        *   **Assets:** Criminal expertise, underground economy, violent enforcement of codes.
        *   **Relationships:** Deeply suspicious of everyone; united only by hatred of informants.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **"The Boss":** The mysterious employer who assembled this doomed crew.
    *   **Mr. Crimson:** The experienced professional trying to maintain order.
    *   **Ms. Gold:** The wounded crew member whose condition deteriorates.
    *   **Detective Kross:** The law enforcement officer coordinating the siege.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Color-Coded Criminal"
    *   "Tactical Officer"
    *   "Wounded Crew Member"
    *   "Paranoid Suspect"
    *   "Diamond District Security"
    *   "Fence/Intermediary"
    *   "Siege Negotiator"
    *   "Potential Traitor"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Vault:** The diamond merchant's repository.
        *   **Key Landmarks:** Vault Door, Security Office, Display Cases, Alarm Systems.
        *   **Primary Inhabitants:** Security guards, staff (during business hours).
        *   **Available Goods & Services:** High-value diamonds, security systems to overcome.
        *   **Potential Random Encounters (x5):** Early security patrol, alarm malfunction, civilian witness, security backup, unexpected safe.
        *   **Embedded Plot Hooks & Rumors (x3):** "The vault was supposed to be easy." "Security knew exactly when we'd hit." "Someone gave them our full plan."
        *   **Sensory Details:** Sight (Gleaming display cases, vault architecture, security cameras), Sound (Alarm systems, security radios, breaking glass), Smell (New carpet, electronics, fear-sweat).
    *   **The Ambush Point:** The street where law enforcement sprang their trap.
        *   **Key Landmarks:** Intersection, Police Barricades, Civilian Areas, Escape Routes (blocked).
        *   **Primary Inhabitants:** Law enforcement in force, fleeing criminals, civilian bystanders.
        *   **Available Goods & Services:** None—this is a combat zone.
        *   **Potential Random Encounters (x5):** Sniper fire, tactical team, fleeing crew member, civilian interference, dropped loot.
        *   **Embedded Plot Hooks & Rumors (x3):** "They were waiting for us." "Someone called in our exact route." "This wasn't random—they knew."
        *   **Sensory Details:** Sight (Police lights, drawn weapons, blood on pavement), Sound (Gunfire, sirens, shouting, breaking glass), Smell (Gunpowder, blood, car exhaust).
    *   **The Warehouse Safehouse:** The crew's prison/refuge.
        *   **Key Landmarks:** Loading Bay, Office Space, Storage Areas, Blocked Exits, Windows to Siege.
        *   **Primary Inhabitants:** The surviving crew members, surrounded by law enforcement.
        *   **Available Goods & Services:** Temporary shelter, diminishing supplies, interrogation space.
        *   **Potential Random Encounters (x5):** Crew argument, weapon drawn, wounded member worsening, law enforcement communication, attempt to escape.
        *   **Embedded Plot Hooks & Rumors (x3):** "The warehouse was supposed to be secure." "One of us is the reason cops found this place." "We're trapped until someone dies or talks."
        *   **Sensory Details:** Sight (Industrial lighting, blood stains, drawn weapons, police lights through windows), Sound (Echoing voices, sirens outside, weapons cocking, labored breathing), Smell (Blood, industrial dust, fear-sweat, gunpowder residue).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The crew accuses someone of being the traitor.
    *   **THEN:** That crew member must defend themselves, potentially with violence. Generate interrogation, defense, and possible execution scenarios.
    *   **IF:** Violence breaks out in the safehouse.
    *   **THEN:** Multiple crew members may die in crossfire, further reducing survivors. Generate cascading gunfight mechanics.
    *   **IF:** The wounded crew member dies without revealing information.
    *   **THEN:** The crew loses potential evidence and tensions escalate. Generate paranoia increase and violent responses.
    *   **IF:** Law enforcement makes an ultimatum or assault.
    *   **THEN:** The crew must choose between surrender, suicide mission escape, or turning on each other. Generate desperate final stand scenarios.
    *   **IF:** The traitor is correctly identified.
    *   **THEN:** That revelation changes all previous events' context, potentially too late to matter. Generate aftermath where everyone still dies despite knowing the truth.
    *   **IF:** The crew turns on each other in a Mexican standoff.
    *   **THEN:** Multiple simultaneous attacks result in most or all crew members dying. Generate tragic finale where paranoia kills everyone.
