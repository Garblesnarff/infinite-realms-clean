### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Ten Pledges**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The party awakens in Disboard, a vibrant fantasy world governed by the Ten Pledges—absolute magical laws that forbid violence and mandate that all conflicts be resolved through games of chance, skill, or wit. To survive and thrive, the party must master this world's unique rules, challenge the Sixteen Races (each with their own magical advantages) in creative contests, and ultimately play their way to political power.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the Great War—the ancient, apocalyptic conflict between the races that nearly destroyed the world, before Tet became the One True God and established the Ten Pledges.
    *   Write the history of how humans, with no magical advantages, survived the transition from war to games and established the Kingdom of Elkia.
    *   Describe the legendary First King of Humanity and the impossible game he won to secure humanity's initial territory.
    *   Explain the decline of Elkia over generations as better players from other races systematically won away human lands and rights.
    *   Detail the Tournament of Sixteen, a recurring grand competition where all races participate, and its importance in the political landscape.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Kingdom of Elkia** (Major - Human)
        *   **Goals:** Survive as an independent nation and reclaim lost territories.
        *   **Hierarchy:** Constitutional monarchy with a king/queen and noble council.
        *   **Public Agenda:** We represent humanity's dignity and right to self-determination.
        *   **Secret Agenda:** Many nobles are secretly defeatist, believing submission to stronger races is inevitable.
        *   **Assets:** The capital city, remaining farmlands, human population's creativity.
        *   **Relationships:** Indebted to Elvenkind, pressured by the Eastern Union, pitied by most other races.
    *   **The Elven Gard** (Major - Elf)
        *   **Goals:** Expand their magical empire through strategic games and wagers.
        *   **Hierarchy:** Council of High Elves led by the Archsage.
        *   **Public Agenda:** To bring enlightenment and proper governance to lesser races.
        *   **Secret Agenda:** They view themselves as natural rulers and believe the Ten Pledges favor them due to their lie-detection abilities.
        *   **Assets:** Vast magical forests, powerful spellcasters, superior information gathering.
        *   **Relationships:** Condescending toward humans, competitive with Flugel, trading partners with Dwarves.
    *   **The Eastern Union** (Major - Werebeast)
        *   **Goals:** Economic and territorial dominance through trade and gaming prowess.
        *   **Hierarchy:** Merchant clans led by a Shrine Priestess.
        *   **Public Agenda:** Prosperity through commerce and fair competition.
        *   **Secret Agenda:** Using compulsion magic on human rulers to gradually absorb Elkia.
        *   **Assets:** Incredible instincts, wealthy trade networks, master gamblers.
        *   **Relationships:** Friendly with most races due to trade, secretly manipulating Elkia.
    *   **The Flugel Collective** (Minor)
        *   **Goals:** Collect knowledge and test themselves against worthy opponents.
        *   **Hierarchy:** Individual Flugel serve various gods and operate independently.
        *   **Public Agenda:** We seek intellectual stimulation and worthy challenges.
        *   **Secret Agenda:** Some Flugel miss the Great War and find the gaming world boring.
        *   **Assets:** Mind-reading abilities, ancient knowledge, individual power.
        *   **Relationships:** Respected and feared by all, competitive with Elves.
    *   **The Dwarven Forgeholds** (Minor)
        *   **Goals:** Perfect their craft and maintain their mountain territories.
        *   **Hierarchy:** Guild system led by Master Smiths.
        *   **Public Agenda:** We build the greatest works and win through superior calculation.
        *   **Secret Agenda:** Secretly developing technology to counter other races' magic.
        *   **Assets:** Probability manipulation, incredible craftsmanship, mountain fortresses.
        *   **Relationships:** Trade partners with Elves, respectful toward humans who prove clever.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Stephanie Dola:** Human noble and the party's primary ally, passionate but inexperienced, seeking to redeem her family's legacy.
    *   **Kurami Zell:** Talented human player working with Elvenkind, seen as either a traitor or a realist depending on perspective.
    *   **Jibril:** Ancient Flugel scholar who collects knowledge and becomes fascinated by the party's strategies.
    *   **Chlammy Zell:** Werebeast agent posing as human, conflicted between duty and honor.
    *   **Tet:** The One True God who created the Ten Pledges, childlike and mysterious.
    *   **The Corrupted King:** Current human monarch under magical compulsion, trying to lose in a way that leads to his own freedom.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Arrogant Elven Game Master"
    *   "Dwarven Probability Expert"
    *   "Desperate Human Gambler"
    *   "Curious Flugel Observer"
    *   "Werebeast Merchant Prince"
    *   "Fallen Noble seeking redemption"
    *   "Tournament Referee (various races)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **Elkia Royal City:** Humanity's colorful capital with a mix of grandeur and decay.
        *   **Key Landmarks:** The Pledged Throne, Grand Gaming Hall, Stephanie's Estate, Royal Library.
        *   **Primary Inhabitants:** Humans of all social classes, some Elven embassy staff.
        *   **Available Goods & Services:** Game supplies, information brokers, lodging, basic magical items.
        *   **Potential Random Encounters (x5):** A street game drawing a crowd, a noble losing their house in a wager, an Elf insulting human players, a child challenging adults to simple games, a merchant offering "guaranteed winning" strategies.
        *   **Embedded Plot Hooks & Rumors (x3):** "The King hasn't left his throne room in weeks." "Elves are buying up property near the eastern wall." "Someone won a major game using a strategy no one's seen before."
        *   **Sensory Details:** Sight (Colorful banners, gaming tables everywhere, the Ten Pledges in golden script), Sound (Dice rolling, cards shuffling, cheers and groans), Smell (Paper, wood polish, incense from game halls).
    *   **The Grand Arena:** Interdimensional space for the Tournament of Sixteen.
        *   **Key Landmarks:** The Central Stadium, Race Pavilions (16 distinct areas), the Wager Vault, Observation Galleries.
        *   **Primary Inhabitants:** Representatives from all Sixteen Races, spectators, referees.
        *   **Available Goods & Services:** Exotic game supplies, information on opponents, coaching from former champions.
        *   **Potential Random Encounters (x5):** A challenge from an overconfident youth, a veteran giving advice, a spy trying to learn strategies, a race representative offering an alliance, a god (Tet) watching in disguise.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Flugel haven't fielded their strongest player." "Someone's been bribing referees." "The arena itself is alive and might interfere."
        *   **Sensory Details:** Sight (Impossible architecture, floating game boards, crowds of diverse races), Sound (Multiple languages, magical effects, thunderous applause), Smell (Ozone from magic, exotic foods from sixteen cultures).
    *   **Elven Embassy District:** Territory within Elkia controlled by Elvenkind.
        *   **Key Landmarks:** The Living Tree Embassy, Memory Gardens, the Hall of Contracts.
        *   **Primary Inhabitants:** High Elves, their servants, humans who've wagered themselves into service.
        *   **Available Goods & Services:** Elven luxuries, truth-detection services (for a price), access to Elven game strategies.
        *   **Potential Random Encounters (x5):** An Elf testing your honesty, a servant begging for help winning back their freedom, a magical plant causing minor chaos, a game challenge from a bored noble, a contract lawyer offering dubious advice.
        *   **Embedded Plot Hooks & Rumors (x3):** "Humans who enter service never seem to win their freedom back." "The High Elves are planning something big." "There's a secret entrance to their private vaults."
        *   **Sensory Details:** Sight (Glowing trees, perfect architecture, bound humans in servants' garb), Sound (Wind through leaves, haughty laughter, whispered contracts), Smell (Flowers, ancient wood, expensive perfumes).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The party wins against the Elven merchant in Session 3.
    *   **THEN:** Elvenkind begins taking them seriously as threats. Generate new Elven NPCs who actively work to undermine them, and increase difficulty of future Elven opponents.
    *   **IF:** The party loses a major wager during the tournament.
    *   **THEN:** Generate consequences based on what was wagered. If territory: show that land now controlled by another race. If freedom: create a questline about escaping service. If memory: roleplay the character not remembering key information.
    *   **IF:** The party exposes the king's compulsion in Session 7.
    *   **THEN:** Create political upheaval. Generate noble factions: some support the party, others see them as troublemakers. The Eastern Union sends agents to eliminate evidence.
    *   **IF:** The party allies with Jibril by defeating her in a game.
    *   **THEN:** She becomes bound to serve them per her ancient wager. Generate scenarios where her immense power helps but also attracts unwanted attention from other Flugel.
    *   **IF:** The party wins the Crown Game but chooses not to take the throne.
    *   **THEN:** Generate multiple succession candidates and a questline about establishing a new form of government, with various factions vying for influence.
