# World-Building Specification: Descent into Yomi

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**Descent into Yomi**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The players have died and descended into Yomi, the Japanese underworld of darkness, decay, and pollution. Unlike afterlives with judgment or purpose, Yomi is simply where the dead rot eternally. Players must escape before decaying beyond recovery, navigating absolute darkness while pursued by Izanami, the death goddess who refuses abandonment. They race against their own corruption, gather sacred items that can repel pollution, and ultimately confront Izanami with choice: defeat her, convince her, or seal her. This campaign is survival horror exploring decay and purity, abandonment and loneliness, the tragedy of death without transcendence.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the myth of Izanagi and Izanami: their creation of Japan, Izanami's death giving birth to fire, Izanagi's descent to retrieve her, his horror at seeing her decay, his abandonment and flight, and Izanami's fury.
    *   Explain Yomi as the land of the dead in Shinto tradition - not a place of judgment but simply where the dead exist in corruption.
    *   Describe the concept of kegare (pollution/impurity) and kiyome (purification) in Shinto - how death pollutes, how purification works, and why it matters.
    *   Write about Izanagi's purification ritual after escaping Yomi, throwing down his possessions which became deities, and washing himself to create Amaterasu, Tsukuyomi, and Susanoo.
    *   Explain the significance of the boulder Izanagi used to seal Yomi's exit, creating the boundary between life and death.
    *   Detail the yomotsu-shikome (hags of Yomi) who Izanami sent to pursue Izanagi.
    *   Describe the peaches Izanagi threw to delay pursuit, and their power to repel evil.
    *   Explain the comb Izanagi threw that became bamboo shoots, creating obstacles.
    *   Write about the concept of death pollution in Japanese tradition and funeral practices designed to manage it.
    *   Detail the yokai and spirits that emerge from corruption and decay in Japanese mythology.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **Izanami's Court** (Major - Tragic Authority)
        *   **Goals:** Prevent anyone from escaping Yomi, maintain Izanami's rule, keep her company in loneliness, punish those who try to abandon her.
        *   **Hierarchy:** Izanami as queen, yomotsu-shikome as hunters and servants, the Thousand-Warriors as guardians, corruption spirits as minions.
        *   **Public Agenda:** Rule the dead, maintain Yomi as the land of death.
        *   **Secret Agenda:** Izanami is desperately lonely; every escape wounds her; she's not evil, just abandoned and grief-mad; her servants are trapped victims serving her.
        *   **Assets:** Control over Yomi itself, ability to manipulate darkness and decay, the yomotsu-shikome hunters, awareness of all souls in her domain, the power of pollution.
        *   **Relationships:** Opposed to anyone escaping; betrayed by Izanagi; isolated from other deities; her servants fear and pity her; represents the finality of death.

    *   **The Peach Grove Sanctuary** (Minor - Rebellion and Hope)
        *   **Goals:** Provide temporary refuge from decay, help souls attempting escape, resist Izanami's absolute rule, preserve purity in corruption.
        *   **Hierarchy:** The Peach Tree Guardian as keeper, purified spirits as helpers, those temporarily staying as protected guests.
        *   **Public Agenda:** Offer sanctuary and purification.
        *   **Secret Agenda:** The Guardian is Izanami's severed pure self; helping escapees is rebellion against what Izanami became; represents the possibility of redemption.
        *   **Assets:** Peaches of Purification, sanctuary where decay halts, knowledge of escape routes, immunity to Izanami's direct control.
        *   **Relationships:** Secretly part of Izanami yet opposed to her; helps escapees; hated by yomotsu-shikome; connected to Amaterasu's light.

    *   **The Resigned Dead** (Major - Victims and Obstacles)
        *   **Goals:** Accept death, stop fighting decay, find peace in finality, sometimes prevent others from escaping out of belief death should be final.
        *   **Hierarchy:** No formal hierarchy - united by resignation at various stages of decay.
        *   **Public Agenda:** Accept fate, rest, decay peacefully.
        *   **Secret Agenda:** Some oppose escape attempts, believing life's grasp should be released; others secretly hope but are too decayed to try; represent acceptance of death.
        *   **Assets:** Numbers, knowledge of Yomi, acceptance of environment, some so decayed they're part of the landscape itself.
        *   **Relationships:** Pity those still fighting; observed by Izanami; ignored by hunters (not trying to escape); some become yomotsu-shikome if they fully surrender.

    *   **The Recently Dead** (Minor - Companions and Competition)
        *   **Goals:** Survive, resist decay, find escape, maintain humanity and sanity, help each other (sometimes), compete for scarce resources (other times).
        *   **Hierarchy:** No formal structure - temporary alliances based on arrival time and personality.
        *   **Public Agenda:** Escape Yomi before decaying too far.
        *   **Secret Agenda:** Competition for purifying resources; some willing to betray others for better chance at escape; fear becoming resigned or corrupted; represent the players' potential fates.
        *   **Assets:** Recent memories of life, low pollution levels initially, desperation driving creativity, potential allies or rivals.
        *   **Relationships:** Natural allies to players but also competitors; hunted by yomotsu-shikome; avoided by the resigned; represent stages of decay players will face.

    *   **Amaterasu's Light** (Minor - Divine Interest)
        *   **Goals:** Guide lost souls, provide light in darkness, represent hope, maintain connection between living world and dead, subtly oppose Izanami without direct confrontation.
        *   **Hierarchy:** Amaterasu (sun goddess) as divine patron, the Messenger spirit as agent, light-bearing yokai as helpers.
        *   **Public Agenda:** Bring light to darkness, guide those trying to return to life.
        *   **Secret Agenda:** Amaterasu is Izanagi's daughter born from his purification; has sympathy for her mother Izanami but supports life over death; cannot intervene directly without violating death's domain; the Messenger is her compromise - help without breaking cosmic law.
        *   **Assets:** The Messenger (light source), divine protection (limited), connection to living world, purifying influence.
        *   **Relationships:** Opposes Izanami by supporting escapees; daughter of Izanagi (who abandoned Izanami); represents life and light; her presence in Yomi is transgressive but tolerated.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Izanami-no-Mikoto:** Death goddess, ruler of Yomi, tragic figure, both beautiful and horrifically decayed.
    *   **The Peach Tree Guardian:** Spirit of purity, actually Izanami's severed pure self, keeper of the grove.
    *   **The Messenger:** Light-spirit sent by Amaterasu, provides light, silent but expressive.
    *   **Lead Yomotsu-shikome:** Most ancient and decayed of the hags, remembers when she was human.
    *   **The Thousand-Warrior Commander:** Ancient soldier guarding Yomi's exit, resigned to duty, barely human.
    *   **The Comb Spirit:** Imprisoned essence of separation, tool used by Izanagi, bitter about its purpose.

*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Recently Dead Soul (Various Stages)" - NPCs at different decay levels showing player's potential futures.
    *   "Yomotsu-shikome Hag" - Tragic horror servants of Izanami, hunters in darkness.
    *   "Resigned Dead" - Those who've given up escape, at peace or despairing.
    *   "Corruption Spirit" - Yokai born from decay and pollution in Yomi.
    *   "Thousand-Warrior Guard" - Ancient soldiers, more obstacles than people.
    *   "Fellow Escapee" - Potential ally or competitor for resources.
    *   "Voice in Darkness" - Cannot be seen, only heard, offers advice or lures to doom.
    *   "Merged with Yomi" - So decayed they're landscape now, horrifying warnings.

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**

    *   **The Threshold of Darkness:**
        *   **Key Landmarks:** The vague sense of the living world above, the descent into deeper darkness, scattered confused recently dead, the last place light naturally filters.
        *   **Primary Inhabitants:** Recently deceased, confused spirits, minor corruption yokai.
        *   **Available Goods & Services:** Initial orientation, meeting other dead, last chance to see without magical light, beginning of decay.
        *   **Potential Random Encounters (x5):** Confused soul asking what happened; discovery of first signs of personal decay; the Messenger appearing with light; distant sounds of yomotsu-shikome; finding a more decayed corpse as warning.
        *   **Embedded Plot Hooks & Rumors (x3):** "There's a way out but Izanami guards it." "The darkness gets worse the deeper you go." "Someone said there's a grove of light somewhere." "Keep moving or you'll become part of the ground."
        *   **Sensory Details:** Sight (Dim, shadowy, outlines barely visible, gradual transition to absolute darkness). Sound (Dripping, whispers, breathing, distant movement). Smell (Damp earth, first hints of decay, must). Touch (Cold, damp, the first tingling of pollution). Taste (Air tastes stale, beginning of wrongness).

    *   **The Labyrinth of Bones:**
        *   **Key Landmarks:** Passages made of ancient bones, wrong turns leading to worse places, the sound of hunters, occasional markers left by previous escapees.
        *   **Primary Inhabitants:** Yomotsu-shikome, lost souls, corruption spirits, bone-creatures.
        *   **Available Goods & Services:** Passage (if you navigate correctly), horror and danger, potential clues from the desperate.
        *   **Potential Random Encounters (x5):** Yomotsu-shikome hunting by sound; bones whispering their death stories; finding skeletal remains of failed escapees; navigating blind in absolute darkness; hearing Izanami's voice echoing.
        *   **Embedded Plot Hooks & Rumors (x3):** "The bones remember the way." "Don't trust left turns." "The hags hunt by sound and smell." "Someone left marks but they're old and fading."
        *   **Sensory Details:** Sight (Absolute darkness, perhaps occasional bioluminescent decay). Sound (Bones scraping, whispers, dripping, hunters in distance, your own breathing too loud). Smell (Decay, ancient death, pollution). Touch (Bones smooth and cold, narrow passages). Taste (Dust, age, death).

    *   **The Peach Grove:**
        *   **Key Landmarks:** Impossible light in darkness, beautiful peach trees bearing purifying fruit, the Guardian's shrine, sanctuary boundaries.
        *   **Primary Inhabitants:** The Peach Tree Guardian, temporarily purified souls, light-spirits.
        *   **Available Goods & Services:** Sanctuary where decay stops, Peaches of Purification, information about escape, temporary rest, hope.
        *   **Potential Random Encounters (x5):** The Guardian offering wisdom; souls resting before continuing; witnessing purification ritual; yomotsu-shikome unable to enter but circling outside; experiencing decay reversal temporarily.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Guardian was once part of Izanami." "These peaches came from what Izanagi threw when fleeing." "Sanctuary won't last forever - even this place weakens." "Izanami hates this place but cannot destroy it."
        *   **Sensory Details:** Sight (Impossible beauty and light, peach blossoms, the Guardian's serene presence, color after monochrome). Sound (Gentle breeze, leaves rustling, peace after horror). Smell (Peach blossoms, purification, life). Touch (Warmth, clean air, decay stopping). Taste (Fresh peaches, sweetness, hope).

    *   **The Palace of Rot:**
        *   **Key Landmarks:** Izanami's throne, elegant halls crumbling with decay, maggots arranged in patterns, the tragic beauty of corrupted grandeur.
        *   **Primary Inhabitants:** Izanami, her court of yomotsu-shikome, the completely resigned, corruption made manifest.
        *   **Available Goods & Services:** Confrontation with Izanami, truth about her loneliness, the Comb Spirit imprisoned here, understanding the tragedy.
        *   **Potential Random Encounters (x5):** Izanami holding court; yomotsu-shikome serving tea from darkness; witnessing her loneliness; hearing her story; the horror of seeing her decay up close; her tragic offer to stay.
        *   **Embedded Plot Hooks & Rumors (x3):** "She was beautiful once." "Izanagi fled when he saw what she'd become." "She won't let anyone leave because everyone abandons her." "Her rage is grief."
        *   **Sensory Details:** Sight (Horrific beauty, elegant decay, Izanami's form both queenly and corpse-like, maggots moving in artistic patterns). Sound (Her voice echoing, the soft sound of decay, mournful music). Smell (Overwhelming decay somehow made elegant, incense failing to mask rot). Touch (Damp, clinging, the pollution is strongest here). Taste (Corruption, but also the bitter taste of loneliness).

    *   **The Boulder Pass:**
        *   **Key Landmarks:** The massive boulder that sealed Yomi (now moved aside), the upward passage to the living world, narrow climbing terrain, Izanami's final stand.
        *   **Primary Inhabitants:** Izanami (guarding personally), the Thousand-Warriors, the desperate making final push.
        *   **Available Goods & Services:** The exit (if you can pass Izanami), confrontation, final choice, the boundary between death and life.
        *   **Potential Random Encounters (x5):** Izanami blocking the path; the Thousand-Warriors in formation; using sacred items to create opening; sealing Izanami behind the boulder; her final plea or curse; the desperate climb in darkness.
        *   **Embedded Plot Hooks & Rumors (x3):** "This is where Izanagi sealed her." "She can leave if she chooses but stays in grief." "The living world is just beyond." "Your choice here determines everything."
        *   **Sensory Details:** Sight (The faint suggestion of light above, the boulder, Izanami's form blocking escape, narrow walls). Sound (Your climbing, her voice, rocks scraping, the living world calling faintly). Smell (Decay giving way gradually to life). Touch (Cold stone, desperate climbing, the boundary between realms). Taste (Hope mixing with fear, the last of Yomi's pollution).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**

    *   **IF:** Players accumulate high pollution levels.
    *   **THEN:** Mechanical penalties, visible decay, attract dangers, NPCs react with horror or pity, magic becomes harder. Generate decay description and consequences.

    *   **IF:** Players use Peaches of Purification.
    *   **THEN:** Reduce pollution, halt decay temporarily, provide relief, but limited resource creates future desperation. Generate purification scene.

    *   **IF:** Izanami's awareness level increases (players are loud, use light extensively, kill her servants).
    *   **THEN:** She hunts personally, encounters become more dangerous, escape becomes harder. Generate hunting sequences.

    *   **IF:** Players show kindness to yomotsu-shikome or resigned dead.
    *   **THEN:** Some NPCs remember humanity, might provide help or avoid hunting players, generate moments of tragedy and connection.

    *   **IF:** Players progress to higher decay stages.
    *   **THEN:** Appearance changes, abilities limited, NPCs treat them differently, the urge to give up increases. Generate transformation scenes and moral tests.

    *   **IF:** The Messenger's light dies or is lost.
    *   **THEN:** Absolute darkness, navigation by sound only, extreme danger, desperation. Generate blind navigation sequence.

    *   **IF:** Players spend too long in one area.
    *   **THEN:** Decay accelerates, pollution increases, Izanami's awareness grows, environment degrades further. Generate time pressure consequences.

    *   **IF:** Players reach the Peach Grove.
    *   **THEN:** Sanctuary and rest, learn key information, acquire purification resources, temporary hope. Generate relief and character moments.

    *   **IF:** Players confront Izanami with evidence of empathy for her situation.
    *   **THEN:** She responds differently than to violence, possibility of tragic resolution, requires genuine understanding. Generate emotional confrontation.

    *   **IF:** Players escape successfully.
    *   **THEN:** Return to living world but changed, carry pollution, require purification rituals, consequences for choices about Izanami. Generate aftermath and new status quo.

**7. Mechanics & Systems**
*   **Pollution Tracking:** Accumulates from environment and actions. Causes penalties. Creates urgency.
*   **Decay Stages:** Visual and mechanical progression toward becoming part of Yomi. Creates horror and stakes.
*   **Light Management:** Precious resource. Darkness is dangerous. Stealth vs. visibility tradeoffs.
*   **Sound Navigation:** Navigate by audio in absolute darkness. Perception-based gameplay.
*   **Purification Resources:** Limited peaches that reduce pollution. Resource management creates tension.
*   **Izanami's Awareness:** Track her attention. High levels trigger hunting. Stealth and distraction matter.

**8. Theme & Tone Consistency**
*   **Core Themes:** Decay and purity, abandonment and loneliness, the horror of death without transcendence, whether those trapped in darkness have right to trap others, survival against environment itself, the tragedy of Izanami's grief.
*   **Tone Guidance:** Oppressive survival horror with tragic undertones. Dark, desperate, claustrophobic. But not hopeless - tragedy requires the possibility of something better lost. The horror comes from inevitability and the tragic nature of Izanami's situation.
*   **Avoid:** Making it purely grotesque without tragedy, simplifying Izanami into just a monster, ignoring the philosophical questions about death and abandonment, making decay purely cosmetic rather than meaningful, losing the Japanese cultural context.
