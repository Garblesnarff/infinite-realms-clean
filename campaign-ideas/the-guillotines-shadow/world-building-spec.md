### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Guillotine's Shadow**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The players are revolutionaries who helped overthrow a corrupt monarchy in the name of "liberté, égalité, fraternité," only to watch their movement devour itself during the Reign of Terror when yesterday's heroes become today's enemies of the Revolution. As activists, politicians, soldiers, and idealists, they must navigate the impossible contradiction between revolutionary ideals and revolutionary violence, choosing whether to feed the guillotine, become its victims, or somehow stop the terror they helped create. The campaign explores how noble revolutions turn bloody, the horror of purity testing run amok, and whether anything justifies the Terror.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the ancien régime's inequality that justified revolution—aristocratic excess contrasted with popular suffering.
    *   Write about Enlightenment ideals inspiring the Revolution: liberty, equality, fraternity, reason, popular sovereignty.
    *   Describe the Revolution's escalation: from moderate reform to radical transformation to the Terror.
    *   Explain the Revolutionary Tribunal system and how denunciation became weapon and duty.
    *   Detail the Committee of Public Safety's emergency powers and Robespierre's ideology of Virtue through Terror.
    *   Write about the Revolutionary Calendar, Festival of Reason, and attempts to completely transform society and time itself.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Radicals (Montagnards)** (Major)
        *   **Goals:** To completely transform France, purge counter-revolutionaries, and enforce revolutionary virtue through terror if necessary.
        *   **Hierarchy:** Committee of Public Safety, Revolutionary Tribunal, radical clubs, sans-culotte enforcers.
        *   **Public Agenda:** We are saving the Revolution from internal enemies through necessary vigilance.
        *   **Secret Agenda:** Many use ideological purity as excuse for political power and settling scores.
        *   **Assets:** Control of Committee, guillotine, popular support, ideological certainty, emergency powers.
        *   **Relationships:** Purging Moderates as counter-revolutionary sympathizers; suspicious of everyone; competing internally for revolutionary purity.
    *   **The Moderates (Girondins)** (Major—Being Purged)
        *   **Goals:** To preserve Revolutionary ideals while limiting violence and maintaining some traditional structures.
        *   **Hierarchy:** Convention delegates, provincial leaders, moderate clubs.
        *   **Public Agenda:** We support the Revolution but oppose unnecessary bloodshed.
        *   **Secret Agenda:** Many are terrified and either fleeing or making desperate compromises to survive.
        *   **Assets:** Moral arguments, provincial support, former revolutionary credentials.
        *   **Relationships:** Being systematically arrested and executed by Radicals; desperate to stop the Terror; losing badly.
    *   **The Sans-Culottes** (Major—Popular Base)
        *   **Goals:** To achieve genuine equality, redistribute wealth, and ensure the Revolution serves working people.
        *   **Hierarchy:** Neighborhood councils, revolutionary clubs, popular societies without formal structure.
        *   **Public Agenda:** We are the true Revolution—the voice of the people.
        *   **Secret Agenda:** Divided between genuine idealists and those using revolution for mob violence and looting.
        *   **Assets:** Numbers, street power, popular legitimacy, revolutionary passion.
        *   **Relationships:** Support Radicals initially but increasingly uneasy with Terror; manipulated by leaders; suffering from economic crisis.
    *   **The Opportunists** (Minor)
        *   **Goals:** To survive and gain power by appearing maximally revolutionary.
        *   **Hierarchy:** Individual politicians, Committee members, denunciators using system for personal gain.
        *   **Public Agenda:** We are loyal revolutionaries rooting out enemies.
        *   **Secret Agenda:** Cynically using Terror to eliminate rivals and advance themselves.
        *   **Assets:** Manipulation skills, willingness to betray anyone, knowledge of revolutionary rhetoric.
        *   **Relationships:** Pretending to be radical while planning to survive any outcome; creating denunciations; positioning for post-Terror power.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Citizen Robespierre:** The incorruptible radical who believes terror purifies the Revolution.
    *   **Citizeness Lucille:** The moderate voice courageously opposing the Terror.
    *   **Citizen Fouché:** The opportunist using ideology for power.
    *   **The Sans-Culotte Jacques:** The true believer whose family was guillotined but still defends the cause.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Committee Member"
    *   "Revolutionary Orator"
    *   "Denouncer"
    *   "Accused Counter-Revolutionary"
    *   "Sans-Culotte Militant"
    *   "Moderate Trying to Survive"
    *   "Execution Victim"
    *   "Tribunal Judge"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Place de la Révolution:** Where the guillotine and daily executions occur.
        *   **Key Landmarks:** The Guillotine (center), Execution Platform, Crowd Viewing Areas, Tumbril Arrival Point.
        *   **Primary Inhabitants:** Executioners, crowd spectators (tricoteuses), guards, condemned arriving.
        *   **Available Goods & Services:** Public executions as spectacle, revolutionary demonstration, denunciation opportunities.
        *   **Potential Random Encounters (x5):** Daily execution schedule, crowd cheering or silent, someone you know being executed, revolutionary speech during execution, execution going wrong.
        *   **Embedded Plot Hooks & Rumors (x3):** "Tomorrow's list has fifty names." "They're executing children now." "The Terror will never end."
        *   **Sensory Details:** Sight (Guillotine dominating, tricolor everywhere, crowds in liberty caps, blood being washed away), Sound (Blade falling, crowds reacting, death drums, revolutionary songs), Smell (Blood, fear, crowd sweat).
    *   **The National Convention:** Where revolutionaries debate and denounce.
        *   **Key Landmarks:** Speaker's Platform, Montagnard Section (high seats), Moderate Section (being emptied), Galleries.
        *   **Primary Inhabitants:** Convention delegates, Committee members, observers, guards ready to arrest.
        *   **Available Goods & Services:** Political debate, denunciation, voting on life and death, revolutionary legislation.
        *   **Potential Random Encounters (x5):** Passionate revolutionary speech, denunciation from the floor, vote on execution, political maneuvering, arrest during session.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Moderates are being purged one by one." "Every speech could be your last." "The Committee has complete power."
        *   **Sensory Details:** Sight (Packed galleries, tricolor displays, empty Moderate seats, Committee members watching), Sound (Passionate speeches, accusations, galleries responding, arrest orders), Smell (Tension, fear, revolutionary fervor).
    *   **The Conciergerie:** Prison for the accused awaiting trial.
        *   **Key Landmarks:** Cells, Interrogation Rooms, Chapel (repurposed), Courtyard, Departure Point for Tumbrils.
        *   **Primary Inhabitants:** The accused (aristocrats, moderates, radicals, anyone), guards, interrogators.
        *   **Available Goods & Services:** Final meetings with accused, interrogation, bribery attempts, last letters.
        *   **Potential Random Encounters (x5):** Former ally imprisoned, dignified prisoner, breakdown, futile escape attempt, final goodbyes.
        *   **Embedded Plot Hooks & Rumors (x3):** "Everyone here dies—the trial is theater." "They arrested her for insufficient enthusiasm." "Some prisoners are already dead but don't know it."
        *   **Sensory Details:** Sight (Crowded cells, diverse prisoners, Revolutionary symbols on walls, carts arriving), Sound (Whispers, crying, revolutionary songs ironically, names being called for trial), Smell (Confinement, despair, the scent of too many people).
    *   **The Streets of Paris:** Where revolution and terror mix daily.
        *   **Key Landmarks:** Revolutionary Clubs, Bread Lines, Defaced Churches, Renamed Streets.
        *   **Primary Inhabitants:** Sans-culottes, denouncers, Committee agents, desperate citizens, revolutionary enthusiasts.
        *   **Available Goods & Services:** Revolutionary fervor, denunciation, bread (scarce), political education, survival.
        *   **Potential Random Encounters (x5):** Revolutionary festival, bread riot, denunciation scene, checkpoint demanding virtue papers, midnight arrest.
        *   **Embedded Plot Hooks & Rumors (x3):** "They arrested an entire neighborhood for one person's words." "Revolutionary Virtue can't buy bread." "Everyone informs on everyone."
        *   **Sensory Details:** Sight (Tricolor everywhere, revolutionary slogans, crowds in liberty caps, suspicion), Sound (Revolutionary songs, denunciations, political discussions, marching), Smell (Bread baking but scarce, fear, revolutionary possibility).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** Players support the king's execution.
    *   **THEN:** Radicals trust them more but moderates fear them. Generate radicalization path and moderate alienation.
    *   **IF:** Players speak against the Terror publicly.
    *   **THEN:** They are denounced and must defend themselves or flee. Generate tribunal trial and survival scenarios.
    *   **IF:** Players denounce someone to save themselves.
    *   **THEN:** Revolutionary Virtue increases but moral weight accumulates. Generate guilt and opportunist path scenarios.
    *   **IF:** Players successfully save someone from the guillotine.
    *   **THEN:** Temporary victory but increased scrutiny on them. Generate heroic moment and dangerous suspicion.
    *   **IF:** Moderate faction is completely purged.
    *   **THEN:** Radicals begin purging each other for insufficient radicalism. Generate accelerating Terror and ideological competition.
    *   **IF:** Players join the Thermidorian Reaction against Robespierre.
    *   **THEN:** The Terror ends but revolutionary ideals are compromised. Generate moral complexity of ending Terror through Terror.
    *   **IF:** Players maintained moral integrity throughout.
    *   **THEN:** Epilogue shows their example influenced Revolutionary legacy positively. Generate hope despite horror outcomes.
