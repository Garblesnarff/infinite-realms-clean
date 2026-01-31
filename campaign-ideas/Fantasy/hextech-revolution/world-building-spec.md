### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**Hextech Revolution**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** Piltover, the gleaming City of Progress, thrives on Hextech innovation while the undercity of Zaun suffocates beneath chemical waste and oppression. When a heist goes wrong, two sisters are torn apart—one becomes an enforcer for order, the other a revolutionary for change. Players navigate this divided city as class warfare escalates, choosing between maintaining an unjust peace or supporting a violent revolution. Magic fused with technology reshapes society, but who truly benefits from progress?

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the founding of Piltover and how it was built literally on top of Zaun, using the undercity's resources and labor.
    *   Explain the invention of Hextech by Jayce and Viktor—magic crystallized into stable technology, revolutionizing Piltover but widening inequality.
    *   Describe Shimmer's creation by Singed for Silco—a dangerous alchemical substance that enhances human abilities but causes addiction and mutation.
    *   Write the history of the failed Zaun independence movement and how Silco survived betrayal to become the undercity's most powerful figure.
    *   Detail the class structure: Piltover's hereditary council and merchant families vs. Zaun's chem-barons and desperate workers.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **Piltover Enforcers** (Major)
        *   **Goals:** Maintain order; protect Piltover citizens; suppress Zaun unrest; prevent hextech theft.
        *   **Hierarchy:** Sheriff Caitlyn, captains, enforcers, hextech security.
        *   **Public Agenda:** Serve and protect all citizens.
        *   **Secret Agenda:** Protect Piltover's interests over Zaun's welfare; some are corrupt and take bribes from chem-barons.
        *   **Assets:** Hextech weapons and armor, legal authority, superior resources, tactical training.
        *   **Relationships:** At war with Zaun revolutionaries; tools of the Council; Vi is trying to reform from within.
    *   **The Chem-Barons of Zaun** (Major, Fragmented)
        *   **Goals:** Control Shimmer production and distribution; maintain power in the undercity; resist Piltover control.
        *   **Hierarchy:** Silco (most powerful), other chem-barons competing for territory, enforcers, Shimmer-enhanced fighters.
        *   **Public Agenda:** Provide for Zaun when Piltover won't.
        *   **Secret Agenda:** Profit from poisoning their own people; some want independence, others just want power.
        *   **Assets:** Shimmer production, territory in Zaun, loyalty through fear and necessity, Jinx's weapons.
        *   **Relationships:** United against Piltover but competing with each other; Silco is using revolution as a vehicle for his own power.
    *   **The Firelights** (Minor, Resistance)
        *   **Goals:** Protect Zaun from both Piltover and the chem-barons; provide aid to victims of Shimmer; create genuine change.
        *   **Hierarchy:** Ekko (leader), resistance fighters, community organizers.
        *   **Public Agenda:** Help Zaun's people.
        *   **Secret Agenda:** Sabotage both Shimmer production and hextech shipments; they represent the third option.
        *   **Assets:** Mobility, community support, guerrilla tactics, moral authority.
        *   **Relationships:** Fight both Piltover enforcers and chem-barons; see Silco as betraying Zaun's true interests.
    *   **The Council** (Major)
        *   **Goals:** Maintain Piltover's prosperity; advance hextech development; contain Zaun unrest; preserve the existing order.
        *   **Hierarchy:** Councilors (hereditary and appointed), Jayce (newest member), advisors, merchant representatives.
        *   **Public Agenda:** Lead Piltover wisely.
        *   **Secret Agenda:** Preserve their wealth and power; some genuinely want peace, others want to crush Zaun.
        *   **Assets:** Political power, control of hextech, wealth, ability to declare war or negotiate.
        *   **Relationships:** Divided on how to handle Zaun; control the enforcers; will be Jinx's final target.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Vi (Violet):** Former Zaun street kid, now Piltover enforcer. Tough, loyal, seeks redemption and her sister.
    *   **Jinx (Powder):** Vi's sister, brilliant but unstable inventor. Creates weapons for Silco's revolution. Traumatized, chaotic, desperate for acceptance.
    *   **Silco:** Zaun crime lord controlling Shimmer trade. Revolutionary who adopted Jinx. Ruthless but genuinely loves her.
    *   **Jayce Talis:** Hextech inventor and councilor. Idealistic, believes progress solves problems, politically naive.
    *   **Viktor:** Jayce's partner, from Zaun, dying and experimenting with hextech enhancement of humans.
    *   **Caitlyn Kiramman:** Piltover enforcer from wealthy family. Wants justice, partners with Vi, must choose between order and justice.
    *   **Ekko:** Leader of the Firelights, former friend of Vi and Jinx. Represents hope for a better Zaun.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Shimmer-enhanced Zaun fighter"
    *   "Piltover enforcer with hextech equipment"
    *   "Desperate Zaun citizen caught in the crossfire"
    *   "Wealthy Piltover merchant oblivious to Zaun's suffering"
    *   "Chem-baron lieutenant"
    *   "Firelight resistance member"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Last Drop (Zaun):** A bar and Silco's base of operations in Zaun's heart.
        *   **Key Landmarks:** The bar itself, Silco's office, the basement Shimmer lab, the hidden escape routes, the memorial to those killed in the original revolution.
        *   **Primary Inhabitants:** Silco, his enforcers, Jinx (her workshop), patrons, Shimmer addicts, informants.
        *   **Available Goods & Services:** Information, Shimmer (various grades), weapons, sanctuary (if you're on Silco's good side).
        *   **Potential Random Encounters (x5):** Shimmer deal goes violent, Jinx testing explosives, Piltover raid, rival chem-baron attack, emotional breakdown from Jinx.
        *   **Embedded Plot Hooks & Rumors (x3):** "Silco is planning something big with hextech." "Jinx is building a weapon that could level Piltover." "Vander's ghost still haunts this place."
        *   **Sensory Details:** Sight (Dim neon lighting, green chemical smog seeping through cracks, Jinx's graffiti art, purple shimmer glow), Sound (Rough music, hushed criminal deals, occasional explosions from Jinx's workshop), Smell (Alcohol, chemical tang, decay).
    *   **The Council Chamber (Piltover):** Where Piltover's elite make decisions affecting both cities.
        *   **Key Landmarks:** The circular council table, stained glass windows showing Piltover's history, hextech security systems, the balcony overlooking the city.
        *   **Primary Inhabitants:** The Council members, Jayce, guards, petitioners, political operatives.
        *   **Available Goods & Services:** Political decisions, access to hextech funding, legal authority, information from the top.
        *   **Potential Random Encounters (x5):** Heated debate about Zaun, Jayce arguing for reform, emergency session about hextech theft, assassination attempt, Jinx's final attack.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Council is divided on war with Zaun." "Jayce wants to share hextech with the undercity." "Someone on the Council is taking bribes from chem-barons."
        *   **Sensory Details:** Sight (Elegant Art Nouveau architecture, blue hextech lighting, golden fixtures, stained glass), Sound (Formal debates, the hum of hextech systems), Smell (Polished wood, fresh air—nothing like Zaun).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** Players side primarily with Piltover.
    *   **THEN:** They gain access to hextech equipment and legal authority but are seen as traitors in Zaun. Silco marks them for death.
    *   **IF:** Players side primarily with Zaun/Silco.
    *   **THEN:** They gain Shimmer enhancements and revolutionary support but are hunted as terrorists by Piltover. They must live in hiding.
    *   **IF:** Jinx completes her hextech weapon.
    *   **THEN:** She gains the ability to destroy the Council chamber. The final confrontation accelerates. Vi must choose: stop her sister or let her commit mass murder.
    *   **IF:** Vi and Jinx confront each other.
    *   **THEN:** Generate an emotional, violent encounter. Their relationship can be mended (requiring players' intervention) or shattered forever. If shattered, one may die.
    *   **IF:** The Council chamber is attacked.
    *   **THEN:** War is declared. Piltover mobilizes its full hextech military. Zaun erupts in revolution. The campaign enters endgame—total war.
    *   **IF:** Players find a third way (supporting the Firelights or negotiating peace).
    *   **THEN:** Generate difficult skill challenges to broker genuine reform. Requires sacrifices from both cities. Success creates hope; failure creates martyrs.
    *   **IF:** Viktor completes his hextech human enhancement.
    *   **THEN:** He transforms into something beyond human—perhaps ascending, perhaps becoming monstrous. He represents the ultimate question: what cost for progress?
