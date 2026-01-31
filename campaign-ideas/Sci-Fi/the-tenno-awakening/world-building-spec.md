### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Tenno Awakening**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The players are Tenno—ancient warriors awakening from cryosleep, piloting bio-mechanical Warframes. They navigate a war between Corpus, Grineer, and Infested while uncovering the truth: they're children with Void powers controlling living weapons.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts.
*   **Prompts:**
    *   Detail the Orokin Empire's rise and fall, their hubris and advanced biotechnology.
    *   Write the history of the Sentient rebellion and how they destroyed the Orokin.
    *   Describe the creation of Warframes from Infested humans, transformed into controllable weapons.
    *   Explain the Zariman Ten-Zero incident when children gained Void powers.
    *   Detail the formation of the Grineer clone army and their genetic degradation.
    *   Write about the Corpus cult of profit and their robotic proxies.
    *   Describe Transference technology—how consciousness can pilot bodies remotely.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below.
*   **Factions Roster:**
    *   **The Tenno** (Player Faction)
        *   **Goals:** Survival, understanding their nature, maintaining balance.
        *   **Hierarchy:** Guided by Lotus, but operate independently.
        *   **Public Agenda:** Mercenaries for hire, neutral warriors.
        *   **Secret Agenda:** Some seek to escape their weapon-nature; others embrace it.
        *   **Assets:** Warframes, advanced Orokin technology, Void powers.
        *   **Relationships:** Neutral to all factions; feared and desired by everyone.
    *   **The Corpus** (Major)
        *   **Goals:** Profit, technological supremacy, worship the Void as source of wealth.
        *   **Hierarchy:** Led by the Board of Directors, with Alad V as a rogue scientist.
        *   **Public Agenda:** Free market expansion through any means.
        *   **Secret Agenda:** Seek to harvest Tenno powers for profit.
        *   **Assets:** Advanced robotics, energy shields, moa proxies, wealth.
        *   **Relationships:** At war with Grineer; neutral-hostile to Tenno.
    *   **The Grineer Empire** (Major)
        *   **Goals:** Conquest, genetic restoration, domination of Origin System.
        *   **Hierarchy:** Led by the Twin Queens, with generals commanding clone armies.
        *   **Public Agenda:** Strength through unity, glory through conquest.
        *   **Secret Agenda:** Desperately seeking cure for genetic degradation.
        *   **Assets:** Massive clone armies, heavy armor, crude but effective weapons.
        *   **Relationships:** At war with Corpus; hostile to Tenno (want to possess them).
    *   **The Infested** (Major Enemy)
        *   **Goals:** Spread, consume, assimilate all organic life.
        *   **Hierarchy:** Controlled by various Infested intelligences (no central command).
        *   **Public Agenda:** None—they are a plague.
        *   **Secret Agenda:** Some Infested retain fragments of memory, seeking purpose.
        *   **Assets:** Rapid mutation, overwhelming numbers, techno-organic corruption.
        *   **Relationships:** Enemy of all factions; created by Orokin as weapon.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed.
*   **Tier 1 (Unique, Major NPCs):**
    *   **The Lotus / Natah:** Guide to Tenno, secretly a reprogrammed Sentient, maternal but conflicted.
    *   **Teshin:** Ancient Dax warrior, trains Tenno, honorable warrior-philosopher.
    *   **Alad V:** Corpus scientist, charming and ruthless, experiments on Warframes.
    *   **The Grineer Queens:** Twin tyrants, desperate for immortality, cruel and degraded.
    *   **Ordis:** The Tenno's ship AI, cheerful but glitching, hides dark past.
    *   **Hunhow:** Sentient leader, seeks to destroy all Tenno and reclaim Natah.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Corpus Technician"
    *   "Grineer Clone Trooper"
    *   "Infested Mutant"
    *   "Syndicate Operative"
    *   "Orokin Construct"
    *   "Ostron Civilian (Earth settlers)"
    *   "Sentient Scout"
    *   "Fellow Tenno Operative"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below.
*   **Location Roster:**
    *   **The Orbiter (Player Ship):** Personal spacecraft, customizable home base.
        *   **Key Landmarks:** Arsenal (Warframe selection), Foundry (crafting), Quarters, Navigation.
        *   **Primary Inhabitants:** The Tenno, Ordis (ship AI).
        *   **Available Goods & Services:** Crafting, modding, mission selection, customization.
        *   **Potential Random Encounters (x5):** Ordis glitch revelation, transmission interception, surprise inspection, void manifestation, Lotus contact.
        *   **Embedded Plot Hooks & Rumors (x3):** "Ordis's memory banks are corrupted." "Strange signals from the Void." "Lotus hasn't contacted in days."
        *   **Sensory Details:** Sight (sleek corridors, blue lighting, Warframe display), Sound (Ordis's cheerful commentary, ship hum), Smell (sterile air, ozone).
    *   **Lua (Hidden Moon of Earth):** Orokin facility containing Tenno origin secrets.
        *   **Key Landmarks:** The Reservoir (child cryopods), Orokin Halls, The Second Dream chamber.
        *   **Primary Inhabitants:** Orokin constructs, Sentients, dormant systems.
        *   **Available Goods & Services:** Ancient knowledge, Orokin technology, truth.
        *   **Potential Random Encounters (x5):** Sentient patrol, Orokin trial puzzle, memory vision, void storm, awakening child.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Tenno are children, not warriors." "Lua was hidden in the Void during Sentient war." "The Operator sleeps here."
        *   **Sensory Details:** Sight (ivory and gold architecture, impossible angles, childrenin pods), Sound (ancient machinery, whispers, silence), Smell (age, ozone, absence).
    *   **Corpus Ice Planet (Europa):** Industrial mining and research facility.
        *   **Key Landmarks:** Research Labs, Robotics Bays, Vaults, Alad V's laboratory.
        *   **Primary Inhabitants:** Corpus technicians, Moa robots, Crewmen.
        *   **Available Goods & Services:** Technology theft, credit farming, research data.
        *   **Potential Random Encounters (x5):** Robot patrol, security lockdown, sabotage opportunity, profit cult ritual, Zanuka hunter.
        *   **Embedded Plot Hooks & Rumors (x3):** "Alad V is experimenting on captured Warframes." "The Corpus discovered a new Void artifact." "Board of Directors ordered Tenno elimination."
        *   **Sensory Details:** Sight (clean white halls, blue energy, chrome robots), Sound (mechanical footsteps, alarms, humming shields), Smell (ozone, recycled air, cold).
    *   **The Kuva Fortress (Asteroid):** Mobile Grineer Queens' fortress.
        *   **Key Landmarks:** Throne Room, Clone Barracks, Genetic Labs, Kuva Reservoir.
        *   **Primary Inhabitants:** Elite Grineer guards, Kuva Guardians, the Twin Queens.
        *   **Available Goods & Services:** Final confrontation, Kuva harvesting (power resource).
        *   **Potential Random Encounters (x5):** Elite guard patrol, genetic experiment escape, Queen's decree, Kuva ritual, orbital defense activation.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Queens can transfer consciousness." "They seek Tenno bodies for immortality." "Kuva extends life but corrupts."
        *   **Sensory Details:** Sight (industrial red metal, clone vats, deteriorating structures), Sound (marching boots, machinery, Queens' commands), Smell (rust, chemicals, degradation).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes.
*   **Triggers:**
    *   **IF:** The players discover their true nature as Operators (children).
    *   **THEN:** They gain Transference abilities—can possess enemies, exit Warframe. Generate new ability tutorials.
    *   **IF:** The players side with the Corpus in too many missions.
    *   **THEN:** Grineer become extremely hostile. Corpus offer exclusive tech but may betray later.
    *   **IF:** The Lotus disappears (becomes Natah).
    *   **THEN:** Ordis must guide missions. Tenno feel abandoned. Generate search missions.
    *   **IF:** The players defeat the Grineer Queens.
    *   **THEN:** Grineer splinter into warring factions. Generate power vacuum missions.
    *   **IF:** The players ally with Hunhow and the Sentients.
    *   **THEN:** Dark ending—they betray all organic life. Generate Sentient transformation epilogue.
    *   **IF:** The players protect Lotus/Natah's hybrid identity.
    *   **THEN:** She remains their guide, accepting both natures. Generate epilogue of continued balance.
