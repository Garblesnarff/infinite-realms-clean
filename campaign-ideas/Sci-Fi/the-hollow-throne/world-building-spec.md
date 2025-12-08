# World-Building Specification Brief: The Hollow Throne

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Hollow Throne**

**1. Core Concept & Narrative Hook**
* **Directive:** This is the foundational context. All generated content must align with this core premise.
* **Content:** Deep beneath the mountains lies Karak-Thun, the greatest dwarven kingdom ever carved from stone. For three thousand years, the Hollow Throne has stood empty, its rightful heir lost to legend. When the party discovers an ancient heir with legitimate claim, they're thrust into a brutal civil war between seven noble houses, each with their own vision for the kingdom's future. As ancient tunnels collapse, resources dwindle, and something stirs in the deepest mines, the party must navigate deadly politics and decide the fate of an underground civilization on the brink of collapse.

**2. Lore & History Primer**
* **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
* **Prompts:**
    * Detail the founding of Karak-Thun three thousand years ago by King Durin Deepdelver and the original compact between the seven founding clans.
    * Write the history of the last king, Thordak the Mad, who made a pact with an entity from the deep and then disappeared, leaving the throne empty.
    * Describe the Treaty of the Hollow Throne—the agreement that left the throne empty for 3,000 years rather than risk civil war.
    * Explain the dwarven caste system in Karak-Thun: the noble houses, the artisan guilds, the warrior clans, and the deep miners.
    * Detail the architecture and engineering of Karak-Thun: how they carved entire cities from solid rock, managed air circulation, water systems, and food production underground.
    * Write the legend of the Ancestor Stones—magical runestones that grant legitimacy to rule but can only be activated by true royal blood.
    * Describe the religious beliefs of Karak-Thun: worship of the Stone Father (god of mountains), the Forge Mother (goddess of creation), and the Dark Below (forbidden god of the depths).
    * Explain the collapse crisis: why the ancient tunnels are failing, the engineering challenges, and the resource shortages it creates.

**3. Faction Deep-Dive**
* **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
* **Factions Roster:**
    * **House Ironforge** (Major)
        * **Goals:** Seize the throne through military might and restore absolute monarchy.
        * **Hierarchy:** Led by Lady Brunhilde Ironforge; military generals and weapon smiths form the leadership council.
        * **Public Agenda:** Strong leadership is needed to save the kingdom from collapse.
        * **Secret Agenda:** Lady Brunhilde killed her own son to prevent a previous civil war; she seeks the throne to absolve her guilt.
        * **Assets:** Largest military force, best weapon smiths, control of primary iron mines.
        * **Relationships:** Allied with House Blackstone through marriage pacts; hostile to House Goldvein.
    * **House Blackstone** (Major)
        * **Goals:** Establish trial by combat as the sole means of determining rulership.
        * **Hierarchy:** War Chief Durak Blackstone leads; meritocracy based on combat prowess.
        * **Public Agenda:** Only the strongest should rule; tradition of warrior kings.
        * **Secret Agenda:** Durak has been corrupted by whispers from the deep and secretly serves the entity below.
        * **Assets:** Elite warriors, gladiatorial pits, volcanic forges that can work adamantine.
        * **Relationships:** Military alliance with Ironforge; philosophical opposition to Goldvein's diplomacy.
    * **House Goldvein** (Major)
        * **Goals:** Prevent the throne from being filled; maintain the status quo of house confederation.
        * **Hierarchy:** Princess Helga Goldvein leads a council of merchant lords and diplomats.
        * **Public Agenda:** The empty throne has kept peace for 3,000 years; filling it invites tyranny.
        * **Secret Agenda:** House Goldvein is bankrupt and has been embezzling from other houses; war would expose their fraud.
        * **Assets:** Richest house (on paper), control of gem mines and crystal caverns, extensive spy network.
        * **Relationships:** Leading the diplomatic faction; allied with Silverbeard and Copperhelm.
    * **House Silverbeard** (Major)
        * **Goals:** Elect the king through democratic vote of all houses.
        * **Hierarchy:** Council of Elders representing different districts; emphasis on scholarship.
        * **Public Agenda:** Enlightened democracy, not hereditary monarchy, should determine leadership.
        * **Secret Agenda:** They possess ancient texts suggesting the throne's emptiness is intentional—a safeguard against the deep pact.
        * **Assets:** Libraries, arcane knowledge, innovative engineering, educational institutions.
        * **Relationships:** Allied with Goldvein's peace faction; philosophical rivalry with Stonemantle.
    * **House Copperhelm** (Major)
        * **Goals:** Secure trade routes and maintain economic stability regardless of who rules.
        * **Hierarchy:** Merchant Princes; leadership determined by wealth and trade influence.
        * **Public Agenda:** Economic prosperity before political ideology; whoever can restore trade gets their support.
        * **Secret Agenda:** They have secret trade agreements with the surface world and would sell out the kingdom for profit.
        * **Assets:** Control of main trade routes, merchant fleet (underground river barges), food storage.
        * **Relationships:** Neutral in the war, selling to all sides; pragmatic alliance with Goldvein.
    * **House Stonemantle** (Major)
        * **Goals:** Restore theocratic rule with a priest-king chosen by the gods.
        * **Hierarchy:** High Priest Council led by Patriarch Grimstone; religious authority.
        * **Public Agenda:** Divine mandate should determine rulership; the heir must prove worthiness through religious trials.
        * **Secret Agenda:** They know the truth about Thordak's pact and believe filling the throne will trigger apocalypse.
        * **Assets:** Religious authority, control of the Ancestor Vault and sacred sites, devoted followers.
        * **Relationships:** Ideological opposition to secular Silverbeard; uneasy alliance with Goldvein to keep throne empty.
    * **House Shadowforge** (Major)
        * **Goals:** Assassinate all claimants and let the throne remain empty forever.
        * **Hierarchy:** Secret society structure; led by shadowy council called the Empty Circle.
        * **Public Agenda:** None—they operate entirely through proxies and agents.
        * **Secret Agenda:** They are descendants of the assassins who killed King Thordak; they know the full truth of the deep pact.
        * **Assets:** Spy network, assassins, blackmail material on every house, secret passages throughout the kingdom.
        * **Relationships:** No public alliances; infiltrators in every house; ultimate wildcards.
    * **The Deep Cult** (Hidden)
        * **Goals:** Awaken Grendok the Deep and transform all dwarves into servants of the entity.
        * **Hierarchy:** Led by corrupted deep miners who first heard the whispers; Durak Blackstone is a high-ranking but unwitting member.
        * **Public Agenda:** None—they masquerade as members of other houses.
        * **Secret Agenda:** Cause the civil war to weaken defenses and feed the deep entity with blood and chaos.
        * **Assets:** Ancient magic from the deep, corrupted monsters, ability to cause tunnel collapses.
        * **Relationships:** Infiltrated into all houses, particularly Blackstone and deep mining operations.
    * **The Lost Heir's Faction** (Player-Aligned)
        * **Goals:** Unite the kingdom under legitimate rule and stop both the civil war and the deep threat.
        * **Hierarchy:** The heir, the party, and whatever allies they recruit.
        * **Public Agenda:** Restore the ancient compact and bring peace.
        * **Secret Agenda:** Varies based on the heir's development and player choices.
        * **Assets:** Legitimacy (if proven), player party capabilities, potential alliances.
        * **Relationships:** Initially neutral with all houses; shifts based on player actions.

**4. NPC Generation Roster**
* **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
* **Tier 1 (Unique, Major NPCs):**
    * **Thorgrim Stoneheart:** The lost heir, half-dwarf raised on the surface, idealistic but naive, suffers from claustrophobia.
    * **Lady Brunhilde Ironforge:** Iron Matriarch, haunted by killing her own son, ruthlessly practical, military genius.
    * **Durak Blackstone:** War Chief, honorable warrior being slowly corrupted by deep whispers, tragic figure.
    * **Princess Helga Goldvein:** Young diplomatic leader, idealistic, hiding her house's bankruptcy, potential romantic interest.
    * **Keeper Malgrim:** Ancient lorekeeper, neutral arbiter of law and tradition, knows the truth about the throne.
    * **Grendok the Deep:** The corrupted former king, now an eldritch entity, mad but with fragments of nobility remaining.
    * **Patriarch Grimstone:** High Priest of Stonemantle, fanatic believer trying to prevent apocalypse.
    * **Merchant Prince Brassbelly (Copperhelm):** Pragmatic trader selling to all sides, secretly dealing with surface world.
    * **Elder Runebeard (Silverbeard):** Democratic reformer, scholarly, possesses dangerous knowledge about the throne's curse.
    * **The Empty Hand:** Mysterious leader of House Shadowforge, identity unknown, could be anyone.
* **Tier 2 & 3 (Archetypes for Generation):**
    * "Ironforge Heavy Infantry Sergeant"
    * "Blackstone Gladiator Champion"
    * "Goldvein Spy and Diplomat"
    * "Silverbeard Scholar-Engineer"
    * "Copperhelm Merchant Negotiator"
    * "Stonemantle War Priest"
    * "Shadowforge Assassin"
    * "Deep Cult Corrupted Miner"
    * "Refugee from Collapsed Tunnels"
    * "Artisan Guild Representative"
    * "Royal Guard Loyal to the Heir"
    * "Deep Creature (Whisperer, Corrupted, Ancient)"

**5. Location Blueprints**
* **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
* **Location Roster:**
    * **The Hollow Court:** Ancient parliament chamber, circular with seven house sections, dominated by the empty obsidian throne at center.
        * **Key Landmarks:** The Hollow Throne (obsidian, massive, empty for 3,000 years), Seven House Galleries, the Judgment Circle, the Ancestor Stones.
        * **Primary Inhabitants:** House representatives, guards, political operatives, neutral servants.
        * **Available Goods & Services:** Political negotiations, legal arbitration, intelligence gathering, alliance formation.
        * **Potential Random Encounters (x5):** Assassination attempt during session, diplomatic duel of words, discovery of spy, house representatives arguing, mysterious sabotage of house banner.
        * **Embedded Plot Hooks & Rumors (x3):** "The Shadowforge have infiltrated the guard." "House Goldvein is bankrupt." "The throne whispers to those who touch it."
        * **Sensory Details:** Sight (massive obsidian throne, house banners, torch-lit chamber), Sound (echoing voices, formal proclamations, whispers), Smell (stone, torch smoke, tension).
    * **The Adamant Halls (House Ironforge Territory):** Military fortress and forge complex, all angles and iron.
        * **Key Landmarks:** The Iron Throne Room (lesser throne of iron), the Grand Forge, the Armory Vault, the War Chamber, Lady Brunhilde's private quarters.
        * **Primary Inhabitants:** Ironforge military, weapon smiths, strategic planners, soldiers in training.
        * **Available Goods & Services:** Weapon and armor smithing (best quality), military training, strategic intelligence, mercenary contracts.
        * **Potential Random Encounters (x5):** Military drill in progress, weapon testing gone wrong, strategic briefing the party overhears, soldier challenges party to duel, forge accident.
        * **Embedded Plot Hooks & Rumors (x3):** "Lady Brunhilde is haunted by her past." "A secret forge produces weapons for Blackstone." "The heir's bloodline records are kept in the vault."
        * **Sensory Details:** Sight (angular iron architecture, weapons everywhere, military precision), Sound (hammering, marching, shouted commands), Smell (hot metal, coal smoke, weapon oil).
    * **The Black Pits (House Blackstone Territory):** Gladiatorial complex built into volcanic rock, brutal and hot.
        * **Key Landmarks:** The Great Arena, the Champion's Gate, the Volcanic Forges, Durak's War Hall, the Warrior's Cemetery.
        * **Primary Inhabitants:** Gladiators, warriors, forge masters, spectators, beast handlers.
        * **Available Goods & Services:** Gladiatorial combat participation, adamantine smithing, warrior training, proving grounds.
        * **Potential Random Encounters (x5):** Forced to fight in arena, challenged to honor duel, witness execution by combat, volcanic eruption threatens area, corrupted warrior attacks randomly.
        * **Embedded Plot Hooks & Rumors (x3):** "Durak has been acting strange lately." "Champions who go too deep never return the same." "The volcanic forges connect to the Forgotten Deeps."
        * **Sensory Details:** Sight (red glow from lava, obsidian architecture, blood on arena sand), Sound (roaring crowds, combat, volcanic rumbling), Smell (sulfur, blood, ash).
    * **The Gemstone Gardens (House Goldvein Territory):** Once opulent, now showing signs of disrepair, crystal caverns.
        * **Key Landmarks:** The Crystal Palace, the Treasury (mostly empty), the Diamond Gallery, the Spy's Bazaar, Helga's Court.
        * **Primary Inhabitants:** Goldvein diplomats, spies, merchants, servants maintaining appearances.
        * **Available Goods & Services:** Diplomatic negotiation, spy recruitment, information brokering, gem cutting (but limited stock).
        * **Potential Random Encounters (x5):** Elaborate ball hiding financial distress, spy exchange of information, party catches embezzlement in action, assassination attempt on Helga, creditor confrontation.
        * **Embedded Plot Hooks & Rumors (x3):** "The treasury is empty." "Helga is personally investigating the embezzlement." "Goldvein spies are everywhere."
        * **Sensory Details:** Sight (crystal formations, faded opulence, careful lighting to hide wear), Sound (whispered conversations, subtle music), Smell (perfumes hiding decay, crystal dust).
    * **The Great Library (House Silverbeard Territory):** Vast repository of knowledge, engineering marvels, scholarly atmosphere.
        * **Key Landmarks:** The Archive of Kings, the Engineering Labs, the Democratic Forum, the Forbidden Section.
        * **Primary Inhabitants:** Scholars, engineers, students, archivists, democratic reformers.
        * **Available Goods & Services:** Research assistance, engineering consultation, education, revolutionary ideas.
        * **Potential Random Encounters (x5):** Discovery of dangerous knowledge, engineering experiment goes wrong, democratic debate turns violent, spy stealing documents, revelation about the throne's curse.
        * **Embedded Plot Hooks & Rumors (x3):** "Silverbeard knows why the throne is empty." "The engineering labs have a solution to the collapse crisis." "Democratic revolution is brewing."
        * **Sensory Details:** Sight (endless shelves, complex machinery, blackboards with equations), Sound (turning pages, quiet discussion, machinery humming), Smell (old parchment, ink, oil from machines).
    * **The Trading Warrens (House Copperhelm Territory):** Bustling underground market, neutral ground, economic hub.
        * **Key Landmarks:** The Grand Bazaar, the River Docks, the Currency Exchange, the Smuggler's Gate, the Neutral Inn.
        * **Primary Inhabitants:** Merchants, traders, smugglers, refugees, agents from all houses.
        * **Available Goods & Services:** Buy/sell any goods, hire smugglers, gather rumors, neutral meeting ground.
        * **Potential Random Encounters (x5):** Market day chaos, smuggling deal gone wrong, refugee crisis, price gouging riot, surface traders in disguise.
        * **Embedded Plot Hooks & Rumors (x3):** "Copperhelm trades with the surface." "The River Docks connect to the Forgotten Deeps." "You can buy anything here, even loyalty."
        * **Sensory Details:** Sight (crowded stalls, diverse goods, busy river docks), Sound (haggling, river water, crowd noise), Smell (food, spices, river dampness, too many people).
    * **The Temple Quarter (House Stonemantle Territory):** Sacred district, ancient temples, heavy with religious atmosphere.
        * **Key Landmarks:** The Temple of the Stone Father, the Forge Mother's Shrine, the Ancestor Vault, the Sealed Shrine (Dark Below).
        * **Primary Inhabitants:** Priests, pilgrims, temple guards, religious scholars, fanatics.
        * **Available Goods & Services:** Healing, divination, religious counsel, access to Ancestor Vault (restricted).
        * **Potential Random Encounters (x5):** Religious ceremony, fanatic accosts party about legitimacy, divine vision or omen, discovery in Ancestor Vault, Dark Below cultist infiltration.
        * **Embedded Plot Hooks & Rumors (x3):** "The priests know the truth about Thordak." "The Ancestor Vault holds proof of the heir's bloodline." "The Dark Below cult is growing."
        * **Sensory Details:** Sight (religious iconography, holy flames, tomb architecture), Sound (chanting, prayer, echoing hymns), Smell (incense, candle wax, ancient stone).
    * **The Shadowforge Quarter (House Shadowforge Territory):** Hard to find, intentionally confusing, paranoid atmosphere.
        * **Key Landmarks:** The Empty Chamber (headquarters, location shifts), the Secret Archives, the Assassination Guild Hall, the Hidden Passages network.
        * **Primary Inhabitants:** Assassins, spies, information brokers, rogues, those who want to disappear.
        * **Available Goods & Services:** Assassination contracts, blackmail material, secret passage access, identity changes.
        * **Potential Random Encounters (x5):** Followed by unseen presence, assassination attempt, blackmail offer, discovery of secret passage, meeting with the Empty Hand.
        * **Embedded Plot Hooks & Rumors (x3):** "Shadowforge killed King Thordak." "They have blackmail on every house." "The Empty Hand is actually one of the other house leaders."
        * **Sensory Details:** Sight (shadows, hidden doors, paranoid glances), Sound (barely audible footsteps, whispers, silence), Smell (poison, darkness, fear).
    * **The Forgotten Deeps (Deep Threat Territory):** Abandoned mining levels, corrupted atmosphere, source of the threat.
        * **Key Landmarks:** The Whispering Caverns, the Corrupted Throne Room (Grendok's lair), the Deep Forges (overrun), the Breach (where the entity entered).
        * **Primary Inhabitants:** Corrupted miners, deep creatures, cultists, things that should not be, Grendok the Deep.
        * **Available Goods & Services:** None. This is pure dungeon/horror territory.
        * **Potential Random Encounters (x5):** Whispers offering power, corrupted creature attack, cave-in or structural failure, discovery of cult ritual site, vision of the past showing Thordak's pact.
        * **Embedded Plot Hooks & Rumors (x3):** "This is where Thordak made his pact." "The entity feeds on blood and chaos." "Some who come here are transformed."
        * **Sensory Details:** Sight (unnatural darkness, bio-luminescent fungi, wrongness), Sound (whispers, scraping, things moving in dark), Smell (decay, corruption, ancient evil).

**6. Causality Chains & Dynamic World States**
* **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
* **Triggers:**
    * **IF:** The party publicly presents the heir's claim with proof.
    * **THEN:** The seven houses fracture into three factions: Support Heir (Silverbeard, maybe others), Oppose Heir (Ironforge, Blackstone), Neutral Merchants (Copperhelm). Civil war becomes inevitable. Generate faction war mechanics.
    * **IF:** The party sides with House Ironforge.
    * **THEN:** They gain military might but face moral compromises. Lady Brunhilde assigns increasingly brutal missions. Other houses unite against Ironforge. Generate military campaign structure.
    * **IF:** The party sides with House Goldvein's peace faction.
    * **THEN:** They work to prevent the throne from being filled. Must manage complex diplomatic missions. Eventually discover Goldvein's bankruptcy. Generate diplomatic crisis scenarios.
    * **IF:** The party discovers House Goldvein's embezzlement.
    * **THEN:** Can blackmail Goldvein, expose them publicly (destroying peace faction), or help cover it up. Each choice has major political ramifications. Generate branching consequences.
    * **IF:** The party kills Durak Blackstone before discovering his corruption.
    * **THEN:** House Blackstone becomes implacable enemy. The deep corruption spreads to Blackstone's successor. Generate revenge scenarios and escalating corruption.
    * **IF:** The party frees Durak from corruption.
    * **THEN:** Blackstone becomes loyal ally but is weakened. Durak helps them understand the deep threat. Deep cult targets them for elimination. Generate redemption arc and cult attacks.
    * **IF:** The party enters the Forgotten Deeps too early (before level 10).
    * **THEN:** They face overwhelming horror encounters. May suffer corruption or madness. Must retreat or risk death. Generate horror escalation and escape scenarios.
    * **IF:** The party touches the Hollow Throne before proving legitimacy.
    * **THEN:** The throne rejects them, possibly dealing damage or cursing them. Rumors spread about their unworthiness. Generate political fallout and curse mechanics.
    * **IF:** The heir proves their bloodline with the Ancestor Stones.
    * **THEN:** Stonemantle recognizes legitimacy but reveals the throne's curse. Must now decide whether to risk filling it. Generate theological crisis and the revelation of Thordak's pact.
    * **IF:** The party learns the full truth of Thordak's pact.
    * **THEN:** They discover that filling the throne will either bind the entity or release it, depending on the heir's worthiness. Generate moral dilemma scenarios and trials.
    * **IF:** The civil war continues past 20 sessions without resolution.
    * **THEN:** Resource shortages become critical. Food riots, entire districts sealed off, mass casualties. The deep threat grows stronger. Generate collapse scenarios and urgency mechanics.
    * **IF:** The party makes an alliance between three or more houses.
    * **THEN:** Combined faction becomes powerful enough to force others to negotiate. Generate grand alliance politics and united military campaigns.
    * **IF:** The party attempts to take the throne for themselves (non-heir PC).
    * **THEN:** If they can prove worthiness through trials, it becomes possible. Houses fracture based on whether they accept usurper. Generate legitimacy crisis and player-king scenarios.
    * **IF:** The party defeats Grendok without resolving the civil war.
    * **THEN:** The deep threat is contained but the kingdom remains fractured. Generate post-war scenarios with permanent faction divisions.
    * **IF:** The party crowns the heir successfully.
    * **THEN:** Must manage the pact's consequences, rebuild the kingdom, and deal with the aftermath. Generate ruling scenarios and reconstruction challenges.
    * **IF:** The party chooses to evacuate rather than resolve the conflict.
    * **THEN:** They must organize mass exodus to surface while holding off both civil war and deep threat. Generate escape sequence and refugee crisis scenarios.

**7. Resource Tracking System**
* **Directive:** Implement kingdom-wide resource management affecting all storylines.
* **Resources to Track:**
    * **Food Supplies:** Measured in "weeks of supply." Decreases based on tunnel collapses cutting off farms. Can be raided, traded, or produced.
    * **Water Quality:** Measured in "purity levels." Decreases as deep corruption spreads. Affects morale and health.
    * **Breathable Air:** Measured in "circulation efficiency." Decreases as engineering systems fail. Requires maintenance missions.
    * **Military Strength:** For each faction. Increases/decreases based on battles and recruitment.
    * **Political Influence:** For party and heir. Increases through successful missions, decreases through failures or scandals.
* **Consequences of Resource Depletion:**
    * Food below 4 weeks: Riots, reduced military effectiveness, desperate raids.
    * Water purity below 50%: Sickness, corruption vulnerability increases, morale drops.
    * Air circulation below 60%: Mandatory evacuation of lower levels, claustrophobia effects increase.
    * Zero resources: Faction collapse, mass casualties, game over scenarios.

**8. Corruption Mechanics**
* **Directive:** Track individual character corruption from deep entity exposure.
* **Corruption Sources:**
    * Spending time in Forgotten Deeps
    * Listening to whispers without resisting
    * Accepting power from the deep
    * Fighting corrupted creatures
    * Touching artifacts from Thordak's era
* **Corruption Effects (Progressive):**
    * Stage 1: Whispers offer knowledge, advantage on some rolls but nightmares.
    * Stage 2: Physical changes (eyes darkening, veins visible), power increase but wisdom loss.
    * Stage 3: Becoming an NPC under deep entity control.
* **Cure Mechanisms:**
    * Religious rituals at Stonemantle temples
    * Magical purification (expensive, rare)
    * Defeating Grendok permanently removes corruption
    * Redemption through sacrifice
