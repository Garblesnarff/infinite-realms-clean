### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**Seven Days Remain**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The party discovers a cursed magical scroll that shows viewers a vision of their death—in exactly seven days. This is the manifestation of Sadako Yamamura, a psychic murdered 30 years ago and thrown into a well. The party has one week to investigate her death, uncover the conspiracy behind her murder, retrieve her remains, and properly lay her spirit to rest. Failure means death. The easy solution is passing the curse to someone else, but this creates a moral dilemma: save yourself by dooming an innocent.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail Sadako's life: a girl with powerful psychic abilities (clairvoyance, telekinesis, thought projection) who frightened her community.
    *   Chronicle her murder: 30 years ago, local residents conspired to kill her, throwing her alive into a well where she died slowly over days, her rage and terror creating the curse.
    *   Explain the curse mechanics: those who read/view the cursed scroll see a vision of their death. Seven days later, Sadako manifests and kills them unless the curse is appeased or passed on.
    *   Describe the spread mechanism: creating a copy of the scroll and showing it to someone else transfers the curse to the new victim, saving the original but dooming the new person.
    *   Detail Sadako's spirit nature: a vengeful onryō (Japanese vengeful ghost) who cannot distinguish between the guilty and the cursed, driven only by rage.
    *   Chronicle previous victims and survivors: a chain of deaths and those who saved themselves by passing the curse, creating cycles of guilt.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Cursed (The Players)** (Minor)
        *   **Goals:** Break the curse through investigation and appeasement, or pass it to someone else.
        *   **Hierarchy:** None. United by shared doom.
        *   **Public Agenda:** Investigate Sadako's death and find a solution.
        *   **Secret Agenda:** Each character must grapple with the temptation to pass the curse to save themselves.
        *   **Assets:** Seven days, their investigative skills, potential allies who've researched the curse.
        *   **Relationships:** Allied initially; tested by desperation and temptation; potentially fractured by moral disagreements.
    *   **Sadako's Vengeance** (Major)
        *   **Goals:** Kill those who have seen the cursed image as surrogate revenge for her murder.
        *   **Hierarchy:** Sadako herself; the curse as mechanism; manifestations and omens.
        *   **Public Agenda:** None. The curse spreads impersonally.
        *   **Secret Agenda:** Sadako's spirit cannot be reasoned with unless her remains are found and her story is told/justice is served.
        *   **Assets:** Inevitability, psychic manifestation, ability to appear through reflections and water, unkillable nature as a spirit.
        *   **Relationships:** Hostile to all cursed; indifferent to their guilt or innocence; can only be appeased through specific actions.
    *   **The Conspirators** (Minor - Historical)
        *   **Goals:** Were trying to eliminate Sadako whom they saw as dangerous.
        *   **Hierarchy:** Led by a prominent townsperson; included several witnesses and accomplices.
        *   **Public Agenda:** Protecting the town from a dangerous psychic.
        *   **Secret Agenda:** They murdered a child out of fear and have hidden it for 30 years.
        *   **Assets:** Most are dead. The survivor has knowledge but also guilt and fear.
        *   **Relationships:** All but one are dead; the survivor may help or obstruct depending on approach.
    *   **Previous Victims & Passers** (Minor)
        *   **Goals:** Varied—some sought to break the curse and failed; others passed it on and live with guilt.
        *   **Hierarchy:** None. Disconnected individuals.
        *   **Public Agenda:** Some try to warn others; some hide in shame.
        *   **Secret Agenda:** Those who passed the curse know they condemned innocents. Some try to make amends; others justify their actions.
        *   **Assets:** Knowledge of the curse, research into Sadako, guilt.
        *   **Relationships:** May help or hinder the party; some are dying from the curse right now; some represent cautionary tales.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Sadako Yamamura:** The vengeful spirit, murdered psychic, source of the curse.
    *   **Shizuko Yamamura:** Sadako's elderly mother, knows the truth but fears speaking.
    *   **The Surviving Conspirator:** Elderly townsperson who participated in Sadako's murder, wracked with guilt.
    *   **Reiko Asakawa:** Previous cursed individual who survived by passing the curse, now trying to make amends or continuing the cycle.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Recent Victim" (someone who viewed the scroll and is on their own countdown)
    *   "Curse Researcher" (investigator who studied the phenomenon but may have been cursed in the process)
    *   "Passer of the Curse" (someone who saved themselves by condemning another, guilt-ridden or unrepentant)
    *   "Sadako Manifestation" (ghostly appearance in mirrors, water, emerging from wells)
    *   "Town Elder" (knows about Sadako's murder, may help or obstruct)

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Ancient Library:** Where the cursed scroll was discovered.
        *   **Key Landmarks:** Restricted section, curator's office, records of Sadako's case.
        *   **Primary Inhabitants:** Librarians, researchers, possibly previous cursed individuals researching.
        *   **Available Goods & Services:** Information, historical records, potential clues.
        *   **Potential Random Encounters (x5):** Finding other cursed scrolls, meeting another cursed person, discovering Sadako's childhood records, manifestation of Sadako in reflection, finding previous victims' research notes.
        *   **Embedded Plot Hooks & Rumors (x3):** "The scroll came from the Izu region 30 years ago." "Multiple people who researched Sadako died mysteriously." "There's a way to break the curse but it requires finding her remains."
        *   **Sensory Details:** Sight (Books, scrolls, dim lighting, dust), Sound (Pages turning, whispers, dripping water inexplicably), Smell (Old paper, mildew, occasionally seawater).
    *   **Sadako's Childhood Home:** Abandoned house in Izu.
        *   **Key Landmarks:** Her bedroom (psychic manifestations), mother's room, evidence of psychic activity, photographs.
        *   **Primary Inhabitants:** Shizuko (mother, if still living) or abandoned.
        *   **Available Goods & Services:** Backstory, evidence of Sadako's powers, mother's testimony.
        *   **Potential Random Encounters (x5):** Psychic echoes of Sadako's childhood, the mother's confession, finding Sadako's diary, water inexplicably filling rooms, seeing young Sadako's ghost (non-hostile).
        *   **Embedded Plot Hooks & Rumors (x3):** "Sadako could project thoughts into reality." "She predicted her own death." "The townspeople feared her power."
        *   **Sensory Details:** Sight (Abandoned home, old photographs, water damage), Sound (Creaking, distant child's voice, dripping), Smell (Decay, dampness, age).
    *   **The Well:** Where Sadako was murdered.
        *   **Key Landmarks:** Stone well opening, shaft descending 30 feet, water at bottom, Sadako's remains.
        *   **Primary Inhabitants:** Sadako's corpse (skeletal remains); her spirit is strongest here.
        *   **Available Goods & Services:** The remains (necessary for appeasement), the truth of her final moments.
        *   **Potential Random Encounters (x5):** Sadako crawling up from the well, psychic visions of her murder, the well water rising, finding evidence of her slow death, encountering her at full power.
        *   **Embedded Plot Hooks & Rumors (x3):** "She was thrown in alive and took days to die." "Her rage is strongest at the well." "Retrieving her remains is necessary but incredibly dangerous."
        *   **Sensory Details:** Sight (Stone well, darkness below, suggestion of white bones), Sound (Water echoing, wet breathing, scraping), Smell (Stagnant water, death, cold stone).
    *   **Izu Town:** Where the conspiracy happened and survivors remain.
        *   **Key Landmarks:** Town hall (records), homes of conspirators, local shrine (for burial ritual).
        *   **Primary Inhabitants:** Normal townspeople, the surviving conspirator, elders who remember.
        *   **Available Goods & Services:** Information from witnesses, confession from conspirator, shrine for proper burial.
        *   **Potential Random Encounters (x5):** Meeting the conspirator, discovering town records, resistance from those protecting the secret, Sadako manifestations increasing as truth emerges, finding other cursed individuals.
        *   **Embedded Plot Hooks & Rumors (x3):** "The truth has been hidden for 30 years." "Some townspeople know but won't speak." "Proper burial and confession can appease Sadako."
        *   **Sensory Details:** Sight (Traditional Japanese town, normal but hiding secrets), Sound (Daily life, whispers, rain), Smell (Sea air, rain, incense from shrines).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The party reaches Day 4 (halfway point).
    *   **THEN:** Escalate manifestations. All cursed characters experience vivid nightmares of their death. Sadako appears in reflections more frequently. Water inexplicably appears near them.
    *   **IF:** The party finds Sadako's remains in the well.
    *   **THEN:** Sadako's spirit becomes more active, testing whether they will properly honor her or are just stealing the remains. Generate an encounter where she manifests but pauses, watching their intentions.
    *   **IF:** A party member shows the scroll to someone else (passing the curse).
    *   **THEN:** They are immediately freed from the curse. The new victim is cursed. Generate the moral weight: show the new victim's fear, their countdown beginning. The party must roleplay the guilt or justification.
    *   **IF:** The party achieves all appeasement conditions (remains buried properly, truth told, confession obtained) before Day 7 ends.
    *   **THEN:** Sadako's spirit appears one final time, makes eye contact with each party member, then fades. The curse is broken. Generate a scene of her finding peace.
    *   **IF:** Day 7 ends and the curse is not broken or passed.
    *   **THEN:** Sadako manifests to kill cursed characters. Each experiences their vision coming true: she crawls toward them, emerging from water/screens/wells, unstoppable. Death is inevitable unless someone intervenes with late-stage appeasement.
    *   **IF:** The party partially completes appeasement (e.g., found remains but didn't get confession).
    *   **THEN:** Sadako is weakened but not stopped. Generate a final confrontation where she can be bargained with—perhaps accepting a partial justice or one final sacrifice.
