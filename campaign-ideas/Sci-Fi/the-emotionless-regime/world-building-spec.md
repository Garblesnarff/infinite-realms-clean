### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Emotionless Regime**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** In the dystopian city-state of Equilibrium, all emotion is outlawed. Elite Clerics trained in Gun Kata enforce suppression, but when a party member accidentally experiences feeling, they discover what humanity has lost. Now secretly awakened, they must hide their emotions while working to overthrow the Father and the Tetragrammaton Council, liberating humanity from emotionless compliance.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the war that led to emotional suppression—what happened and how the Father rose to power.
    *   Write the history of Suppressant development and how it eliminates emotion at a neurological level.
    *   Describe Gun Kata—its principles, training, and why emotionless fighters were thought superior.
    *   Explain the Tetragrammaton Council's structure and how it maintains power through propaganda and suppression.
    *   Detail the Resistance—how it formed, how it preserves culture, and how members hide from the Clerics.
    *   Describe what happened to art, music, literature, and love in this world—all declared illegal sense offense.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Tetragrammaton** (Major)
        *   **Goals:** Maintain order through emotional suppression, prevent war through elimination of passion.
        *   **Hierarchy:** The Father (propaganda figure), the four Council members, Vice-Clerics, Clerics, citizens.
        *   **Public Agenda:** Protect humanity from destructive emotion that led to war.
        *   **Secret Agenda:** The Council maintains power through control; they've suppressed emotions to create docile, manageable citizens.
        *   **Assets:** Cleric army, surveillance state, Suppressant distribution, propaganda network, Gun Kata training facilities.
        *   **Relationships:** Absolute authority over citizens; hunting the Resistance; will eliminate awakened Clerics.
    *   **The Clerics (Party's Former Faction)** (Major)
        *   **Goals:** Enforce emotional suppression laws, eliminate sense offenders, maintain order.
        *   **Hierarchy:** DuPont leads, Vice-Clerics supervise, elite Clerics execute.
        *   **Public Agenda:** Protect society from dangerous emotion.
        *   **Secret Agenda:** Most are true believers; some secretly question; a few are awakening.
        *   **Assets:** Gun Kata mastery, authority to kill on sight, access to government resources.
        *   **Relationships:** Feared by citizens; hunting awakened former colleagues; some conflicted.
    *   **The Resistance (Nether)** (Major)
        *   **Goals:** Preserve human culture, awaken citizens, overthrow the regime.
        *   **Hierarchy:** Cell-based with Jurgen as symbolic leader; decentralized for security.
        *   **Public Agenda:** None—they're criminals from regime perspective.
        *   **Secret Agenda:** Stockpiling weapons and evidence for eventual revolution.
        *   **Assets:** Hidden safe houses, preserved art and literature, awakened citizens, knowledge of Suppressant's true nature.
        *   **Relationships:** Protect sense offenders; recruitment targets for awakening Clerics; hope for liberation.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Vice-Cleric Brandt:** Emotionless hunter investigating the party, perfect loyal enforcer.
    *   **Jurgen:** Passionate Resistance leader who's never taken Suppressant.
    *   **DuPont:** The Father figure, greatest Gun Kata master, true believer who's forgotten humanity.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Cleric (Fellow enforcement monks, potential allies or enemies)"
    *   "Suppressed Citizen (Emotionless, compliant, potentially awakening)"
    *   "Sense Offender (Awakened individual hunted by Clerics)"
    *   "Resistance Cell Member (Preserving culture in hiding)"
    *   "Peacekeeper (Military unit for emergency suppression)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The City of Equilibrium:** Clean, efficient, colorless dystopia.
        *   **Key Landmarks:** The central plaza (propaganda displays), Suppressant distribution centers, Cleric headquarters, execution grounds, residential blocks.
        *   **Primary Inhabitants:** Suppressed citizens, patrolling Clerics, Council propaganda displays.
        *   **Available Goods & Services:** Suppressant (mandated), basic needs, nothing aesthetic or emotional.
        *   **Potential Random Encounters (x5):** Suppressant distribution, sense offense arrest, propaganda broadcast, Cleric patrol, citizen behaving irregularly.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Father sees all." "Emotion caused the war." "Those who feel are dangerous."
        *   **Sensory Details:** Sight (Monochromatic, geometric, perfect order), Sound (Propaganda broadcasts, synchronized footsteps, artificial quiet), Smell (Antiseptic, sterile, absence of cooking or perfume).
    *   **The Nether (Resistance Underground):** Hidden spaces preserving human culture.
        *   **Key Landmarks:** The library (forbidden books), the gallery (hidden art), the concert hall (preserved music), safe houses.
        *   **Primary Inhabitants:** Awakened Resistance members, protected sense offenders, artists.
        *   **Available Goods & Services:** Cultural education, true history, emotional support, weapons for revolution.
        *   **Potential Random Encounters (x5):** First experience of music, viewing forbidden art, reading pre-war literature, meeting fully emotional humans, preparation for raids.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Father is a lie." "Emotion makes us human, not dangerous." "There's evidence in the Archive that proves everything."
        *   **Sensory Details:** Sight (COLOR—art, books, decoration, human touches), Sound (Music, laughter, crying, human voices), Smell (Cooking, incense, the scent of old books).
    *   **The Tetragrammaton Center:** Government fortress where the Council rules.
        *   **Key Landmarks:** The throne room, the Archive, Council chambers, DuPont's training facility, the fail-safe vault.
        *   **Primary Inhabitants:** The Council, DuPont, elite guards, Vice-Clerics.
        *   **Available Goods & Services:** Ultimate authority, truth about the regime, control systems.
        *   **Potential Random Encounters (x5):** Elite guard patrols, encounter with DuPont, discovery of Archive secrets, activation of Peacekeepers, confrontation with Council.
        *   **Embedded Plot Hooks & Rumors (x3):** "DuPont has never felt emotion." "The fail-safe will erase emotion permanently." "The Father never existed—it was always the Council."
        *   **Sensory Details:** Sight (Even more sterile than the city, perfect geometry), Sound (Echoing emptiness, mechanical precision), Smell (Nothing—perfectly filtered air).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** A party member misses a Suppressant dose.
    *   **THEN:** Generate their emotional awakening sequence. Initially overwhelming, gradually manageable. Must hide reactions from others.
    *   **IF:** The party awakens other Clerics.
    *   **THEN:** Create ally NPCs who are conflicted but committed. Generate their personal emotional journeys and specializations.
    *   **IF:** The party's cover is blown before they're ready.
    *   **THEN:** Generate immediate pursuit by Vice-Clerics. The party becomes fugitives, changing the campaign's structure.
    *   **IF:** The party broadcasts proof of the Father's lies.
    *   **THEN:** Generate city-wide reactions: some citizens awaken and rebel, others defend the regime more fiercely, chaos erupts.
    *   **IF:** The party defeats DuPont in Gun Kata without killing him.
    *   **THEN:** Generate his forced emotional awakening. Decades of suppressed feeling overwhelm him—he either breaks or becomes the party's greatest ally.
    *   **IF:** In the finale, the fail-safe is triggered and cannot be stopped.
    *   **THEN:** Generate a bittersweet ending where emotion is erased but the party's sacrifice inspires a legend that eventually leads to rediscovery of feeling.
