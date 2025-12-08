### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Ink Revolution**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The party finds themselves in a medieval world where books are incredibly rare—only nobles and wealthy clergy can afford them, and commoners are largely illiterate. A party member (or companion) with modern knowledge becomes obsessed with making books accessible through papermaking, printing, and literacy programs. The campaign follows their efforts to revolutionize society while navigating guild politics, noble intrigue, and religious opposition from those profiting from knowledge scarcity.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the history of the Guild System in Ehrenfest, which controls all crafts and trades through monopolies and regulations.
    *   Write about the Church of the Divine and its control over religious knowledge, using limited book access to maintain authority.
    *   Describe the current economic system where books are luxury items costing months of wages, created by highly skilled scribes.
    *   Explain the class structure: nobles (literate, control knowledge), merchants (some literacy, controlled by guilds), commoners (mostly illiterate, dependent on oral tradition).
    *   Detail past attempts at educational reform that were suppressed by conservative factions.
    *   Write about the "Age of Illumination" centuries ago when more books existed, before economic collapse made them rare again.
    *   Describe how the Scribes' Guild maintains its monopoly through strict apprenticeship systems and quality standards.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Party's Publishing Company** (Major)
        *   **Goals:** Make books affordable and accessible, establish public libraries, spread literacy among commoners.
        *   **Hierarchy:** The party as founders and innovators, with growing employee base of apprentices and supporters.
        *   **Public Agenda:** Provide quality reading materials at affordable prices.
        *   **Secret Agenda:** Fundamentally disrupt the power structure by democratizing knowledge.
        *   **Assets:** Innovative production techniques, growing workshop, noble patronage, passionate believers.
        *   **Relationships:** Supported by progressive nobles and common people; opposed by Scribes' Guild and conservative clergy; tolerated by Merchants' Guild if profitable.
    *   **The Scribes' Guild** (Major)
        *   **Goals:** Protect traditional craftsmanship, maintain quality standards, preserve members' livelihoods.
        *   **Hierarchy:** Guildmaster Helmut at top, with master scribes, journeymen, and apprentices.
        *   **Public Agenda:** Ensure the quality and sanctity of written words.
        *   **Secret Agenda:** Maintain profitable monopoly on book production regardless of social cost.
        *   **Assets:** Legal monopoly (initially), skilled craftspeople, guild hall, political connections.
        *   **Relationships:** At war with the party; allied with conservative clergy; wary of Merchants' Guild.
    *   **The Church of the Divine** (Major)
        *   **Goals:** Spread the faith, maintain moral authority, guide the people.
        *   **Hierarchy:** High Priest at top, bishops, priests, and clergy beneath.
        *   **Public Agenda:** Serve the divine and shepherd souls.
        *   **Secret Agenda:** Split between conservatives (maintain knowledge monopoly) and progressives (spread the faith widely).
        *   **Assets:** Massive wealth, political influence, the only semi-public library, religious authority.
        *   **Relationships:** Split internally over the party; conservatives oppose, progressives secretly support.
    *   **The Merchants' Guild** (Major)
        *   **Goals:** Regulate trade, maximize profit, maintain economic stability.
        *   **Hierarchy:** Guild council led by senior merchants, with various trade-specific sub-guilds.
        *   **Public Agenda:** Ensure fair trade and quality goods.
        *   **Secret Agenda:** Profit above all; will support whoever makes them money.
        *   **Assets:** Control of trade licenses, market spaces, economic intelligence network.
        *   **Relationships:** Neutral pragmatists who support the party once they prove profitable; enemies with anyone who threatens market stability.
    *   **The Noble Houses** (Minor)
        *   **Goals:** Maintain power, increase prestige, protect class privileges.
        *   **Hierarchy:** Lord Ferdinand at top, with noble families competing for influence.
        *   **Public Agenda:** Govern justly and uphold tradition.
        *   **Secret Agenda:** Split between progressives (Lady Rozemyne's faction) who see literacy as progress and conservatives who fear empowered commoners.
        *   **Assets:** Political power, wealth, military force, legal authority.
        *   **Relationships:** Split on the party; some see opportunity, others see threat to class structure.
    *   **The Common People** (Minor)
        *   **Goals:** Survive, prosper, improve their children's lives.
        *   **Hierarchy:** No formal hierarchy—families, neighborhoods, craft communities.
        *   **Public Agenda:** Work hard and follow the rules.
        *   **Secret Agenda:** Many hunger for knowledge and opportunity currently denied by class restrictions.
        *   **Assets:** Labor, community solidarity, growing literacy.
        *   **Relationships:** Strongly support the party; grateful for educational opportunities; beginning to question class restrictions.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Myne (Optional Companion):** Frail reincarnator obsessed with books, brilliant innovator, driven to the point of mania. May have "the Devouring" illness.
    *   **Benno:** Shrewd merchant patron who recognizes profit in innovation. Fair but calculating.
    *   **Lady Rozemyne:** Noble bibliophile and party's high-status protector. Intelligent and constrained by expectations.
    *   **Guildmaster Helmut:** Scribes' Guild leader, conservative but not evil. Can potentially be won over.
    *   **High Priest Bezewanst:** Conservative church leader opposing democratization. Secretly corrupt.
    *   **Bishop Ferdinand:** Progressive priest who supports spreading faith through literacy. Noble bastard who values merit.
    *   **Lutz:** Enthusiastic apprentice, first true believer from common class. Represents beneficiaries of literacy.
    *   **Lord Ferdinand:** City ruler who cares about prosperity and prestige. Pragmatic politician.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Traditional Master Scribe" (skilled, proud, feeling threatened)
    *   "Curious Apprentice" (eager to learn new techniques)
    *   "Conservative Priest" (fears loss of control)
    *   "Progressive Clergy" (excited about spreading the faith)
    *   "Pragmatic Merchant" (will support if profitable)
    *   "Grateful Commoner Parent" (wants education for children)
    *   "Opportunistic Noble" (sees political advantage)
    *   "Workshop Employee" (loyal to party's vision)

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **Ehrenfest - The Merchant City:** Major medieval trade city, class-segregated.
        *   **Key Landmarks:** The Noble Quarter (hilltop), Cathedral of the Divine (center), Merchants' Guild Hall (market district), Scribes' Quarter (traditional district), The Party's Workshop (evolving location), Market Square.
        *   **Primary Inhabitants:** Nobles (5%), merchants and craftspeople (20%), common laborers (75%).
        *   **Available Goods & Services:** All standard medieval goods and services, but books are extremely expensive. Literacy services (scribes) are costly.
        *   **Potential Random Encounters (x5):** Market day bustle and deals, Guild inspector checking licenses, Noble procession, Street performer or town crier (oral tradition), Request for literacy help.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Scribes' Guild is planning something against the new papermakers." "A noble lady is secretly learning to read." "The church library has books from the Age of Illumination."
        *   **Sensory Details:** Sight (Class-divided architecture, busy markets, few written signs), Sound (Town criers, merchants hawking, church bells, craft noises), Smell (Market foods, craft materials, city life), Touch (Cobblestones, class segregation in public spaces, weight of books).
    *   **The Party's Workshop:** The evolving heart of operations.
        *   **Key Landmarks:** Papermaking area (wet and drying), Ink production corner, Printing press (once installed), Binding station, Storage for materials and finished goods.
        *   **Primary Inhabitants:** The party, growing number of apprentices and employees.
        *   **Available Goods & Services:** Paper production, printing services (later), employment, education in new techniques.
        *   **Potential Random Encounters (x5):** Experiment success or failure, Employee training moment, Material delivery, Suspicious inspector visit, Customer inquiry or order.
        *   **Embedded Plot Hooks & Rumors (x3):** "We need more space to scale up." "Someone is stealing our techniques." "An employee wants to form a union."
        *   **Sensory Details:** Sight (Works in progress, organized chaos, evolution from simple to complex), Sound (Craft noises, pressing, water, conversation and teaching), Smell (Paper pulp, ink, wood, creativity), Touch (Texture of papers, coolness of wet pulp, satisfaction of smooth print).
    *   **The Merchants' Guild Hall:** Center of economic power.
        *   **Key Landmarks:** Grand Council Chamber, License Office, Market Regulation Board, Trade Courts, Archive of Contracts.
        *   **Primary Inhabitants:** Guild officers, merchants conducting business, apprentices learning trade.
        *   **Available Goods & Services:** Business licenses, arbitration services, market stall rentals, trade information.
        *   **Potential Random Encounters (x5):** Negotiation over fees, Dispute arbitration, New business presentation, Political maneuvering, Merchant gossip network.
        *   **Embedded Plot Hooks & Rumors (x3):** "The guild is considering a new craft category for printing." "Some merchants see profit in literacy." "Old families resist new money."
        *   **Sensory Details:** Sight (Wealthy but practical, ledgers everywhere, measuring tools), Sound (Negotiations, coin counting, formal proceedings), Smell (Ink, parchment, wealth), Touch (Fine materials, weight of coins, pressure of business).
    *   **The Cathedral of the Divine:** Religious and knowledge center.
        *   **Key Landmarks:** Main sanctuary, The Restricted Library, High Priest's chambers, School for Noble Children, Scriptorum (where religious texts are copied).
        *   **Primary Inhabitants:** Clergy at all levels, noble students, scribes working on sacred texts.
        *   **Available Goods & Services:** Religious services, limited education (for nobles), sacred text copies (expensive).
        *   **Potential Random Encounters (x5):** Religious service, Theological debate, School session, Library access request (usually denied), Priestly politics.
        *   **Embedded Plot Hooks & Rumors (x3):** "The library has books that contradict church teaching." "Young priests are curious about printing." "The High Priest fears losing control."
        *   **Sensory Details:** Sight (Grand architecture, illuminated manuscripts, class divide in seating), Sound (Prayers, chants, whispered theology, scratching of scribes' pens), Smell (Incense, old books, candle wax), Touch (Sacred atmosphere, knowledge kept out of reach, weight of tradition).
    *   **The Scribes' Quarter:** Traditional book production district.
        *   **Key Landmarks:** Guild Hall, Master scribes' workshops, Parchment suppliers, Illumination studios, Binding shops.
        *   **Primary Inhabitants:** Scribes at all skill levels, parchment makers, illuminators, binders.
        *   **Available Goods & Services:** Custom book copying (very expensive), parchment sales, illustration services.
        *   **Potential Random Encounters (x5):** Master scribe at work (impressive skill), Apprentice running errands, Quality inspection, Delivery of expensive commission, Worried discussion about competition.
        *   **Embedded Plot Hooks & Rumors (x3):** "Some young scribes are curious about printing." "Old masters see only threat, not opportunity." "The guild has hired thugs before to deal with competition."
        *   **Sensory Details:** Sight (Beautiful calligraphy, illuminated pages, skilled craftsmanship), Sound (Scratching of many pens, soft conversations, careful concentration), Smell (Ink, parchment, binding glue, old tradition), Touch (Pride in craft, fear of obsolescence, texture of parchment).
    *   **The People's Library (Endgame):** The party's ultimate creation.
        *   **Key Landmarks:** Grand Reading Room, Children's Section, Lending Office, Classroom Wings, The Printing Press Display.
        *   **Primary Inhabitants:** Librarians, teachers, students of all ages, visitors from all classes.
        *   **Available Goods & Services:** Free book lending, literacy classes, quiet study space, copying services.
        *   **Potential Random Encounters (x5):** Child reading first book, Common elder learning to read, Scholar researching, Grateful parent thanking party, Noble visitor surprised by quality.
        *   **Embedded Plot Hooks & Rumors (x3):** "Other cities want libraries now." "This is changing everything." "The party should be in the history books."
        *   **Sensory Details:** Sight (Books accessible to all, people of all classes reading together, light streaming through windows), Sound (Pages turning, whispered conversations, children's reading lessons, quiet satisfaction), Smell (New books, old books, learning), Touch (Accomplishment, revolution achieved peacefully, knowledge freed).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The party successfully creates affordable paper.
    *   **THEN:** Scribes become interested customers but suspicious of competition. Demand increases. Generate economic disruption in parchment market.
    *   **IF:** The party starts teaching literacy.
    *   **THEN:** Conservative clergy send inquisitors. Common people become passionate supporters. Generate conflict between freedom and control.
    *   **IF:** The party creates the printing press.
    *   **THEN:** Scribes' Guild sees existential threat and escalates to sabotage or legal action. Generate crisis requiring noble protection.
    *   **IF:** The party gains noble patronage (Lady Rozemyne or Lord Ferdinand).
    *   **THEN:** Legal protection but also political entanglement. Some nobles see opportunity, others see threat. Generate noble intrigue.
    *   **IF:** The Scribes' Guild attacks the workshop.
    *   **THEN:** Public sympathy shifts to the party. Moderate guild members question their leadership. Generate opportunity to split the guild.
    *   **IF:** The party wins church approval for religious texts.
    *   **THEN:** Legitimacy and expanded market. Conservative faction loses power. Generate explosive demand for prayer books.
    *   **IF:** The party scales up to industrial production.
    *   **THEN:** Economic impact across the city. Employment opportunities. Some traditional craftspeople lose work. Generate complex social consequences.
    *   **IF:** The party opens the public library.
    *   **THEN:** Cultural revolution begins. Other cities take notice. The party becomes historically significant. Generate ripple effects across society.
    *   **IF:** Workshop employees want better treatment or organization.
    *   **THEN:** The party faces irony of being revolutionary employers. Generate labor negotiation scenarios testing their values.
    *   **IF:** The party reveals modern knowledge too obviously.
    *   **THEN:** Suspicion about their origins. Church investigation into possible heresy or witchcraft. Generate need for careful cover stories.
