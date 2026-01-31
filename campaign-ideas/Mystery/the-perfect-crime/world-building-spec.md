### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Perfect Crime: Hostage to Fortune**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The players execute what appears to be a straightforward bank heist that goes wrong, taking hostages and becoming trapped inside during a tense standoff with law enforcement. But as the siege unfolds, it becomes clear that the heist and the hostage situation are all misdirection—the real crime is happening behind the scenes through layers of careful planning and psychological manipulation. The investigators, hostages, and even some crew members don't realize they're all playing roles in an elaborate performance designed to obscure the true objective. What seems like a failed robbery is actually a perfect crime unfolding exactly as planned, and by the time anyone realizes it, the mastermind will have vanished with something far more valuable than gold.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the founding of Sterling Bank and its dark history of being used to hide evidence of crimes by powerful families.
    *   Write about the historical conspiracy the Architect seeks to expose—murders, theft, and corruption buried in safe deposit boxes.
    *   Describe famous perfect crimes in history and the philosophy that inspired the Architect's approach.
    *   Explain the psychology of hostage negotiation and how it can be manipulated by those who understand it.
    *   Detail the safe deposit system and how it became a repository for secrets meant to stay buried.
    *   Write about Marcus "The Ghost" Vale's childhood witness to the original crime and his lifetime of planning revenge.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Architect's Plan** (Major—partially hidden)
        *   **Goals:** To expose historical crimes and achieve justice through the perfect heist.
        *   **Hierarchy:** The Architect at the top, with crew members at different knowledge levels.
        *   **Public Agenda:** We're bank robbers who got trapped and took hostages.
        *   **Secret Agenda:** We're gathering evidence and witnesses to expose a decades-old conspiracy.
        *   **Assets:** Perfect planning, psychological manipulation, misdirection, insider knowledge.
        *   **Relationships:** Crew members trust the Architect; law enforcement thinks they understand the situation but don't.
    *   **Law Enforcement Response** (Major)
        *   **Goals:** To resolve the hostage situation peacefully and capture the criminals.
        *   **Hierarchy:** SWAT teams, negotiators, detectives, led by experienced commanders.
        *   **Public Agenda:** We protect innocent lives and bring criminals to justice.
        *   **Secret Agenda:** Some officers may be connected to the conspiracy being exposed.
        *   **Assets:** Numbers, tactical response capabilities, negotiation expertise, surveillance.
        *   **Relationships:** Antagonistic toward the crew; protective of hostages; increasingly suspicious as events unfold.
    *   **The Conspiracy** (Minor—being exposed)
        *   **Goals:** To keep historical crimes buried and protect powerful families from consequences.
        *   **Hierarchy:** Wealthy families, corrupt officials, connected through the bank's secret services.
        *   **Public Agenda:** We are respectable pillars of society.
        *   **Secret Agenda:** We used the bank to hide evidence of murders, theft, and corruption decades ago.
        *   **Assets:** Wealth, influence, legal protection, safe deposit boxes full of secrets.
        *   **Relationships:** Unaware the heist targets them specifically; some may be hostages without knowing why.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **The Architect:** The mastermind whose perfect plan exposes conspiracy through apparent failure.
    *   **Detective Sarah Kane:** The negotiator who slowly realizes nothing is as it seems.
    *   **Arthur Cassian:** The banker-hostage connected to the historical conspiracy.
    *   **Marcus "The Ghost" Vale:** The inside man who witnessed the original crime as a child.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Crew Member with Limited Knowledge"
    *   "Hostage with Secrets"
    *   "SWAT Tactical Officer"
    *   "Bank Employee"
    *   "Conspiracy Family Member"
    *   "Negotiation Specialist"
    *   "Evidence Carrier (unknowing)"
    *   "Corrupt Official"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Sterling Bank:** The setting for the entire operation.
        *   **Key Landmarks:** The Vault, Safe Deposit Room, Lobby (hostage zone), Executive Offices, Hidden Archives.
        *   **Primary Inhabitants:** Crew (in control), hostages (varying importance), law enforcement (outside).
        *   **Available Goods & Services:** Money (misdirection), safe deposit boxes (real objective), evidence (hidden).
        *   **Potential Random Encounters (x5):** Hostage medical emergency, evidence discovery, negotiation breakthrough, internal crew doubt, hidden passage discovery.
        *   **Embedded Plot Hooks & Rumors (x3):** "The bank was built to hide secrets, not protect money." "Safe deposit boxes contain evidence of unsolved murders." "The Architect has been planning this for decades."
        *   **Sensory Details:** Sight (Professional bank interior, hostages seated orderly, masked crew), Sound (Tense silence, negotiation radios, safe mechanisms), Smell (Fear-sweat, bank perfume, old documents).
    *   **The Negotiation Zone:** Outside the bank.
        *   **Key Landmarks:** Police Command Center, Sniper Positions, Perimeter Barriers, Media Area.
        *   **Primary Inhabitants:** Law enforcement, negotiators, SWAT teams, media.
        *   **Available Goods & Services:** Tactical response, negotiation expertise, surveillance capabilities.
        *   **Potential Random Encounters (x5):** Media interference, political pressure, tactical disagreement, breakthrough in understanding, conspiracy member in crowd.
        *   **Embedded Plot Hooks & Rumors (x3):** "This feels staged, like they wanted to be trapped." "The demands don't make sense for a bank robbery." "Someone inside is controlling the narrative."
        *   **Sensory Details:** Sight (Police vehicles, crowds, media cameras, bank exterior), Sound (Radios, crowd noise, helicopter), Smell (Coffee, exhaust, tension).
    *   **The Safe Deposit Room:** Where the real objective lies.
        *   **Key Landmarks:** Thousands of boxes, Access terminal, Hidden archive entrance, Evidence boxes (specific).
        *   **Primary Inhabitants:** Crew members accessing specific boxes.
        *   **Available Goods & Services:** The secrets of decades, evidence of conspiracy, truth.
        *   **Potential Random Encounters (x5):** Discovery of crucial evidence, booby-trapped box, historical document revelation, photograph from the original crime, witness statement.
        *   **Embedded Plot Hooks & Rumors (x3):** "Box 392 contains proof of murder." "The founding families used these boxes as insurance." "Some boxes have been sealed for fifty years."
        *   **Sensory Details:** Sight (Rows of identical boxes, one open revealing secrets), Sound (Lock mechanisms, paper rustling, breathing), Smell (Old paper, metal, secrets).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The crew maintains perfect control of the hostage situation.
    *   **THEN:** They have time to execute the real plan. Generate evidence gathering and psychological manipulation scenarios.
    *   **IF:** Detective Kane realizes the robbery is misdirection.
    *   **THEN:** She changes tactics and gets closer to the truth. Generate intellectual confrontations and respect between adversaries.
    *   **IF:** A hostage is revealed to be connected to the conspiracy.
    *   **THEN:** Their role in the plan becomes clear. Generate revelations about historical crimes and current justice.
    *   **IF:** Law enforcement prepares to assault.
    *   **THEN:** The crew must accelerate the real plan. Generate desperate final evidence gathering and strategic surrenders.
    *   **IF:** The perfect crime is revealed.
    *   **THEN:** All previous events are recontextualized as genius planning. Generate satisfying explanations of layered deception.
    *   **IF:** The Architect walks away clean.
    *   **THEN:** Justice is served against the conspiracy while the perfect crime goes unpunished. Generate bittersweet endings where truth matters more than arrests.
