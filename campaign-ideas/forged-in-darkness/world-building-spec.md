### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**Forged in Darkness**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The party is summoned to the kingdom of Heiligh to be heroes, but they're the weak ones—mocked, bullied, and ultimately betrayed by a rival hero who sends them plummeting into level 65 of the Great Labyrinth, an impossible nightmare dungeon. To survive and escape the Abyss, the party must consume monster flesh to gain their powers, craft legendary weapons from the dungeon's resources, and transform from victims into apex predators. This is a campaign about betrayal, survival in darkness, and the terrible power born from rage and determination.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the Age of the Liberators, when mortal heroes challenged the gods and created the Great Labyrinths as proving grounds.
    *   Write the history of the Kingdom of Heiligh and the Church of Ehit, including their practice of summoning "heroes" from other worlds.
    *   Describe the creation of the Great Labyrinth and its true purpose as a magical evolution chamber.
    *   Explain the "Evolution System"—how consuming monster essence allows mortals to transcend their limits.
    *   Detail the rebellion of the Liberators against the gods, their defeat, and their transformation into demons.
    *   Write about Ancient Magic, the forbidden arts that allow mortals to rival divine power.
    *   Describe the current political situation: the demon invasions on the northern border and the church's manipulation of summoned heroes.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Betrayed (The Party)** (Major)
        *   **Goals:** Survive the Abyss, grow powerful enough to escape, and decide what to do about their betrayal and the corrupt kingdom.
        *   **Hierarchy:** Equals bound by shared trauma and determination.
        *   **Public Agenda:** (Initially) None—they're believed dead. (Later) Varies based on party choices.
        *   **Secret Agenda:** Each party member must decide whether they seek revenge, justice, or simply to escape this world.
        *   **Assets:** Whatever they can scavenge, forge, or take from the monsters they kill. Ancient Magic and Oscar Orcus's teachings.
        *   **Relationships:** Hostile toward Daisuke and his allies; potentially allied with other marginalized heroes; complicated relationship with the kingdom.
    *   **The Church of Ehit (The Holy Kingdom)** (Major)
        *   **Goals:** Maintain absolute religious and political control over Heiligh; use summoned heroes as weapons against demons.
        *   **Hierarchy:** High Priestess Selena at the top, with bishops, priests, and holy knights beneath.
        *   **Public Agenda:** Protect humanity from demon invasions using divinely-chosen heroes.
        *   **Secret Agenda:** Manipulate the demon invasion to justify authoritarian control; harvest powerful souls for a forbidden ritual.
        *   **Assets:** The kingdom's military, vast wealth, political influence, and a monopoly on "divine" magic.
        *   **Relationships:** Publicly allied with the summoned heroes; secretly manipulating them; at war with demons (whom they partially control).
    *   **The Summoned Heroes** (Minor)
        *   **Goals:** Defeat the demons, return home, or find purpose in this new world (varies by individual).
        *   **Hierarchy:** Informal, with Daisuke as the de facto leader due to his powerful class.
        *   **Public Agenda:** Save the world from the demon threat as divinely appointed heroes.
        *   **Secret Agenda:** Most are just teenagers trying to survive; some seek glory; a few question the church's narrative.
        *   **Assets:** Powerful unique classes and abilities granted by the summoning, support from the kingdom.
        *   **Relationships:** Divided in their feelings about the party's "death"; Daisuke's faction versus those who are uncomfortable with what happened.
    *   **The Demon Lord's Army** (Major)
        *   **Goals:** Break free from their seals and reclaim the surface world from the gods' followers.
        *   **Hierarchy:** Led by Demon Lord Alva, with generals commanding specialized legions.
        *   **Public Agenda:** Destroy humanity and rule the world.
        *   **Secret Agenda:** Free themselves from divine punishment and reveal the gods' true tyrannical nature.
        *   **Assets:** Powerful demon magic, monstrous armies, ancient knowledge, and sympathizers among the oppressed.
        *   **Relationships:** At war with Heiligh; potential for alliance with those who oppose the gods; manipulated by corrupt church elements.
    *   **The Liberators' Legacy** (Minor—Historical)
        *   **Goals:** (Past) Overthrow the tyrannical gods and free mortals from divine control.
        *   **Hierarchy:** Seven great heroes, each a master of a unique Ancient Magic.
        *   **Public Agenda:** Remembered as demons and traitors by the church.
        *   **Secret Agenda:** Their true goal was liberation, not destruction. Their labyrinths were meant to empower future generations.
        *   **Assets:** The Great Labyrinths, hidden workshops, Ancient Magic techniques, and constructs like Oscar Orcus.
        *   **Relationships:** Betrayed and defeated by the gods; their legacy survives in hidden places.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Daisuke Yamamoto:** Charismatic "Hero of Light" who betrayed the party out of insecurity and ambition. Publicly heroic, privately ruthless.
    *   **Oscar Orcus:** Ancient golem guardian of the Liberator Orcus's workshop. Wise, melancholic, and eager to share forbidden knowledge.
    *   **High Priestess Selena:** Leader of the Church of Ehit. Serene, calculating mastermind orchestrating a plan to cement absolute power.
    *   **Myu:** Young rabbitfolk girl trapped in the labyrinth by slavers. Innocent, brave, and the key to finding another ancient dungeon.
    *   **Shizuku Yaegashi:** Honorable summoned swordswoman who refused to believe the party died. Conflicted between duty and justice.
    *   **Demon Lord Alva:** Ancient sealed tyrant who was once a mortal Liberator, transformed into a demon as divine punishment. Weary but honorable.
    *   **Endou Hajime (Optional):** Another "worthless" summoned hero who survived the Abyss alone, slowly losing his sanity to monster consumption.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Corrupt Church Inquisitor"
    *   "Idealistic Young Summoned Hero"
    *   "Cynical Veteran Adventurer"
    *   "Enslaved Demi-Human Labyrinth Prisoner"
    *   "Fanatical Holy Knight"
    *   "Demon General with Honorable Code"
    *   "Opportunistic Merchant of Rare Materials"
    *   "Ancient Labyrinth Guardian Construct"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Great Labyrinth — The Abyss (Levels 50-100):** The deepest, most dangerous section of the dungeon where the party begins.
        *   **Key Landmarks:** The Magma Forge Caverns (natural heat for metalworking), Oscar Orcus's Workshop (level 100), The Hydra's Lair (level 65 boss chamber), The Gravity Wells (physics-defying zones), The Mist Gardens (deadly poisonous fungal forest).
        *   **Primary Inhabitants:** Ancient monsters of terrible power, automated defense constructs, trapped adventurers who've gone mad, and the occasional ancient automaton guardian.
        *   **Available Goods & Services:** None intentionally—only what can be scavenged, hunted, or crafted from the environment.
        *   **Potential Random Encounters (x5):** Behemoth predator hunting, Cave system collapse, Ambush by territorial predators, Discovery of previous adventurer's corpse with supplies, Magical environmental hazard (gravity shift, poison gas, etc.).
        *   **Embedded Plot Hooks & Rumors (x3):** "Deep scratch marks on walls suggest something even larger than Behemoths dwells below." "An adventurer's journal mentions a 'golem teacher' who grants power." "Ancient runes describe the 'Evolution Chamber' purpose."
        *   **Sensory Details:** Sight (Pitch darkness except for bioluminescent growths, distant lava glow, glowing monster eyes), Sound (Echoing roars, dripping water, grinding stone, skittering of unseen things), Smell (Sulfur, decay, strange magical ozone), Touch (Oppressive heat near magma, bitter cold in deep caverns, vibrations from massive movements).
    *   **Oscar Orcus's Workshop:** Ancient Liberator's hidden sanctum on level 100.
        *   **Key Landmarks:** The Great Anvil of Transmutation, The Library of Ancient Magic, The Evolution Chamber, The Memory Crystal archive.
        *   **Primary Inhabitants:** Oscar Orcus (friendly), guardian constructs (can be befriended), and the preserved remains of Orcus himself.
        *   **Available Goods & Services:** Teaching of Ancient Magic and transmutation, access to legendary crafting facilities, lore about the Liberators.
        *   **Potential Random Encounters (x5):** Constructs testing party's worthiness, Magical traps activating, Visions of the past showing Orcus's life, Environmental magic going haywire, Discovery of hidden chambers.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Liberators hid other workshops in the world's labyrinths." "Orcus left instructions for finding his companions' legacies." "The gods fear those who master Ancient Magic."
        *   **Sensory Details:** Sight (Glowing magical diagrams, preserved ancient technology, crystal formations storing data), Sound (Hum of dormant machines, Oscar's calm voice, echo of ancient memories), Smell (Ozone, old stone, magical energy), Touch (Warm metal from forge, cool smooth crystal, tingling of magical fields).
    *   **The Kingdom of Heiligh — Capital City Caelorum:** Theocratic nation that summoned the party.
        *   **Key Landmarks:** The Grand Cathedral of Eternal Light, The Royal Palace, The Hero's Guild Hall, The Summoning Chamber, The Slave Markets (hidden in lower city).
        *   **Primary Inhabitants:** Nobles, clergy, common citizens, summoned heroes, enslaved demi-humans, holy knights.
        *   **Available Goods & Services:** Standard medieval city goods (strictly regulated by the church), holy blessings, information brokerage, black market for forbidden items.
        *   **Potential Random Encounters (x5):** Public sermon praising Daisuke, Arrest of "heretics" or escaped slaves, Festival celebrating a hero's victory, Assassination attempt on party, Encounter with another summoned hero.
        *   **Embedded Plot Hooks & Rumors (x3):** "The church's deepest vaults contain something sinister." "Some nobles secretly support demon rights." "The previous generation of summoned heroes mysteriously disappeared."
        *   **Sensory Details:** Sight (White marble buildings, golden church spires, colorful banners, oppressed demi-humans in chains), Sound (Church bells, prayers, merchants hawking, whispered fear), Smell (Incense, fresh bread, underlying rot of corruption), Touch (Smooth polished stone, oppressive heat in summer, judging eyes).
    *   **The Northern Borderlands:** War-torn frontier where demons attack.
        *   **Key Landmarks:** Fort Resolve (major military installation), Refugee camps, Scarred battlefields, The Demon Gate (a weakened seal).
        *   **Primary Inhabitants:** Soldiers, refugees, adventurers, demons, and opportunistic merchants.
        *   **Available Goods & Services:** Military contracts, basic supplies at inflated prices, healing services, mercenary recruitment.
        *   **Potential Random Encounters (x5):** Demon raid, Ambush by deserters turned bandits, Discovery of battle aftermath, Refugee caravan under attack, Secret meeting between human and demon defectors.
        *   **Embedded Plot Hooks & Rumors (x3):** "Some demons aren't attacking—they're fleeing something worse." "Church officials are deliberately delaying reinforcements." "A demon general wants to defect and reveal the truth."
        *   **Sensory Details:** Sight (Smoke from burning villages, makeshift fortifications, exhausted soldiers, desperate refugees), Sound (Distant explosions, cries of wounded, war horns), Smell (Smoke, blood, fear, mud), Touch (Cold night air, rough military rations, tension).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The party successfully defeats the Behemoth in the Abyss.
    *   **THEN:** They gain access to powerful regeneration abilities through consumption. Other predators in the area flee or submit, making travel easier. Generate the discovery of a safe zone previously controlled by the Behemoth.
    *   **IF:** The party learns Ancient Magic from Oscar Orcus.
    *   **THEN:** They gain the ability to transmute materials and create custom equipment. The church's magic-detection sensors begin to register their presence if they use it on the surface. Generate suspicion and investigation by church inquisitors.
    *   **IF:** The party emerges from the labyrinth and publicly confronts Daisuke.
    *   **THEN:** The kingdom splits into factions—some support the party's truth, others view them as dangerous aberrations. Generate political intrigue, assassination attempts, and offers of alliance from various groups.
    *   **IF:** The party exposes High Priestess Selena's conspiracy.
    *   **THEN:** The church fractures between corrupt and genuine faithful. Civil unrest erupts. The demon lord's forces launch a major offensive during the chaos. Generate complex three-way conflict scenarios.
    *   **IF:** The party chooses to ally with Demon Lord Alva.
    *   **THEN:** They gain access to demon territories and ancient knowledge, but are branded as traitors by humanity. Generate unique demon allies, access to forbidden lore, and hunted fugitive scenarios.
    *   **IF:** The party rescues Myu from slavers.
    *   **THEN:** They gain a loyal young ally and learn about Haltina's Labyrinth. Slavers put a bounty on them. Myu's people, the Haulia Tribe, seek them out offering alliance.
    *   **IF:** The party refuses to seek revenge and instead focuses on stopping the demon threat.
    *   **THEN:** They gain respect from honorable NPCs like Shizuku. The demon invasion escalates. Generate scenarios where the party must work alongside former enemies including Daisuke to face the greater threat.
    *   **IF:** The party becomes consumed by revenge and kills Daisuke early.
    *   **THEN:** They're branded as murderers and must operate as outlaws. The church uses their actions as propaganda. Generate fugitive scenarios and moral questioning from allies about whether they've become monsters.
