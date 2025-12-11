# World-Building Specification Brief: Beast of Skull Isle

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**Beast of Skull Isle**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The party is hired by the eccentric explorer-entrepreneur Lord Havelock Crane to escort his expedition to the legendary Skull Isle, a mysterious landmass shrouded in perpetual storms and said to hold untold riches. Upon arrival, they discover a lost world of prehistoric creatures, ancient ruins, and a tribe that worships a colossal ape-god they call Kong. When Crane captures Kong to display as a spectacle in the capital city, the party must decide: are they complicit in this exploitation, or will they help the Beast reclaim what was stolen from him—knowing it may cost countless lives?

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the legends of Skull Isle and why most sailors believe it is only a myth or cursed.
    *   Write the history of the Iwala Tribe: their arrival on Skull Isle centuries ago, their covenant with Kong, and their role as guardians of the balance.
    *   Describe the "Deep Things"—the tentacled horrors that dwell in the island's subterranean lakes, and why Kong is necessary to keep them contained.
    *   Explain the ancient civilization that built the ruins on Skull Isle, their fall, and the artifacts they left behind.
    *   Detail the rise of Lord Havelock Crane: his past expeditions, his debts, his reputation as both a visionary and a charlatan.
    *   Write about the culture of Meridian, the capital city: its obsession with spectacle, entertainment, and "civilizing the savage world."

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Crane Expedition** (Major)
        *   **Goals:** Reach Skull Isle, secure wealth and fame, capture Kong for public exhibition.
        *   **Hierarchy:** Led by Lord Crane, with First Mate Renwick as second-in-command, Dr. Selene Voss as chief scholar, and various sailors, mercenaries, and specialists.
        *   **Public Agenda:** We are explorers and adventurers, bringing the wonders of the unknown to the civilized world.
        *   **Secret Agenda:** Crane is deeply in debt and sees Kong as his salvation. He will betray anyone to secure his prize.
        *   **Assets:** The ship *The Siren's Call*, alchemical weapons, mechanical restraints, funding from wealthy investors.
        *   **Relationships:** Employing the party; may turn hostile if the party resists; viewed as heroes by Meridian society.
    *   **The Iwala Tribe** (Minor)
        *   **Goals:** Protect Skull Isle, maintain the balance between Kong and the Deep Things, prevent outsiders from disrupting their world.
        *   **Hierarchy:** Led by Elder Moana and a council of shamans and warriors.
        *   **Public Agenda:** We are the guardians of the sacred isle. Kong is our protector.
        *   **Secret Agenda:** The tribe knows that if Kong is taken, the island—and they—will fall to the Deep Things. They are resigned to tragedy.
        *   **Assets:** Knowledge of the island's secrets, poison weapons, ritual magic, the loyalty of Kong (until he is captured).
        *   **Relationships:** Initially hostile to the expedition; may ally with sympathetic party members; doomed by the expedition's actions.
    *   **The Investors' Consortium** (Minor)
        *   **Goals:** Profit from Crane's exhibition, expand colonial holdings, exploit new lands for resources.
        *   **Hierarchy:** A coalition of wealthy merchants, nobles, and industrialists who funded Crane's expedition.
        *   **Public Agenda:** We are pioneers of progress, bringing civilization to savage lands.
        *   **Secret Agenda:** They want Skull Isle's resources (rare minerals, exotic creatures, slave labor) and plan a follow-up colonization effort.
        *   **Assets:** Vast wealth, political influence in Meridian, private militias.
        *   **Relationships:** Crane's patrons; will protect him from consequences; will scapegoat him if Kong's rampage threatens their own holdings.
    *   **The People of Meridian** (Minor)
        *   **Goals:** Seek entertainment, safety, and prosperity.
        *   **Hierarchy:** No formal structure; represented by public opinion, the press, and mob mentality.
        *   **Public Agenda:** We deserve to see the wonders of the world. Kong is a marvel!
        *   **Secret Agenda:** None; they are victims of propaganda and spectacle, ignorant of the cost.
        *   **Assets:** Numbers, public pressure, the ability to turn from adoration to rage instantly.
        *   **Relationships:** Adore Crane until Kong's rampage, then demand his head; the party may become scapegoats or heroes depending on their choices.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Kong, the Guardian:** A 60-foot silverback gorilla, intelligent and emotional, the island's protector, capable of great gentleness and terrible rage.
    *   **Lord Havelock Crane:** Charismatic explorer-entrepreneur, ambitious and ruthless, driven by debt and legacy.
    *   **Elder Moana:** Spiritual leader of the Iwala Tribe, wise and resigned, knows the tragedy is inevitable.
    *   **Dr. Selene Voss:** Expedition naturalist, intelligent and morally conflicted, eventually becomes horrified by Crane's actions.
    *   **First Mate Renwick:** Jaded sailor, loyal to Crane but growing increasingly uneasy about the plan.
    *   **The Deep Things (Representative):** A massive tentacled horror from the island's depths, awakening without Kong to stop it.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Grizzled Expedition Sailor"
    *   "Iwala Tribe Warrior"
    *   "Meridian Noble Investor"
    *   "Fascinated City Scholar"
    *   "Panicked Civilian During Rampage"
    *   "Ruthless Mercenary Hunter"
    *   "Sympathetic Reporter"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **Skull Isle (Coastal Region):** The beachhead where the expedition crashes, a rocky shore surrounded by jungle.
        *   **Key Landmarks:** The wrecked *Siren's Call*, the Storm Wall (visible offshore), the Jungle's Edge, the First Ruins (stone pillars covered in vines).
        *   **Primary Inhabitants:** Giant crabs, pteranodons, small raptors, Iwala scouts.
        *   **Available Goods & Services:** Salvage from the wreck, foraging for food (with risk), expedition supplies (limited).
        *   **Potential Random Encounters (x5):** Giant crab attack, raptor pack ambush, discovery of ancient idol, Iwala scout observation, storm surge flooding.
        *   **Embedded Plot Hooks & Rumors (x3):** "The navigator swears he's been here before and barely survived." "Strange drumming echoes from the jungle at night." "Some crew members want to mutiny and repair the ship to leave immediately."
        *   **Sensory Details:** Sight (Crashing waves, dense green wall of jungle, storm clouds overhead), Sound (Waves, distant animal calls, wind), Smell (Salt, rotting vegetation, ozone from storms).
    *   **The Deep Jungle (Skull Isle Interior):** The heart of the island, Kong's domain.
        *   **Key Landmarks:** Kong's Mountain (a massive rocky outcrop), the Sunken Temple (ancient ruins half-swallowed by a lake), the Bone Field (dinosaur graveyard), the Underground Lake (where the Deep Things dwell).
        *   **Primary Inhabitants:** Kong, T-Rex, triceratops herds, giant spiders, the Deep Things (below).
        *   **Available Goods & Services:** None; pure survival.
        *   **Potential Random Encounters (x5):** T-Rex ambush, Kong sighting, stampeding herbivores, giant spider web, Deep Thing tentacle from lake.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Iwala say Kong mourns—he is the last of his kind." "The temple holds a treasure that can control the beasts." "The lake is bottomless, and something ancient stirs below."
        *   **Sensory Details:** Sight (Towering trees, shafts of light, massive footprints, ancient stonework), Sound (Kong's distant roars, rustling canopy, dripping water), Smell (Rich earth, flowers, decay, sulfur from underground).
    *   **Iwala Village:** The tribe's home, built in the treetops and on cliff faces.
        *   **Key Landmarks:** Elder Moana's longhouse, the Kong Shrine (a massive carved idol), the Watchtower, the Healing Grove.
        *   **Primary Inhabitants:** The Iwala Tribe (hunters, shamans, elders, children).
        *   **Available Goods & Services:** Healing herbs, guidance (if friendly), poison for weapons, historical knowledge.
        *   **Potential Random Encounters (x5):** Ritual ceremony, trial by combat challenge, shaman vision quest, warning of danger, offering of hospitality.
        *   **Embedded Plot Hooks & Rumors (x3):** "Moana can speak to Kong through dreams." "The tribe once numbered thousands, but disease from outsiders killed most." "If Kong falls, the tribe will perform a final ritual and die with the island."
        *   **Sensory Details:** Sight (Wooden platforms, colorful ritual cloth, carved totems, firelight), Sound (Drums, chanting, children playing, shaman rattles), Smell (Smoke, roasting meat, incense, jungle flowers).
    *   **Meridian (The Capital City):** A sprawling, prosperous metropolis by the sea.
        *   **Key Landmarks:** The Grand Theater, Skyspire Tower, the Harbor District, the Noble Quarter, the Industrial Sector.
        *   **Primary Inhabitants:** Nobles, merchants, workers, entertainers, soldiers, city guard.
        *   **Available Goods & Services:** Anything money can buy—luxury goods, information, weapons, magic items, bribes.
        *   **Potential Random Encounters (x5):** Pickpocket attempt, street protest, noble's carriage, merchant offering deal, news-crier announcing Kong's arrival.
        *   **Embedded Plot Hooks & Rumors (x3):** "Crane owes the Consortium a fortune—he's bankrupted without Kong." "The press is calling Kong the 'Eighth Wonder of the World.'" "Some scholars are protesting the exhibition as cruel."
        *   **Sensory Details:** Sight (Marble facades, gaslight lamps, crowded streets, elegant attire), Sound (Street vendors, carriage wheels, music from taverns, bells), Smell (Perfume, baked goods, horse manure, sea breeze).
    *   **The Grand Theater:** Meridian's premier entertainment venue, where Kong is exhibited.
        *   **Key Landmarks:** The Main Stage (where Kong is chained), the Royal Box, backstage (where Crane commands), the vast auditorium.
        *   **Primary Inhabitants:** Audience members, theater staff, Crane's guards, Kong (in chains).
        *   **Available Goods & Services:** Tickets (extremely expensive), backstage access (heavily guarded), press interviews.
        *   **Potential Random Encounters (x5):** Excited crowd, celebrity sighting, Crane's promotional speech, Kong's roar (causing panic), security confrontation.
        *   **Embedded Plot Hooks & Rumors (x3):** "Kong hasn't eaten in days—he's dying of despair." "Crane has bet everything on this exhibition." "Someone in the crowd is planning to free Kong."
        *   **Sensory Details:** Sight (Red velvet, gold trim, spotlight on Kong, well-dressed crowd), Sound (Applause, gasps, Kong's anguished roar, orchestra), Smell (Perfume, sweat, fear, popcorn and wine).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The party helps Crane capture Kong.
    *   **THEN:** The Iwala Tribe places a curse on the party. Elder Moana delivers a final prophecy. News arrives within a week that the Deep Things have destroyed the village. The party gains wealth but also guilt.
    *   **IF:** The party sabotages Crane's capture attempt.
    *   **THEN:** Crane turns hostile and attempts to kill or imprison the party. Kong remains free, but the expedition is stranded longer. Crane uses explosives to threaten the Iwala Village, forcing a hostage situation.
    *   **IF:** The party forms a bond with Kong (via the Bonded PC).
    *   **THEN:** Kong becomes protective of that PC and will prioritize their safety. This bond becomes central during Kong's rampage—he is searching for them, not mindlessly destroying.
    *   **IF:** The party exposes Crane's debt and true motives before the exhibition.
    *   **THEN:** The Investors' Consortium scapegoats Crane. The exhibition is delayed, giving the party a window to free Kong or negotiate. Public opinion turns, but Kong is still captive.
    *   **IF:** Kong escapes during the exhibition.
    *   **THEN:** The rampage begins. The Rampage Counter starts. The party must navigate the chaos. The military mobilizes. The city descends into panic.
    *   **IF:** The party helps Kong escape the city (difficult).
    *   **THEN:** Kong flees toward the ocean, attempting to swim back to Skull Isle. The party may face trial for treason. Crane is ruined. The city recovers but is forever changed.
    *   **IF:** Kong is killed atop Skyspire.
    *   **THEN:** The campaign ends in tragedy. Kong's final act is to gently set down the person he tried to protect. Dr. Voss publishes her journal, destroying Crane's legacy. The party must live with their choices.
