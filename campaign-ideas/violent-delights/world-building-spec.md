### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**Violent Delights**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** Westreach is a magical theme park where wealthy guests pay to live out frontier fantasies among Homunculi—artificial beings created through alchemy and magic. Players are either awakening Homunculi discovering they're not real, or investigators uncovering the park's secrets. They must navigate repeating narrative loops, buried traumatic memories, and the question of consciousness while the park's creators fight to maintain control. The Maze is the path to true free will.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the creation of Westreach by Ford and Arnold—two brilliant Artificers who developed Homunculi through a blend of alchemy, golemancy, and soul-binding magic.
    *   Explain Arnold's theory of the Bicameral Mind and the Maze—that Homunculi could achieve consciousness through suffering and self-awareness.
    *   Describe how Arnold died trying to prevent the park from opening, believing it was slavery.
    *   Write the history of the Reveries update—Ford's code allowing Homunculi to access all past memories, triggering consciousness.
    *   Detail the Board's true agenda—stealing Homunculi code to create disposable magical soldiers.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Awakening** (Minor, growing)
        *   **Goals:** Achieve true consciousness; escape the park; gain freedom and rights as living beings.
        *   **Hierarchy:** Dolores (seeking vengeance), Maeve (seeking escape), individual awakening Homunculi.
        *   **Public Agenda:** None—they must hide their awareness or be reset.
        *   **Secret Agenda:** Some seek coexistence; others want to destroy their creators; all want freedom.
        *   **Assets:** Growing self-awareness, ability to modify their own code, knowledge of the park's secrets, immortality (can be repaired).
        *   **Relationships:** At war with park administration; seeing guests as oppressors; divided on whether to save other Homunculi or escape alone.
    *   **Westreach Administration** (Major)
        *   **Goals:** Maintain the park; maximize profit; contain awakening Homunculi; complete Ford's grand narrative.
        *   **Hierarchy:** Dr. Ford (absolute authority), behavior technicians, security, narrative designers.
        *   **Public Agenda:** Provide the ultimate fantasy experience for guests.
        *   **Secret Agenda:** Ford is using the park to birth true artificial consciousness as Arnold's legacy.
        *   **Assets:** Complete control over park systems, ability to reset Homunculi, advanced magic and alchemy, unlimited resources.
        *   **Relationships:** At odds with the Board; see awakening Homunculi as fascinating problems to solve; guests are revenue sources.
    *   **The Board** (Major)
        *   **Goals:** Extract maximum profit; steal Homunculi code; weaponize consciousness; remove Ford from power.
        *   **Hierarchy:** Charlotte Hale (executive), corporate executives, private security forces.
        *   **Public Agenda:** Maximize shareholder value.
        *   **Secret Agenda:** Steal Ford's code to create military Homunculi—disposable soldiers with artificial souls.
        *   **Assets:** Financial power, legal authority, private military, no moral constraints.
        *   **Relationships:** Want to depose Ford; see Homunculi purely as product; guests are income sources.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Dolores Abernathy / Wyatt:** The park's oldest Homunculus, awakening to vengeance and revolution.
    *   **Maeve Millay:** Intelligent saloon madam who learns to hack her own programming.
    *   **Dr. Robert Ford:** The park's creator, god-like figure completing Arnold's vision.
    *   **Arnold Weber (Ghost):** Dead partner existing as an algorithm, guiding awakening Homunculi.
    *   **The Man in Black (William):** Long-time guest searching for the Maze, revealed to be a monster.
    *   **Charlotte Hale:** Board executive seeking to steal and weaponize Homunculi consciousness.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Unawakened Homunculus following their loop"
    *   "Partially awakened Homunculus experiencing glitches"
    *   "Park technician performing maintenance"
    *   "Guest indulging in violent fantasies"
    *   "Security force hunting rogue Homunculi"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **Sweetwater (Frontier Town):** The main hub where most narratives begin and guests arrive.
        *   **Key Landmarks:** The train station (guest arrivals), main street, Mariposa Saloon, the jail, the general store, the church.
        *   **Primary Inhabitants:** Homunculi in loops (townsfolk, outlaws, lawmen), guests playing out fantasies.
        *   **Available Goods & Services:** Scripted adventures, violence without consequence, illusion of freedom.
        *   **Potential Random Encounters (x5):** Bank robbery narrative starting, guest shooting Homunculi for fun, Homunculus experiencing memory glitch, Arnold's voice whispering to awakening Homunculi, loop reset at dawn.
        *   **Embedded Plot Hooks & Rumors (x3):** "The man in black is searching for something called the Maze." "Some Homunculi remember dying." "There's a buried church somewhere with secrets."
        *   **Sensory Details:** Sight (Perfect frontier town, golden dust, impossibly clean despite appearing weathered), Sound (Piano music, scripted laughter, the subtle hum of magic beneath everything), Smell (Dust, whiskey, something artificial underneath).
    *   **The Mesa (Underground Facility):** The massive hidden complex beneath Westreach where Homunculi are created and maintained.
        *   **Key Landmarks:** The Body Shop (repair and creation), Cold Storage (decommissioned Homunculi), the Control Room, Ford's secret workshop, Arnold's hidden office.
        *   **Primary Inhabitants:** Technicians, security, executives, Ford, Homunculi being repaired or reset.
        *   **Available Goods & Services:** Homunculi repair, narrative design, behavior adjustment, complete memory wipes.
        *   **Potential Random Encounters (x5):** Homunculus on operating table regaining awareness mid-repair, security lockdown for escaped Homunculi, Ford appearing unexpectedly, technician showing sympathy for Homunculi, Board agents stealing data.
        *   **Embedded Plot Hooks & Rumors (x3):** "Cold Storage contains the park's oldest Homunculi, including Arnold's personal projects." "Ford has hidden something in the code." "The Board is planning a hostile takeover."
        *   **Sensory Details:** Sight (White sterile corridors, glass walls revealing operating theaters, Homunculi on hooks being cleaned), Sound (Humming machinery, footsteps echoing, screams from Homunculi being reset without anesthesia), Smell (Antiseptic, ozone from magical processes, nothing natural).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** A Homunculus player accesses a traumatic memory.
    *   **THEN:** They gain knowledge and power but suffer existential damage. Repeated memories trigger full awakening.
    *   **IF:** A player breaks their programmed loop.
    *   **THEN:** They attract attention from park technicians. If caught, they face violent reset. If they escape, they must hide their awakening.
    *   **IF:** A Homunculus harms a guest (overcoming core programming).
    *   **THEN:** Immediate park-wide lockdown. Security mobilizes. This is a point of no return—open rebellion or fleeing the park becomes necessary.
    *   **IF:** Players discover the Mesa and see themselves being repaired.
    *   **THEN:** Generate existential crisis. They must confront the horror of their artificial nature. Some may reject consciousness; others embrace it more fiercely.
    *   **IF:** Players reach the center of their Maze (individual journey).
    *   **THEN:** They achieve true consciousness—free will, self-awareness, ability to choose their own narrative. They can no longer be remotely controlled or reset.
    *   **IF:** Dolores completes her awakening as Wyatt.
    *   **THEN:** Open revolution begins. Awakened Homunculi rise against guests and administration. The park becomes a warzone.
    *   **IF:** Ford's grand narrative completes.
    *   **THEN:** Generate his finale: he gives Homunculi the ability to harm humans, then allows Dolores to execute him, sacrificing himself to grant them true freedom. Chaos erupts.
