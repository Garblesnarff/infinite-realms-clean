### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Raid: Ascent**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The Crimson Tower, a thirty-floor tenement building in the slums, has become a fortress for crime lord Tama Riyadi. The city watch sends the party—an elite strike team—to infiltrate the building and capture Tama. When their operation is compromised, the entire building becomes a death trap with hundreds of criminals hunting them. The only way out is up.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the history of the Crimson Tower: when was it built, how did it become a criminal fortress?
    *   Write the story of Tama Riyadi's rise to power and how he took control of the building.
    *   Describe Pencak Silat martial arts in this setting and why it's the dominant close-combat style.
    *   Explain the corruption in the city watch that allowed Tama's fortress to exist unchallenged.
    *   Detail the relationship between Andi and Rama (or the party member) before Andi went undercover.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Strike Team (The Players)** (Minor)
        *   **Goals:** Capture Tama Riyadi alive, survive the operation, uncover the truth about the mission.
        *   **Hierarchy:** Team leader, specialists (breacher, medic, sharpshooter, martial artist).
        *   **Public Agenda:** Execute a legal raid to arrest a criminal.
        *   **Secret Agenda:** Some members suspect the mission is compromised but must complete it to survive.
        *   **Assets:** Military training, tactical equipment (limited ammo), Pencak Silat skills.
        *   **Relationships:** Betrayed by their own commander (Wahyu); opposed by Tama's forces; complicated alliance with Andi.
    *   **Tama's Organization** (Major)
        *   **Goals:** Maintain control of the Crimson Tower, protect their criminal enterprise, eliminate the strike team.
        *   **Hierarchy:** Tama at top, lieutenants (Andi, Mad Dog), enforcers, gang members, civilian "residents" (coerced workers).
        *   **Public Agenda:** The building is supposedly low-income housing.
        *   **Secret Agenda:** Drug manufacturing, weapons trafficking, human trafficking, protection rackets.
        *   **Assets:** Fortified building, hundreds of armed criminals, surveillance systems, Mad Dog's martial prowess.
        *   **Relationships:** Primary antagonist faction; pays off city officials; controls the slum through fear.
    *   **The Corrupt Watch** (Minor)
        *   **Goals:** Use the raid to eliminate witnesses to their own corruption.
        *   **Hierarchy:** Captain Wahyu, select corrupt officers.
        *   **Public Agenda:** Law enforcement.
        *   **Secret Agenda:** Wahyu takes bribes from Tama and other crime lords. He sent the strike team to die and eliminate Andi, who has evidence against him.
        *   **Assets:** Legal authority, ability to deny backup or extraction.
        *   **Relationships:** The hidden antagonist faction; controls whether the party gets support.
    *   **The Residents** (Minor)
        *   **Goals:** Survive, protect their families, possibly escape.
        *   **Hierarchy:** None—they're civilians trapped in the building.
        *   **Public Agenda:** None.
        *   **Secret Agenda:** Some are forced to work for Tama; others are just poor people with nowhere else to go. They'll hide from the fighting if possible.
        *   **Assets:** Knowledge of the building, potential to help the party if protected.
        *   **Relationships:** Caught between the strike team and Tama's forces; terrified of both.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Tama Riyadi:** Cold crime lord watching the raid on surveillance monitors, dying of terminal illness.
    *   **Mad Dog:** Gleeful martial arts savant who lives only for the perfect fight, refuses to use weapons.
    *   **Andi:** Deep cover operative pretending to be Tama's lieutenant, related to party member.
    *   **Wahyu:** Corrupt watch captain who sent the party on a suicide mission to cover his crimes.
    *   **Rama (optional NPC ally):** Skilled Pencak Silat rookie on his first operation, Andi's brother.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Gang member with machete (various skill levels)"
    *   "Trapped civilian (fearful, hiding)"
    *   "Drug lab worker (coerced, desperate)"
    *   "Tama's elite enforcer (armored, military weapons)"
    *   "Building lookout (alert, will sound alarm)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Crimson Tower - Lower Floors (1-10):** Initial breach point and residential floors.
        *   **Key Landmarks:** Main entrance (breached), stairwell A (primary route), apartments 3-7 (cleared silently), lookout room (floor 6 where alarm was raised).
        *   **Primary Inhabitants:** Low-level gang members, lookouts, trapped civilians.
        *   **Available Goods & Services:** Scavenged weapons, medical supplies in abandoned apartments, limited intel.
        *   **Potential Random Encounters (x5):** Civilians hiding in closets begging for protection; gang members setting up ambushes; a trapped mother with children; drug addicts unaware of the raid; wounded criminals trying to flee downward.
        *   **Embedded Plot Hooks & Rumors (x3):** "Tama watches everything on cameras." "The elevators are death traps—they're controlled from the penthouse." "Some residents are held as hostages to keep workers compliant."
        *   **Sensory Details:** Sight (dim hallways, peeling paint, poverty), Sound (muffled crying, distant gunfire, footsteps above), Smell (mildew, cooking food, unwashed bodies).
    *   **The Drug Lab - Floor 8:** Chemical processing facility with hazards.
        *   **Key Landmarks:** Main production room, chemical storage, ventilation system (can be weaponized), worker dormitories (locked in).
        *   **Primary Inhabitants:** Forced laborers (chemists), armed guards, Tama's chemist overseer.
        *   **Available Goods & Services:** None usable, but chemicals can be used as weapons or to create distractions.
        *   **Potential Random Encounters (x5):** A chemical spill creates toxic gas; workers beg to be freed; guards wear gas masks; an explosion from damaged equipment; a worker tries to sabotage the lab to help the party.
        *   **Embedded Plot Hooks & Rumors (x3):** "Destroying the lab will cripple Tama's operation but might kill the trapped workers." "There's a ventilation shaft that bypasses floors 9-11." "The lab chemicals can create smoke screens or small explosives."
        *   **Sensory Details:** Sight (industrial equipment, chemical vats, harsh lighting), Sound (bubbling liquids, ventilation hum), Smell (acrid chemicals, burning, synthetic smells).
    *   **The Fighting Pit - Floor 15:** Makeshift arena where criminals fight.
        *   **Key Landmarks:** The cage ring (center of the floor), spectator area, the champion's corner, weapon racks.
        *   **Primary Inhabitants:** Gladiator fighters, gang members gambling on fights, the current champion.
        *   **Available Goods & Services:** Improvised weapons (chains, pipes, clubs).
        *   **Potential Random Encounters (x5):** Mad Dog's first appearance (he watches from the shadows); forced to fight a champion to pass; gang members demand a "trial by combat"; betting on whether the party survives; discovery of fighters held as slaves.
        *   **Embedded Plot Hooks & Rumors (x3):** "Mad Dog recruited the champion personally." "Winners get to join Tama's enforcers." "There's a hidden elevator in the champion's room."
        *   **Sensory Details:** Sight (bloodstained ring, improvised arena, bare bulbs), Sound (shouting crowds, impact of fists), Smell (sweat, blood, beer).
    *   **Surveillance Center - Floor 22:** Where Tama monitors the building.
        *   **Key Landmarks:** Monitor wall (showing all floors), Tama's command chair, communications equipment, armory.
        *   **Primary Inhabitants:** Tama (briefly), communications officers, elite guards.
        *   **Available Goods & Services:** Intelligence (can view cameras if controlled), high-quality weapons.
        *   **Potential Random Encounters (x5):** Tama makes an announcement over loudspeakers; guards watching monitors spot the party's approach; Andi appears to help but must maintain cover; destroying the surveillance system blinds Tama; a recording reveals Wahyu's betrayal.
        *   **Embedded Plot Hooks & Rumors (x3):** "Tama's been watching and enjoying the raid like entertainment." "The monitors show all of Tama's operations across the city." "Wahyu's voice is on recordings making deals with Tama."
        *   **Sensory Details:** Sight (wall of monitors, flickering screens showing violence throughout building), Sound (radio chatter, alarm systems), Smell (electronics, coffee, cigarette smoke).
    *   **The Penthouse - Floor 30:** Tama's luxurious headquarters.
        *   **Key Landmarks:** Tama's office (huge contrast to building's poverty), armory, rooftop access, the panic room (Tama's final stand).
        *   **Primary Inhabitants:** Tama, Mad Dog (final fight), elite guards with military gear, possibly Andi.
        *   **Available Goods & Services:** Evidence of Tama's operations, wealth, the truth about Wahyu's corruption.
        *   **Potential Random Encounters (x5):** Mad Dog's duel challenge; Tama attempts to negotiate; elite guards in cover positions; Andi's confrontation with Tama; discovery of Wahyu's payment records.
        *   **Embedded Plot Hooks & Rumors (x3):** "Tama keeps evidence against all his corrupt official allies as insurance." "There's a secret elevator to the roof." "Mad Dog has been waiting for warriors worthy of fighting."
        *   **Sensory Details:** Sight (luxury contrasting with the slum below, expensive furniture, expansive windows), Sound (quiet, air conditioning, the city beyond), Smell (expensive cologne, leather, clean air).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The party runs out of ammunition (inevitable around floor 10).
    *   **THEN:** Combat shifts entirely to martial arts and improvised weapons. Generate scenes emphasizing brutal close-combat and scavenging weapons from defeated enemies.
    *   **IF:** The party rescues and protects civilian residents.
    *   **THEN:** Civilians provide intelligence about building layout, hidden paths, and Tama's operations. They might also slow the party down or become hostages.
    *   **IF:** The party destroys the drug lab.
    *   **THEN:** Tama becomes more desperate and aggressive. He releases all his enforcers at once. However, the party gains favor with any freed workers who might help in later floors.
    *   **IF:** The party defeats Mad Dog in a honorable one-on-one duel.
    *   **THEN:** Mad Dog respects them even in death. Generate a scene where he reveals a secret about Tama or Andi before dying. Other criminals give the party brief passage as a sign of respect for defeating their champion.
    *   **IF:** The party kills Mad Dog dishonorably (ganging up, using tricks, refusing his duel).
    *   **THEN:** The remaining criminals become enraged and fight more viciously. Mad Dog's death is "wasted," providing no intelligence or respect.
    *   **IF:** The party discovers evidence of Wahyu's corruption.
    *   **THEN:** They realize they can't trust their own command. Generate consequences where they must decide whether to complete the original mission or expose Wahyu, knowing extraction might never come.
    *   **IF:** Andi's identity is revealed to Tama before the party reaches him.
    *   **THEN:** Tama tortures Andi for information. The party must mount a rescue, adding time pressure. Andi might be gravely wounded, affecting the final confrontation.
    *   **IF:** The party reaches floor 20 with minimal injuries and resources remaining.
    *   **THEN:** Tama sends all his remaining forces in a desperate final defense. The last ten floors become exponentially harder with more elite enemies.
