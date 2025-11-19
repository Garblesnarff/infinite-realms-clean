### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Endless Loop**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The players are transported to the Kingdom of Lugnica, a fantasy realm of magic and monsters. They're granted "Return by Death" - when they die, time resets to a checkpoint and only they remember. Using knowledge from countless failed loops, they must navigate assassination plots, political intrigue, and supernatural threats while protecting those they care about. Each death teaches them something but inflicts psychological trauma. They must unravel why they were brought here and whether their curse is a gift or damnation.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the legend of the Witch of Envy, Satella, who nearly destroyed the world 400 years ago.
    *   Write the history of the Kingdom of Lugnica and why it currently has no heir to the throne.
    *   Describe the Royal Selection process and the five candidates competing for the throne.
    *   Explain the spirit magic system and the pacts between humans and spirits.
    *   Detail the Witch Cult, their goals, and the Archbishops who each embody a deadly sin.
    *   Describe the Great Three - the Sword Saint, the Divine Dragon, and the Sage - who protect Lugnica.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **Emilia Camp** (Major - Allied)
        *   **Goals:** Win the royal selection, prove half-elves deserve respect, create a kind kingdom.
        *   **Hierarchy:** Emilia as candidate, Roswaal as patron, Puck as protector, Ram and Rem as servants/warriors.
        *   **Public Agenda:** Present Emilia as the rightful heir and capable ruler.
        *   **Secret Agenda:** Roswaal manipulates events to match his Gospel's prophecy; will sacrifice anyone for his goal.
        *   **Assets:** Roswaal's vast magical power and wealth, Puck's apocalyptic potential, talented servants.
        *   **Relationships:** Most hated camp due to Emilia resembling the Witch; allied with mercenaries; relies on players.
    *   **The Witch Cult** (Major - Hostile)
        *   **Goals:** Resurrect the Witch of Envy, spread madness and death in her name.
        *   **Hierarchy:** Archbishops lead (each represents a sin), finger cultists beneath them.
        *   **Public Agenda:** They have no legitimate face; pure terrorist organization.
        *   **Secret Agenda:** Some archbishops have personal goals; possession by Witch Factors drives them mad.
        *   **Assets:** Reality-warping Authority powers, fanatical followers, immortality through possession.
        *   **Relationships:** Universally despised; specifically target anyone connected to Satella or the players.
    *   **The Royal Selection Council** (Major - Neutral/Political)
        *   **Goals:** Choose the best candidate to rule, maintain kingdom stability.
        *   **Hierarchy:** Wise Men of the Council advise; five camps compete (Emilia, Priscilla, Crusch, Anastasia, Felt).
        *   **Public Agenda:** Fair selection of the next monarch.
        *   **Secret Agenda:** Each camp has hidden motivations and backers; political maneuvering is constant.
        *   **Assets:** Political legitimacy, knight orders, vast resources across all camps.
        *   **Relationships:** Complex web of alliances and rivalries; all suspicious of Emilia camp.
    *   **The Oni Village (Destroyed)** (Minor - Background)
        *   **Goals:** [Were] Peaceful coexistence, protecting their people.
        *   **Hierarchy:** Village elders led; Rem and Ram were powerful twins.
        *   **Public Agenda:** None - the village was destroyed.
        *   **Secret Agenda:** The truth of what happened haunts Rem and Ram.
        *   **Assets:** Powerful warrior tradition, magical horns granting immense power.
        *   **Relationships:** Destroyed by the Witch Cult; survivors serve Roswaal; deep trauma remains.
    *   **The Astrea House** (Minor - Neutral)
        *   **Goals:** Uphold justice, protect the innocent, maintain the Sword Saint bloodline.
        *   **Hierarchy:** The current Sword Saint leads; family of legendary warriors.
        *   **Public Agenda:** Serve as heroes and protectors of the kingdom.
        *   **Secret Agenda:** Burden of the Sword Saint title passes without consent; family conflicts remain.
        *   **Assets:** The Sword Saint - strongest warrior in the world; legendary sword that chooses its wielder.
        *   **Relationships:** Respected universally; one family member (Felt) is a royal candidate.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Emilia:** Half-elf royal candidate, kind but politically naive.
    *   **Rem:** Blue-haired oni maid, loyal warrior.
    *   **Ram:** Pink-haired oni maid, sharp-tongued and protective.
    *   **Roswaal L. Mathers:** Eccentric noble, manipulative patron.
    *   **Puck:** Spirit cat, protective and apocalyptic.
    *   **Beatrice:** Spirit librarian, lonely and tsundere.
    *   **Petelgeuse Romanée-Conti:** Insane Archbishop of Sloth.
    *   **The Witch of Envy (Satella):** Source of the players' power.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Fanatical Witch Cult Finger"
    *   "Other Royal Selection Candidate"
    *   "Knight in Service to a Camp"
    *   "Village Resident to be Protected"
    *   "Merchant with Critical Information"
    *   "Spirit with Specific Domain"
    *   "Assassin Targeting a Candidate"
    *   "Traumatized Survivor of Witch Cult Attack"
    *   "Noble with Political Agenda"
    *   "Mercenary for Hire"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Checkpoint (Fruit Stall):** Where time always resets.
        *   **Key Landmarks:** Simple fruit vendor stall, busy market square around it, view of castle district.
        *   **Primary Inhabitants:** Fruit vendor (never remembers), various merchants and shoppers.
        *   **Available Goods & Services:** Fruit, general market goods, crowds for anonymity.
        *   **Potential Random Encounters (x5):** First meeting with Emilia (always plays same), pickpocket attempt, suspicious figure watching players, merchant with rumor, street performer.
        *   **Embedded Plot Hooks & Rumors (x3):** "A half-elf was seen in the noble quarter." "The slums have been dangerous lately." "Strange deaths have been occurring."
        *   **Sensory Details:** Sight (Colorful fruit, busy crowds, distant castle), Sound (Market chatter, vendor calls, city bells), Smell (Fresh fruit, street food, urban mix).
    *   **Roswaal's Mansion:** Estate where early loops occur.
        *   **Key Landmarks:** Guest wing, servant quarters, Forbidden Library entrance, master's chambers, grounds and gardens.
        *   **Primary Inhabitants:** Roswaal, Ram, Rem, Beatrice (in library), Emilia (guest), Puck, various servants.
        *   **Available Goods & Services:** Shelter, meals, access to knowledge (through Beatrice), magical training.
        *   **Potential Random Encounters (x5):** Maid performing duties, Puck playing, strange sounds at night, magical disturbance, visiting merchant or messenger.
        *   **Embedded Plot Hooks & Rumors (x3):** "The library can't be found unless it wants to be." "Something killed the previous guests." "Roswaal is rarely home at night."
        *   **Sensory Details:** Sight (European manor luxury, portraits, magical lighting), Sound (Footsteps echoing, clock ticking, wind), Smell (Wood polish, cooking, faint magical ozone).
    *   **The Flügel Tree:** Sacred site in the forest.
        *   **Key Landmarks:** Enormous ancient tree, clearing around it, hidden Witch Cult symbols, graves of important figures.
        *   **Primary Inhabitants:** Spirits, occasionally Witch Cult members, wild animals.
        *   **Available Goods & Services:** Spiritual connection, sacred ground for rituals (good or evil).
        *   **Potential Random Encounters (x5):** Witch Cult ambush, spirit manifestation, grave of someone important, vision or memory, magical phenomenon.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Witch was sealed near here." "Cultists gather at the tree during new moons." "Spirits whisper secrets to those pure of heart."
        *   **Sensory Details:** Sight (Impossibly large tree, dappled light, ancient presence), Sound (Wind through leaves, whispers, unsettling silence), Smell (Earth, flowers, something faintly wrong).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** A player dies.
    *   **THEN:** All players reset to the last checkpoint. Physical world reverts; player memories and Trauma Points remain. Generate different NPC actions if players choose different approaches.
    *   **IF:** Players successfully prevent a major death.
    *   **THEN:** Checkpoint advances. That NPC becomes permanently saved and available as ally. Generate celebration/bonding scene.
    *   **IF:** Players attempt to tell an NPC about Return by Death.
    *   **THEN:** Witch's hand manifests, crushing player's heart. Immediate death and reset. Generate increased Trauma Points.
    *   **IF:** Players accumulate too many Trauma Points.
    *   **THEN:** Generate mental breakdown scene. Player character may temporarily lose control or make irrational decisions. Require Wisdom saves.
    *   **IF:** Players form deep bonds with specific NPCs through repeated loops.
    *   **THEN:** Those NPCs begin to sense something strange about the players. Generate trust-building opportunities. Unlock deeper character quests.
    *   **IF:** Players defeat an Archbishop.
    *   **THEN:** Checkpoint advances significantly. Generate Witch Factor absorption choice (gain power but risk madness). Other Archbishops become aware of players.
    *   **IF:** Players meet Satella in the dream castle.
    *   **THEN:** Generate revelation about the true nature of Return by Death. Offer cryptic guidance. Inflict Trauma Points but provide hope.
    *   **IF:** Players achieve the "perfect run" (everyone survives).
    *   **THEN:** Unlock true ending path. Generate final confrontation with the source of all conflicts. Offer choice to keep or reject Return by Death.
