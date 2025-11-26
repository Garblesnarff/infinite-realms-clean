### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Five Serpents Revenge**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The party leader, once part of the elite Five Serpents assassin squad, was betrayed and left for dead on their wedding day. Years later, they awaken from a coma with a revenge list: hunt down each former teammate and the Dragon Emperor who ordered it. Each target reveals more about the betrayal's true nature, forcing the party to question whether revenge or forgiveness is the answer.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the Dragon Emperor's empire and its use of elite assassin squads to maintain power.
    *   Write the history of the Five Serpents squad—their training, legendary missions, and bond.
    *   Describe the wedding day attack—what happened, who survived, who escaped.
    *   Explain the martial arts traditions of this world—different fighting styles and their philosophies.
    *   Detail the party leader's fiancé—who they were and why their death/marriage was politically significant.
    *   Describe the years between the attack and the awakening—how the world changed, how the Serpents' lives evolved.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Five Serpents (Former Squad)** (Major)
        *   **Goals:** (Varies) Some seek redemption, others have moved on, others still serve the Emperor.
        *   **Hierarchy:** Was a unit of equals led by Diamondback; now scattered individuals.
        *   **Public Agenda:** Each has built new lives and identities.
        *   **Secret Agenda:** All carry guilt about the betrayal; some want forgiveness, others want to forget.
        *   **Assets:** Elite martial arts skills, connections from their former lives, knowledge of the party leader.
        *   **Relationships:** Complex—former family now enemies, but not without sympathy; each views the party leader differently.
    *   **The Dragon Emperor's Court** (Major)
        *   **Goals:** Maintain power, eliminate threats, test and recruit the worthy.
        *   **Hierarchy:** The Dragon Emperor at the top, elite guard, administrators, the Serpent squads.
        *   **Public Agenda:** Rule justly and protect the empire.
        *   **Secret Agenda:** The Emperor manipulates from shadows, sees people as tools, believes in harsh mercy.
        *   **Assets:** Armies, assassins, political power, vast intelligence network.
        *   **Relationships:** Former employer of the party leader; ordered the attack; views the revenge quest as either threat or test.
    *   **Monasteries & Dojos** (Minor)
        *   **Goals:** Train warriors, preserve martial arts traditions, maintain neutrality.
        *   **Hierarchy:** Masters and students, traditional master-disciple relationships.
        *   **Public Agenda:** Teach discipline and combat arts.
        *   **Secret Agenda:** Some monasteries are actually Emperor recruitment centers; others shelter fugitives.
        *   **Assets:** Training grounds, ancient techniques, neutral ground status.
        *   **Relationships:** Where the Serpents trained; potential allies or obstacles; some sympathize with party's quest.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Diamondback:** The former lover who pulled the trigger, now seeking redemption.
    *   **The Dragon Emperor:** The calculating ruler who ordered the attack.
    *   **Copperhead:** Poison specialist trying to forget her past.
    *   **Cottonmouth:** Honorable warrior serving a new master.
    *   **Sidewinder:** Clever crime lord who escaped into a new life.
    *   **Rattlesnake:** Enforcer who secretly loved the party leader.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Elite Guard (Skilled warriors protecting the Serpents)"
    *   "Dojo Student (Practitioners who idolize or fear the legends)"
    *   "Crime Underling (Working for Sidewinder)"
    *   "Monastery Master (Wise teacher offering guidance or tests)"
    *   "Emperor's Agent (Spy or assassin still loyal to the throne)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **House of Blue Steel:** Prestigious dojo where Cottonmouth works, site of iconic army battle.
        *   **Key Landmarks:** The main training hall, the master's chamber, the courtyard, the weapon racks.
        *   **Primary Inhabitants:** Cottonmouth, elite students, the dojo master, guards.
        *   **Available Goods & Services:** Training (if diplomatic approach), information about other Serpents.
        *   **Potential Random Encounters (x5):** Students practicing forms, demonstration of technique, challenge from arrogant fighter, tea ceremony before combat, master offering wisdom.
        *   **Embedded Plot Hooks & Rumors (x3):** "Cottonmouth never speaks of her past." "The master knows secrets of the Dragon Emperor." "This dojo trains the Emperor's elite guard."
        *   **Sensory Details:** Sight (Polished wooden floors, weapons on walls, paper lanterns), Sound (Students training, wooden swords clacking, breath control), Smell (Incense, wood polish, sweat).
    *   **Temple Mountain:** Remote monastery where Diamondback seeks redemption.
        *   **Key Landmarks:** The thousand steps, the meditation hall, the master's chamber, the cherry blossom garden.
        *   **Primary Inhabitants:** Diamondback, monks seeking peace, the enlightened master.
        *   **Available Goods & Services:** Sanctuary, spiritual guidance, advanced training, healing.
        *   **Potential Random Encounters (x5):** Monks in meditation, test of spiritual worthiness, encounter with nature spirits, previous seekers who never left, vision quest.
        *   **Embedded Plot Hooks & Rumors (x3):** "Diamondback has been here for years doing penance." "The monastery master once defeated the Dragon Emperor in single combat." "There's a secret technique only taught to those who achieve enlightenment."
        *   **Sensory Details:** Sight (Mountain mists, cherry blossoms, simple wooden structures), Sound (Wind chimes, distant gongs, rustling leaves), Smell (Mountain air, cherry blossoms, incense).
    *   **The Dragon's Throne:** The Emperor's palace, where truth and lies intertwine.
        *   **Key Landmarks:** The throne room, the garden of reflection, the hall of ancestors, the execution ground.
        *   **Primary Inhabitants:** The Dragon Emperor, elite guard, courtiers, surviving Serpents.
        *   **Available Goods & Services:** Audience with the Emperor (if worthy), ultimate answers.
        *   **Potential Random Encounters (x5):** Imperial guard inspection, court intrigue, summons to audience, encounter with former ally, trial by combat.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Emperor hasn't left the palace in years." "He knows everything that happens in his empire." "No one has ever successfully assassinated an Emperor."
        *   **Sensory Details:** Sight (Opulent gold and red, jade decorations, perfect symmetry), Sound (Echoing footsteps, whispered court gossip, formal announcements), Smell (Rare incense, aged wood, power).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The party shows mercy to a defeated Serpent.
    *   **THEN:** That Serpent may provide aid later or speak on the party's behalf. Generate specific assistance scenarios.
    *   **IF:** The party kills all Serpents without mercy.
    *   **THEN:** The Dragon Emperor views them as monsters, not heroes. Generate a darker finale where they've become what they hated.
    *   **IF:** The party learns the truth about their fiancé before confronting Diamondback.
    *   **THEN:** The Diamondback confrontation becomes more about understanding than revenge. Generate dialogue options for reconciliation.
    *   **IF:** The party trains at Temple Mountain before the final confrontation.
    *   **THEN:** They learn an ultimate technique. Generate a special ability available only through this path.
    *   **IF:** Rattlesnake survives and reveals their love.
    *   **THEN:** They offer to help against the Emperor or take Diamondback's place in the final duel. Generate this dramatic alliance.
    *   **IF:** In the finale, the party chooses forgiveness over revenge.
    *   **THEN:** Generate an epilogue where the Five Serpents reunite and work to reform the Emperor's methods from within, or leave service together to build something better.
