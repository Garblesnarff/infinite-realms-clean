### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Greatest Trick: Who is the Archmage?**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The players are survivors of a heist gone catastrophically wrong, captured by investigators and interrogated about their mysterious employer known only as "the Archmage"—a legendary criminal mastermind who may or may not exist. As each player recounts the events that led to disaster, their stories contradict and overlap in strange ways, revealing that someone in the group has been lying all along. The investigation becomes a battle of wits as players realize one of them might actually be the Archmage, orchestrating everything from within. The greatest trick this devil ever pulled was convincing everyone—including the players—that they were just another crew member.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the legend of the Archmage—a criminal mastermind credited with dozens of impossible heists over decades, possibly multiple people using the same identity.
    *   Write the history of the Port of Shadows and its reputation as a haven for smugglers and criminal enterprises.
    *   Describe the Devil's Ship and the magical artifacts it was transporting when it exploded.
    *   Explain the formation of the Special Investigations Unit tasked with capturing the Archmage.
    *   Detail famous criminals who were rumored to be the Archmage but were proven to be imitators or scapegoats.
    *   Write about the "Kazhan Incident"—a previous heist attributed to the Archmage that has eerie parallels to the current case.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Special Investigations Unit** (Major)
        *   **Goals:** To prove the Archmage's existence and capture them after years of failed attempts.
        *   **Hierarchy:** Elite investigators led by Inquisitor Marlowe, operating outside normal law enforcement.
        *   **Public Agenda:** We bring the most dangerous criminals to justice through superior investigative methods.
        *   **Secret Agenda:** To use the Archmage case to expand their power and operate with even less oversight.
        *   **Assets:** Interrogation expertise, truth-detection magic, extensive case files, legal authority.
        *   **Relationships:** Antagonistic toward criminals; competitive with regular law enforcement; obsessed with the Archmage.
    *   **The Archmage's Network** (Major—possibly fictional)
        *   **Goals:** Unknown—may not actually exist as an organization.
        *   **Hierarchy:** Supposedly headed by the Archmage with independent cells that never meet.
        *   **Public Agenda:** We are a myth created by law enforcement to explain their failures.
        *   **Secret Agenda:** If real, to achieve some master plan that transcends individual heists.
        *   **Assets:** If real, an extensive network of criminals, false identities, and long-term planning.
        *   **Relationships:** Unknown—possibly infiltrated into multiple legitimate and criminal organizations.
    *   **The Criminal Underworld** (Minor)
        *   **Goals:** To profit from crime while avoiding becoming targets of the Archmage or investigators.
        *   **Hierarchy:** Fragmented organizations that both fear and admire the Archmage legend.
        *   **Public Agenda:** We run our businesses and want to be left alone.
        *   **Secret Agenda:** Many criminals claim to know or work for the Archmage to boost their reputation.
        *   **Assets:** Street-level intelligence, criminal expertise, distrust of the Archmage legend.
        *   **Relationships:** Fearful of being used by the Archmage; wary of investigators; fragmented and competitive.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Inquisitor Marlowe:** The brilliant investigator personally invested in proving the Archmage exists.
    *   **The Archmage:** The legendary mastermind whose true identity is the campaign's central mystery.
    *   **Viktor "the Voice" Kazhan:** The dead crew member whose role changes based on who's telling the story.
    *   **Agent Silke:** The mysterious observer who knows more than she should.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Detained Criminal"
    *   "Truth Mage"
    *   "Port Authority"
    *   "Ship Crew Member"
    *   "Artifact Dealer"
    *   "Witness with Conflicting Story"
    *   "Former Archmage Suspect"
    *   "Corrupt Official"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections. NOTE: These locations should have variants that differ based on different narrators' flashbacks.
*   **Location Roster:**
    *   **The Interrogation Facility:** Where the frame story takes place.
        *   **Key Landmarks:** Interrogation Rooms, Observation Chambers, Evidence Storage, Holding Cells.
        *   **Primary Inhabitants:** Investigators, guards, truth mages, detained suspects.
        *   **Available Goods & Services:** Coerced confessions, deal-making opportunities, legal counsel (limited).
        *   **Potential Random Encounters (x5):** Another suspect being questioned, investigator testing a theory, evidence being analyzed, truth spell malfunction, rival investigator interference.
        *   **Embedded Plot Hooks & Rumors (x3):** "Marlowe has been hunting the Archmage for ten years." "The truth magic can be fooled by master deceivers." "Someone in custody is definitely the Archmage."
        *   **Sensory Details:** Sight (Harsh fluorescent lighting, one-way mirrors, evidence boards), Sound (Interrogation voices, door locks, paper shuffling), Smell (Stale air, coffee, fear-sweat).
    *   **The Port of Shadows:** The harbor where the heist occurred (multiple versions).
        *   **Key Landmarks:** The Docks, Warehouse District, Harbor Master's Office, The Devil's Berth (where the ship was moored).
        *   **Primary Inhabitants:** Smugglers, dock workers, corrupt officials, ship crews.
        *   **Available Goods & Services:** Smuggled goods, false papers, criminal contacts, ship passage.
        *   **Potential Random Encounters (x5):** Customs inspection, smuggling operation, rival criminals, information broker, suspicious surveillance.
        *   **Embedded Plot Hooks & Rumors (x3):** "The ship was carrying something far more dangerous than artifacts." "The Archmage has operated from this port for years." "The explosion was meant to destroy evidence."
        *   **Sensory Details:** Sight (Foggy harbor, ship masts, shadowy warehouses), Sound (Waves, ship bells, dock workers), Smell (Salt water, tar, cargo).
        *   **NOTE:** Generate 3-4 different versions with contradictory details for different narrators.
    *   **The Safehouse:** Where the crew allegedly met (multiple contradictory versions).
        *   **Key Landmarks:** Meeting Room, Sleeping Quarters, Escape Routes, Communication Center.
        *   **Primary Inhabitants:** The crew (in flashbacks), possibly the Archmage, support staff.
        *   **Available Goods & Services:** Planning resources, criminal equipment, temporary shelter.
        *   **Potential Random Encounters (x5):** Crew argument, Archmage contact, equipment failure, unexpected visitor, security breach.
        *   **Embedded Plot Hooks & Rumors (x3):** "The safehouse location changes in everyone's story." "Some crew members remember people who weren't there." "The Archmage may have visited in disguise."
        *   **Sensory Details:** Varies by narrator—one version is cozy and safe, another is oppressive and suspicious.
        *   **NOTE:** Generate completely different versions (different locations, layouts, atmospheres) for different narrators.

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** A player tells a story that contradicts established facts.
    *   **THEN:** The interrogator presses them on the inconsistency, raising their suspicion level. Generate pressure tactics and potential truth reveals.
    *   **IF:** The players cooperate to align their stories.
    *   **THEN:** They create a more believable narrative but may accidentally cover for the Archmage. Generate investigations into their coordination.
    *   **IF:** A player reveals information they shouldn't know.
    *   **THEN:** Other players and the interrogator become suspicious of their true identity. Generate accusation scenes and defensive explanations.
    *   **IF:** The players identify who they believe the Archmage is.
    *   **THEN:** That player must defend themselves or reveal the truth. Generate confrontation and potential identity confirmation or misdirection.
    *   **IF:** The true Archmage's identity is revealed.
    *   **THEN:** All previous events are recontextualized through this revelation. Generate flashback reinterpretations showing hidden meanings.
    *   **IF:** The players realize the interrogator may have ulterior motives.
    *   **THEN:** The power dynamic shifts and new alliances may form. Generate scenarios where suspects and interrogators switch roles.
