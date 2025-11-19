### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Arcane Illusion: Now You See Me**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The players are recruited into a mysterious crew of magical performers who pull off impossible heists disguised as spectacular public shows, using illusion magic and misdirection to steal from corrupt elites and redistribute wealth to the people. Led by an enigmatic benefactor known only as "The Eye," they perform increasingly audacious magical spectacles that are simultaneously entertainment and elaborate crimes, always staying one step ahead of investigators. As they delve deeper into The Eye's agenda, they discover that the heists are part of a larger plan to expose corruption and join an ancient order of magical Robin Hood figures. The campaign becomes a thrilling combination of stage magic, real sorcery, and social justice through spectacular theft.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the history of The Eye's ancient order—centuries of magical performers using their abilities for Robin Hood justice.
    *   Write about famous historical magical heists that became legends, inspiring the current crew.
    *   Describe the city's theater culture and how performance magic exists alongside real magical power.
    *   Explain how corrupt elites accumulated wealth through exploitation that the order seeks to redistribute.
    *   Detail the philosophy of using spectacular performance to achieve social justice through magical means.
    *   Write about the symbolic importance of playing cards, stage magic, and the Eye symbol to the order.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Eye's Order** (Major—secret)
        *   **Goals:** To use magical performance to redistribute wealth, expose corruption, and inspire belief in justice.
        *   **Hierarchy:** The Eye leads, with performing crews operating independently but coordinated.
        *   **Public Agenda:** We are legendary magical performers who may or may not exist.
        *   **Secret Agenda:** We are an ancient order dedicated to magical Robin Hood justice spanning centuries.
        *   **Assets:** Real magical power, performance skills, centuries of accumulated knowledge, public acclaim.
        *   **Relationships:** Unknown to most; antagonistic toward corrupt elites; beloved by the public as folk heroes.
    *   **The Corrupt Elite** (Major)
        *   **Goals:** To maintain wealth and power accumulated through exploitation and corruption.
        *   **Hierarchy:** Council members, wealthy merchants, corrupt officials operating as a loose coalition.
        *   **Public Agenda:** We are successful businesspeople and civic leaders.
        *   **Secret Agenda:** We've stolen from the people for years and will protect our wealth by any means.
        *   **Assets:** Vast wealth, political influence, security forces, legal protections.
        *   **Relationships:** Target of the Eye's order; antagonistic toward reformers; exploitative toward the public.
    *   **The Investigators** (Minor)
        *   **Goals:** To prove the magical heists are real crimes and apprehend the perpetrators.
        *   **Hierarchy:** Led by brilliant investigators with support from law enforcement.
        *   **Public Agenda:** We protect the law and pursue criminals regardless of public opinion.
        *   **Secret Agenda:** Some investigators secretly sympathize with the crew's cause despite their duty.
        *   **Assets:** Investigative skills, legal authority, evidence (eventually), determination.
        *   **Relationships:** Pursuing the crew; conflicted about the corruption being exposed; pressured by the elite to stop the performances.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **The Eye:** The mysterious leader recruiting the crew into the ancient order.
    *   **Investigator Thalia Vance:** The brilliant pursuer conflicted about the crew's heroism.
    *   **Councilor Marcus Greed:** The corrupt official who is the ultimate target.
    *   **Cassian "The Prestige" Noir:** The crew's charismatic lead performer.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Magical Performer"
    *   "Order Member"
    *   "Corrupt Official"
    *   "Amazed Audience Member"
    *   "Investigator Team"
    *   "Wealth Redistribution Recipient"
    *   "Theater Staff"
    *   "Security Force"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Grand Theater:** Performance venue and heist stage.
        *   **Key Landmarks:** Main Stage, Backstage Areas, Audience Seating (thousands), Hidden Magical Apparatus.
        *   **Primary Inhabitants:** Performers, crew, audiences, investigators (sometimes), theatrical staff.
        *   **Available Goods & Services:** Spectacular performances, magical entertainment, heist opportunities hidden in shows.
        *   **Potential Random Encounters (x5):** Audience member receiving redistributed wealth, investigator surveillance, magical effect goes spectacularly right, spontaneous crowd reaction, Eye communication.
        *   **Embedded Plot Hooks & Rumors (x3):** "The performances are real magic, not tricks." "Money appears in audience members' pockets." "The crew are modern Robin Hoods."
        *   **Sensory Details:** Sight (Stage lights, magical effects, amazed crowds, elaborate sets), Sound (Dramatic music, crowd applause and gasps, magical sounds), Smell (Theater atmosphere, anticipation, magic in the air).
    *   **The Eye's Sanctum:** Secret headquarters of the ancient order.
        *   **Key Landmarks:** Hall of Legendary Heists, Training Stages, Magical Archives, The Eye's Chamber.
        *   **Primary Inhabitants:** The Eye, order members, recruits being tested.
        *   **Available Goods & Services:** Order knowledge, magical training, historical context, membership.
        *   **Potential Random Encounters (x5):** Historical magical demonstration, meeting legendary order member, revelation about order's purpose, magical test, recruitment ceremony.
        *   **Embedded Plot Hooks & Rumors (x3):** "The order has existed for centuries." "Every legendary magical thief was a member." "The Eye symbol appears when justice is needed."
        *   **Sensory Details:** Sight (Ancient magical architecture, Eye symbols, historical artifacts), Sound (Echoes of legendary performances, magical resonance), Smell (Old magic, history, purpose).
    *   **The City Streets:** Where legends grow and wealth redistributes.
        *   **Key Landmarks:** Public Squares, Wealthy Districts, Poor Districts, Performance Venues.
        *   **Primary Inhabitants:** Citizens ranging from impoverished to elite, witnesses to magical justice.
        *   **Available Goods & Services:** Folk tales about the crew, redistribution recipient testimonials, investigative leads.
        *   **Potential Random Encounters (x5):** Someone sharing wealth redistribution story, investigator interviewing witnesses, spontaneous performance appreciation, corrupt elite complaining, magical effect witnessed.
        *   **Embedded Plot Hooks & Rumors (x3):** "They steal from the corrupt and give to victims." "Magic is real and it's on our side." "The crew will expose the Council's corruption."
        *   **Sensory Details:** Sight (Contrasts between wealthy and poor districts, visible redistribution effects), Sound (Street buzz about performances, grateful testimonials), Smell (City life, hope returning).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The crew performs a spectacular heist successfully.
    *   **THEN:** Public acclaim increases and wealth is redistributed. Generate folk hero growth and investigator pressure increase.
    *   **IF:** The investigator gets closer to proving the crimes.
    *   **THEN:** The crew must be more careful but stakes increase. Generate cat-and-mouse escalation and moral complexity scenarios.
    *   **IF:** The crew exposes specific corruption through a heist.
    *   **THEN:** That corrupt official faces consequences while others become more dangerous. Generate ripple effects through the elite.
    *   **IF:** The Eye reveals themselves and the order's purpose.
    *   **THEN:** The crew must decide whether to join permanently. Generate choice scenarios and revelation of deeper purpose.
    *   **IF:** The crew pulls off the grand finale heist.
    *   **THEN:** Massive corruption is exposed and they become legends. Generate spectacular success and legendary status scenarios.
    *   **IF:** The crew chooses to join The Eye's order.
    *   **THEN:** They dedicate their lives to magical Robin Hood justice. Generate membership ceremonies and new missions hinted at.
