### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Alchemist's Descent**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** A terminally ill alchemist partners with a failed rogue to manufacture an addictive magical substance called Blue Crystal. As they build a criminal empire to secure his family's future, they must navigate rival gangs, corrupt guards, and their own moral descent. This is a tragedy about how good people become monsters through incremental choices.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the history of alchemy in this city and the prestigious Mage's Guild where Walden once taught.
    *   Explain the magical wasting disease that afflicts Walden—its symptoms, progression, and why healing magic cannot cure it.
    *   Describe the discovery of Blue Crystal: what makes it unique, how it grants temporary spellcasting to non-mages, and why it's so addictive.
    *   Write the backstory of how the city's underworld is organized—the old cartels, the new powers, and the corrupt elements within the city guard.
    *   Detail Gus Fring's history and his long-planned revenge against the southern cartels.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Whitebeard Operation** (Minor, growing to Major)
        *   **Goals:** Manufacture and distribute Blue Crystal; amass wealth to secure Walden's family's future; maintain secrecy.
        *   **Hierarchy:** Walden (mastermind), Jessep (cook and distributor), Saul (legal fixer), various dealers and enforcers.
        *   **Public Agenda:** Walden is a dying teacher. Jessep is a small-time criminal. No one suspects them.
        *   **Secret Agenda:** Build the largest Blue Crystal empire in the realm, regardless of cost.
        *   **Assets:** Walden's alchemical genius, underground laboratory, laundromat front, Saul's legal expertise.
        *   **Relationships:** In conflict with local gangs; forced partnership with Gus Fring; hunted by Captain Hank.
    *   **The Fring Organization** (Major)
        *   **Goals:** Control all drug distribution in the region; destroy the southern cartels; maintain legitimate business fronts.
        *   **Hierarchy:** Gus (absolute leader), Mike (head of security), Victor and Tyrus (enforcers), vast network of distributors.
        *   **Public Agenda:** Gus owns Los Pollos Hermanos, a successful chain of fried chicken taverns, and is a pillar of the community.
        *   **Secret Agenda:** Use the drug trade to fund a war against the cartels who killed his partner.
        *   **Assets:** Massive wealth, political connections, legitimate businesses, underground distribution network, trained enforcers.
        *   **Relationships:** Walden and Jessep are valued assets but expendable; the cartels are mortal enemies; the city guard are obstacles to be bribed or eliminated.
    *   **The City Guard** (Major, Fragmented)
        *   **Goals:** Maintain order; investigate and stop the Blue Crystal epidemic (for some); profit from corruption (for others).
        *   **Hierarchy:** Captain Hank (investigator), corrupt officers, informants, beat guards.
        *   **Public Agenda:** Serve and protect the city.
        *   **Secret Agenda:** Some guards are on Gus's payroll; others genuinely want justice but are hampered by corruption.
        *   **Assets:** Legal authority, investigative resources, informant networks.
        *   **Relationships:** Hank is unknowingly hunting his brother-in-law; corrupt guards aid the Fring Organization; honest guards are often undermined.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Walden Whitebeard:** Terminally ill alchemist turned drug lord. Begins sympathetic, becomes ruthless. Brilliant, prideful, manipulative.
    *   **Jessep Pinkmantle:** Young half-elf rogue, Walden's partner. Emotional, loyal, conflicted, struggles with addiction and guilt.
    *   **Gus Fring:** Sophisticated crime lord with a legitimate business front. Calm, calculating, patient, ruthless. Driven by revenge.
    *   **Guard Captain Hank Schraderhelm:** Walden's brother-in-law and investigator. Boisterous, talented, dedicated, loves his family.
    *   **Saul Goodmanson:** Morally flexible lawyer-mage. Fast-talking, opportunistic, cowardly but competent and surprisingly loyal.
    *   **Mike Ehrmantrout:** Gus's head of security. Grizzled, professional, follows a strict code despite working for criminals.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Blue Crystal addict (various stages of addiction)"
    *   "Corrupt city guard officer"
    *   "Low-level drug distributor"
    *   "Cartel enforcer"
    *   "Innocent family member caught in the crossfire"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Laundromat:** A modest stone building that serves as the front for Walden's operation.
        *   **Key Landmarks:** The main washing floor with large tubs, the secret trapdoor beneath a specific washing station, the underground laboratory with alchemical equipment, the hidden escape tunnel.
        *   **Primary Inhabitants:** Walden (during cooking sessions), Jessep, hired guards, occasional money launderers.
        *   **Available Goods & Services:** Gold laundering, access to Blue Crystal production, meeting space for criminal business.
        *   **Potential Random Encounters (x5):** City guards conducting a routine inspection, a rival gang scouting the location, Jessep having a breakdown, equipment malfunction during a cook, an unexpected visit from Gus's people.
        *   **Embedded Plot Hooks & Rumors (x3):** "Someone has been watching the laundromat at night." "Captain Hank asked questions about the owner." "A competing alchemist claims they can match Walden's quality."
        *   **Sensory Details:** Sight (Steam from washing tubs, blue glow from hidden laboratory below), Sound (Splashing water, bubbling alchemical reactions), Smell (Soap and lye, sharp chemical scents from below).
    *   **Los Pollos Hermanos (Main Location):** A popular fried chicken tavern that serves as Gus's primary front.
        *   **Key Landmarks:** The public dining area, Gus's office, the hidden basement, the industrial kitchen, the secret meeting room behind a false wall.
        *   **Primary Inhabitants:** Gus Fring (manager), Mike (security), legitimate employees, undercover distributors.
        *   **Available Goods & Services:** Excellent fried chicken, meeting space for criminal business, access to Gus's distribution network, protection services.
        *   **Potential Random Encounters (x5):** Gus is present and observing everything, Mike is conducting security sweeps, a cartel representative arrives unannounced, a health inspector (real or fake) appears, a Blue Crystal deal happens in plain sight using coded language.
        *   **Embedded Plot Hooks & Rumors (x3):** "Gus has a secret past involving a murdered partner." "The restaurant has never been robbed—even hardened criminals fear Gus." "Some employees disappear without explanation."
        *   **Sensory Details:** Sight (Clean, well-maintained tavern, yellow and red color scheme, Gus's calm presence), Sound (Sizzling chicken, cheerful dining conversation, the hum of secrecy), Smell (Delicious fried chicken, spices, underneath it all a faint chemical scent in certain rooms).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** Walden and Jessep produce a batch of exceptionally pure Blue Crystal.
    *   **THEN:** Demand skyrockets, attracting both wealthy customers and dangerous rivals. Gus Fring takes notice and makes contact. Heat from law enforcement increases.
    *   **IF:** The players eliminate a rival gang or distributor.
    *   **THEN:** They gain territory and reputation, but create a power vacuum that attracts more dangerous enemies. The violence escalates.
    *   **IF:** Captain Hank gets a significant lead on the Blue Crystal cook's identity.
    *   **THEN:** The investigation closes in. Players must decide whether to flee, eliminate witnesses, or try to misdirect Hank. Family dinners become tense interrogations.
    *   **IF:** Walden's wife discovers the truth about his activities.
    *   **THEN:** Generate a major relationship crisis. She may try to leave with their son, confront him, or be in danger from his enemies. Walden must choose between honesty and more lies.
    *   **IF:** Players choose to work exclusively for Gus Fring.
    *   **THEN:** They gain access to better resources and protection, but lose all autonomy. Gus dictates their every move. They are trapped in a gilded cage.
    *   **IF:** Jessep tries to leave the operation.
    *   **THEN:** Generate complications: Gus won't allow it, Walden manipulates him into staying, or his departure creates a dangerous void. Departure attempts rarely succeed.
    *   **IF:** The players' Breaking Point meter reaches maximum.
    *   **THEN:** A major NPC death occurs as a result of their actions—possibly someone innocent or beloved. This serves as a point of no return.
