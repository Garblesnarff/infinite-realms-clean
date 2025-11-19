### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**Fall of the Last Legion**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The players are members of the last loyal legion defending the remnants of a once-mighty empire as barbarian invasions overwhelm the borders, corruption rots the core, and a new religion rises to challenge the old gods. As commanders, soldiers, and specialists of this final legion, they must decide what to preserve from a dying civilization while the world transforms around them. The campaign explores whether they fight to restore the empire, protect refugees and knowledge as it falls, or help build something new from the ashes. This is a story of twilight—where heroes witness the end of an age and must choose what survives into the next.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the empire's thousand-year history from founding to current decline—its greatest victories, the gradual corruption, the first barbarian treaties.
    *   Write about the old imperial cult and pagan gods that unified the empire for centuries.
    *   Describe the new monotheistic religion spreading through the lower classes and its appeal during crisis.
    *   Explain the barbarian confederation's formation—dozens of tribes uniting under charismatic warlords for the first time.
    *   Detail the great legions of old and how the current force is a shadow of past glory.
    *   Write about famous last stands in imperial history and how they've become legends the current generation tries to emulate.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Last Loyal Legion** (Major—Player Faction)
        *   **Goals:** To defend the empire, protect citizens, preserve Roman civilization, and maintain honor in collapse.
        *   **Hierarchy:** Military structure with tribune commander, centurions, and specialized units.
        *   **Public Agenda:** We are the defenders of Rome and will hold the line no matter the cost.
        *   **Secret Agenda:** Many secretly know the empire is doomed and struggle with what to preserve versus what to let die.
        *   **Assets:** Military training, discipline, loyalty, traditional Roman virtue, combat experience.
        *   **Relationships:** Loyal to the ideal of Rome but increasingly disillusioned with its reality; protective of citizens; respectful enemies with honorable barbarians.
    *   **The Barbarian Confederation** (Major)
        *   **Goals:** To carve kingdoms from Roman territory, gain land for growing populations, and claim the empire's wealth.
        *   **Hierarchy:** Charismatic warlords leading tribal armies with loose confederation structure.
        *   **Public Agenda:** We take what Rome can no longer hold.
        *   **Secret Agenda:** Many barbarian leaders genuinely admire Roman civilization and want to inherit it, not just destroy it.
        *   **Assets:** Numbers, tactical innovation, desperation, vitality, adaptability.
        *   **Relationships:** Enemies of the empire but increasingly integrated through settlement; some seek alliance and adoption of Roman ways.
    *   **The New Church** (Major)
        *   **Goals:** To spread the new faith, preserve knowledge and culture, and offer hope during collapse.
        *   **Hierarchy:** Bishops, priests, and monastic orders with growing organization.
        *   **Public Agenda:** We offer salvation and spiritual hope to all people regardless of their origin.
        *   **Secret Agenda:** They see Rome's fall as divine judgment but also opportunity to spread their faith and preserve Roman knowledge under religious authority.
        *   **Assets:** Growing converts, organization, literacy, compelling message of hope, ability to bridge Roman and barbarian divide.
        *   **Relationships:** Increasingly popular among legionnaires and citizens; tolerated by some officials, persecuted by others; able to negotiate with barbarians.
    *   **The Corrupt Senate** (Minor)
        *   **Goals:** To preserve personal wealth and status regardless of the empire's fate.
        *   **Hierarchy:** Senators, corrupt officials, tax farmers profiteering from crisis.
        *   **Public Agenda:** We maintain the traditions and government of Rome.
        *   **Secret Agenda:** Many are already negotiating with barbarian kings to preserve their wealth in the new order.
        *   **Assets:** Remaining imperial wealth, legal authority, political connections, accumulated treasure.
        *   **Relationships:** Exploitative toward the legion and citizens; increasingly irrelevant as empire crumbles; willing to betray Rome for personal survival.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Tribune Maximus Severus:** The legion's honorable commander struggling with empire's decline.
    *   **Father Gregorius:** Charismatic priest of the new faith offering hope and preservation.
    *   **Alaric Bloodaxe:** Cultured barbarian warlord who respects what he conquers.
    *   **Senator Gaius Decadus:** Corrupt official embodying everything rotten about late Rome.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Veteran Legionnaire"
    *   "Barbarian Warrior"
    *   "Christian Convert"
    *   "Pagan Priest"
    *   "Refugee Family"
    *   "Corrupt Official"
    *   "Scholar Preserving Knowledge"
    *   "Barbarian Settler"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Northern Frontier:** Where invasions begin and empire weakness is revealed.
        *   **Key Landmarks:** Frontier Forts, Hadrian's Wall equivalent, Barbarian Camps, Abandoned Settlements.
        *   **Primary Inhabitants:** Legion border guards, barbarian scouts, refugees fleeing south.
        *   **Available Goods & Services:** Military supplies (dwindling), frontier intelligence, desperate alliances.
        *   **Potential Random Encounters (x5):** Barbarian scouting party, refugees with tales of invasion, deserters fleeing, abandoned Roman villa, evidence of Roman-barbarian trade.
        *   **Embedded Plot Hooks & Rumors (x3):** "The barbarians have new tactics and weapons." "Some Roman officers are negotiating private truces." "Entire legions have vanished from the northern border."
        *   **Sensory Details:** Sight (Vast forests beyond the wall, watchtowers with cold fires, barbarian campfires multiplying), Sound (Distant horns, nervous sentries, wind through abandoned forts), Smell (Pine, smoke, approaching army).
    *   **The Eternal City:** Capital under siege, filled with refugees and fading glory.
        *   **Key Landmarks:** The Forum, Imperial Palace, Great Temples, Aqueducts, City Walls, Senate House.
        *   **Primary Inhabitants:** Imperial court, senators, refugees, legion headquarters, religious factions.
        *   **Available Goods & Services:** Political intrigue, religious conversion, supplies (increasingly scarce), corruption opportunities.
        *   **Potential Random Encounters (x5):** Religious riot between pagans and Christians, corrupt official demanding bribes, refugee family begging for help, senators fleeing the city, barbarian embassy.
        *   **Embedded Plot Hooks & Rumors (x3):** "The emperor is already dead and they're hiding it." "Half the grain for the legions was sold to barbarians." "The new religion is spreading through the army."
        *   **Sensory Details:** Sight (Marble buildings cracking, refugee camps in forums, religious competition, signs of decay), Sound (Crowds, religious chanting, distant siege engines), Smell (Too many people, incense, decay).
    *   **The Sacred Archive:** Monastery-fortress where knowledge is preserved.
        *   **Key Landmarks:** Library Halls, Scriptorium, Fortified Walls, Hidden Vaults, Chapel.
        *   **Primary Inhabitants:** Scholars, monks, converted barbarians, defenders, scribes.
        *   **Available Goods & Services:** Knowledge preservation, religious instruction, sanctuary, cultural continuity.
        *   **Potential Random Encounters (x5):** Scholars debating what to preserve, barbarian wanting to learn, refugees seeking sanctuary, old pagan priest donating texts, scribes working desperately.
        *   **Embedded Plot Hooks & Rumors (x3):** "They're copying everything—Roman law, literature, engineering, everything." "Barbarian chiefs send their sons here to learn." "This will be all that survives when Rome falls."
        *   **Sensory Details:** Sight (Books being copied, mixed Roman and barbarian students, fortifications protecting knowledge), Sound (Scratching quills, religious prayers, lessons being taught), Smell (Parchment, ink, hope).
    *   **The Fields of Twilight:** Where the last battle determines the future.
        *   **Key Landmarks:** Ancient battlefield, Roman road, River crossing, Hilltop fort.
        *   **Primary Inhabitants:** The last loyal legion, barbarian confederation army, religious observers.
        *   **Available Goods & Services:** Final stand opportunities, negotiation with barbarians, legendary status.
        *   **Potential Random Encounters (x5):** Barbarian offering honorable terms, religious miracle, reinforcements arriving unexpectedly, enemy showing respect, historical echo.
        *   **Embedded Plot Hooks & Rumors (x3):** "This is where Rome ends or transforms." "The barbarian king wants Roman warriors to join his new kingdom." "What we fight for today shapes the next thousand years."
        *   **Sensory Details:** Sight (Two armies facing each other, twilight sky, mixed symbols), Sound (Battle preparations, prayers in multiple languages, historical weight), Smell (Coming storm, turned earth, significance).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The legion successfully defends a critical position.
    *   **THEN:** Temporary morale boost but Collapse Tracker continues. Generate pride and desperate hope scenarios.
    *   **IF:** Players expose corruption among imperial officials.
    *   **THEN:** Political instability increases but some resources are recovered. Generate political backlash and public support.
    *   **IF:** Players allow barbarians to settle peacefully in exchange for defense.
    *   **THEN:** Cultural transformation accelerates with mixed communities forming. Generate Roman-barbarian synthesis scenarios.
    *   **IF:** Players prioritize preserving knowledge over military victory.
    *   **THEN:** Legacy Points increase significantly but territory is lost faster. Generate long-term versus short-term trade-off consequences.
    *   **IF:** The new religion gains majority support in the legion.
    *   **THEN:** Religious transformation complete and old pagan faction marginalized. Generate unity under new faith versus loss of traditional identity.
    *   **IF:** Players negotiate with Alaric instead of fighting to the death.
    *   **THEN:** Barbarian kingdom inherits Roman civilization with players as honored advisors. Generate synthesis ending scenarios.
    *   **IF:** Players choose a heroic last stand refusing all compromise.
    *   **THEN:** Legendary status achieved but less practical legacy preserved. Generate tragic glory versus practical preservation outcomes.
