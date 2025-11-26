### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Memory Mines**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** One party member has been living a quiet life in Rubicon, a city built inside mining tunnels on the hostile plane of Rust. When they visit a memory-modification parlor called Rekall for a fantasy vacation, the procedure triggers hidden memories of a past life as a secret agent for the resistance. Now hunted by corporate forces and unsure what's real, the party must travel to the Rust Wastes to find the truth, discover an ancient alien reactor that could free the plane's oppressed miners, and decide who they really are.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the colonization of the plane of Rust and the discovery of valuable minerals beneath the red sand.
    *   Write the story of how Administrator Cohaagen rose to power and established a monopoly on breathable air.
    *   Describe the ancient alien civilization that once inhabited Rust and built the terraforming reactor.
    *   Explain the technology behind memory modification—Rekall's process, its uses, and its dangers.
    *   Detail the formation of the resistance movement and its leader, the psychic mutant Kuato.
    *   Describe the identity of Hauser—Cohaagen's former best agent who may or may not have defected to become the party member.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Resistance** (Major)
        *   **Goals:** Overthrow Cohaagen, activate the alien reactor, free the miners from air rationing.
        *   **Hierarchy:** Led by Kuato (psychic leader), organized in secret cells.
        *   **Public Agenda:** None—operate in complete secrecy.
        *   **Secret Agenda:** Finding and activating the alien reactor to make the atmosphere breathable.
        *   **Assets:** Hidden bases, smuggling networks, Kuato's psychic abilities, sympathetic miners.
        *   **Relationships:** Allied with the party; opposed by Cohaagen; supported by miners.
    *   **The Cohaagen Administration** (Major)
        *   **Goals:** Maintain control over Rust, suppress knowledge of the reactor, maximize mining profits.
        *   **Hierarchy:** Administrator Cohaagen (dictator), corporate executives, security forces.
        *   **Public Agenda:** Providing order, security, and economic prosperity.
        *   **Secret Agenda:** Using air rationing as control mechanism, preventing reactor activation to maintain power.
        *   **Assets:** Vast wealth, private army, control over air supply, propaganda machine, memory modification technology.
        *   **Relationships:** Primary antagonists; hunting the party; controlling the miners.
    *   **The Mining Population** (Major)
        *   **Goals:** Survive, afford breathable air, avoid trouble.
        *   **Hierarchy:** No formal structure—workers organized by company.
        *   **Public Agenda:** Working to earn enough for air rations.
        *   **Secret Agenda:** Many secretly support the resistance but are too afraid to act openly.
        *   **Assets:** Numbers, labor power, local knowledge.
        *   **Relationships:** Oppressed by Cohaagen; sympathetic to resistance; wary of outsiders.
    *   **Rekall Corporation** (Minor)
        *   **Goals:** Profit from memory modification services.
        *   **Hierarchy:** Corporate structure, affiliated with Cohaagen.
        *   **Public Agenda:** Providing escapist fantasy vacations through implanted memories.
        *   **Secret Agenda:** Also used for interrogation, mind-wiping, and intelligence gathering by Cohaagen.
        *   **Assets:** Memory technology, client records, technical expertise.
        *   **Relationships:** Technically neutral but controlled by Cohaagen; unwittingly trigger the campaign's events.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Melina:** Tough resistance fighter, possibly the party member's former partner.
    *   **Kuato:** Wise mutant psychic who leads the resistance and can unlock hidden memories.
    *   **Administrator Cohaagen:** Ruthless dictator who controls Rust's air supply to maintain power.
    *   **Hauser (Possible PC Identity):** The party member's possible true identity—Cohaagen's former best agent who may have defected.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Cohaagen Security Officer"
    *   "Resistance Fighter"
    *   "Oppressed Miner"
    *   "Rekall Technician"
    *   "Mutant from Atmospheric Exposure"
    *   "Corporate Executive"
    *   "Venusville Resident"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **Rubicon:** The main city, built inside massive mining tunnels.
        *   **Key Landmarks:** Rekall Memory Parlor, The Party Member's Apartment, Corporate Security HQ, The Air Distribution Center, Mining Elevator Shafts.
        *   **Primary Inhabitants:** Corporate employees, miners, security forces, merchants.
        *   **Available Goods & Services:** Memory implantation, air rations, mining equipment, black market goods.
        *   **Potential Random Encounters (x5):** Security checkpoint, air ration line, propaganda broadcast, resistance recruitment, corporate patrol.
        *   **Embedded Plot Hooks & Rumors (x3):** "Rekall has been doing secret work for Cohaagen." "Some miners have never seen the surface." "There are ruins in the desert that Cohaagen forbids anyone from visiting."
        *   **Sensory Details:** Sight (Industrial tunnels, pipes carrying air, propaganda screens, artificial lighting), Sound (Mining equipment, air hissing through pipes, security announcements), Smell (Recycled air, machine oil, rock dust).
    *   **The Rust Wastes:** The deadly surface desert.
        *   **Key Landmarks:** The Red Dunes, Mining Outposts, Venusville Settlement, The Alien Ruins, The Reactor Site.
        *   **Primary Inhabitants:** Desperate miners, mutants, resistance fighters, corporate patrols.
        *   **Available Goods & Services:** Survival gear, smuggling services, resistance contacts.
        *   **Potential Random Encounters (x5):** Sandstorm, toxic atmosphere damage, corporate ambush, mutant scavengers, ancient alien technology.
        *   **Embedded Plot Hooks & Rumors (x3):** "Venusville is a hotbed of resistance activity." "The ruins predate human arrival by millennia." "Kuato lives somewhere in these wastes."
        *   **Sensory Details:** Sight (Red sand stretching to horizon, massive rock formations, distant alien structures), Sound (Howling wind, breathing apparatus, crunching sand), Smell (Dry, dusty, toxic—without masks, acrid).
    *   **Venusville:** A squalid settlement on the surface where the poorest miners live.
        *   **Key Landmarks:** The Bar, The Resistance Safe House, The Air Vendor Stalls, The Mutant Quarter.
        *   **Primary Inhabitants:** Impoverished miners, mutants, resistance members, criminals.
        *   **Available Goods & Services:** Cheap air, black market goods, resistance information, hiding places.
        *   **Potential Random Encounters (x5):** Brawl over air rations, mutant beggar, corporate raid, resistance meeting, desperate miner sells information.
        *   **Embedded Plot Hooks & Rumors (x3):** "Kuato can free your mind from corporate programming." "The reactor is real and it's in the old ruins." "Cohaagen's agents are everywhere—trust no one."
        *   **Sensory Details:** Sight (Ramshackle buildings, mutant disfigurements, red dust everywhere), Sound (Coughing, arguments, hissing air tanks), Smell (Unwashed bodies, desperation, cheap alcohol).
    *   **The Alien Reactor Complex:** Ancient ruins containing the terraforming device.
        *   **Key Landmarks:** The Excavation Site, The Sealed Entrance, The Guardian Chambers, The Central Reactor, The Control Interface.
        *   **Primary Inhabitants:** Ancient security constructs, Cohaagen's guards (later), excavation workers.
        *   **Available Goods & Services:** None—this is forbidden territory.
        *   **Potential Random Encounters (x5):** Ancient security activates, structural collapse, alien technology fluctuation, Cohaagen's forces arrive, reality distortion from reactor.
        *   **Embedded Plot Hooks & Rumors (x3):** "The aliens built this to terraform Rust eons ago." "Activation requires biological interaction." "Cohaagen knows about it and wants it destroyed."
        *   **Sensory Details:** Sight (Smooth alien architecture unlike human construction, strange hieroglyphs, massive machinery), Sound (Deep humming, ancient mechanisms, echoes), Smell (Stale air, ozone, something completely alien).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The party member visits Rekall and triggers hidden memories.
    *   **THEN:** Generate immediate corporate response—security forces attack. The party becomes fugitives. Reality becomes questionable.
    *   **IF:** The party meets Kuato and has their memories read.
    *   **THEN:** Generate revelation scene. Confirm some memories are real. Provide clues about reactor location. Kuato becomes a target.
    *   **IF:** The party experiences the "psychiatrist" illusion.
    *   **THEN:** Generate convincing false reality where everything since Rekall was a dream. Test player trust. Breaking free proves their strength of will.
    *   **IF:** The party activates the alien reactor.
    *   **THEN:** Generate atmosphere transformation beginning. Breathable air spreads slowly across Rust. Miners tear off masks. Cohaagen's power crumbles.
    *   **IF:** The party member chooses to embrace their Hauser identity.
    *   **THEN:** They regain Hauser's skills and memories but risk losing who they've become. Generate conflict between past and present self.
    *   **IF:** The party member rejects Hauser and chooses their current identity.
    *   **THEN:** They forge a new path, combining the best of both. Generate acceptance and growth.
