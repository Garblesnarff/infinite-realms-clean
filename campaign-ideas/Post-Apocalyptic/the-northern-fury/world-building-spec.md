### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Northern Fury**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The party are Norse warriors whose peaceful village was destroyed by Askeladd's jomsvikings during a raid. They swear revenge and spend years infiltrating his warband, participating in brutal Viking raids across England during the Danish invasion (circa 1013). As they grow stronger and closer to their goal, they realize revenge is consuming their souls—they're becoming the monsters they hate. The campaign explores the question: does revenge bring peace, or does it perpetuate cycles of violence? Can warriors steeped in blood find redemption through pacifism and building instead of destroying? The party must choose between hollow vengeance, difficult redemption, or pragmatic balance, in a historically grounded world where moral choices have weight and consequences.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Chronicle the Viking Age (793-1066 AD): Scandinavian raiders, traders, and explorers ranging from Russia to North America. Focus on 1013 AD—Danish invasion of England under Sweyn Forkbeard.
    *   Detail Norse culture: honor-based society, importance of oaths and reputation, Thing (assemblies), raiding as way of life, transition to Christianity, slavery (thralls).
    *   Explain the Jomsvikings: legendary mercenary order of elite Viking warriors, bound by strict code, serve the highest bidder, reputation for brutality and skill.
    *   Describe Askeladd's history: Half-Welsh (mother was Welsh princess enslaved by Vikings), half-Norse; avenges his mother's people by manipulating politics; brilliant tactician who uses cruelty strategically.
    *   Chronicle the Danish conquest: Sweyn Forkbeard's invasion of England; his son Canute's eventual rule; political maneuvering between Danish, Norwegian, and English factions.
    *   Detail Thors' legend: Greatest Jomsviking who defected, chose pacifism, tried to protect his family by fleeing to Iceland; killed by Askeladd when discovered; his philosophy: "A true warrior needs no sword."
    *   Explain Vinland: Norse name for North American settlements (Newfoundland); represents hope for land without war where people can start over.
    *   Describe the Cycle of Revenge: cultural understanding that blood demands blood, but also wisdom that revenge perpetuates suffering endlessly.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Party (Revenge-Seekers)** (Minor)
        *   **Goals:** Initially: revenge against Askeladd. Mid-campaign: survival and grappling with moral costs. Late: varies by path chosen (revenge, redemption, or balance).
        *   **Hierarchy:** No formal structure; bound by shared trauma and oath of vengeance.
        *   **Public Agenda:** Mercenaries in Askeladd's crew (cover story); skilled warriors for hire.
        *   **Secret Agenda:** Assassinate Askeladd when the moment is right; struggling with whether revenge is still what they want.
        *   **Assets:** Combat skills, insider knowledge of Askeladd's plans, growing wealth from raids, bonds with some crew members.
        *   **Relationships:** Embedded in Askeladd's crew (false loyalty); targets of Askeladd's suspicions; potential allies with Canute's faction or Leif's expedition.
    *   **Askeladd's Jomsvikings** (Major)
        *   **Goals:** Serve Askeladd; profit from raids; survive warfare; some seek glory, others just payment.
        *   **Hierarchy:** Askeladd commands; Bjorn is lieutenant; crew members ranked by skill and reputation.
        *   **Public Agenda:** Elite mercenary company serving highest bidder (currently Danish invasion).
        *   **Secret Agenda:** Askeladd manipulates them toward his goal: install Canute as king to protect Wales. Most crew unaware of his true motives.
        *   **Assets:** Longships, combat expertise, reputation that precedes them, insider access to Danish command.
        *   **Relationships:** Serve Danish invasion; raid English settlements; compete with other Viking bands; Askeladd secretly serves Canute over Sweyn.
    *   **The Danish Invasion Force** (Major)
        *   **Goals:** Conquer England, install Danish rule, extract tribute (Danegeld).
        *   **Hierarchy:** King Sweyn Forkbeard leads; Prince Canute is heir (initially weak); jarls command divisions.
        *   **Public Agenda:** Military conquest and occupation.
        *   **Secret Agenda:** Internal politics—Sweyn favors his older son Harold over Canute; Canute's advisors (including Askeladd) maneuver for his ascension.
        *   **Assets:** Large armies, longship fleets, control of Danish territories, wealth for bribes and payment.
        *   **Relationships:** Employ jomsvikings like Askeladd's crew; opposed by English resistance; political intrigue within Danish leadership.
    *   **The English Resistance** (Major)
        *   **Goals:** Defend England from invasion, protect families and villages, resist occupation.
        *   **Hierarchy:** King Æthelred leads (ineffectively); local thegns and lords defend their regions; some consider betrayal to save themselves.
        *   **Public Agenda:** National defense.
        *   **Secret Agenda:** Many nobles willing to pay Danegeld (tribute) to avoid fighting; political fractures weaken resistance.
        *   **Assets:** Fortified towns, local militias, knowledge of terrain, support of population.
        *   **Relationships:** Victims of Viking raids; desperate to survive; some collaborate with Danes to save their people.
    *   **Vinland Expedition (Leif's Explorers)** (Minor)
        *   **Goals:** Explore and settle Vinland (North America); find land without war; create peaceful society.
        *   **Hierarchy:** Leif Erikson leads; small group of settlers and explorers.
        *   **Public Agenda:** Exploration and trade.
        *   **Secret Agenda:** Offering escape from cycle of violence to those wise enough to take it.
        *   **Assets:** Knowledge of western routes, ships, optimism and vision.
        *   **Relationships:** Separate from political conflicts; represent alternative path for the party; Leif seeks to recruit those tired of war.
    *   **Canute's Inner Circle** (Minor - Growing)
        *   **Goals:** Transform Canute from weak prince to great king; create "paradise on earth" through strong rule.
        *   **Hierarchy:** Canute at center; advisors including Askeladd (military) and churchmen (legitimacy).
        *   **Public Agenda:** Support Canute's claim to throne.
        *   **Secret Agenda:** Willing to commit atrocities for "greater good"; Canute grapples with morality of absolute power.
        *   **Assets:** Canute's legitimacy as heir, Askeladd's tactical genius, growing political support.
        *   **Relationships:** Opposed by Sweyn's favorite son Harold; allied with ambitious nobles; manipulate events toward Canute's ascension.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Askeladd:** Jomsviking leader; party's target; half-Welsh, half-Norse; brilliant tactician with hidden agenda to protect Wales via Canute.
    *   **Prince Canute:** Danish heir; transforms from timid, feminine prince to ruthless king; grapples with morality of power.
    *   **Bjorn:** Askeladd's lieutenant; berserker; loyal unto death; tragic figure consumed by violence with no place in peace.
    *   **Thorfinn:** (Optional - can be NPC or party member) Another revenge-seeker in Askeladd's crew; son of Thors; mirrors party's journey.
    *   **Leif Erikson:** Explorer seeking Vinland; wise mentor offering alternative to revenge; patient and hopeful.
    *   **Thors:** (Appears in flashbacks/visions) Legendary Jomsviking turned pacifist; killed by Askeladd; represents ideal warrior who chooses peace.
    *   **King Sweyn Forkbeard:** Danish king invading England; ruthless conqueror; favors his son Harold over Canute.
    *   **Willibald:** Priest in Canute's circle; helps transform Canute's thinking toward love and power.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Jomsviking Warrior" (veteran raiders with personal codes of honor)
    *   "English Thegn/Defender" (local nobles defending homes)
    *   "Slave/Thrall" (captured people serving Vikings)
    *   "Danish Soldier" (regular invasion force troops)
    *   "English Villager" (innocents caught in war)
    *   "Berserker" (warriors who enter frenzied rage)
    *   "Trader/Merchant" (opportunists profiting from war)

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Burnt Village (Iceland):** Party's destroyed home; ruins and memories.
        *   **Key Landmarks:** Charred longhouse remains, burial mounds, the pier where raiders landed, memorial stones.
        *   **Primary Inhabitants:** None—destroyed. Ghosts of memory.
        *   **Available Goods & Services:** None. Only serves as emotional anchor.
        *   **Potential Random Encounters (x5):** Flashback visions of the raid, spirits of the dead (if supernatural), returning to find scavengers, meeting other survivors, discovering clues about Askeladd.
        *   **Embedded Plot Hooks & Rumors (x3):** "Askeladd targeted this village specifically—why?" "One elder survived and knows the truth." "The village had a hidden treasure the raiders didn't find."
        *   **Sensory Details:** Sight (black timber skeletons, snow covering ash, empty), Sound (wind through ruins, silence), Smell (old smoke, decay, salt air), Touch (cold, rough burnt wood).
    *   **Askeladd's War Camp:** Mobile base for the warband.
        *   **Key Landmarks:** Command tent, longship moorings, training grounds, campfires, loot storage.
        *   **Primary Inhabitants:** Askeladd, Bjorn, 50-100 warriors, slaves.
        *   **Available Goods & Services:** Training, weapon/armor repair, information, camaraderie, alcohol.
        *   **Potential Random Encounters (x5):** Training duels, Askeladd's tactical meetings, Bjorn's berserker episodes, bonding with crew members, overhearing plots.
        *   **Embedded Plot Hooks & Rumors (x3):** "Askeladd is half-Welsh and hates the English." "Bjorn would die for Askeladd without question." "Some crew members suspect the party's true purpose."
        *   **Sensory Details:** Sight (tents, weapons racks, fires, warriors), Sound (combat training, laughter, Norse songs), Smell (smoke, sweat, salt, roasting meat), Touch (rough ground, cold steel).
    *   **English Village (Generic):** Represents countless raided settlements.
        *   **Key Landmarks:** Timber hall, church, farms, wooden palisade, well.
        *   **Primary Inhabitants:** English villagers, local thegn, priest.
        *   **Available Goods & Services:** Food, shelter, information (if party is peaceful).
        *   **Potential Random Encounters (x5):** Raid in progress (party must choose side), hiding villagers, thegn offering tribute to avoid raid, survivors fleeing, moral dilemma encounter.
        *   **Embedded Plot Hooks & Rumors (x3):** "This village looks just like our old home." "The villagers are just people trying to survive." "If we raid them, we become what destroyed us."
        *   **Sensory Details:** Sight (thatched roofs, farmland, wooden buildings, simple but homey), Sound (livestock, daily life, screams if raided), Smell (fresh bread, animals, earth), Touch (mud, wooden fences).
    *   **The North Sea:** Treacherous waters between lands.
        *   **Key Landmarks:** Open water, storm zones, sea routes, occasional islands.
        *   **Primary Inhabitants:** Vikings on longships, merchants, occasional sea creatures.
        *   **Available Goods & Services:** Travel, fishing, naval combat.
        *   **Potential Random Encounters (x5):** Massive storm (survival challenge), rival Viking band, whale sighting, shipwreck rescue/salvage, navigation challenge.
        *   **Embedded Plot Hooks & Rumors (x3):** "The sea doesn't care about revenge or honor." "Many warriors die to water, not swords." "Leif sailed west from here to Vinland."
        *   **Sensory Details:** Sight (gray water, waves, distant shores, gulls), Sound (waves, wind, creak of ship, rowing songs), Smell (salt, fish, tar), Touch (spray, cold, rocking deck).
    *   **London/Canute's Court:** Political center of the invasion.
        *   **Key Landmarks:** Great hall, church, docks, fortifications, market.
        *   **Primary Inhabitants:** Canute, his advisors, Danish nobility, English collaborators, Askeladd (when summoned).
        *   **Available Goods & Services:** Political intrigue, contracts, information, luxury goods.
        *   **Potential Random Encounters (x5):** Audience with Canute, political assassination plot, Askeladd's maneuvering, philosophical debate, witnessing Canute's transformation.
        *   **Embedded Plot Hooks & Rumors (x3):** "Canute is becoming a great king, but at what cost?" "Askeladd serves Canute, not Sweyn—treason?" "Power corrupts even those with good intentions."
        *   **Sensory Details:** Sight (stone buildings, banners, wealth contrasting with war outside), Sound (political discussions, music, guards), Smell (incense, food, wine), Touch (fine fabrics, warmth from fires).
    *   **Vinland (North America):** The promised land of peace.
        *   **Key Landmarks:** Pristine forests, clear rivers, native settlements, potential Norse outpost.
        *   **Primary Inhabitants:** Indigenous peoples, Leif's expedition.
        *   **Available Goods & Services:** New beginning, land to settle, freedom from European wars.
        *   **Potential Random Encounters (x5):** Meeting indigenous peoples, exploring wilderness, building settlement, hunting, establishing peaceful trade.
        *   **Embedded Plot Hooks & Rumors (x3):** "This land has no kings or wars—a fresh start." "Can warriors become farmers?" "Will we bring violence here, or leave it behind?"
        *   **Sensory Details:** Sight (untouched forests, wildlife, clean rivers, vast skies), Sound (birds, wind through trees, rivers, silence of no war), Smell (pine, fresh water, earth), Touch (rough bark, cool streams, potential).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The party's village is destroyed (Session 1).
    *   **THEN:** Party gains revenge motivation; oaths are sworn; Askeladd becomes primary antagonist; journey begins. Generate: personal losses for each PC, revenge tracker activation, Askeladd's initial stats and location.
    *   **IF:** The party joins Askeladd's crew.
    *   **THEN:** They gain insider access but must participate in raids. Generate: crew bonding opportunities, moral dilemma events (raiding innocents), suspicion from some crew, Askeladd testing their loyalty.
    *   **IF:** The party commits atrocities (raids, kills innocents).
    *   **THEN:** Increase "Weight of Deeds" tracker; cause nightmares, PTSD, moral degradation. Generate: specific guilt moments, flashbacks, NPCs reacting with fear or disgust, internal conflict.
    *   **IF:** The party refuses to raid a village similar to their own.
    *   **THEN:** Turning point—Askeladd and crew become suspicious, OR Askeladd respects their conviction. Generate: confrontation with Askeladd, crew split in reactions, party's cover may be blown, opportunity to question revenge path.
    *   **IF:** The party witnesses or participates in Canute's transformation.
    *   **THEN:** They see how power changes people. Generate: philosophical discussions, Canute offering them positions if they serve, questioning whether ends justify means.
    *   **IF:** The party meets Leif and learns about Vinland.
    *   **THEN:** Redemption path becomes available. Generate: Leif's recruitment pitch, visions of peaceful life, party must choose between revenge and redemption.
    *   **IF:** The party achieves revenge (kills Askeladd).
    *   **THEN:** Multiple outcomes based on method and context. Generate:
        *   If done in rage: hollow victory, party becomes like Askeladd, cycle continues.
        *   If done justly: bittersweet closure but party still haunted.
        *   If Askeladd orchestrates his own death for Canute: party realizes he was trapped like them.
    *   **IF:** The party chooses redemption (abandons revenge, goes to Vinland).
    *   **THEN:** Hardest path but most meaningful. Generate: Askeladd's reaction (respect? contempt?), building settlement mechanics, finding peace, Weight of Deeds slowly healing.
    *   **IF:** The party finds balance (stops Askeladd's worst acts without obsession).
    *   **THEN:** Pragmatic ending. Generate: Askeladd's fate by other means, party becomes legendary heroes who fight only to protect, respected but not consumed.
