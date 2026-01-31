### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Trophy Hunter**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** Elite soldiers sent to rescue a diplomat's expedition find everyone slaughtered by something that hunts for sport. As team members die to an invisible enemy with advanced technology, the party realizes they're prey for a Yautja—an extraplanar trophy hunter. To survive the deadly jungle and their superior predator, they must adapt, learn, and become hunters themselves.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the Yautja species—their culture of hunting, honor code, and what brings them to hunt in other planes.
    *   Write about the ancient ruins in the jungle and why they attract Yautja hunters.
    *   Describe the Deep Jungle region—its dangers, ecology, and why it's avoided by locals.
    *   Explain Yautja technology—cloaking devices, plasma weapons, thermal vision, self-destruct mechanisms.
    *   Detail the trophy hunting tradition and what makes prey "worthy" in Yautja culture.
    *   Describe previous Yautja hunts in this world—legends of invisible demons that may be true.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Military Expedition (The Party)** (Minor)
        *   **Goals:** Rescue the diplomat, extract safely, survive.
        *   **Hierarchy:** Military chain of command with party as elite unit.
        *   **Public Agenda:** Diplomatic protection and extraction.
        *   **Secret Agenda:** May have been sent for reasons beyond simple rescue—perhaps to investigate the ruins.
        *   **Assets:** Elite training, military equipment, team cohesion.
        *   **Relationships:** Alone in hostile territory; hunted by the Predator; only have each other.
    *   **The Yautja Hunter** (Major - Antagonist)
        *   **Goals:** Prove worth through honorable hunt, collect trophies from worthy prey.
        *   **Hierarchy:** Solo hunter on proving hunt, part of larger Yautja culture.
        *   **Public Agenda:** None—operates in complete secrecy.
        *   **Secret Agenda:** This is a rite of passage hunt. Failure means dishonor; success means respect among its kind.
        *   **Assets:** Superior physical abilities, advanced technology, centuries of hunting experience, understanding of the jungle.
        *   **Relationships:** Predator to the party; bound by honor code; judges prey based on combat prowess.
    *   **The Jungle** (Environmental - Antagonist)
        *   **Goals:** N/A—it's an environment.
        *   **Hierarchy:** Natural ecosystem with its own predators and dangers.
        *   **Public Agenda:** N/A
        *   **Secret Agenda:** The ruins have attracted unnatural attention, subtly corrupting the jungle.
        *   **Assets:** Dangerous wildlife, diseases, difficult terrain, limited visibility.
        *   **Relationships:** Hostile to outsiders; the Yautja has adapted to it; locals avoid it.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **The Yautja Hunter:** Young (by its species' standards) warrior on proving hunt, honorable but aggressive.
    *   **Sergeant Hawkins:** Veteran soldier who provides dark humor until paranoia breaks them.
    *   **Doctor Martinez:** Rescued diplomat who knows the expedition's real purpose.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Elite Soldier (Party backup, likely to die)"
    *   "Local Guide (Knows jungle, terrified of legends)"
    *   "Expedition Survivor (Traumatized, may know crucial information)"
    *   "Jungle Predator (Natural wildlife adding danger)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Massacre Site:** The diplomat's camp turned horror scene.
        *   **Key Landmarks:** Main tent (bodies inside), equipment dump (destroyed), perimeter (breached), the skinning trees.
        *   **Primary Inhabitants:** Bodies of the expedition, scavenger animals, and the party when they arrive.
        *   **Available Goods & Services:** Damaged equipment to scavenge, evidence to investigate.
        *   **Potential Random Encounters (x5):** Discovery of survivor hiding, Predator technology fragment, disturbing trophy display, ambush by jungle predator, finding the diplomat.
        *   **Embedded Plot Hooks & Rumors (x3):** "They found something in the ruins." "The bodies are arranged ritually." "One tent shows signs of combat with something using advanced weapons."
        *   **Sensory Details:** Sight (Destruction, blood, skinned bodies), Sound (Flies buzzing, jungle ambience, unnatural silence), Smell (Death, decay, fear-sweat).
    *   **The Deep Jungle:** Dense rainforest where the hunt occurs.
        *   **Key Landmarks:** The canopy (where the Predator travels), water source (ambush point), various clearings (potential battlegrounds), thick undergrowth (limits movement).
        *   **Primary Inhabitants:** The Yautja, the party, dangerous wildlife, potentially hostile natives.
        *   **Available Goods & Services:** Natural resources for survival, materials for traps and camouflage.
        *   **Potential Random Encounters (x5):** Predator stalking scene, dangerous animal attack, quicksand or other natural hazard, evidence of Predator's passage, suitable ambush location.
        *   **Embedded Plot Hooks & Rumors (x3):** "The jungle is more dangerous than usual." "Locals tell stories of invisible demons." "Animals are fleeing this area."
        *   **Sensory Details:** Sight (Limited by foliage, dappled light, layers of vegetation), Sound (Overwhelming—insects, birds, rustling, clicking), Smell (Humid rot, exotic flowers, blood on wind).
    *   **The Ancient Ruins:** Alien structures that attracted both expedition and Predator.
        *   **Key Landmarks:** The main temple, carved walls showing hunting scenes, a chamber with strange technology, the altar.
        *   **Primary Inhabitants:** Now abandoned except when the Predator visits to honor the site.
        *   **Available Goods & Services:** Cover for ambushes, high ground advantage, ancient knowledge if deciphered.
        *   **Potential Random Encounters (x5):** Predator performing ritual, discovery of ancient warning, trapped room activation, shelter from jungle, vantage point for observation.
        *   **Embedded Plot Hooks & Rumors (x3):** "This site is sacred to the Predators." "The ruins show hunts across multiple worlds." "There's technology here that still functions."
        *   **Sensory Details:** Sight (Ancient stone covered in jungle growth, alien architecture, carved hunting scenes), Sound (Echoing, wind through stone, distant Predator clicks), Smell (Ancient stone, ozone from active technology).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** An NPC panics and breaks from the group.
    *   **THEN:** The Predator hunts them immediately. Generate a scene where the party hears but cannot save them, raising terror.
    *   **IF:** The party successfully wounds the Predator.
    *   **THEN:** It begins respecting them as worthy prey. Generate escalated but more "honorable" tactics—fewer cheap ambushes, more direct combat.
    *   **IF:** The party uses mud to hide thermal signatures.
    *   **THEN:** The Predator adapts, using vision modes they haven't seen before. Generate new hunting tactics.
    *   **IF:** The party discovers and studies Predator technology.
    *   **THEN:** They can jury-rig countermeasures or weapons. Generate specific advantages they gain.
    *   **IF:** The party kills the Predator but triggers its self-destruct.
    *   **THEN:** Generate a desperate escape sequence with massive explosion. Survivors are marked by Yautja society as worthy.
    *   **IF:** The party defeats the Predator without triggering self-destruct.
    *   **THEN:** Generate an epilogue where they keep trophies but are now marked. Other Yautja may seek them out for honor duels.
