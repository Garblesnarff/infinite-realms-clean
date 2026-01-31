### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**Streets of Hammerfast**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The city of Hammerfast is dying from within. The drug trade hollows out neighborhoods. The City Watch is hamstrung by politics and corruption. The docks are failing economically, driving workers to crime. Schools fail children. Politics rewards ambition over reform. Players navigate this interconnected web of institutional failure from multiple perspectives—as detectives, criminals, workers, or reformers. The question is not if the system is broken, but whether anyone can survive it with integrity intact.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the economic history of Hammerfast—once a thriving port city, now in decline as trade routes shift and automation eliminates dockworker jobs.
    *   Explain the drug trade's evolution in Hammerfast—from small-time dealers to organized crews with hierarchies and territories.
    *   Describe the City Watch's internal politics—how promotions require political favor, how real police work is punished, how statistics are manipulated.
    *   Write the history of the dockworker's union and its decline from powerful protector to desperate compromiser.
    *   Detail the political machine that runs Hammerfast and how genuine reformers are co-opted or destroyed.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **Major Crimes Unit** (Minor)
        *   **Goals:** Build legal cases against major drug organizations; follow the money; pursue real police work.
        *   **Hierarchy:** Lieutenant Daniels (commander), Detectives Freamon, McNulty, and others.
        *   **Public Agenda:** Reduce drug-related crime.
        *   **Secret Agenda:** Fight against their own department's political interference and incompetence.
        *   **Assets:** Wiretap capabilities, investigative skills, a few principled cops.
        *   **Relationships:** At odds with Watch leadership; pursuing the Barksdale and later other organizations; limited resources.
    *   **The Barksdale Organization** (Major)
        *   **Goals:** Control drug distribution in the Western District; maximize profits; maintain territory.
        *   **Hierarchy:** Avon Barksdale (leader), Stringer Bell (lieutenant), captains, soldiers, street dealers.
        *   **Public Agenda:** None—they are a criminal organization.
        *   **Secret Agenda:** Stringer wants to transition to legitimate business; Avon wants to maintain street control.
        *   **Assets:** Territory, loyal soldiers, legal fronts, political connections through bribes.
        *   **Relationships:** At war with rival dealers; hunted by Major Crimes; corrupting low-level Watch officers.
    *   **The Dockworkers Union** (Major, Declining)
        *   **Goals:** Protect dockworker jobs and wages; maintain political influence; survive economic changes.
        *   **Hierarchy:** Frank Sobotka (union leader), his nephew Ziggy, union members.
        *   **Public Agenda:** Represent dockworkers' interests.
        *   **Secret Agenda:** Frank makes deals with smugglers to fund political lobbying for port development.
        *   **Assets:** Control of dock operations, political connections, legitimate labor power.
        *   **Relationships:** Compromised by deals with criminal smugglers; investigating by police; ignored by politicians.
    *   **The Political Machine** (Major)
        *   **Goals:** Maintain power; secure funding; manage optics; control narratives.
        *   **Hierarchy:** The Mayor, City Council, political operatives, campaign managers.
        *   **Public Agenda:** Govern the city effectively.
        *   **Secret Agenda:** Prioritize political survival over genuine reform; manipulate crime statistics; co-opt reformers.
        *   **Assets:** Control of city budget, media access, ability to promote or destroy careers.
        *   **Relationships:** Use the Watch for political gain; court votes through patronage; destroy genuine reformers who threaten the system.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Detective Lester Freamon:** Patient, brilliant investigator who "follows the money." Wise mentor figure.
    *   **Detective Jimmy McNulty:** Talented but self-destructive detective who can't stop pursuing cases against orders.
    *   **Avon Barksdale:** Charismatic drug kingpin, traditionalist who values loyalty and the street code.
    *   **Stringer Bell:** Intelligent lieutenant who wants to apply business principles to the drug trade.
    *   **Omar Little:** Stick-up man who robs dealers but lives by a code—never harm civilians.
    *   **Tommy Carcetti:** Ambitious politician who campaigns on reform but learns governing requires compromise.
    *   **Frank Sobotka:** Union leader trying to save his workers through increasingly desperate compromises.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Street-level drug dealer, trapped by circumstances"
    *   "Corrupt Watch officer on the take"
    *   "Principled detective hamstrung by bureaucracy"
    *   "Desperate dockworker supplementing wages with crime"
    *   "Political operative managing optics over substance"
    *   "Failed youth being pulled into the drug trade"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Low-Rise Projects (Western District):** Decaying tenement buildings controlled by the Barksdale organization.
        *   **Key Landmarks:** The main corner where drugs are sold, the pit (central courtyard), vacant buildings used as stash houses, Orlando's (Avon's strip club front).
        *   **Primary Inhabitants:** Residents living in poverty, street dealers, lookouts, enforcers, occasional Watch patrols.
        *   **Available Goods & Services:** Drugs, stolen goods, protection (for a price), information (if you can be trusted).
        *   **Potential Random Encounters (x5):** Drug deal goes bad and violence erupts, Watch raid on a stash house, stick-up by Omar's crew, community members trying to reclaim their neighborhood, funeral for a fallen dealer.
        *   **Embedded Plot Hooks & Rumors (x3):** "Stringer Bell is taking business classes at the university." "Omar is hunting Barksdale soldiers." "The Watch has a wire on the main crew."
        *   **Sensory Details:** Sight (Crumbling brick buildings, boarded windows, young men posted on corners watching), Sound (Distant music, children playing, occasional shouts or gunshots), Smell (Urban decay, cooking food, sometimes the sweet smell of drugs).
    *   **Major Crimes Unit Office:** A cramped, underfunded office in the Watch headquarters where real investigation happens.
        *   **Key Landmarks:** The bullpen with cluttered desks, the case board covered in surveillance photos and connections, the wiretap monitoring room, Lieutenant Daniels's office.
        *   **Primary Inhabitants:** Major Crimes detectives, technical surveillance operators, occasional visits from frustrated commanders.
        *   **Available Goods & Services:** Access to investigative resources (limited), wiretap authorization (hard to get), case files.
        *   **Potential Random Encounters (x5):** Breakthrough in wiretap surveillance, political pressure to shut down the case, witness comes in with information, internal conflict between detectives, orders to manipulate statistics instead of pursuing real work.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Deputy Commissioner wants the unit disbanded." "Following the money leads to city politicians." "A key witness is about to flip."
        *   **Sensory Details:** Sight (Cluttered desks, case board with photos and string, fluorescent lighting, stacks of files), Sound (Ringing phones, typed reports, hushed conversations about the case), Smell (Old coffee, paper, cheap institutional cleaning products).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** Players successfully wiretap the Barksdale organization.
    *   **THEN:** They gather evidence of the hierarchy and operations, but political pressure mounts to end the investigation before it reaches connected officials.
    *   **IF:** Avon Barksdale is arrested.
    *   **THEN:** Stringer Bell takes over and begins transitioning to a more business-like operation. New rivals move into the power vacuum. The drug trade continues.
    *   **IF:** Players investigate the docks too deeply.
    *   **THEN:** They uncover connections between the union, smuggling, and city politics. Frank Sobotka is murdered by his criminal partners to prevent him from talking.
    *   **IF:** A reformist politician gains power.
    *   **THEN:** Generate scenarios where reform requires compromise: funding education means cutting Watch budgets, reducing arrests means appearing "soft on crime." Good intentions meet impossible choices.
    *   **IF:** The Major Crimes Unit is disbanded due to political pressure.
    *   **THEN:** Players are reassigned to meaningless positions. Their cases are shelved. The drug trade continues. The system wins.
    *   **IF:** Players try to work outside the system entirely (vigilantism, media leaks, etc.).
    *   **THEN:** They may achieve short-term victories but face legal consequences, career destruction, or violent retaliation. The question becomes: is martyrdom worth it?
    *   **IF:** The campaign reaches its conclusion.
    *   **THEN:** Show the long-term consequences: some criminals are imprisoned, but others rise to replace them. Some cops keep fighting, others burn out or compromise. The city remains broken. The game continues with new players.
