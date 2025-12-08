### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Diamond Underworld: Connected Chaos**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** A legendary diamond is stolen and passes through the hands of the city's interconnected criminal underworld, with the players caught up in the chaos as various factions pursue the prize. What starts as a simple theft spirals into a web of boxers with gambling debts, gangsters with anger issues, pawnbrokers with dangerous connections, and amateur thieves in way over their heads. Every character and scheme is connected to every other in unexpected ways, creating a domino effect of escalating violence and absurdity. The campaign is a darkly comic exploration of how one diamond can unite, destroy, and reveal the true nature of a city's criminal ecosystem.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the history of the legendary diamond—where it came from, its curse, and why every criminal wants it.
    *   Write about the city's underground boxing culture and how it connects to organized crime.
    *   Describe the criminal ecosystem—how pawnbrokers, gangsters, boxers, thieves, and fences all interconnect.
    *   Explain the code of the streets and how reputation, debt, and violence govern criminal interactions.
    *   Detail famous criminal disasters caused by schemes colliding in unexpected ways.
    *   Write about Brick Top's rise to power through spectacular violence and pig farming.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Boxing Underworld** (Major)
        *   **Goals:** To profit from bare-knuckle fighting through gambling, fixed matches, and criminal connections.
        *   **Hierarchy:** Promoters manage fighters who owe debts and take orders.
        *   **Public Agenda:** We provide entertainment and opportunity for fighters.
        *   **Secret Agenda:** To use boxing as cover for criminal operations and debt enforcement.
        *   **Assets:** Fighters, gambling operations, connections to broader criminal world.
        *   **Relationships:** Indebted to gangsters; exploiting boxers; connected to pawnbrokers for equipment and fencing.
    *   **Brick Top's Organization** (Major)
        *   **Goals:** To control criminal operations through fear, violence, and efficiency.
        *   **Hierarchy:** Brick Top at the top with loyal but terrified enforcers.
        *   **Public Agenda:** We run a pig farm.
        *   **Secret Agenda:** We disappear enemies in pig pens and control crime through spectacular violence.
        *   **Assets:** Ruthless reputation, effective disposal methods, fear-based loyalty.
        *   **Relationships:** Everyone fears them; antagonistic toward anyone who crosses them; uses violence to solve problems.
    *   **The Criminal Network** (Minor—interconnected)
        *   **Goals:** To profit from various criminal schemes while navigating dangerous connections.
        *   **Hierarchy:** Loose network of pawnbrokers, fences, thieves, and opportunists.
        *   **Public Agenda:** We're legitimate businesspeople.
        *   **Secret Agenda:** We're all connected through crime, debts, and shared secrets.
        *   **Assets:** Information, stolen goods, connections throughout the ecosystem.
        *   **Relationships:** Everyone knows everyone through one or two degrees of separation; debts and favors create complex web.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **"Turkish":** The fast-talking boxing promoter caught in schemes beyond his control.
    *   **Brick Top:** The terrifying gangster who feeds enemies to pigs.
    *   **Sol:** The pawnbroker manipulating all factions for profit.
    *   **Mickey:** The bare-knuckle boxer with his own agenda and dangerous skills.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Underground Fighter"
    *   "Violent Enforcer"
    *   "Incompetent Thief"
    *   "Gambling Addict"
    *   "Fence/Dealer"
    *   "Unlicensed Promoter"
    *   "Traveler Criminal"
    *   "Connected Pawnbroker"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Underground Boxing Ring:** Where violence and gambling intersect.
        *   **Key Landmarks:** The Ring, Betting Windows, Back Rooms for Deals, Fighter Quarters.
        *   **Primary Inhabitants:** Boxers, promoters, gamblers, gangsters watching investments.
        *   **Available Goods & Services:** Fixed fights, gambling opportunities, criminal contacts.
        *   **Potential Random Encounters (x5):** Fight goes wrong, gambling debt called in, gangster makes appearance, diamond mentioned in bet, violent enforcement.
        *   **Embedded Plot Hooks & Rumors (x3):** "The next fight is fixed." "Someone bet the diamond on the match." "Brick Top owns half the fighters through debts."
        *   **Sensory Details:** Sight (Blood on canvas, betting slips, crowd pressed close), Sound (Fight bells, crowd roaring, bones breaking), Smell (Sweat, blood, beer, desperation).
    *   **Sol's Pawnshop:** The nexus of criminal connections.
        *   **Key Landmarks:** Display Cases, Back Room (stolen goods), Safe (valuables), Hidden Passages.
        *   **Primary Inhabitants:** Sol, various criminals pawning or fencing goods.
        *   **Available Goods & Services:** Fencing stolen goods, information brokering, criminal introductions.
        *   **Potential Random Encounters (x5):** Gangster collecting payment, thief trying to fence diamond, criminal connection revealed, dangerous goods pawned, confrontation over debts.
        *   **Embedded Plot Hooks & Rumors (x3):** "Sol knows everyone's business." "Everything stolen in this city passes through here." "Sol is playing all sides for profit."
        *   **Sensory Details:** Sight (Cluttered shelves, stolen goods, nervous glances), Sound (Door chime, hushed negotiations, cash registers), Smell (Dust, old goods, fear-sweat).
    *   **Brick Top's Pig Farm:** Where enemies disappear.
        *   **Key Landmarks:** Pig Pens, Farmhouse (deceptively normal), Disposal Areas, Meeting Rooms.
        *   **Primary Inhabitants:** Brick Top, terrified employees, doomed enemies, pigs.
        *   **Available Goods & Services:** Permanent disposal, terrifying negotiations, violent enforcement.
        *   **Potential Random Encounters (x5):** Someone being fed to pigs, philosophical conversation about violence, threat delivered with charm, pig feeding demonstration, narrow escape.
        *   **Embedded Plot Hooks & Rumors (x3):** "Never cross Brick Top—you'll feed his pigs." "He's charming until he's not, then you're pig food." "More people have died here than anyone knows."
        *   **Sensory Details:** Sight (Deceptively rural, pigs in pens, blood in feeding troughs), Sound (Pig snuffling, Brick Top's charming voice, screams), Smell (Pig farm, fear, death).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The diamond changes hands through theft or deal.
    *   **THEN:** New factions enter pursuit and previous holders become desperate. Generate cascading criminal complications.
    *   **IF:** A fixed boxing match goes wrong.
    *   **THEN:** Gambling debts explode and violence follows. Generate chaotic consequences and angry gangsters.
    *   **IF:** Characters discover their unexpected connections.
    *   **THEN:** New alliances or conflicts form based on shared history. Generate revelations that explain earlier events.
    *   **IF:** Brick Top decides someone needs to die.
    *   **THEN:** That character is in mortal danger requiring desperate action. Generate pig farm scenarios and narrow escapes.
    *   **IF:** All factions converge on the diamond's location.
    *   **THEN:** Massive chaotic confrontation with multiple agendas colliding. Generate absurd violence and unexpected outcomes.
    *   **IF:** The interconnected nature of crime is revealed.
    *   **THEN:** Characters realize how every action affected every other. Generate satisfying reveals of the connection web.
