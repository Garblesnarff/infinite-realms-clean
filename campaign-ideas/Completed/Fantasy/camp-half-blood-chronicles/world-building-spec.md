### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**Camp Half-Blood Chronicles**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The players are demigods—children of Greek gods and mortal parents—who discover their divine heritage and train at Camp Half-Blood. When Zeus's Master Bolt is stolen and the Summer Solstice deadline approaches, the party must quest across modern America to retrieve it from the Underworld, battling monsters and navigating godly politics. They discover the theft is part of a larger plot by Kronos (the Titan King) to start a divine war and escape his prison in Tartarus. The campaign explores heroism, parental relationships, prophecy versus choice, and found family.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the Titanomachy—the ancient war where Zeus and the Olympians overthrew Kronos and the Titans, banishing them to Tartarus.
    *   Write the history of demigods throughout human history—heroes like Hercules, Perseus, Theseus—and how their legacies shaped mythology.
    *   Describe the creation of Camp Half-Blood by Chiron and the gods as a safe haven for demigods in the modern age.
    *   Explain the Mist—magical energy that prevents mortals from seeing mythological truth, showing them mundane explanations instead (a sword looks like a bat, a monster looks like a large dog).
    *   Detail the prophecy system—how the Oracle of Delphi speaks Apollo's visions in cryptic verse, guiding and warning demigods of their fates.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Olympian Gods** (Major)
        *   **Goals:** Maintain their rule over Western Civilization's heart (currently centered in New York), prevent Titan resurgence, manage their demigod children.
        *   **Hierarchy:** The Twelve Olympians, led by Zeus (king), with minor gods serving beneath them.
        *   **Public Agenda:** Unknown to mortals (hidden by the Mist); to demigods: protect the mortal world from monsters and Titans.
        *   **Secret Agenda:** The gods are flawed, petty, and often neglectful parents who see demigods as tools and occasionally nuisances.
        *   **Assets:** Divine powers, Olympus (600th floor of Empire State Building), control over natural forces, immortality.
        *   **Relationships:** Rule over demigods, monsters, and minor gods; increasingly dysfunctional family politics; threatened by Titan resurgence.
    *   **Camp Half-Blood** (Major)
        *   **Goals:** Train demigods to survive, complete quests, and defend Olympus.
        *   **Hierarchy:** Led by Chiron (activities director) and Mr. D/Dionysus (reluctant camp director as punishment). Cabin counselors lead their siblings.
        *   **Public Agenda:** Safe haven and training ground for demigods.
        *   **Secret Agenda:** Prepares child soldiers for the coming Titan War, though most campers don't realize it yet.
        *   **Assets:** Magical barrier (protects from monsters), training facilities, Oracle of Delphi, Celestial Bronze weapons.
        *   **Relationships:** Loyal to Olympus; shelters demigods from all parents; rival to Camp Jupiter (Roman demigod camp).
    *   **The Titans (Hidden/Rising)** (Major - Antagonists)
        *   **Goals:** Escape Tartarus, overthrow the Olympians, reclaim rule over the world.
        *   **Hierarchy:** Led by Kronos (the Titan King), supported by other Titans (Atlas, Hyperion, etc.) and demigod traitors.
        *   **Public Agenda:** None—most demigods don't know they're rising.
        *   **Secret Agenda:** Manipulate demigods resentful of godly neglect (like Luke) to weaken Olympus from within.
        *   **Assets:** Ancient power, ability to whisper from Tartarus, demigod traitors, monsters loyal to the old regime.
        *   **Relationships:** Opposed by Olympus; recruit bitter demigods; command primordial monsters.
    *   **Monsters** (Minor - Widespread)
        *   **Goals:** Hunt demigods (their scent attracts them), serve dark powers, cause chaos.
        *   **Hierarchy:** Some serve gods, some serve Titans, some act independently. Echidna is Mother of Monsters.
        *   **Public Agenda:** None—hidden by the Mist from mortals.
        *   **Secret Agenda:** Weaken the gods by killing their children; many sense Kronos's return and grow bolder.
        *   **Assets:** Immortality (reform in Tartarus when killed), natural weapons, ability to track demigod scent.
        *   **Relationships:** Enemies of demigods and gods; some commanded by Titans or dark gods.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Chiron:** Ancient centaur, trainer of heroes for millennia, activities director at Camp Half-Blood, wise and patient mentor figure.
    *   **Luke Castellan:** Son of Hermes, charismatic counselor, secretly serves Kronos due to bitterness about godly neglect, the Master Bolt thief.
    *   **Annabeth Chase:** Daughter of Athena, brilliant tactician, proud and loyal, becomes the party's ally and strategist.
    *   **Grover Underwood:** Satyr protector assigned to guard demigods, nervous but brave, searches for the lost god Pan.
    *   **Ares:** God of war, manipulated by Kronos into stealing the bolt and helm, aggressive and conflict-loving.
    *   **Zeus:** King of the gods, lord of the sky, paranoid about his stolen Master Bolt, quick to anger.
    *   **Poseidon:** God of the sea, Zeus's brother, accused of the theft, more sympathetic to his demigod children than most gods.
    *   **Hades:** God of the dead, rules the Underworld, his Helm of Darkness also stolen, suspects demigods.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Child of Ares (Aggressive, competitive, battle-focused demigod)"
    *   "Child of Athena (Intelligent, strategic, pride-driven demigod)"
    *   "Child of Apollo (Healer, archer, artistic demigod)"
    *   "Child of Hermes (Trickster, thief, messenger demigod)"
    *   "Satyr Protector (Nervous, nature-loving, loyal guide)"
    *   "Minor God (Lesser Olympian or nature spirit with specific domain)"
    *   "Monster (Minotaur, Fury, Hellhound, Chimera, Medusa, etc.)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **Camp Half-Blood:**
        *   **Key Landmarks:** The Big House (HQ), twelve cabins (one per Olympian), training arena, forge (Hephaestus cabin), archery range (Apollo cabin), strawberry fields, the Oracle's cave, magical barrier.
        *   **Primary Inhabitants:** Demigods (ages 7-19), Chiron, Mr. D/Dionysus, satyrs, dryads, naiads.
        *   **Available Goods & Services:** Combat training, quest preparation, prophecies from the Oracle, magical weapon forging, healing.
        *   **Potential Random Encounters (x5):** Capture the Flag game in progress, chariot race, cabin rivalry escalating, monster testing the barrier, new demigod arrival.
        *   **Embedded Plot Hooks & Rumors (x3):** "Some campers never return from quests." "The Oracle's prophecies always come true, but not how you expect." "Luke seems troubled lately—spending time alone."
        *   **Sensory Details:** Sight (Orange camp shirts, white Greek columns, strawberry fields, magical barrier shimmer), Sound (Swords clashing, campers laughing, Capture the Flag horns), Smell (Strawberries, campfire smoke, sea breeze from Long Island Sound).
    *   **The Underworld:**
        *   **Key Landmarks:** The River Styx (black water, ferryman Charon), Fields of Asphodel (gray eternity for average souls), Elysium (paradise for heroes), Tartarus (prison of Titans, deepest darkness), Hades' palace (obsidian throne room).
        *   **Primary Inhabitants:** Shades of the dead, Hades and Persephone, Charon, Cerberus (three-headed dog), the Furies, judges of the dead.
        *   **Available Goods & Services:** None for the living—a realm of death. Possibly bargains with Hades (dangerous).
        *   **Potential Random Encounters (x5):** Shades pleading to be remembered, Cerberus patrolling, Furies investigating intruders, souls being judged, whispers from Tartarus.
        *   **Embedded Plot Hooks & Rumors (x3):** "Hades is not the villain—he's a victim too." "Tartarus is weakening—the Titans stir." "The Helm of Darkness grants invisibility and fear."
        *   **Sensory Details:** Sight (Gray stone, black rivers, pale wandering souls, distant hellfire), Sound (Whispers, Cerberus growling, river flowing, echoing footsteps), Smell (Sulfur, dampness, decay, cold air).
    *   **Olympus (Empire State Building):**
        *   **Key Landmarks:** The throne room (twelve massive thrones), gardens of eternal spring, armory, temples to each god, view of New York from divine heights.
        *   **Primary Inhabitants:** The Twelve Olympians, minor gods, nature spirits, divine servants.
        *   **Available Goods & Services:** Audience with gods, divine boons, judgment on quests.
        *   **Potential Random Encounters (x5):** Gods arguing, Hera's peacocks roaming, Hephaestus working on divine weapons, Apollo performing music, Artemis's hunters passing through.
        *   **Embedded Plot Hooks & Rumors (x3):** "The gods are preparing for war—again." "Some gods sympathize with demigods; others see them as annoyances." "Kronos's influence reaches even here."
        *   **Sensory Details:** Sight (White marble, gold accents, celestial sky, massive god-sized thrones), Sound (Divine music, godly arguments, thunder from Zeus), Smell (Ambrosia, fresh flowers, ozone from lightning).
    *   **Medusa's Emporium (Roadside Trap):**
        *   **Key Landmarks:** Garden gnome statues (petrified victims), Aunty Em's storefront, stone garden, Medusa's lair (basement).
        *   **Primary Inhabitants:** Medusa (disguised as Aunty Em), potential victims (travelers).
        *   **Available Goods & Services:** False hospitality, food (laced with slow-acting paralysis), "photo opportunities" (petrification trap).
        *   **Potential Random Encounters (x5):** Medusa offering food, party recognizes petrified victims as stone statues, reflection puzzle to avoid her gaze, escape chase.
        *   **Embedded Plot Hooks & Rumors (x3):** "Never look directly at Aunty Em." "The garden gnomes look too realistic." "Medusa was once beautiful—cursed by Athena."
        *   **Sensory Details:** Sight (Too-realistic statues in terror poses, Medusa's serpent hair hidden by scarf), Sound (Hissing snakes, forced cheerfulness), Smell (Cooking meat, stone dust, reptilian musk).
    *   **Lotus Casino (Las Vegas Time Trap):**
        *   **Key Landmarks:** Endless arcade games, luxury suites, all-you-can-eat buffet, cash exchange (time for tokens).
        *   **Primary Inhabitants:** Trapped guests from various decades, casino staff (immortal servants).
        *   **Available Goods & Services:** Infinite entertainment, free food and lodging, time itself (unwittingly traded away).
        *   **Potential Random Encounters (x5):** A guest from the 1970s unaware of modern technology, addictive arcade game, party realizes hours have become days, desperate escape attempt.
        *   **Embedded Plot Hooks & Rumors (x3):** "Time doesn't work right here—you could lose days." "No one leaves the Lotus Casino willingly." "The lotus flowers in the food cause memory loss."
        *   **Sensory Details:** Sight (Neon lights, infinite arcade floor, guests in outdated fashion), Sound (Bells, music, laughter, game sounds), Smell (Lotus flowers, popcorn, recycled air).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The party fails to retrieve the Master Bolt by the Summer Solstice.
    *   **THEN:** Generate the beginning of a divine war—Zeus and Poseidon clash, causing natural disasters (hurricanes, earthquakes). The party must seek a ceasefire while being hunted as failures.
    *   **IF:** The party confronts Luke before he's ready to reveal his betrayal.
    *   **THEN:** Generate a premature confrontation where Luke escapes, taking critical information. The prophecy is incomplete, and the party must adapt.
    *   **IF:** The party defeats Ares in combat on the beach.
    *   **THEN:** Generate Ares's grudging respect and the gods' surprise—demigods who can defeat gods are both valuable and dangerous. Ares becomes a recurring antagonist.
    *   **IF:** The party negotiates with Hades successfully.
    *   **THEN:** Generate Hades as a reluctant ally—he provides information about Kronos's stirring and may aid in future quests (unlike other gods who ignore demigods).
    *   **IF:** The party loses too much time in the Lotus Casino.
    *   **THEN:** Generate a rush scenario—the Summer Solstice passes, and the party must prevent war already begun. Increased difficulty and consequences.
    *   **IF:** The party reveals Kronos's involvement to the gods.
    *   **THEN:** Generate mixed reactions—Zeus dismisses it (hubris), Poseidon and Athena take it seriously, the gods begin preparing for the Titan War (though they won't admit it publicly).
    *   **IF:** The party embraces their divine heritage and seeks godly parents' favor.
    *   **THEN:** Generate boons and blessings—magical items, divine guidance, increased powers. But also increased expectations and pressure from godly parents.
    *   **IF:** The party rejects the gods and sides with Luke's perspective.
    *   **THEN:** Generate a tragic path where they join Kronos's army, becoming antagonists in future campaigns. The gods hunt them as traitors.
