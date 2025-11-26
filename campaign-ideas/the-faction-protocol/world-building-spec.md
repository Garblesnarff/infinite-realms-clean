### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Faction Protocol**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The players are 16-year-olds who discover they're Divergent—showing aptitude for multiple factions instead of the required single affinity. In a dystopian city divided into five virtue-based factions (Abnegation, Amity, Candor, Dauntless, Erudite), they must hide their true nature during brutal initiation trials while uncovering an Erudite conspiracy to overthrow the government using mind-control serums. Their choices determine whether the faction system is reformed, destroyed, or exposed as a genetic experiment by an outside authority.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the Purity War that preceded the faction system—a conflict over human nature's flaws that nearly destroyed civilization.
    *   Write the history of the Founder's Council that established the five-faction system to isolate and cultivate specific virtues, preventing war.
    *   Describe the creation of the aptitude test and Choosing Ceremony rituals—"faction before blood" as the society's core principle.
    *   Explain why Divergents are dangerous to the system—they cannot be controlled by simulations and represent genetic "purity" that threatens the experiment.
    *   Detail the truth about the city's enclosure—it's a genetic experiment by the Bureau of Genetic Welfare to restore humanity's damaged genome after the Purity War.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **Abnegation (The Selfless)** (Major)
        *   **Goals:** Serve others, govern the city through selflessness, eliminate vanity and greed.
        *   **Hierarchy:** Council of elders led by a head representative (Marcus Eaton), who governs the city.
        *   **Public Agenda:** Provide fair, corruption-free governance and social services.
        *   **Secret Agenda:** Some leaders (like Marcus) hide abusive, hypocritical behavior behind public selflessness.
        *   **Assets:** Control of government, food distribution networks, public trust (until Erudite propaganda undermines it).
        *   **Relationships:** Respected but resented by other factions; targeted by Erudite for overthrow.
    *   **Amity (The Peaceful)** (Major)
        *   **Goals:** Maintain harmony, avoid conflict, cultivate happiness and agriculture.
        *   **Hierarchy:** Council of representatives chosen for their peaceful nature.
        *   **Public Agenda:** Provide food for all factions, mediate disputes, spread joy.
        *   **Secret Agenda:** Use peace serums (mild behavioral drugs) to maintain harmony, suppressing negative emotions.
        *   **Assets:** Farmland outside the city, orchards, peace serums, conflict mediation expertise.
        *   **Relationships:** Neutral in faction conflicts, avoided by Dauntless (seen as weak), valued for food production.
    *   **Candor (The Honest)** (Major)
        *   **Goals:** Uphold truth, serve as legal system, eliminate deception.
        *   **Hierarchy:** Judges and lawyers elected based on honesty and logic.
        *   **Public Agenda:** Provide fair trials, legal representation, truth-telling.
        *   **Secret Agenda:** Use truth serums to extract confessions, sometimes violating privacy for "justice."
        *   **Assets:** Control of legal system, truth serums, investigative expertise.
        *   **Relationships:** Respected but feared (honesty can be brutal); allied with Erudite in valuing logic over emotion.
    *   **Dauntless (The Brave)** (Major)
        *   **Goals:** Protect the city, embody courage, eliminate cowardice.
        *   **Hierarchy:** Leaders chosen through combat trials and fear-conquering, led by Max (secretly allied with Erudite).
        *   **Public Agenda:** Serve as city guards, border patrol, protectors.
        *   **Secret Agenda:** Leadership has been infiltrated by Erudite; used as soldiers in the coup via mind-control serums.
        *   **Assets:** Combat training, weapons, the Dauntless compound, patrol infrastructure.
        *   **Relationships:** Respect strength, disdain weakness; manipulated by Erudite; divided internally between honorable and corrupt leaders.
    *   **Erudite (The Intelligent)** (Major - Antagonist)
        *   **Goals:** Pursue knowledge, govern through intelligence, eliminate ignorance.
        *   **Hierarchy:** Led by Jeanine Matthews (brilliant, ruthless scientist), with councils of researchers and intellectuals.
        *   **Public Agenda:** Provide technology, education, research, and innovation.
        *   **Secret Agenda:** Overthrow Abnegation using propaganda and mind-control serums; eliminate Divergents (who threaten their control); discover the city's true purpose.
        *   **Assets:** Advanced technology, serums (fear, truth, mind-control, Divergent-detection), libraries, propaganda networks.
        *   **Relationships:** Resent Abnegation's political power; allied with corrupt Dauntless leaders; see other factions as inferior.
    *   **Factionless (The Outcasts)** (Minor - Emerging)
        *   **Goals:** Survive; secretly plot to abolish the faction system.
        *   **Hierarchy:** Led by Evelyn Johnson-Eaton (Four's mother), organized into work crews and resistance cells.
        *   **Public Agenda:** None—they're invisible outcasts doing menial labor.
        *   **Secret Agenda:** Ally with Divergents and rebels to destroy the faction system entirely, creating egalitarian society.
        *   **Assets:** Numbers (all failed initiates and exiles), knowledge of hidden city infrastructure, desperation that fuels courage.
        *   **Relationships:** Despised by all factions; secretly recruited by Evelyn for revolution; sympathetic to Divergents.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Jeanine Matthews:** Erudite leader, brilliant and ruthless, orchestrates the coup to seize control and eliminate Divergents, knows the city is an experiment.
    *   **Tris Prior:** Divergent transfer from Abnegation to Dauntless, brave and stubborn, becomes the party's ally, lost family in the coup.
    *   **Four (Tobias Eaton):** Divergent Dauntless instructor, son of abusive Marcus, protective of other Divergents, conflicted about his factionless mother Evelyn.
    *   **Marcus Eaton:** Abnegation leader, publicly selfless but privately abusive, his corruption validates Erudite's propaganda.
    *   **Evelyn Johnson-Eaton:** Factionless leader, Four's mother, charismatic revolutionary seeking to abolish factions entirely.
    *   **Eric Coulter:** Brutal Dauntless leader, allied with Erudite, enforces ruthless initiation standards, antagonist to the party.
    *   **Caleb Prior:** Tris's brother, transfers to Erudite, becomes complicit in Jeanine's conspiracy (represents betrayal of family for faction).
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Dauntless Initiate (Brave, competitive, struggling with fear trials)"
    *   "Erudite Researcher (Intellectual, logical, morally flexible in pursuit of knowledge)"
    *   "Abnegation Servant (Humble, selfless, potentially hiding family secrets)"
    *   "Amity Peacekeeper (Warm, conflict-averse, possibly drugged on peace serum)"
    *   "Candor Lawyer (Brutally honest, black-and-white thinker)"
    *   "Factionless Worker (Bitter outcast, desperate for change)"
    *   "Divergent in Hiding (Multifaceted individual faking conformity)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Hub (Choosing Ceremony Plaza):**
        *   **Key Landmarks:** Five faction bowls (stones, earth, glass, coals, water), the ceremonial knife, faction seating sections, the central platform.
        *   **Primary Inhabitants:** All factions gather here once per year for the Choosing Ceremony.
        *   **Available Goods & Services:** None—purely ceremonial space.
        *   **Potential Random Encounters (x5):** N/A—only used during the ceremony (Session 2).
        *   **Embedded Plot Hooks & Rumors (x3):** "Choosing your birth faction is safest." "Transfers rarely survive initiation." "Divergents are executed if discovered."
        *   **Sensory Details:** Sight (Massive circular plaza, five colored sections, thousands in faction clothing), Sound (Murmured prayers, names called, knife cutting flesh, blood dripping), Smell (Incense, nervous sweat, stone dust).
    *   **Dauntless Compound (The Pit):**
        *   **Key Landmarks:** The Pit (central cavern), the Chasm (deadly ravine), training rooms, dining hall, dormitories, the fear landscape chamber.
        *   **Primary Inhabitants:** Dauntless members, initiates, instructors (Four, Eric).
        *   **Available Goods & Services:** Combat training, weapons, Dauntless initiation trials, meals.
        *   **Potential Random Encounters (x5):** A brutal fight between initiates, Four secretly helping a Divergent, Eric enforcing cruel punishment, a daredevil jumping across the Chasm, Dauntless-born mocking transfers.
        *   **Embedded Plot Hooks & Rumors (x3):** "Eric is stricter than usual—someone's pressuring him." "The fear serum has been modified recently." "Some initiates never wake up from simulations."
        *   **Sensory Details:** Sight (Dark cavern, industrial lights, black-clad warriors, the Chasm's rushing water), Sound (Shouts, fists on punching bags, water roaring, footsteps on metal), Smell (Sweat, leather, dampness from the Chasm).
    *   **Erudite Headquarters:**
        *   **Key Landmarks:** The central library (glass atrium filled with books and tablets), research laboratories (where serums are developed), Jeanine's office (overlooking the city), the simulation control center.
        *   **Primary Inhabitants:** Erudite members, researchers, Jeanine Matthews, security personnel.
        *   **Available Goods & Services:** Books, research materials, serum development, propaganda publication.
        *   **Potential Random Encounters (x5):** A researcher working late on serum formulas, security testing a new Divergent-detection device, Jeanine delivering a speech, a locked lab with suspicious experiments, a propaganda broadcast being recorded.
        *   **Embedded Plot Hooks & Rumors (x3):** "Jeanine is obsessed with Divergents—she's developing a serum to identify and kill them." "Erudite is secretly meeting with Dauntless leaders." "The propaganda against Abnegation is based on half-truths."
        *   **Sensory Details:** Sight (Blue-lit glass buildings, rows of books and screens, white lab coats), Sound (Keyboard typing, whispered discussions, hum of technology), Smell (Paper, antiseptic, coffee, ozone from electronics).
    *   **Abnegation Sector:**
        *   **Key Landmarks:** Rows of identical gray houses, communal kitchens, the government building, Marcus's home (secretly hiding his abuse).
        *   **Primary Inhabitants:** Abnegation members (the selfless), government workers, Tris's family (before the coup).
        *   **Available Goods & Services:** Simple food, basic clothing, government services, selfless aid to factionless.
        *   **Potential Random Encounters (x5):** An Abnegation member serving food to factionless, children being taught selflessness, a quiet family dinner (no mirrors, no vanity), Marcus publicly perfect but privately threatening, whispers about Erudite accusations.
        *   **Embedded Plot Hooks & Rumors (x3):** "Marcus isn't what he seems—his son left for a reason." "Erudite's accusations aren't entirely false." "Abnegation leaders are meeting in secret about the propaganda."
        *   **Sensory Details:** Sight (All gray—houses, clothing, streets; no decoration, no mirrors), Sound (Quiet conversations, prayer before meals, footsteps on stone), Smell (Simple bread, plain soap, clean but unscented air).
    *   **The Fence (City Boundary):**
        *   **Key Landmarks:** The massive fence surrounding the city (supposedly for protection), guard posts (Dauntless patrol), the gate (always locked).
        *   **Primary Inhabitants:** Dauntless guards, occasional Amity farmers working nearby fields.
        *   **Available Goods & Services:** None—forbidden area for most citizens.
        *   **Potential Random Encounters (x5):** A Dauntless guard on patrol, a factionless person sneaking close (curious about the outside), Amity workers tending crops, a section of fence showing signs of age/weakness, a locked gate with mysterious symbols.
        *   **Embedded Plot Hooks & Rumors (x3):** "No one knows what's beyond the fence—it's been closed since before the factions." "Some Dauntless guards have disappeared near the fence." "The fence isn't for keeping threats out—it's for keeping us in."
        *   **Sensory Details:** Sight (Tall metal fence stretching endlessly, guard towers, farmland beyond), Sound (Wind, electric hum from the fence, distant guard radios), Smell (Grass, earth, ozone from electric fence).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The party chooses different factions during the Choosing Ceremony.
    *   **THEN:** Generate separate initiation storylines for each faction. Party members must communicate secretly to share information. This increases investigation difficulty but provides more faction perspectives.
    *   **IF:** The party reveals their Divergence to faction leadership.
    *   **THEN:** Generate immediate execution attempts or imprisonment. The party must escape and join the factionless or live as fugitives. Trust with that faction drops to zero.
    *   **IF:** The party fails initiation rankings.
    *   **THEN:** Generate factionless storyline—they're outcasts but encounter Evelyn and learn about the rebellion. They gain factionless allies but lose faction resources.
    *   **IF:** The party successfully fakes conformity during fear simulations.
    *   **THEN:** Generate continued cover—instructors remain unaware of Divergence. The party can gather information from within factions but lives under constant risk of discovery.
    *   **IF:** The party is present but inactive during the simulation attack (Session 9).
    *   **THEN:** Generate mass casualties in Abnegation—including potential allies and innocent families. The party's guilt affects future choices. The coup succeeds more thoroughly.
    *   **IF:** The party destroys the simulation control center early.
    *   **THEN:** Generate Dauntless freedom but Jeanine's escape with critical data. She activates contingency plans (Divergent-hunting squads, faction lockdowns). The conspiracy goes underground.
    *   **IF:** The party publicly reveals they're Divergent during the faction summit (Session 12).
    *   **THEN:** Generate polarized reactions—some factions demand execution, others see them as proof the system is flawed. This galvanizes the debate about the faction system's future.
    *   **IF:** The party sides with Evelyn and the factionless.
    *   **THEN:** Generate a violent revolution where factions are forcibly abolished. Society descends into temporary chaos. The party must decide if egalitarian anarchy is better than structured oppression.
    *   **IF:** The party discovers and reveals the truth about the city being an experiment.
    *   **THEN:** Generate mass existential crisis—the faction system is revealed as artificial, citizens question their identities. The outside world (Bureau of Genetic Welfare) makes contact, offering integration or continued isolation.
    *   **IF:** The party kills or imprisons Jeanine before she can reveal the experiment's truth.
    *   **THEN:** Generate a secret that dies with her—the party never learns why the city exists. The faction system continues, reformed but still based on a lie. Future generations may rediscover the truth.
