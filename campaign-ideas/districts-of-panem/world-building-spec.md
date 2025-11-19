### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**Districts of Panem**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The players are tributes from different districts, forced to compete in the annual Reaping Games—a brutal televised death match in a wilderness arena. They must navigate deadly environmental hazards, engineered monsters, political sponsorship, and moral choices about murder versus survival. Their actions are broadcast across Panem, making them either entertainment or symbols of rebellion. The campaign explores survival, propaganda, class warfare, and whether defiance can spark revolution against an oppressive Capitol.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the Dark Days—the rebellion 75 years ago when the 13 districts rose against the Capitol and were brutally crushed. District 13 was obliterated as an example.
    *   Write the history of the Treaty of Treason, which established the Hunger Games as annual punishment and reminder of the Capitol's power.
    *   Describe the first Hunger Games—a brutal, unrefined slaughter that evolved into the televised spectacle it is today.
    *   Explain each district's specialty and how the Capitol controls them through economic dependence (District 12: coal, District 4: fishing, District 7: lumber, District 11: agriculture, etc.).
    *   Detail the Quarter Quell tradition—every 25 years, a special Hunger Games with unique, cruel rules (e.g., reaping previous victors, double tributes, etc.).

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Capitol** (Major)
        *   **Goals:** Maintain absolute control over the districts through fear, spectacle, and economic dependency.
        *   **Hierarchy:** President Snow at the top, supported by the Gamemakers, Peacekeepers, and a wealthy citizen class.
        *   **Public Agenda:** Provide order, prosperity, and entertainment to Panem.
        *   **Secret Agenda:** Use the Hunger Games to prevent rebellion by forcing districts to sacrifice their children and turn potential allies into murderers.
        *   **Assets:** Advanced technology, Peacekeepers (military police), control over all resources, media domination.
        *   **Relationships:** Oppressors of the districts; beneficiaries of district labor; manipulators of public narrative.
    *   **The Districts** (Major - 12 oppressed regions)
        *   **Goals:** Survival under Capitol rule; secret goal of some: rebellion.
        *   **Hierarchy:** Each district has a mayor (Capitol-appointed puppet), Peacekeepers enforcing order, and a population divided by wealth (merchants vs. Seam workers).
        *   **Public Agenda:** Provide their specialized resource to the Capitol.
        *   **Secret Agenda:** Some districts harbor rebellion networks using secret signals (three-finger salute, mockingjay songs).
        *   **Assets:** Specialized skills (mining, fishing, electronics, agriculture), underground resistance networks (limited).
        *   **Relationships:** Exploited by the Capitol; forced to compete against each other through the Games; slowly building solidarity.
    *   **The Career Tributes** (Minor - Districts 1, 2, 4)
        *   **Goals:** Win the Hunger Games for glory and wealth.
        *   **Hierarchy:** Trained in secret academies, volunteer for the Games, form packs to dominate early competition.
        *   **Public Agenda:** Represent their districts with pride and skill.
        *   **Secret Agenda:** View the Games as an honor, not a punishment—complicit in the Capitol's system.
        *   **Assets:** Years of combat training, superior weapons from the Cornucopia, ruthless tactics.
        *   **Relationships:** Allies of convenience (often betray each other in the end); enemies of "weaker" districts; tools of Capitol propaganda.
    *   **The Rebellion (Hidden)** (Minor - emerges later)
        *   **Goals:** Overthrow the Capitol and establish democracy.
        *   **Hierarchy:** Decentralized cells in various districts, coordinated by District 13 (secretly survived).
        *   **Public Agenda:** None—operates in absolute secrecy.
        *   **Secret Agenda:** Use the Hunger Games tributes as symbols to inspire mass uprising.
        *   **Assets:** Hidden District 13's technology, underground networks, the mockingjay symbol.
        *   **Relationships:** Opposes the Capitol; seeks to recruit victors and tributes as propaganda; risks innocent lives for revolution.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **President Coriolanus Snow:** Tyrannical ruler of Panem, maintains power through fear and spectacle, poisoned rivals (drinks blood to mask the scent).
    *   **Haymitch Abernathy:** Cynical, alcoholic mentor from District 12, previous victor who humiliated the Capitol (lost his family as punishment).
    *   **Cinna:** The party's stylist, kind and artistic, secretly works for the rebellion (uses designs to send coded messages, eventually executed).
    *   **Seneca Crane:** Head Gamemaker, creative and ambitious, executed for allowing the double-victor outcome that inspired rebellion.
    *   **Effie Trinket:** Capitol escort for District 12, obsessed with manners and appearances, gradually develops sympathy for tributes.
    *   **Caesar Flickerman:** Charismatic television host who interviews tributes, treats the Games as entertainment, genuinely skilled at making guests shine.
    *   **Rue (District 11):** Young tribute (age 12), clever and kind, forms alliance with the party, her death galvanizes rebellion.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Career Tribute (Brutal, trained killer from Districts 1, 2, or 4)"
    *   "District Tribute (Desperate survivor with specialized skills from their region)"
    *   "Peacekeeper (Faceless enforcer in white armor)"
    *   "Capitol Citizen (Grotesquely fashionable, treats the Games as entertainment)"
    *   "Stylist (Artistic, transforms tributes into spectacles)"
    *   "Sponsor (Wealthy Capitol citizen betting on tributes)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **District 12 (The Seam):**
        *   **Key Landmarks:** The Justice Building (Reaping ceremony site), the Hob (black market), the coal mines, the electrified fence (keeps residents in).
        *   **Primary Inhabitants:** Coal miners, merchants, Peacekeepers, the mayor.
        *   **Available Goods & Services:** Basic food (trade bread, wild game from illegal hunting), coal for heating, black market goods (medicine, luxuries).
        *   **Potential Random Encounters (x5):** Peacekeepers harassing a merchant, a miner injured in a collapse, children playing with makeshift toys, a secret trade of game meat, rumors of rebellion signals.
        *   **Embedded Plot Hooks & Rumors (x3):** "The fence is electrified now—no one can escape to the woods." "They say District 13 wasn't really destroyed." "President Snow is watching District 12 closely this year."
        *   **Sensory Details:** Sight (Gray wooden houses, coal dust on everything, threadbare clothing), Sound (Pickaxes in the mines, the Reaping bell, whispered conversations), Smell (Coal smoke, stale bread, damp earth).
    *   **The Capitol:**
        *   **Key Landmarks:** The Presidential Palace, the Training Center, the Remake Center (where stylists work), the Avenue of Tributes (parade route), Caesar Flickerman's studio.
        *   **Primary Inhabitants:** Wealthy citizens with extreme fashion (dyed skin, surgical modifications), government officials, stylists, Peacekeepers.
        *   **Available Goods & Services:** Extravagant food and drink, high-tech gadgets, cosmetic surgery, luxury clothing, entertainment.
        *   **Potential Random Encounters (x5):** Capitol citizens treating tributes like celebrities, a stylist discussing designs, a sponsor negotiating gifts, a Peacekeeper escorting dignitaries, a propaganda broadcast.
        *   **Embedded Plot Hooks & Rumors (x3):** "President Snow is unhappy with this year's Gamemakers." "Some tributes are more valuable as symbols than victors." "The Capitol's control is slipping in the outer districts."
        *   **Sensory Details:** Sight (Towering glass buildings, holographic ads, citizens in absurd costumes), Sound (Orchestral music, laughter, propaganda announcements), Smell (Perfume, exotic foods, artificial flowers).
    *   **The Training Center:**
        *   **Key Landmarks:** Weapon stations (swords, bows, spears), survival stations (fire-making, camouflage, shelter), combat ring, private evaluation room.
        *   **Primary Inhabitants:** Tributes, trainers, Gamemaker observers, stylists preparing for interviews.
        *   **Available Goods & Services:** Three days of skill training, strategy advice (limited), physical conditioning.
        *   **Potential Random Encounters (x5):** A Career tribute showing off their skills, a trainer offering advice, a tribute sabotaging another's practice, an argument between allies, Gamemakers taking notes.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Gamemakers only watch tributes who do something unexpected." "Some tributes are hiding their real skills." "Alliances formed here never last past the Bloodbath."
        *   **Sensory Details:** Sight (High-tech equipment, tributes practicing combat, Gamemakers watching from balconies), Sound (Clash of weapons, grunts of effort, whispered strategies), Smell (Sweat, leather, artificial pine from survival stations).
    *   **The Arena (Forest Dome):**
        *   **Key Landmarks:** The Cornucopia (golden supply horn), the lake (fresh water source), tracker jacker nests (deadly mutations), the cave (potential shelter), the clearing (forced confrontation zone).
        *   **Primary Inhabitants:** Tributes (24 at start, dwindling rapidly), mutations (tracker jackers, wolf mutts), Gamemaker-controlled hazards.
        *   **Available Goods & Services:** None directly—tributes must scavenge from the Cornucopia, hunt, or receive sponsor gifts.
        *   **Potential Random Encounters (x5):** A tribute ambush, a tracker jacker attack, a Gamemaker-created fire storm, a sponsor gift parachute, a Career pack hunting expedition.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Gamemakers can hear everything—hidden microphones everywhere." "Certain zones are death traps activated when the action slows." "The force field boundary shimmers when tributes get too close."
        *   **Sensory Details:** Sight (Dense green forest, golden Cornucopia gleaming, cameras hidden in trees), Sound (Birds, wind, cannons marking deaths, rustling that could be tributes or mutations), Smell (Pine, fresh water, blood from combat, smoke from fires).
    *   **The Victor's Village:**
        *   **Key Landmarks:** Twelve mansions (one per district, most empty), Haymitch's house (perpetually messy), the party's new homes.
        *   **Primary Inhabitants:** Victors (few and traumatized), Peacekeepers (surveillance), servants (Capitol-sent).
        *   **Available Goods & Services:** Luxury food and goods, but no freedom—constant surveillance.
        *   **Potential Random Encounters (x5):** Haymitch drunk and cynical, a Peacekeeper checking in, a Capitol servant delivering gifts, a nightmare waking a victor, a secret rebel contact.
        *   **Embedded Plot Hooks & Rumors (x3):** "Haymitch's family was killed after he embarrassed the Capitol." "Victors are never truly free—they're owned by the Capitol." "Some victors work for the rebellion in secret."
        *   **Sensory Details:** Sight (Pristine mansions contrasting with district poverty, most houses dark and empty), Sound (Silence broken by occasional screams from nightmares, Peacekeeper patrols), Smell (Clean, sterile air, Haymitch's alcohol, roses from Snow's threats).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The party rushes the Cornucopia during the initial Bloodbath.
    *   **THEN:** Generate a brutal combat encounter with Career tributes. High risk of injury or death, but access to superior weapons and supplies. Survivors gain Sponsor Favor for boldness.
    *   **IF:** The party flees the Cornucopia and hides.
    *   **THEN:** Generate survival challenges (finding water, avoiding starvation, crafting tools). Lower immediate danger but harder long-term survival. Sponsor Favor depends on how cleverly they survive.
    *   **IF:** The party forms an alliance with Career tributes.
    *   **THEN:** Generate easier access to supplies and safety in numbers, but the Careers will eventually betray them. Sponsor Favor decreases (seen as cowardly). Rebellion factions lose interest.
    *   **IF:** The party befriends Rue (District 11).
    *   **THEN:** Generate survival assistance (she knows edible plants, can climb and scout). When she dies, her district riots. The party gains rebel sympathy but Capitol hostility.
    *   **IF:** The party performs well in interviews and training.
    *   **THEN:** Generate higher Sponsor Point income and favorable odds. More sponsor gifts arrive during the arena. Capitol sees them as entertainment, not threats (yet).
    *   **IF:** The party defies the Capitol during the finale (threatens suicide with nightlock berries).
    *   **THEN:** Generate Capitol panic and rule change allowing double victors. This humiliates President Snow and makes the party targets. Rebellion is inspired. Quarter Quell is designed to kill them.
    *   **IF:** The party kills each other in the finale to obey the rules.
    *   **THEN:** Generate a tragic, hollow victory for the survivor. They become a propaganda tool but are psychologically destroyed. No rebellion is inspired.
    *   **IF:** The party destroys the arena force field during the Quarter Quell.
    *   **THEN:** Generate their rescue by rebel forces. They become symbols of rebellion (the Mockingjay). The districts rise in open war against the Capitol.
    *   **IF:** The party refuses to participate in the Victory Tour propaganda.
    *   **THEN:** Generate threats from President Snow (execution of family members). Peacekeepers increase violence in their districts. The party must choose compliance or escalation.
