### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Endless War Cycle**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The kingdom faces alien Mimic invasion. When the party dies in battle, one member wakes the previous morning with perfect memory—trapped in a time loop. They must die repeatedly, learning from each failure, until they can execute the perfect battle plan. The loop is connected to an Omega Mimic hive mind that can manipulate time. Victory requires breaking the cycle by defeating the Omega while retaining hard-won loop knowledge.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the Mimic invasion—where they came from, why they're here, their biology and capabilities.
    *   Write about the Omega and Alpha Mimics—how they control the hive and manipulate time.
    *   Describe how the time loop works—what triggers reset, what carries over, why only certain individuals maintain memory.
    *   Explain the kingdom's military structure and how they're losing the war against predictive alien enemies.
    *   Detail previous Mimic conflicts on other worlds—this isn't the first time loop war.
    *   Describe the psychological toll of loop warfare and what happens to those who've died too many times.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Kingdom's Army (The Party)** (Major)
        *   **Goals:** Repel the Mimic invasion, protect civilians, defeat the Omega.
        *   **Hierarchy:** Military chain of command with party as special forces unit.
        *   **Public Agenda:** Win the war through conventional military strategy.
        *   **Secret Agenda:** Military leadership doesn't believe the time loop claims; party must work around official orders.
        *   **Assets:** Military training, equipment, manpower, fortifications.
        *   **Relationships:** Defending their homeland; most don't remember the loops; frustrated by party's "impossible" knowledge.
    *   **The Mimic Hive** (Major - Antagonist)
        *   **Goals:** Conquer and consume the kingdom, spread Mimic eggs, serve the Omega.
        *   **Hierarchy:** Omega commands all, Alphas lead sectors, standard Mimics are drones.
        *   **Public Agenda:** None—they're incomprehensible aliens.
        *   **Secret Agenda:** The invasion is a distraction; the real goal is planting eggs beneath the capital.
        *   **Assets:** Overwhelming numbers, predictive hive mind, time manipulation, adaptation to strategies.
        *   **Relationships:** Hunting the loop-aware party specifically; learning from each iteration.
    *   **Military Research Division** (Minor)
        *   **Goals:** Understand the Mimics, develop countermeasures, validate loop theory.
        *   **Hierarchy:** Dr. Carter leads a small team of scientists.
        *   **Public Agenda:** Scientific support for military operations.
        *   **Secret Agenda:** Dr. Carter knows about the loops but can't prove it without party's testimony.
        *   **Assets:** Research data on Mimics, tactical analysis, potential technical solutions.
        *   **Relationships:** Allied with party once convinced; bridge between loop knowledge and military action.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Sergeant Farell:** Gruff veteran who dies heroically in early loops, saved by party knowledge later.
    *   **Doctor Carter:** Brilliant scientist who independently theorized the loop.
    *   **The Omega Mimic:** Hive mind core with time manipulation, remembers all loops.
    *   **The Alpha Mimic:** Time-aware hunter sent to kill the loop-connected party member.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Soldier (Regular forces who reset each loop, may die repeatedly)"
    *   "Mimic Drone (Standard alien units)"
    *   "Officer (Command structure, may need convincing of loop)"
    *   "Civilian (Caught in war, different fates across loops)"
    *   "Elite Mimic (Advanced forms with special abilities)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Beach Landing Zone:** Where the counterattack begins and most loops reset.
        *   **Key Landmarks:** The landing craft positions, Mimic nests in the cliffs, the seawall, the first bunker.
        *   **Primary Inhabitants:** Attacking soldiers, defending Mimics, the same dying faces loop after loop.
        *   **Available Goods & Services:** Military equipment, scavenged Mimic technology.
        *   **Potential Random Encounters (x5):** Same encounters that repeat: specific soldier asking for help, Mimic ambush at specific location, vehicle breakdown at predictable time, NPC heroic sacrifice, hidden Mimic nest.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Mimics seem to know our plans." "Someone claims they've lived this day before." "There's a larger Mimic inland coordinating the defense."
        *   **Sensory Details:** Sight (Gray morning, beach churned by combat, Mimic bodies, endless repetition), Sound (Same explosions, same screams, the variation tells which loop), Smell (Saltwater, blood, alien biochemistry).
    *   **The Capital City:** Urban environment under siege where Omega prepares true invasion.
        *   **Key Landmarks:** The palace, refugee centers, military headquarters, the underground where Omega nests.
        *   **Primary Inhabitants:** Civilians, city guard, infiltrating Mimics, the Omega.
        *   **Available Goods & Services:** Urban resources, strategic positions, access to Omega.
        *   **Potential Random Encounters (x5):** Civilian evacuation, hidden Mimic eggs, resistance fighters, structural collapse, Alpha hunter appearance.
        *   **Embedded Plot Hooks & Rumors (x3):** "Something is growing beneath the city." "The invasion is a distraction." "Time feels wrong here—like we're moving in circles."
        *   **Sensory Details:** Sight (Buildings damaged differently each loop, same faces in different places), Sound (Urban combat, screaming, alien clicks echoing through streets), Smell (Smoke, fear, alien egg chambers).
    *   **The Omega Nest:** Underground chamber where final confrontation occurs.
        *   **Key Landmarks:** The egg chamber, the Omega's core body, temporal distortion zones, escape routes.
        *   **Primary Inhabitants:** The Omega, elite Mimic guards, potentially trapped soldiers from failed loops.
        *   **Available Goods & Services:** Final confrontation, loop breaking, victory or permanent defeat.
        *   **Potential Random Encounters (x5):** All encounters here are deterministic by this point—the party has mapped them through loops.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Omega remembers all loops too." "Killing it might trap you in eternal combat loop." "Someone must die permanently to break the cycle."
        *   **Sensory Details:** Sight (Organic alien architecture, temporal distortions showing multiple loops simultaneously), Sound (Omega's psychic presence, temporal echoes of past loops), Smell (Alien biology, time displacement—no consistent smell).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The party dies in combat.
    *   **THEN:** Reset to morning before the invasion. Generate the disorientation of waking again, tracking accumulated loop trauma.
    *   **IF:** The party kills a standard Mimic they shouldn't have.
    *   **THEN:** Loop breaks temporarily—they're in "real" time. Generate panic and urgency as they race to reconnect to the loop.
    *   **IF:** The party shares loop knowledge with NPCs.
    *   **THEN:** Generate varied reactions: disbelief, horror at implications, some believe through demonstrated predictions.
    *   **IF:** The party uses loop knowledge to save an NPC who normally dies.
    *   **THEN:** That NPC becomes an ally with unique abilities. Generate their gratitude and how they help in the final battle.
    *   **IF:** The party defeats the Alpha Mimic hunter.
    *   **THEN:** They're no longer hunted through time. Generate the relief and increased focus on finding the Omega.
    *   **IF:** In the final battle, the loop-connected character chooses to sacrifice their connection.
    *   **THEN:** Generate the permanent death/transformation that breaks the loop. Victory is assured but at personal cost.
    *   **IF:** The party defeats the Omega without sacrificing the loop connection.
    *   **THEN:** Generate an epilogue where the loop remains dormant but could reactivate. They're marked as time-warriors by the universe.
