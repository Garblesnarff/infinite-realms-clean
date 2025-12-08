### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Emerald Abyss**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The party's expedition into the uncharted Emerald Abyss—a vast, hostile rainforest—goes disastrously wrong when their guide is killed by a jaguar and half the team vanishes in a storm. Stranded deep in the jungle with minimal supplies, they must master realistic survival techniques (water purification, wound treatment, nutrition management) while their mental health deteriorates from isolation, parasites, and the constant threat of predators. An indigenous tribe watches from the shadows, and the party must decide whether to seek their help or fear them. The only way out is to reach a research station deep in the jungle, but the Abyss itself seems to resist their escape, and visions begin to plague the weak-minded.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the history of the Yawanawa tribe: how they have lived in harmony with the Abyss for thousands of years.
    *   Write the legend of the Lost City: an ancient civilization that tried to dominate the jungle with arcane magic and was consumed by it.
    *   Describe the Crystalline Growth: a strange, fungal-magical hybrid found in the Lost City that induces hallucinations and madness.
    *   Explain the fate of previous expeditions into the Abyss: most vanished, a few members returned mad, and none found what they sought.
    *   Detail the Yawanawa's spiritual beliefs: they see the jungle as a living entity, and the Jaguar Spirit as its guardian and judge.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Yawanawa Tribe** (Major)
        *   **Goals:** To protect the jungle, maintain their way of life, and avoid the curse of the Lost City.
        *   **Hierarchy:** Led by a council of elders, with the Shaman (Aiyanna) holding spiritual authority.
        *   **Public Agenda:** We will help those who respect the jungle. We will drive out those who seek to exploit it.
        *   **Secret Agenda:** They know the Lost City's location but hide it to prevent outsiders from awakening its curse.
        *   **Assets:** Deep knowledge of the jungle, survival skills, spiritual magic, the Jaguar Spirit's favor.
        *   **Relationships:** Cautiously neutral to the party; hostile to the Bloodwood Warriors.
    *   **The Bloodwood Warriors** (Minor)
        *   **Goals:** To expand their territory, enslave other tribes, and loot the Lost City.
        *   **Hierarchy:** Warlord-led, with shamans who use dark, blood magic.
        *   **Public Agenda:** The jungle belongs to the strong. We will take what we want.
        *   **Secret Agenda:** They seek the Crystalline Growth to create a hallucinogenic weapon to control their enemies.
        *   **Assets:** Superior numbers, brutal tactics, knowledge of poison and traps.
        *   **Relationships:** Hostile to the Yawanawa and all outsiders.
    *   **The Jungle Itself** (Major — Environmental Faction)
        *   **Goals:** None. It is an ecosystem, not a sentient faction, but it acts as a constant enemy.
        *   **Hierarchy:** Food chain dynamics. Predators, prey, and environmental hazards.
        *   **Public Agenda:** None. It simply exists.
        *   **Secret Agenda:** The jungle seems to resist outsiders, as if it is aware and protective of its secrets.
        *   **Assets:** Infinite predators, diseases, poisons, and hazards.
        *   **Relationships:** Hostile to all who do not understand it; neutral to the Yawanawa who live in harmony.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Aiyanna (The Shaman):** The wise spiritual leader of the Yawanawa, testing the party's intentions.
    *   **Kael (The Madman):** A survivor of a previous expedition, driven insane by the Lost City.
    *   **The Jaguar Spirit:** A legendary predator and the jungle's guardian, both real and symbolic.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Yawanawa Hunter"
    *   "Bloodwood Warrior"
    *   "Infected Survivor (Crystalline Growth victim)"
    *   "Deadly Jungle Predator (Jaguar, Anaconda, Caiman)"
    *   "Helpful Jungle Animal (Parrot with warnings, Monkey with food)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Crash Site:** The scattered remains of the expedition, overgrown and looted by scavengers.
        *   **Key Landmarks:** The wrecked supplies, the guide's grave, scattered equipment.
        *   **Primary Inhabitants:** Scavengers (vultures, insects), possibly a jaguar attracted by the smell.
        *   **Available Goods & Services:** Minimal salvage (rope, a machete, a medical kit).
        *   **Potential Random Encounters (x5):** A jaguar investigates, a Yawanawa scout watches, a Bloodwood patrol passes nearby, a snake is hiding in the wreckage, a hallucinatory vision (low Sanity).
        *   **Embedded Plot Hooks & Rumors (x3):** "The guide's journal mentions the research station to the west." "Footprints suggest they are being watched." "Strange totems are found nearby."
        *   **Sensory Details:** Sight (Wrecked gear, dense vines, the guide's body), Sound (Buzzing insects, distant bird calls, rustling leaves), Smell (Decay, wet earth, jungle rot).
    *   **The Yawanawa Village:** A hidden settlement of huts built in the jungle canopy.
        *   **Key Landmarks:** The Shaman's Hut, the Central Fire, the Trial Grounds.
        *   **Primary Inhabitants:** Yawanawa tribe members, children, elders.
        *   **Available Goods & Services:** Healing, food, water, guidance (if the party earns their trust).
        *   **Potential Random Encounters (x5):** A trial is offered, a feast is held, a Bloodwood attack, a spiritual ritual, a story about the Lost City.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Shaman knows the way to the research station." "They fear the Lost City's curse." "The Jaguar Spirit tests all who seek to leave."
        *   **Sensory Details:** Sight (Huts woven from vines, body-painted tribe members, the warm fire), Sound (Drumming, chanting, laughter of children), Smell (Smoke, roasting meat, herbal medicines).
    *   **The Lost City:** Ancient stone ruins swallowed by vines, filled with traps and the Crystalline Growth.
        *   **Key Landmarks:** The Central Temple, the Crystalline Chamber, the Treasure Vault.
        *   **Primary Inhabitants:** The Crystalline Growth (causes hallucinations), infected creatures, Kael (the madman).
        *   **Available Goods & Services:** Treasure, arcane knowledge, the Crystalline Growth (dangerous).
        *   **Potential Random Encounters (x5):** A hallucination (low Sanity), Kael attacks, a trap triggers, an infected creature, a vision of the city's fall.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Crystalline Growth is the source of the curse." "Destroying it may free Kael's mind." "The treasure is cursed."
        *   **Sensory Details:** Sight (Ancient stone covered in vines, glowing crystals, eerie shadows), Sound (Dripping water, distant whispers, the rustle of wings), Smell (Mold, decay, something sweet and wrong).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The party's collective Sanity drops below 50.
    *   **THEN:** Hallucinations become more frequent. Party members may see threats that aren't there, distrust each other, or refuse to act. Generate random Sanity challenges.
    *   **IF:** The party earns the trust of the Yawanawa by completing their trials.
    *   **THEN:** Aiyanna provides a guide to the research station, teaches jungle survival techniques, and warns them about the Jaguar Spirit's final test.
    *   **IF:** The party enters the Lost City without proper preparation (antidotes, high Sanity).
    *   **THEN:** The Crystalline Growth's influence is overwhelming. Generate a scenario where the party must resist hallucinations, possibly turning on each other.
    *   **IF:** The party destroys the Crystalline Growth.
    *   **THEN:** Kael's madness begins to fade, and he can guide them to the research station. The Yawanawa are grateful, seeing it as breaking the city's curse.
    *   **IF:** The party successfully repairs the radio and calls for rescue.
    *   **THEN:** They must survive several days defending the research station from predators and the Bloodwood Warriors (who want to capture them). Rescue arrives, ending the campaign.
