### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**War of Seven Kingdoms**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** Seven noble houses vie for control of the Iron Throne after the king's death. Players navigate deadly court politics, forge alliances through marriage and war, and choose sides in a conflict where honor often leads to death. Meanwhile, ancient evils awaken beyond the Wall, and dragons return to a world that had forgotten magic. Winter is coming, and with it, the army of the dead.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the Conquest, when the Dragon Lords united the Seven Kingdoms under one throne three centuries ago.
    *   Explain the Long Night, the ancient war against the White Walkers that occurred eight thousand years ago, and why most now believe it to be myth.
    *   Describe the construction of the Wall—a 700-foot barrier of ice and magic that has defended the realm for millennia.
    *   Write the history of the Targaryen dynasty, their dragons, and the civil war that caused the dragons' extinction.
    *   Detail the Rebellion that overthrew the Mad King fifteen years ago and placed the current royal family on the throne.
    *   Explain the prophecy of "The Prince That Was Promised" who will defend the realm from darkness.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **House Stormwind of Winterfell** (Major)
        *   **Goals:** Defend the North; uphold honor and duty; investigate the king's death.
        *   **Hierarchy:** Lord Eddard (head), his wife Lady Catelyn, their children, bannermen from northern houses.
        *   **Public Agenda:** Serve the realm justly and honorably.
        *   **Secret Agenda:** Protect a dangerous secret about the true heir to the throne.
        *   **Assets:** The North's loyalty, ancient Valyrian steel swords, knowledge of the White Walker threat.
        *   **Relationships:** Honor-bound to the crown; distrusts the Lionhearts; allied with the Night's Watch.
    *   **House Lionheart of Casterly Rock** (Major)
        *   **Goals:** Maintain power; protect the Queen Regent's children; control the Iron Throne.
        *   **Hierarchy:** Tywin (patriarch), Queen Regent Cerenna, her twin brother Jaime, their dwarf brother Tyrion.
        *   **Public Agenda:** Support the "rightful" king, Cerenna's son.
        *   **Secret Agenda:** Hide the truth that the royal children are bastards born of incest.
        *   **Assets:** Immense wealth, largest army, political cunning, control of the capital.
        *   **Relationships:** At war with most other houses; allies with opportunistic houses through gold.
    *   **The Night's Watch** (Major)
        *   **Goals:** Defend the Wall; protect the realm from what lies beyond; investigate White Walker sightings.
        *   **Hierarchy:** The Lord Commander, officers (rangers, stewards, builders), sworn brothers who have taken vows of celibacy and neutrality.
        *   **Public Agenda:** Guard the realm.
        *   **Secret Agenda:** Most brothers don't believe in White Walkers; the Watch is undermanned and desperate.
        *   **Assets:** The Wall itself, ancient weapons, knowledge of the true threat.
        *   **Relationships:** Neutral in political conflicts; increasingly ignored by southern lords; only the North still sends support.
    *   **Daenerys's Liberation Army** (Minor, growing to Major)
        *   **Goals:** Reclaim the Iron Throne; break the wheel of oppression; free slaves.
        *   **Hierarchy:** Queen Daenerys, her advisors, the Unsullied (elite eunuch soldiers), freed slaves, three dragons.
        *   **Public Agenda:** Liberate the oppressed and rule justly.
        *   **Secret Agenda:** Daenerys struggles between mercy and fire—her family's madness calls to her.
        *   **Assets:** Three growing dragons, fanatical loyalty from freedmen, the Targaryen name.
        *   **Relationships:** Exiled from Westeros; building power across the Narrow Sea; seen as both liberator and foreign invader.
    *   **The White Walkers** (Major, Existential Threat)
        *   **Goals:** March south; kill all living things; raise them as undead soldiers; bring eternal winter.
        *   **Hierarchy:** The Night King, White Walker lieutenants, vast army of undead wights.
        *   **Public Agenda:** None. They do not negotiate.
        *   **Secret Agenda:** The Night King seeks something specific—possibly to destroy the magical protections that have kept him beyond the Wall.
        *   **Assets:** Immortality, ability to raise the dead, immunity to normal weapons, control over winter itself.
        *   **Relationships:** The enemy of all living things; can only be harmed by dragonglass, Valyrian steel, or dragon fire.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Lord Eddard Stormwind:** Honorable northern lord, Hand of the King, doomed by his rigid morality.
    *   **Queen Regent Cerenna Lionheart:** Ruthless, intelligent, fiercely protective mother hiding a terrible secret.
    *   **Daenerys Stormborn:** Exiled princess who hatches three dragons and begins her conquest, struggles with power and madness.
    *   **Jon Snow:** Bastard son defending the Wall, discovers the White Walker threat, secretly the true heir to the throne.
    *   **Tyrion Lannister:** Brilliant dwarf tactician, scorned by his family, becomes advisor to various factions.
    *   **The Night King:** Ancient, silent leader of the White Walkers, represents death incarnate.
    *   **Tywin Lionheart:** Patriarch of House Lionheart, ruthless strategist, builder of his family's power.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Northern bannerman sworn to House Stormwind"
    *   "Southern knight loyal to the crown"
    *   "Scheming courtier seeking advancement"
    *   "Night's Watch ranger who has seen the White Walkers"
    *   "Freed slave in Daenerys's army"
    *   "White Walker lieutenant"
    *   "Undead wight (various types)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Iron Throne Room, King's Landing:** The seat of power, where political games are played and kings are made or broken.
        *   **Key Landmarks:** The Iron Throne (made from a thousand melted swords), the high windows, the audience hall, hidden passages behind the walls.
        *   **Primary Inhabitants:** The current king/queen, the small council, guards, petitioners, courtiers.
        *   **Available Goods & Services:** Royal decrees, justice (or injustice), political alliances, information from court spies.
        *   **Potential Random Encounters (x5):** A public execution, a tense small council meeting, an assassination attempt, a foreign ambassador arrives with demands, a riot outside the keep.
        *   **Embedded Plot Hooks & Rumors (x3):** "The king is not the old king's son." "The Hand of the King was poisoned." "Dragons have been seen across the Narrow Sea."
        *   **Sensory Details:** Sight (The massive Iron Throne looming over all, harsh sunlight through high windows, guards in golden armor), Sound (Echoing voices, the clink of armor, whispered plots), Smell (Stone and steel, incense, fear).
    *   **The Wall:** An impossible 700-foot barrier of ice stretching for hundreds of miles, defending the realm from the terrors beyond.
        *   **Key Landmarks:** Castle Black (main fortress), the great ice stair, the top of the Wall, the tunnel gates, the Haunted Forest beyond.
        *   **Primary Inhabitants:** Night's Watch brothers, rangers, stewards, builders, wildlings (as prisoners or refugees).
        *   **Available Goods & Services:** Shelter, training in combat, information about what lies beyond, ancient weapons.
        *   **Potential Random Encounters (x5):** A ranging party returns with dead or missing members, wildling attack, White Walker sighting, deserter execution, supply caravan from the south.
        *   **Embedded Plot Hooks & Rumors (x3):** "The dead are walking beyond the Wall." "The wildlings are fleeing south from something worse." "Ancient crypts beneath Castle Black hold secrets."
        *   **Sensory Details:** Sight (Endless wall of ice stretching to the horizon, ancient weathered stone of Castle Black, the dark forest beyond), Sound (Howling wind, creaking ice, the silence beyond the Wall), Smell (Cold air, pine from the forest, smoke from the castle's fires).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** Lord Eddard Stormwind discovers and reveals the truth about the royal children's parentage.
    *   **THEN:** He is arrested for treason. Players must choose to support him (risking execution), stay neutral, or side with the Queen Regent (gaining power but betraying honor).
    *   **IF:** The War of Five Kings begins.
    *   **THEN:** The realm fractures. Trade routes are disrupted, food becomes scarce, armies march. Players' home territories may be threatened. They must raise troops and choose sides.
    *   **IF:** The Red Wedding occurs (a major betrayal at a wedding feast).
    *   **THEN:** Generate mass casualties among allied NPCs. Trust is shattered. The rules of hospitality are broken. Players become more paranoid. Guest right means nothing.
    *   **IF:** Daenerys successfully hatches three dragon eggs.
    *   **THEN:** Dragons return to the world. This shifts the balance of power. Players may seek alliance with her, or prepare defenses against dragon fire.
    *   **IF:** The White Walkers breach the Wall.
    *   **THEN:** The Long Night begins. All political games become meaningless. Former enemies must unite or die. The campaign shifts from political intrigue to survival horror.
    *   **IF:** Winter advances (every 5-7 sessions).
    *   **THEN:** Food becomes scarcer, travel becomes harder, smallfolk freeze and starve, undead sightings increase. Armies struggle to campaign in the cold.
    *   **IF:** Players successfully unite the Seven Kingdoms against the White Walkers.
    *   **THEN:** Generate an epic final battle with mass combat. Success saves humanity but at terrible cost. The question of who rules the ashes remains.
