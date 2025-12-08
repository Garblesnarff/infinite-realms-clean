### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Blood Moon Siege**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The party awakens in a post-apocalyptic wasteland overrun by the undead. Every seven days, the Blood Moon rises, and hordes of increasingly powerful zombies descend upon their location, guided by an unholy instinct to destroy the living. To survive, the party must scavenge for resources, fortify a base with traps and defenses, and prepare for each escalating siege. The ultimate goal is to reach the Military Compound on the seventh Blood Moon, where a scientist claims to have a cure for the zombie plague—but the journey there will test their defenses, their resources, and their will to survive.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the origin of the zombie plague: a failed military bioweapon experiment that went global within weeks.
    *   Write the history of the Blood Moon phenomenon: a side effect of the plague that causes zombies to become hyper-aggressive and drawn to the living every 7 days.
    *   Describe Dr. Harrow's research: his controversial experiments to create a cure, and the moral lines he has crossed.
    *   Explain the fall of civilization: how governments collapsed, cities fell, and survivor enclaves became the new normal.
    *   Detail the emergence of special zombie types: mutations caused by prolonged exposure to the bioweapon.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Military Compound (Dr. Harrow's Faction)** (Major)
        *   **Goals:** To develop a cure for the zombie plague and restore civilization.
        *   **Hierarchy:** Led by Dr. Harrow, with a small military escort led by Captain Reyes.
        *   **Public Agenda:** We are working on a cure. Survivors are welcome if they can contribute.
        *   **Secret Agenda:** Dr. Harrow uses survivors as test subjects, often without consent. Many have died in his experiments.
        *   **Assets:** Fortified compound, medical supplies, research equipment, trained soldiers.
        *   **Relationships:** Cautiously welcoming to survivors; hostile to raiders.
    *   **The Iron Haven** (Minor)
        *   **Goals:** To survive, protect their own, and avoid conflict.
        *   **Hierarchy:** Led by Commander Sarah Kane, with a council of senior survivors.
        *   **Public Agenda:** We defend our own. Outsiders are welcome if they prove their worth.
        *   **Secret Agenda:** They are running out of supplies and may resort to raiding weaker groups.
        *   **Assets:** Fortified settlement, skilled defenders, scavenging teams.
        *   **Relationships:** Neutral to the party; hostile to raiders; wary of the Military Compound.
    *   **The Zombie Horde** (Major — Environmental Faction)
        *   **Goals:** None. They are driven by the plague to consume the living.
        *   **Hierarchy:** The Zombie Overlord commands during the Seventh Blood Moon. Otherwise, they are mindless.
        *   **Public Agenda:** None. They attack the living on sight.
        *   **Secret Agenda:** The Overlord seeks revenge on Dr. Harrow for its transformation.
        *   **Assets:** Overwhelming numbers, special types (Ferals, Screamers, Demolishers), relentless aggression.
        *   **Relationships:** Hostile to all living beings.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Dr. Marcus Harrow:** The morally gray scientist obsessed with finding a cure.
    *   **Commander Sarah Kane:** The pragmatic leader of the Iron Haven settlement.
    *   **The Zombie Overlord:** The intelligent, mutated zombie leading the Seventh Blood Moon horde.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Desperate Lone Survivor"
    *   "Iron Haven Defender"
    *   "Military Compound Soldier"
    *   "Raider (hostile survivor)"
    *   "Various Zombie Types (Basic, Feral, Screamer, Demolisher)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Town (Starting Zone):** A small, abandoned town with scavengeable buildings.
        *   **Key Landmarks:** The Police Station (defensible), the Hospital (high-risk, high-reward), the Hardware Store (building materials).
        *   **Primary Inhabitants:** Wandering zombies, scavengers.
        *   **Available Goods & Services:** Basic resources (food, water, tools, building materials).
        *   **Potential Random Encounters (x5):** A zombie horde stumbles upon the party, a friendly survivor offers trade, a building collapses, a Screamer calls reinforcements, a supply cache is found.
        *   **Embedded Plot Hooks & Rumors (x3):** "Radio chatter mentions a scientist at the Military Compound." "The Iron Haven settlement is to the north." "Blood Moons occur every 7 days."
        *   **Sensory Details:** Sight (Crumbling buildings, abandoned cars, wandering zombies), Sound (Distant moans, the wind, creaking metal), Smell (Decay, dust, smoke).
    *   **The Military Compound:** A massive, fortified base with heavy defenses.
        *   **Key Landmarks:** The Research Lab, the Armory, the Command Center, the Outer Walls.
        *   **Primary Inhabitants:** Dr. Harrow, soldiers, test subjects, the party (eventually).
        *   **Available Goods & Services:** Advanced medical supplies, weapons, the cure (if the party succeeds).
        *   **Potential Random Encounters (x5):** A test subject escapes, a Blood Moon approaches, a raider attack, Dr. Harrow requests the party's help, a soldier reports suspicious activity.
        *   **Embedded Plot Hooks & Rumors (x3):** "The cure requires a fungal sample from the Research Facility." "Dr. Harrow has been experimenting on survivors." "The Seventh Blood Moon will be the worst yet."
        *   **Sensory Details:** Sight (High concrete walls, guard towers, the sterile lab), Sound (Generator hum, radio chatter, marching boots), Smell (Antiseptic, gunpowder, fear).
    *   **The Research Facility:** A zombie-infested underground lab where the fungal sample is located.
        *   **Key Landmarks:** The Containment Wing, the Fungal Growth Chamber, the Collapse Zone.
        *   **Primary Inhabitants:** Hundreds of zombies, including special types. The Zombie Overlord may appear here.
        *   **Available Goods & Services:** The fungal sample (required for the cure), rare medical supplies.
        *   **Potential Random Encounters (x5):** A Feral pack ambushes, a Demolisher blocks the path, a Screamer summons a horde, a survivor is trapped, a data log reveals lore.
        *   **Embedded Plot Hooks & Rumors (x3):** "The fungal sample is in the deepest chamber." "The Overlord may be guarding it." "The facility is unstable and may collapse."
        *   **Sensory Details:** Sight (Dark, flooded corridors, fungal growth on walls, zombie-filled rooms), Sound (Moans, dripping water, creaking metal), Smell (Rot, mold, decay).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The party successfully defends against a Blood Moon with minimal losses.
    *   **THEN:** Their reputation grows. Other survivors may seek to join them, offering skills and resources.
    *   **IF:** The party's defenses fail during a Blood Moon, and zombies breach the base.
    *   **THEN:** They lose resources, potentially suffer casualties, and must rebuild or relocate. Generate a desperate escape scenario.
    *   **IF:** The party allies with the Iron Haven.
    *   **THEN:** They gain access to Iron Haven's resources and can coordinate defenses. However, when Iron Haven falls, the party may need to rescue survivors or recover lost supplies.
    *   **IF:** The party retrieves the fungal sample and returns to the Military Compound.
    *   **THEN:** Dr. Harrow begins crafting the cure. The Seventh Blood Moon triggers, and the party must defend the Compound from the Zombie Overlord's assault.
    *   **IF:** The party defeats the Zombie Overlord and the Seventh Blood Moon horde.
    *   **THEN:** The cure is completed. The campaign ends with hope: the party has bought humanity time to rebuild, and the Blood Moons cease (for now).
