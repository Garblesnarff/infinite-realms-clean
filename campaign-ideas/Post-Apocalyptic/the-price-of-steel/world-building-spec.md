### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Price of Steel**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** In the Union, a declining empire locked in perpetual war, there are no true heroes—only survivors making terrible choices. The players are morally compromised individuals (torturer, barbarian, disgraced nobleman, mercenary) who navigate brutal warfare where magic is rare and ugly, leaders are incompetent or cruel, and victory is pyrrhic. They must choose whether to become monsters to fight monsters, or try to keep humanity in a world that punishes decency. There are no good endings, only choices about what you can live with.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the founding of the Union and its perpetual wars with the North and the Gurkish Empire.
    *   Write about the Old Time—the age of Magi and their terrible wars that destroyed ancient empires.
    *   Describe the First of the Magi, Bayaz, and his conflict with Khalul (prophet-mage of the Gurkish).
    *   Explain the rare, disturbing nature of magic—the Art practiced by Magi comes at terrible cost.
    *   Detail the Closed Council and how the Union's democracy is a facade for oligarchy.
    *   Write about the Northern clans, their culture of violence, and King Bethod's unification.
    *   Describe the Gurkish Empire, the Prophet Khalul, and their invasion motivations.
    *   Explain the Eaters—devil-blooded individuals with power but cursed existence.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Union** (Major - Player faction usually)
        *   **Goals:** Maintain power, win wars against North and Gurkish, preserve the oligarchy's privileges.
        *   **Hierarchy:** Closed Council (ruling lords), Lord Marshal (military), Arch Lector (Inquisition), King (powerless figurehead).
        *   **Public Agenda:** Democracy, civilization, order against barbarism.
        *   **Secret Agenda:** The Closed Council cares only for power and wealth. Democracy is theater. Common people are expendable.
        *   **Assets:** Large professional army, Inquisition (torture and espionage), flintlock weapons, Bayaz's support (for now).
        *   **Relationships:** At war with North and Gurkish; manipulated by Bayaz; internally fractured by noble rivalries.

    *   **The Inquisition** (Major - Internal police/torture)
        *   **Goals:** Root out sedition, maintain order through fear, serve the Arch Lector's political agenda.
        *   **Hierarchy:** Arch Lector leads, Superior and lesser Inquisitors beneath, Practicals (torturers/muscle).
        *   **Public Agenda:** Protect the Union from traitors and conspirators.
        *   **Secret Agenda:** The Arch Lector uses the Inquisition for personal power. Many Inquisitors are more monster than protector.
        *   **Assets:** House of Questions (torture chambers), network of informants, legal authority to arrest anyone.
        *   **Relationships:** Feared by everyone; serve the Closed Council nominally but have own agenda; rival noble houses.

    *   **The North (King Bethod's Kingdom)** (Major - Antagonist then ally)
        *   **Goals:** Unity under King Bethod, resist Union expansion, protect clan territories.
        *   **Hierarchy:** King Bethod at top, Named Men (legendary warriors) as champions, clan chiefs beneath.
        *   **Public Agenda:** Freedom for the North, clan honor.
        *   **Secret Agenda:** Bethod made deals with the Other Side (demons) for power to unite clans.
        *   **Assets:** Hardy warriors, knowledge of harsh terrain, Named Men champions, magical support from the Other Side.
        *   **Relationships:** At war with the Union; internally divided between Bethod loyalists and traditional clan system; some clans serve demons.

    *   **The Gurkish Empire** (Major - Antagonist)
        *   **Goals:** Conquer the Union, spread the Prophet Khalul's faith, control Old Empire artifacts.
        *   **Hierarchy:** Emperor (secular ruler), Prophet Khalul (mage-prophet), Hundred Words (magical assassins).
        *   **Public Agenda:** Holy war to spread enlightenment and civilization.
        *   **Secret Agenda:** Khalul seeks revenge against Bayaz and hunts forbidden magical artifacts to win their ancient rivalry.
        *   **Assets:** Massive armies, fanatic devotion, Hundred Words (elite magic-users), superior organization.
        *   **Relationships:** At war with Union; serve Prophet Khalul (who is actually ancient mage); see northerners as irrelevant barbarians.

    *   **Bayaz and the Magi** (Minor - Manipulator faction)
        *   **Goals:** Maintain Bayaz's power over the Union, defeat Khalul, control sources of the Art.
        *   **Hierarchy:** Bayaz as First of the Magi, few remaining apprentices (Yoru Sulfur, Mamun, etc.).
        *   **Public Agenda:** Protect civilization from darkness, guide humanity.
        *   **Secret Agenda:** Bayaz is an ancient tyrant maintaining power through manipulation. His conflict with Khalul is personal, not moral.
        *   **Assets:** Forbidden magic (powered by consuming souls), ancient knowledge, the Seed (ultimate weapon), manipulation of Union leadership.
        *   **Relationships:** Controls the Union from shadows; ancient enemy of Khalul; sees mortals as game pieces.

    *   **Mercenary Companies** (Minor)
        *   **Goals:** Profit, survival, contract fulfillment (mostly).
        *   **Hierarchy:** Captain leads, lieutenants, ordinary mercenaries.
        *   **Public Agenda:** Professional soldiers for hire.
        *   **Secret Agenda:** Loyalty to coin, not cause. Will betray employers if the price is right or survival demands it.
        *   **Assets:** Combat experience, willingness to do dirty work, connections across factions.
        *   **Relationships:** Work for all sides; distrusted but necessary; often more honorable than "civilized" armies.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Bayaz, First of the Magi:** Ancient wizard, arrogant manipulator, claims to protect civilization but is actually ancient tyrant.
    *   **Sand dan Glokta:** Crippled torturer, bitter and brilliant, seeking revenge, capable of surprising compassion.
    *   **Logan Ninefingers / The Bloody-Nine:** Barbarian seeking redemption, contains unstoppable berserker rage.
    *   **Jezal dan Luthar:** Vain nobleman who grows up but becomes powerless puppet king.
    *   **Ferro Maljinn:** Escaped slave consumed by rage, part-devil heritage, incapable of trust.
    *   **King Bethod:** Pragmatic northern king who united clans through demon-deals.
    *   **Arch Lector Sult:** Head of Inquisition, pursuing conspiracy theories, increasingly paranoid and cruel.
    *   **Yoru Sulfur:** Bayaz's servant, powerful mage, utterly loyal, disturbing and inhuman.

*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Union Noble Playing Politics"
    *   "Cynical Veteran Soldier"
    *   "Inquisitor (Torturer)"
    *   "Northern Named Man (Champion)"
    *   "Practical (Inquisition Muscle)"
    *   "Gurkish Hundred Words (Assassin-Mage)"
    *   "Mercenary Captain"
    *   "Incompetent Officer"
    *   "Frightened Conscript"
    *   "Refugee/Civilian Caught in War"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **Adua (Union Capital):**
        *   **Key Landmarks:** The Agriont (noble district on hill), House of Questions (torture chambers), Halls of the Closed Council, slums, the House of the Maker (ancient indestructible tower).
        *   **Primary Inhabitants:** Nobles, commoners, Inquisitors, Practicals, beggars, merchants, soldiers on leave.
        *   **Available Goods & Services:** Black market, luxury goods for nobles, informants, torture-extracted information, mercenary contracts.
        *   **Potential Random Encounters (x5):** Inquisition arrest; noble duel; beggar reveals key information; incompetent noble giving orders; demonstration of Bayaz's power.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Closed Council plans to betray the army." "Bayaz is building something in the House of the Maker." "The King is a puppet."
        *   **Sensory Details:** Sight (contrast between Agriont's elegance and slum's squalor, gallows, Union red), Sound (crowds, screams from House of Questions, noble music), Smell (sewage, perfume, fear).

    *   **The North:**
        *   **Key Landmarks:** Carleon (Bethod's fortress), clan holds in mountains, ancient stone circles with dark power, the High Places.
        *   **Primary Inhabitants:** Clan warriors, Named Men, thralls (slaves), Bethod's court, Hillmen.
        *   **Available Goods & Services:** Weapons, fur, trial-by-combat resolution, harsh wisdom, mercenary work.
        *   **Potential Random Encounters (x5):** Clan feud; finger-game (test of pain tolerance); Shanka (cannibalistic monsters) raid; finding sacrificial site; challenging a Named Man.
        *   **Embedded Plot Hooks & Rumors (x3):** "Bethod speaks with the Other Side." "The Bloody-Nine's legend grows." "Some clans still resist Bethod."
        *   **Sensory Details:** Sight (harsh mountains, rough stone holds, furs and leather), Sound (wind, battle-songs, silence of snow), Smell (peat fires, unwashed bodies, blood on snow).

    *   **Dagoska (Besieged City):**
        *   **Key Landmarks:** Harbor (cut off), walls (bombarded), Upper City (still wealthy), Lower City (starving), the docks.
        *   **Primary Inhabitants:** Union garrison, civilians (starving), incompetent governor, Gurkish besiegers outside.
        *   **Available Goods & Services:** Rationed food (black market prices), desperation contracts, information about Gurkish plans.
        *   **Potential Random Encounters (x5):** Starvation riot; Gurkish bombardment; traitor discovered; disease outbreak; desperate sortie.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Governor hoards food while people starve." "Gurkish will breach the walls soon." "A relief force is coming (it's not)."
        *   **Sensory Details:** Sight (damaged walls, smoke, emaciated civilians, Gurkish camps beyond), Sound (bombardment, weeping, angry crowds), Smell (starvation, disease, smoke, death).

    *   **The Old Empire Ruins:**
        *   **Key Landmarks:** Aulcus (ruined capital), Kanedias's Foundry (where the Seed was made), collapsed temples, monster nests.
        *   **Primary Inhabitants:** Shanka (cannibals), Eaters (devil-blooded creatures), ancient automated defenses, spirits.
        *   **Available Goods & Services:** None—only death and cursed artifacts.
        *   **Potential Random Encounters (x5):** Shanka pack attack; encounter with an Eater; ancient weapon activation; ruins collapse; discovery of forbidden knowledge.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Seed can destroy armies." "Kanedias built it consuming thousands of souls." "The ruins remember the Old Time's atrocities."
        *   **Sensory Details:** Sight (cyclopean architecture, broken carvings, wrong geometry), Sound (Shanka clicking, wind through ruins, ancient echoes), Smell (decay, sulfur, wrongness).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** Logan succumbs to the Bloody-Nine in a critical moment.
    *   **THEN:** He wins the battle but kills allies in the rage. Survivors fear him. He loses further control over the berserker. Generate aftermath of friendly fire and reputation damage.

    *   **IF:** Players gain high Moral Compromise.
    *   **THEN:** They become effective but monstrous. NPCs react with fear or respect (not love). Certain redemptive paths close. Generate consequences of becoming what they fought.

    *   **IF:** Players ally with Bayaz fully.
    *   **THEN:** They gain power and victory, but become his tools. They must commit atrocities "for the greater good." Generate missions requiring soul-crushing choices.

    *   **IF:** Players oppose Bayaz.
    *   **THEN:** They likely lose (he's nearly unstoppable), but maintain moral integrity. Generate desperate resistance and likely tragic ends.

    *   **IF:** The siege of Dagoska falls.
    *   **THEN:** Gurkish gain foothold, Union morale collapses. Players must escape or be captured. Generate desperate evacuation and Gurkish occupation.

    *   **IF:** Bethod is defeated before his demon pact is revealed.
    *   **THEN:** The North fractures again. But demons still have claim on northern souls. Generate clan civil war and demonic manifestation.

    *   **IF:** Players use the Seed (forbidden weapon).
    *   **THEN:** They destroy the enemy but consume countless souls, including their own humanity. The weapon corrupts them. Generate moral reckoning with mass murder.

    *   **IF:** Players try to stay "good" throughout.
    *   **THEN:** They're less effective, often fail, but maintain their souls. The world doesn't reward this—but they can live with themselves. Generate pyrrhic moral victories and respect from unexpected sources.
