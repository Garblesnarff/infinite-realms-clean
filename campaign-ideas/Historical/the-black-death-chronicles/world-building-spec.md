### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Black Death Chronicles**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The players are survivors in a world ravaged by an unstoppable plague that kills half of all people it touches, transforms society into paranoid chaos, and challenges every certainty about divine justice and human nature. As physicians, clergy, merchants, and ordinary people thrust into extraordinary circumstances, they must navigate quarantined cities, flagellant mobs, collapsing feudal order, and the impossible question of whether this is divine punishment or natural disaster. The campaign explores survival when death is random and total, the breakdown of social order when fear overwhelms reason, and whether humanity's worst or best nature emerges in apocalyptic crisis.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the plague's arrival from the East through trade routes and its initial dismissal as common disease.
    *   Write about medieval medical theory (four humors, miasma) and why physicians' treatments fail completely.
    *   Describe the flagellant movement's theology: plague as divine punishment requiring public penance and blood sacrifice.
    *   Explain the medieval social hierarchy and how plague destroys it by killing rich and poor indiscriminately.
    *   Detail previous plagues in history and why this one is unprecedented in scale and lethality.
    *   Write about the scapegoating of minorities, foreigners, and healers as plague continues despite all responses.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Medical Community** (Major)
        *   **Goals:** To understand, treat, and stop the plague using available knowledge.
        *   **Hierarchy:** Guild-trained physicians, barber-surgeons, apothecaries, wise women.
        *   **Public Agenda:** We can cure this disease with proper treatment and quarantine.
        *   **Secret Agenda:** Most privately know their treatments don't work and survival is random chance.
        *   **Assets:** Medical knowledge (inadequate), protective gear, herbs and remedies, authority.
        *   **Relationships:** Respected initially but increasingly blamed for failure; some accused of witchcraft; trying desperately to maintain credibility.
    *   **The Flagellants** (Major)
        *   **Goals:** To appease God's wrath through public penance, blood sacrifice, and purification.
        *   **Hierarchy:** Charismatic preachers leading penitent followers in organized self-flagellation.
        *   **Public Agenda:** The plague is divine punishment for sin; only blood penance can save us.
        *   **Secret Agenda:** Many use religious authority to gain power, scapegoat enemies, and express violent impulses sanctified by faith.
        *   **Assets:** Popular support, religious authority, mob violence, certainty in chaos.
        *   **Relationships:** Antagonistic toward medical community (dismissing natural causes); leading witch hunts; threatening established Church authority.
    *   **The Feudal Authority** (Minor—Collapsing)
        *   **Goals:** To maintain order, enforce quarantine, and preserve social hierarchy.
        *   **Hierarchy:** Lords, bailiffs, town councils, guild masters rapidly losing authority.
        *   **Public Agenda:** We will maintain law and protect the people.
        *   **Secret Agenda:** Many are fleeing to country estates, hoarding resources, and abandoning responsibilities.
        *   **Assets:** Legal authority (eroding), remaining guards, quarantine powers, confiscation rights.
        *   **Relationships:** Losing legitimacy as they fail to stop plague; resented for quarantine enforcement; increasingly irrelevant.
    *   **The Survivors** (Major—Emerging)
        *   **Goals:** To survive by any means, protect loved ones, make sense of apocalypse.
        *   **Hierarchy:** None—atomized individuals, families, and ad hoc communities.
        *   **Public Agenda:** We're just trying to live.
        *   **Secret Agenda:** Divided between those showing compassion and those turning violent and selfish.
        *   **Assets:** Desperation, adaptability, knowledge of who's infected, mutual aid or violent competition.
        *   **Relationships:** Some form aid networks; others loot and scapegoat; all navigating between helping and self-preservation.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Doctor Morbidus:** Plague physician whose treatments fail but keeps trying.
    *   **Father Castigatus:** Flagellant leader whose extremism masks terror.
    *   **Margot the Wise:** Healer accused of witchcraft for plague's continuation.
    *   **Lord Decimus:** Feudal authority collapsing with social order.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Plague Victim"
    *   "Flagellant Penitent"
    *   "Accused Witch"
    *   "Desperate Family"
    *   "Corrupt Official Hoarding"
    *   "Compassionate Caregiver"
    *   "Grave Digger"
    *   "Paranoid Accuser"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Quarantined Quarter:** Where infected are sealed to die.
        *   **Key Landmarks:** Red-crossed doors, barricaded streets, the sealed gate, abandoned homes.
        *   **Primary Inhabitants:** The dying, desperate caregivers, trapped healthy people, corpse collectors.
        *   **Available Goods & Services:** Death, disease exposure, looted supplies, heartbreaking choices.
        *   **Potential Random Encounters (x5):** Family begging to escape quarantine, corpse collector cart, looters fighting over supplies, survivor caring for dying stranger, plague doctor visit.
        *   **Embedded Plot Hooks & Rumors (x3):** "They sealed healthy people inside with the sick." "The quarantine is to contain us, not protect us." "Everyone inside is already dead."
        *   **Sensory Details:** Sight (Red crosses on every door, bodies visible in windows, emptied streets), Sound (Wailing from within homes, death rattles, silence), Smell (Death, rot, fear).
    *   **The Cathedral:** Where prayer competes with violence.
        *   **Key Landmarks:** Main altar, confession booths, plague chapel, burning square outside.
        *   **Primary Inhabitants:** Desperate faithful, flagellants, accused heretics, overwhelmed clergy.
        *   **Available Goods & Services:** Prayer, confession, sanctuary (sometimes), witch trials, mob justice.
        *   **Potential Random Encounters (x5):** Mass for the dead, flagellant procession, witch accusation, miracle claim, religious riot between factions.
        *   **Embedded Plot Hooks & Rumors (x3):** "God has abandoned us." "The plague is punishment for specific sins." "Burning the accused will make it stop."
        *   **Sensory Details:** Sight (Packed with desperate faithful, bloodstains from flagellants, smoke from burnings), Sound (Prayers, screams, whips), Smell (Incense covering death, blood, terror).
    *   **The Plague House:** Doctor Morbidus's hospital.
        *   **Key Landmarks:** Treatment rooms, isolation wards, failed remedy stores, morgue overflowing.
        *   **Primary Inhabitants:** Plague doctors, dying patients, experimental subjects, overwhelmed staff.
        *   **Available Goods & Services:** Medical treatment (ineffective), plague knowledge, protective gear, body disposal.
        *   **Potential Random Encounters (x5):** Failed treatment attempt, patient dying despite care, doctor's breakdown, experimental remedy trial, body removal.
        *   **Embedded Plot Hooks & Rumors (x3):** "Nothing works—it's random who survives." "The doctors know they're helpless." "Science has failed; only faith remains."
        *   **Sensory Details:** Sight (Bird-masked doctors, buboe-covered victims, bloodletting equipment, bodies), Sound (Labored breathing, medical Latin, death rattles), Smell (Herbs, blood, failure).
    *   **The Mass Graves:** Where the scale becomes undeniable.
        *   **Key Landmarks:** Enormous pits, lime deposits, funeral pyres, overwhelmed grave diggers.
        *   **Primary Inhabitants:** Corpse handlers, clergy conducting mass burials, the dying dumped prematurely.
        *   **Available Goods & Services:** Body disposal, confrontation with mortality, statistical horror.
        *   **Potential Random Encounters (x5):** Accidentally living person in corpse cart, mass burial ceremony, grave diggers' dark humor, noble's family buried with peasants, plague survivor guilt.
        *   **Embedded Plot Hooks & Rumors (x3):** "They're burying people still alive." "Half the city is in those pits." "This is how the world ends."
        *   **Sensory Details:** Sight (Endless bodies, lime powder, smoke from pyres, overwhelmed workers), Sound (Bodies dumping, prayers for the dead, shovels), Smell (Overwhelming death and lime).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** Players help the sick despite exposure risk.
    *   **THEN:** Exposure increases but Compassion tracker stabilizes. Generate aid network formation and reputation as heroes.
    *   **IF:** Players expose corrupt officials hoarding supplies.
    *   **THEN:** Order tracker drops but resources redistribute. Generate riots against hoarding and temporary popular support.
    *   **IF:** Flagellants gain majority support in a district.
    *   **THEN:** Witch hunt begins targeting anyone different. Generate paranoia spiral and accusation scenarios.
    *   **IF:** Players prove plague has natural not divine cause.
    *   **THEN:** Flagellant power weakens but paranoia shifts to new scapegoats. Generate medical authority restoration vs new accusations.
    *   **IF:** Social Breakdown reaches total collapse.
    *   **THEN:** All authority dissolves into violence and hedonism. Generate complete anarchic scenarios and desperate survival.
    *   **IF:** The plague recedes naturally after killing its percentage.
    *   **THEN:** Aftermath and transformation begin. Generate survival guilt, transformed society, new power structures.
    *   **IF:** Players maintained compassion throughout crisis.
    *   **THEN:** Their example influences the emerging world positively. Generate hopeful transformation outcomes.
