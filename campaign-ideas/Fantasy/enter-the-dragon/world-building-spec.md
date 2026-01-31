### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**Enter the Dragon**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The legendary Master Han has invited the realm's greatest martial artists to compete in a tournament on his fortress island of Tian Long. But beneath the spectacle of combat lies a sinister truth: Han runs an illegal drug and slavery operation, and uses the tournament to recruit fighters for his criminal empire. The party, infiltrating as competitors, must win the tournament to gain access to Han's inner sanctum while gathering evidence of his crimes and rescuing captives from his dungeons.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the history of Tian Long Island and how Master Han came to control it. Was it a monastery once? A pirate stronghold?
    *   Write the legend of the Five Dragon Styles that compete in Han's tournament and their philosophical differences.
    *   Describe the regional conflict that makes Han's criminal network profitable—what kingdoms or factions need his drugs and mercenaries?
    *   Explain the origin of Han's prosthetic hands collection and the legend of the Jade Hand of Immortality he seeks.
    *   Detail the history of the Hall of Mirrors and the magic that powers its illusions.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Tournament Competitors (The Players)** (Minor)
        *   **Goals:** Win the tournament and complete their individual missions (revenge, rescue, infiltration).
        *   **Hierarchy:** Independent fighters with no formal organization.
        *   **Public Agenda:** To prove themselves as the greatest martial artists and win Han's prize.
        *   **Secret Agenda:** To gather evidence of Han's crimes, free the prisoners, and destroy his operation.
        *   **Assets:** Superior martial arts skills, unique abilities, the cover of being legitimate competitors.
        *   **Relationships:** In competition with other fighters; opposed to Han's organization; potential allies with other infiltrators like Mei Ling.
    *   **Han's Syndicate** (Major)
        *   **Goals:** Expand the drug and slavery operation while maintaining the tournament as a recruiting tool and money laundering front.
        *   **Hierarchy:** Han at the top, lieutenants (Bolo, O'Hara, Parsons), guards and enforcers, enslaved workers at the bottom.
        *   **Public Agenda:** To host the most prestigious martial arts tournament in the realm.
        *   **Secret Agenda:** To process opium from the Jade Poppy fields and sell skilled fighters into slavery to warlords and criminal organizations.
        *   **Assets:** The fortress island, a private army of trained guards, magical defenses, extensive criminal network, wealth.
        *   **Relationships:** The primary antagonist faction; employs corruption in regional governments; in conflict with law enforcement organizations.
    *   **The Shadow Court** (Minor - Mei Ling's Employers)
        *   **Goals:** Eliminate Han to destabilize the region's criminal drug trade so they can control it themselves.
        *   **Hierarchy:** A rival criminal organization or intelligence agency.
        *   **Public Agenda:** None—they operate in complete secrecy.
        *   **Secret Agenda:** Assassinate Han, steal his operation's records, and take over his distribution network.
        *   **Assets:** Highly trained assassins, espionage networks, poison experts.
        *   **Relationships:** Temporary allies to the party through Mei Ling, but their methods conflict with heroic ideals.
    *   **The Enslaved** (Minor)
        *   **Goals:** Survive and hope for freedom.
        *   **Hierarchy:** None—they are victims with various leaders who could organize a revolt if freed.
        *   **Public Agenda:** None.
        *   **Secret Agenda:** Some maintain hope of escape; others have broken and serve Han out of fear.
        *   **Assets:** Knowledge of the underground complex, desperation-fueled courage if freed.
        *   **Relationships:** Need the party's help to escape; some may be informants for Han out of coercion.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Master Han:** The refined, ruthless crime lord with a collection of magical prosthetic hands granting different combat abilities.
    *   **Bolo:** The mountain of muscle, Han's chief enforcer, secretly fighting to protect his captive family.
    *   **Mei Ling:** The graceful spy with her own assassination agenda, potential ally or rival to the party.
    *   **Williams:** The brash street fighter seeking prize money, vulnerable to corruption.
    *   **Roper:** The disgraced monk turned gambler, already compromised by debts to Han.
    *   **O'Hara:** The sadistic tournament overseer who enjoys pain, both giving and receiving it.
    *   **Parsons:** Han's accountant who fights with poison-coated weapons and maintains the financial records.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Tournament competitor (various styles: grappler, striker, weapon specialist)"
    *   "Han's fortress guard (armored soldier)"
    *   "Enslaved laborer (various skills: alchemist, smith, servant)"
    *   "Criminal lieutenant (enforcer, smuggler, torturer)"
    *   "Shadow Court assassin"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Tournament Grounds:** An open-air arena carved into the mountainside with multiple combat platforms.
        *   **Key Landmarks:** The Grand Platform (main fighting stage), the Observation Pavilion (Han's viewing area), the Fighter's Temple (meditation area), the Trophy Wall (displaying weapons of defeated champions).
        *   **Primary Inhabitants:** Tournament competitors, Han's judges, spectators, guards.
        *   **Available Goods & Services:** Healing poultices, weapon repairs, meditation training, gambling on matches.
        *   **Potential Random Encounters (x5):** A fighter challenges the party to a friendly sparring match; Han's guards conduct a random inspection; a fellow competitor offers to share information for an alliance; a spectator tries to bribe a party member to throw a fight; Bolo appears to intimidate competitors.
        *   **Embedded Plot Hooks & Rumors (x3):** "The fighter who won last year's tournament was never seen again." "Han's hands can catch blades barehanded—each one has a different power." "There's a secret entrance to the dungeons beneath the Trophy Wall."
        *   **Sensory Details:** Sight (stone platforms, colorful banners, tropical sun), Sound (gong announcing matches, crowd cheers, ocean waves), Smell (sweat, incense from the temple, salt air).
    *   **The Hall of Mirrors:** A magical arena where reality and illusion blend through countless reflective surfaces.
        *   **Key Landmarks:** The Thousand Reflections Chamber (central fighting space), the Golden Gates (entrance), the True Mirror (one mirror that cannot lie), hidden passages behind mirrors.
        *   **Primary Inhabitants:** Han, his elite guards, mirror illusions.
        *   **Available Goods & Services:** None—this is a combat zone.
        *   **Potential Random Encounters (x5):** Mirror duplicates attack; reflections move independently creating distraction; a mirror shatters revealing a secret passage; the party sees their own deaths in a mirror (illusion or prophecy?); Han appears in multiple mirrors simultaneously.
        *   **Embedded Plot Hooks & Rumors (x3):** "The True Mirror shows your greatest fear." "Han commissioned the Hall from a mad wizard who died in its construction." "Breaking all the mirrors will collapse the chamber."
        *   **Sensory Details:** Sight (infinite reflections, disorienting angles, golden mirror frames), Sound (footsteps echoing from all directions, glass creaking), Smell (polish, ozone from magic).
    *   **The Underground Complex:** A network of caves converted into Han's criminal operation base.
        *   **Key Landmarks:** The Jade Poppy Laboratory (opium processing), the Holding Pens (slave quarters), the Vault (treasure and records), the Serpent's Grotto (smuggling dock).
        *   **Primary Inhabitants:** Enslaved workers, guards, alchemists working for Han, shadow creatures as additional security.
        *   **Available Goods & Services:** None available for purchase, but the vault contains weapons, magic items, and incriminating documents.
        *   **Potential Random Encounters (x5):** Guard patrol changes shifts; an enslaved worker begs for help; an alchemical experiment goes wrong creating toxic gas; smugglers arrive with new captives; a trained owlbear breaks loose.
        *   **Embedded Plot Hooks & Rumors (x3):** "Bolo's family is kept in the deepest cell." "The vault can only be opened with one of Han's hands—literally." "There's a sea exit that's unguarded at low tide."
        *   **Sensory Details:** Sight (torch-lit tunnels, damp stone, cages), Sound (dripping water, groans of prisoners, distant ocean waves through caves), Smell (opium smoke, sweat, mildew, salt).
    *   **Han's Throne Room:** A lavish chamber showcasing his wealth and the trophies of his victories.
        *   **Key Landmarks:** The Dragon Throne (carved from black marble), the Wall of Hands (display of his prosthetic collection), the Victory Tapestry (depicting his tournament wins), secret door to his private chambers.
        *   **Primary Inhabitants:** Han, his personal bodyguards, occasionally honored guests.
        *   **Available Goods & Services:** Audience with Han, bribes and corruption opportunities.
        *   **Potential Random Encounters (x5):** Han offers the party positions in his organization; Bolo stands guard silently; a previous tournament winner serves as Han's servant; Han demonstrates a new prosthetic hand's power; an assassination attempt occurs.
        *   **Embedded Plot Hooks & Rumors (x3):** "Han never removes his gloves in public." "The throne was stolen from a dragon's hoard." "Han's bedroom contains the original tournament records showing his first murder."
        *   **Sensory Details:** Sight (rich tapestries, golden decorations, exotic weapons on display), Sound (quiet, controlled, occasional clink of armor), Smell (expensive incense, polished wood, exotic flowers).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The party wins three tournament matches in a row.
    *   **THEN:** Han personally invites them to a private dinner, offering recruitment into his inner circle and access to restricted areas. Generate a scene where Han subtly tests their loyalty and hints at his true business.
    *   **IF:** The party's Suspicion Score reaches 5 (from failed stealth checks or questioning the wrong people).
    *   **THEN:** Han assigns Bolo to watch them openly. Night exploration becomes much more difficult, and any further suspicion triggers a confrontation.
    *   **IF:** The party frees prisoners before defeating Han.
    *   **THEN:** The island erupts into chaos. Riot encounters throughout the complex, but the party gains numerous NPC allies. Han goes into lockdown in the Hall of Mirrors with his elite guards.
    *   **IF:** The party defeats Bolo in combat but discovers his family is captive.
    *   **THEN:** Generate a moral choice scene where they can free his family to gain him as an ally (he knows all of Han's secrets) or leave them to focus on the main mission. Freeing them adds a rescue sub-quest but provides a powerful ally in the final battle.
    *   **IF:** The party discovers and steals Han's operation records before confronting him.
    *   **THEN:** Han becomes desperate and more aggressive. The final battle difficulty increases, but the party gains post-campaign benefits as they can dismantle his entire network using the stolen information.
    *   **IF:** A party member loses a tournament match.
    *   **THEN:** They are taken to the "recovery rooms" which are actually interrogation cells. Generate an escape challenge or rescue mission, and they discover the fate of other losers (enslaved, killed, or recruited).
    *   **IF:** The party destroys the Jade Poppy Laboratory.
    *   **THEN:** Han loses his primary product source. This cripples his operation financially but also eliminates any evidence of his drug trade. Generate consequences based on whether the party needed that evidence for legal prosecution.
