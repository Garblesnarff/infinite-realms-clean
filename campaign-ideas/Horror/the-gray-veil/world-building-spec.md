# World-Building Specification Brief: The Gray Veil

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Gray Veil**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** A mysterious gray fog rolls into the town of Millhaven, bringing with it nightmarish creatures from beyond reality. The party, along with dozens of townsfolk, takes refuge in the town's General Store as the mist consumes everything outside. Trapped with dwindling supplies, incomprehensible monsters prowling in the fog, and a charismatic zealot claiming the mist is divine punishment, the party must decide: risk the mist to escape, kill the zealot to restore order, or accept that there may be no hope at all.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the Wizard's Tower and its reclusive owner, Magister Eryndor, who was obsessed with piercing the veil between planes.
    *   Write about Eryndor's final ritual: an attempt to contact an entity from the Far Realm, which instead tore a permanent rift.
    *   Describe the nature of the mist: a bridge between the Material Plane and the Far Realm, through which horrors slip.
    *   Explain the creatures of the mist: Veil Stalkers (hunters), Mist Serpents (scavengers), Whisper Wraiths (psionic predators), and the Unseen (the thing that no one has survived seeing).
    *   Detail the Church of the Ascended Sun and Sister Mordane's fundamentalist interpretation of scripture.
    *   Write about Millhaven: a small farming town of 300 people, insular and superstitious, now reduced to 60 survivors in the store.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Rationalists** (Minor)
        *   **Goals:** Maintain order, survive through pragmatism, find a way to close the rift.
        *   **Hierarchy:** Led by Torven (merchant) and Markus (soldier), includes educated townsfolk and skeptics.
        *   **Public Agenda:** Stay calm. Ration supplies. We can survive this if we think clearly.
        *   **Secret Agenda:** Torven knows he's partially responsible for the ritual. He's desperately seeking redemption.
        *   **Assets:** Control of supplies, Markus's combat skills, logical thinking.
        *   **Relationships:** Opposed to Sister Mordane; view the party as potential leaders or allies.
    *   **The Cult of Divine Judgment** (Minor)
        *   **Goals:** Appease the "gods" through sacrifice, save their souls through suffering.
        *   **Hierarchy:** Led by Sister Mordane, includes desperate believers and the terrified.
        *   **Public Agenda:** This is judgment day. Only the faithful will be saved.
        *   **Secret Agenda:** Mordane is using fear to seize control. She will sacrifice anyone she labels "unbeliever."
        *   **Assets:** Numbers (30-40% of survivors), religious fervor, willingness to die (or kill).
        *   **Relationships:** Growing; opposed by Torven and Markus; sees the party as either converts or sacrifices.
    *   **The Entities of the Mist** (Major - Antagonist)
        *   **Goals:** Incomprehensible. They hunt, feed, or simply exist in ways human minds cannot process.
        *   **Hierarchy:** No clear hierarchy. The Unseen may be their "god" or simply the largest predator.
        *   **Public Agenda:** None—they are alien.
        *   **Secret Agenda:** None—they do not think like humans. They are forces of nature from another reality.
        *   **Assets:** The mist itself, overwhelming numbers, psychological warfare (whispers, madness).
        *   **Relationships:** Cannot be negotiated with. They are cosmic indifference made flesh.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Sister Mordane:** Charismatic zealot preaching divine judgment, secretly power-hungry.
    *   **Torven Halleck:** Pragmatic merchant and store owner, guilt-ridden over supplying the wizard's ritual.
    *   **Markus Varn:** Veteran soldier, disciplined but haunted, on the edge of breaking.
    *   **Magister Eryndor (Dead):** The wizard whose ritual caused the disaster, now a mutated horror in the mist.
    *   **The Veil Stalker:** A recurring monster, intelligent and patient, that stalks the party.
    *   **The Unseen:** The greatest horror in the mist—something so vast and alien that seeing it causes instant madness.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Terrified Farmer"
    *   "Mordane's Fanatical Follower"
    *   "Rational Skeptic"
    *   "Child Survivor"
    *   "Injured, Dying Townsperson"
    *   "Twisted by the Mist (Mutated Former Human)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The General Store (Interior):** The primary setting, cramped and tense.
        *   **Key Landmarks:** Main floor (aisles, barricaded windows), second floor (storage loft, lookout), the cellar (food supplies, potential hiding place).
        *   **Primary Inhabitants:** ~60 survivors, split between Rationalists and Cult.
        *   **Available Goods & Services:** Food (rationed), water (rationed), medical supplies (limited), weapons (improvised).
        *   **Potential Random Encounters (x5):** Argument over supplies, cult prayer circle, NPC mental breakdown, creature testing the barricades, Mordane's sermon.
        *   **Embedded Plot Hooks & Rumors (x3):** "Torven is hiding something about the wizard." "Someone saw Markus crying in the cellar." "A child claims the whispers in the mist are calling their name."
        *   **Sensory Details:** Sight (Crowded, dim lamplight, boarded windows), Sound (Whispers, prayers, muffled sobs, creatures outside), Smell (Sweat, fear, damp wood, smoke).
    *   **The Mist (Millhaven Streets):** The hostile environment outside.
        *   **Key Landmarks:** Main Street (abandoned), the Tavern (supply source), the Church (collapsed), distant screams, the Wizard's Tower (visible on the hill, glowing faintly).
        *   **Primary Inhabitants:** Veil Stalkers, Mist Serpents, Whisper Wraiths, the Unseen.
        *   **Available Goods & Services:** None—pure survival.
        *   **Potential Random Encounters (x5):** Veil Stalker ambush, Whisper Wraith (Sanity save), discovery of corpse, twisted survivor, glimpse of the Unseen.
        *   **Embedded Plot Hooks & Rumors (x3):** "The mist is spreading—it's already miles beyond the town." "Something massive moves in the deepest fog." "The wizard's tower still has power—you can see the glow."
        *   **Sensory Details:** Sight (Gray, featureless fog, shapes moving), Sound (Whispers, clicking, distant screams, your own breath), Smell (Ozone, rot, something alien).
    *   **The Wizard's Tower (Ruined):** The source of the rift, a deadly destination.
        *   **Key Landmarks:** Collapsed outer walls, the Ritual Chamber (still glowing with purple light), Eryndor's laboratory (full of notes), the Rift (a swirling tear in reality).
        *   **Primary Inhabitants:** Eryndor (mutated into a mist horror), guardian constructs (malfunctioning), dense concentration of mist creatures.
        *   **Available Goods & Services:** Ritual knowledge (to close the rift), magical items (cursed), the truth.
        *   **Potential Random Encounters (x5):** Eryndor's mutated form, swarm of Mist Serpents, reality distortion (magical wild surge), Veil Stalker ambush, the Rift itself (Sanity check).
        *   **Embedded Plot Hooks & Rumors (x3):** "Eryndor's notes mention a 'failsafe' to close the rift." "The ritual requires a willing sacrifice." "Eryndor is still alive—if you can call it that."
        *   **Sensory Details:** Sight (Purple glow, swirling rift, twisted architecture), Sound (Reality tearing, Eryndor's inhuman voice, absolute silence), Smell (Burnt ozone, something wrong).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The party successfully resists Sister Mordane's influence and keeps the Rationalists in control.
    *   **THEN:** Morale remains relatively stable. Cult Influence does not exceed 50%. However, Mordane will attempt to martyr herself or incite violence.
    *   **IF:** Cult Influence exceeds 50%.
    *   **THEN:** Mordane demands a blood sacrifice. The party must choose: allow it (NPC dies, some survivors are satisfied), stop it (violent confrontation), or offer a volunteer (moral complexity).
    *   **IF:** The party kills Sister Mordane.
    *   **THEN:** Half the cult turns violent in revenge. The store descends into chaos. Rationalists gain control, but at the cost of many lives.
    *   **IF:** The party attempts to flee through the mist without a clear plan.
    *   **THEN:** They become lost. Multiple Sanity checks, deadly encounters, high chance of death or madness. They may return to the store broken.
    *   **IF:** The party reaches the Wizard's Tower and attempts to close the rift.
    *   **THEN:** They discover the ritual requires a willing sacrifice (a PC or major NPC). Closing the rift ends the mist but kills the sacrifice. Alternatively, they can destroy the tower (easier) but the mist never fully dissipates—it just retreats.
    *   **IF:** The party does nothing and waits for rescue.
    *   **THEN:** Days pass. Supplies run out. Cult Influence reaches 80%. The store descends into cannibalistic madness. The campaign ends in total tragedy.
    *   **IF:** A PC's Sanity reaches 0.
    *   **THEN:** That PC is either catatonic or turns hostile, attacking the party or fleeing into the mist. They become an NPC (or die).
