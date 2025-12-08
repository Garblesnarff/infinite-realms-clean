### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Last Score: Professional to the End**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The players are elite professional criminals at the top of their game, planning one last major score before retirement—robbing the kingdom's central treasury during a high-security transfer. Pursuing them is an equally professional detective who respects their expertise even as he hunts them relentlessly, creating a deadly game of cat and mouse between professionals who understand each other too well. As the heist approaches, personal complications threaten to break the crew's ironclad discipline: forbidden romances, family obligations, and the ghosts of past jobs. The campaign explores whether true professionals can walk away from the life, and what price they pay when discipline breaks down in the face of human weakness.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the history of professional crime in the city and the unwritten codes that govern criminal expertise.
    *   Write about Marcus "Stone" Caldwell's legendary career and the jobs that made him a respected name in the underworld.
    *   Describe the kingdom's Central Treasury and its evolution from vulnerable to nearly impregnable.
    *   Explain Detective Branwell's career and the personal costs of his obsessive professionalism.
    *   Detail famous heists that were undone by personal complications rather than professional failures.
    *   Write about the "Thirty-Second Rule" and its origins in a botched job that killed half a crew.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Professional Crews** (Major)
        *   **Goals:** To execute high-value heists with precision, retire wealthy, and maintain reputations as true professionals.
        *   **Hierarchy:** Meritocratic leadership based on expertise and successful operations.
        *   **Public Agenda:** We do not exist.
        *   **Secret Agenda:** To pull off one last impossible score and disappear into legitimate life.
        *   **Assets:** Expert skills, professional networks, disciplined operations, ironclad protocols.
        *   **Relationships:** Respectful distance from other crews; antagonistic toward law enforcement; contemptuous of amateur criminals.
    *   **Major Crimes Division** (Major)
        *   **Goals:** To apprehend professional criminals through equally professional investigation and pursuit.
        *   **Hierarchy:** Elite unit led by experienced detectives with extensive resources.
        *   **Public Agenda:** We protect the kingdom from organized crime through superior investigative methods.
        *   **Secret Agenda:** To prove that professional law enforcement can outsmart professional criminals.
        *   **Assets:** Investigation resources, tactical response teams, surveillance capabilities, legal authority.
        *   **Relationships:** Antagonistic toward professional criminals but with grudging respect; competitive with other law enforcement.
    *   **The Civilian World** (Minor)
        *   **Goals:** To live normal lives unaware of the criminal and law enforcement games being played around them.
        *   **Hierarchy:** Regular social structures—families, businesses, communities.
        *   **Public Agenda:** We go about our lives.
        *   **Secret Agenda:** None—they represent what criminals might want and can never fully have.
        *   **Assets:** Normal life, relationships, legitimacy, stability.
        *   **Relationships:** Unaware of the professionals operating around them; sometimes caught in crossfire; represent temptation for criminals wanting out.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Detective Vincent Branwell:** The obsessive hunter with professional respect for his prey.
    *   **Marcus "Stone" Caldwell:** The crew leader torn between professional discipline and human desire.
    *   **Elena Voss:** The civilian connection representing life beyond crime.
    *   **Silas "Numbers" Kane:** The crew member whose personal vulnerabilities create betrayal potential.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Professional Crew Member"
    *   "Tactical Response Officer"
    *   "Civilian Bystander"
    *   "Treasury Security"
    *   "Fence/Criminal Contact"
    *   "Family Member of Crew"
    *   "Surveillance Specialist"
    *   "Conflicted Criminal"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Crew's Safehouse:** Professional criminal headquarters.
        *   **Key Landmarks:** Planning Room, Equipment Storage, Escape Routes, Living Quarters (austere).
        *   **Primary Inhabitants:** The crew during planning and preparation.
        *   **Available Goods & Services:** Secure planning space, professional equipment, strategic isolation.
        *   **Potential Random Encounters (x5):** Crew disagreement over protocol, personal phone call threatening security, equipment malfunction, surveillance detection, surprise inspection by leader.
        *   **Embedded Plot Hooks & Rumors (x3):** "The safehouse has never been compromised in ten years." "Professionals never bring personal issues here." "The escape routes have been tested dozens of times."
        *   **Sensory Details:** Sight (Clean, organized, tactical maps, professional equipment), Sound (Quiet concentration, equipment checks, strategic discussion), Smell (Coffee, gun oil, paper).
    *   **The Coffee Shop:** Neutral ground for the famous meeting.
        *   **Key Landmarks:** Corner Booth, Large Windows, Busy Public Space.
        *   **Primary Inhabitants:** Civilians, occasionally hosting professionals on opposite sides.
        *   **Available Goods & Services:** Coffee, neutral territory, civilian cover.
        *   **Potential Random Encounters (x5):** Regular customers, surveillance from outside, tense conversation between enemies, personal revelation, mutual understanding moment.
        *   **Embedded Plot Hooks & Rumors (x3):** "Criminals and cops sometimes meet here." "There's an unspoken rule—no violence in this place." "More deals are made here than in courtrooms."
        *   **Sensory Details:** Sight (Normal cafe, city views, civilians unaware), Sound (Espresso machines, conversation, city traffic), Smell (Fresh coffee, pastries, normalcy).
    *   **The Treasury Transport Route:** The heist target.
        *   **Key Landmarks:** Multiple city intersections, security checkpoints, civilian areas, escape routes.
        *   **Primary Inhabitants:** Treasury security, drivers, civilian traffic, law enforcement presence.
        *   **Available Goods & Services:** None—this is a combat and heist zone.
        *   **Potential Random Encounters (x5):** Unexpected security patrol, civilian interference, traffic complication, law enforcement checkpoint, surveillance detection.
        *   **Embedded Plot Hooks & Rumors (x3):** "The route changes randomly for security." "The transport has never been successfully robbed." "Law enforcement always has aerial support."
        *   **Sensory Details:** Sight (Urban streets, armored transport, security presence), Sound (Traffic, radios, alert signals), Smell (Exhaust, asphalt, tension).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** A crew member breaks professional protocol for personal reasons.
    *   **THEN:** Security is compromised and law enforcement gains advantages. Generate scenarios where human weakness creates tactical vulnerabilities.
    *   **IF:** The crew maintains perfect professional discipline.
    *   **THEN:** The heist has maximum chance of success but personal costs mount. Generate personal relationship failures and emotional consequences.
    *   **IF:** Detective Branwell offers a deal to crew members.
    *   **THEN:** Trust within the crew fractures as members consider their options. Generate paranoia and internal conflict scenarios.
    *   **IF:** The crew and detective have their respectful confrontation.
    *   **THEN:** Both sides gain insight into each other's plans and psychology. Generate psychological warfare and tactical adjustments.
    *   **IF:** The crew chooses human connection over professional escape.
    *   **THEN:** Some are captured or killed but achieve meaningful human moments. Generate tragic but emotionally resonant outcomes.
    *   **IF:** The crew follows the Thirty-Second Rule perfectly.
    *   **THEN:** They survive but must live with abandoning people who mattered. Generate guilt and empty victory scenarios.
