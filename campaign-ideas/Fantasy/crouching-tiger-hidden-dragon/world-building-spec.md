### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**Crouching Tiger, Hidden Dragon**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The legendary sword Green Destiny has been stolen from the estate of the recently retired warrior Master Li Mu Bai. The theft triggers a chase across mountain monasteries, bamboo forests, and desert kingdoms, revealing a web of forbidden romance, secret martial arts schools, and a young aristocrat who dreams of freedom through the warrior's path. The party must recover the sword while navigating the complex relationships between masters and students, duty and desire, vengeance and redemption.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the history of the Green Destiny sword, its creation, and why it's considered legendary among warriors.
    *   Write the story of the Wudang Mountain monastery and its role as the keeper of orthodox martial arts traditions.
    *   Describe the incident where Jade Fox was denied training and killed Li Mu Bai's master, creating the cycle of vengeance.
    *   Explain the social structure that prevents women from openly practicing martial arts in this setting.
    *   Detail Lo's bandit clan and their code of honor in the lawless Gobi Desert.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Wudang Orthodox School** (Major)
        *   **Goals:** Preserve traditional martial arts, maintain moral authority, prevent forbidden techniques from spreading.
        *   **Hierarchy:** Abbot at the top, senior masters, warrior monks, novices.
        *   **Public Agenda:** To be the moral and technical authority on martial arts in the realm.
        *   **Secret Agenda:** To suppress any martial arts knowledge that challenges their authority, including techniques they consider too dangerous or evidence of their past discriminatory practices.
        *   **Assets:** Wudang Mountain monastery, ancient texts, network of allied schools, political influence.
        *   **Relationships:** Allies with Li Mu Bai and the establishment; opposed to Jade Fox and independent warriors who reject their authority.
    *   **The Dark Dust Bandits** (Minor)
        *   **Goals:** Survive in the desert, raid caravans, maintain their freedom from Imperial law.
        *   **Hierarchy:** Lo as chief, lieutenant commanders, raiders, scouts.
        *   **Public Agenda:** None—they're outlaws.
        *   **Secret Agenda:** Lo wants to leave the bandit life to be with Jen Yu, but can't abandon his clan without destabilizing their survival.
        *   **Assets:** Desert knowledge, fortress hideout, stolen goods, fierce warriors.
        *   **Relationships:** Opposed to Imperial forces and merchants; connected to Jen Yu through romance; neutral to the party unless provoked.
    *   **The Imperial Aristocracy** (Minor)
        *   **Goals:** Maintain social order, arrange political marriages, preserve their wealth and status.
        *   **Hierarchy:** Emperor, provincial governors (including Governor Yu), nobles, servants.
        *   **Public Agenda:** To govern the realm and uphold traditional values.
        *   **Secret Agenda:** Individual nobles seek to increase their power through marriage alliances and control of resources.
        *   **Assets:** Wealth, legal authority, private guards, political connections.
        *   **Relationships:** Jen Yu's family faction; want to force her into arranged marriage; hire the party to recover stolen property (Green Destiny).
    *   **Jade Fox's Network** (Minor)
        *   **Goals:** Achieve revenge against the martial arts establishment that rejected Jade Fox.
        *   **Hierarchy:** Jade Fox as master, Jen Yu as student (unknowing pawn), hired assassins.
        *   **Public Agenda:** None—they operate in secret.
        *   **Secret Agenda:** Jade Fox uses Jen Yu to interpret the Wudang manual, planning to use this knowledge to destroy the orthodox schools and kill Li Mu Bai.
        *   **Assets:** Stolen Wudang manual, poison expertise, hidden training locations.
        *   **Relationships:** Primary antagonist faction; in conflict with Li Mu Bai and Wudang; manipulating Jen Yu.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Li Mu Bai:** The legendary warrior seeking peace, dying from Jade Fox's poison, mentor figure.
    *   **Yu Shu Lien:** Strong female warrior, security company owner, Li Mu Bai's unspoken love.
    *   **Jen Yu:** Aristocratic young woman torn between duty, love, and the warrior's path, wielder of Green Destiny.
    *   **Jade Fox:** Vengeful master denied training because of her gender, killed Li's master, uses poison.
    *   **Lo (Dark Dust):** Charismatic bandit chief in love with Jen Yu, offers her freedom outside society.
    *   **Governor Yu:** Jen Yu's father, traditional aristocrat arranging her marriage.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Wudang monastery monk (various ranks)"
    *   "Desert bandit (loyal to Lo)"
    *   "Aristocratic servant or guard"
    *   "Jade Fox's hired assassin"
    *   "Imperial soldier"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Bamboo Forest of Tianshan:** A massive grove of towering bamboo where aerial combat becomes possible.
        *   **Key Landmarks:** The Grove Heart (densest area), The Whispering Path (narrow trail), The Stalks of Heaven (tallest bamboo reaching 120 feet), The Mirror Pond (reflecting pool).
        *   **Primary Inhabitants:** Rare wildlife, occasional hermit monks, the party during their pursuit of Jen Yu.
        *   **Available Goods & Services:** Natural resources (bamboo for crafting, medicinal herbs), meditation spots.
        *   **Potential Random Encounters (x5):** A sudden wind gust causes bamboo to sway dangerously; a wild tiger stalks the party; a hermit monk offers cryptic wisdom; Jen Yu appears for a duel; bamboo stalks fall creating obstacles.
        *   **Embedded Plot Hooks & Rumors (x3):** "The bamboo forest is sacred to an ancient nature spirit." "Those who meditate here at dawn achieve perfect balance." "Jen Yu hid something in the hollow of a marked bamboo."
        *   **Sensory Details:** Sight (green stalks rising to the sky, dappled sunlight, swaying motion), Sound (creaking bamboo, rustling leaves, wind whistling through hollow stalks), Smell (fresh green scent, earth, morning dew).
    *   **Wudang Mountain Monastery:** The sacred temple complex atop misty peaks, home of orthodox martial arts.
        *   **Key Landmarks:** The Grand Hall (main temple), The Library of Forms (martial arts texts), The Training Courtyard, The Peak Sanctuary (meditation area).
        *   **Primary Inhabitants:** Abbot, senior masters, warrior monks, pilgrims.
        *   **Available Goods & Services:** Healing, training in orthodox techniques, access to non-forbidden texts, sanctuary.
        *   **Potential Random Encounters (x5):** Morning martial arts practice (display of skill); a monk tests the party's knowledge of philosophy; a ceremony to receive or return sacred objects; Jade Fox's assassins infiltrate; a trial of worthiness.
        *   **Embedded Plot Hooks & Rumors (x3):** "The original Wudang manual has techniques even the masters haven't mastered." "Li Mu Bai's master is buried here with secrets." "The monastery has a women's section that's locked and forbidden."
        *   **Sensory Details:** Sight (white walls, curved roofs, prayer flags, mist rolling through courtyards), Sound (bells, chanting, waterfalls), Smell (incense, mountain air, tea).
    *   **The Gobi Desert & Lo's Fortress:** Vast wasteland with a hidden bandit stronghold in red rock canyons.
        *   **Key Landmarks:** The Oasis of Singing Sands, The Red Canyon Fortress, The Camel Trails, The Windswept Dunes.
        *   **Primary Inhabitants:** Lo's bandit clan, desert merchants, occasional Imperial patrols.
        *   **Available Goods & Services:** Black market goods, desert navigation guides, information about Jen Yu's time here.
        *   **Potential Random Encounters (x5):** Sandstorm requiring survival checks; rival bandit raid; a caravan to rob or protect; desert creatures (giant scorpions); flashback scene of Jen and Lo's romance.
        *   **Embedded Plot Hooks & Rumors (x3):** "Lo keeps Jen's jade comb as a token of love." "There's a hidden route through the canyon only Lo knows." "Jen Yu learned to ride and fight here, freed from aristocratic constraints."
        *   **Sensory Details:** Sight (endless tan dunes, red rock formations, harsh sun), Sound (wind howling, sand hissing, silence), Smell (dry air, dust, distant campfire smoke).
    *   **Jade Fox's Hidden Monastery:** A ruined temple in a remote canyon, converted to a secret training ground.
        *   **Key Landmarks:** The Poisoned Garden (toxic plants), The Training Hall (practice equipment), The Hidden Library (stolen texts including Wudang manual), The Escape Tunnels.
        *   **Primary Inhabitants:** Jade Fox, occasionally Jen Yu during training, hired guards.
        *   **Available Goods & Services:** None for the party—this is enemy territory.
        *   **Potential Random Encounters (x5):** Poison dart trap activates; Jade Fox appears for combat; Jen Yu's training equipment reveals her skill level; discovery of stolen texts; evidence of the master's murder.
        *   **Embedded Plot Hooks & Rumors (x3):** "Jade Fox was denied entrance to Wudang because she was a woman." "She killed Li's master but took a wound that never properly healed." "The Wudang manual has a technique that requires two practitioners—master and student."
        *   **Sensory Details:** Sight (crumbling stone, training equipment, scrolls scattered on tables), Sound (dripping water, rustling papers, footsteps echoing), Smell (poison herbs, old paper, damp stone).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The party supports Jen Yu's freedom over her duty to family.
    *   **THEN:** Jen Yu becomes a potential ally in the final battle. Generate scenes where she helps the party fight Jade Fox, but Governor Yu disowns her. Lo appears to offer her a place in the desert.
    *   **IF:** The party enforces tradition and tries to force Jen Yu back to aristocratic life.
    *   **THEN:** Jen Yu becomes increasingly desperate and reckless with Green Destiny. Generate escalating confrontations where she fights the party. In the tragic ending, she leaps from Wudang Mountain.
    *   **IF:** Li Mu Bai dies from Jade Fox's poison before the cure is found.
    *   **THEN:** Yu Shu Lien becomes consumed with vengeance, abandoning her controlled demeanor. Generate scenes where she hunts Jade Fox without mercy, potentially becoming morally compromised.
    *   **IF:** The party finds and returns all pages of the stolen Wudang manual.
    *   **THEN:** The Wudang monastery offers to teach the party one legendary technique as reward. However, Jen Yu loses access to this knowledge, weakening her in the final confrontation.
    *   **IF:** Lo dies protecting Jen Yu.
    *   **THEN:** Jen Yu loses her path to freedom through love. Generate a scene where she must find meaning in the warrior's path alone, or choose the tragic ending.
    *   **IF:** The party brokers a deal allowing women to train at Wudang.
    *   **THEN:** This revolutionizes the setting's future. Jade Fox's motivation is undercut. Generate an epilogue where female students arrive at the monastery, changing tradition. Jen Yu has a legitimate path.
    *   **IF:** The party defeats Jade Fox but spares her life.
    *   **THEN:** In prison, Jade Fox reveals additional secrets about the old master's death that complicate Li Mu Bai's quest for closure. She could become an unlikely source of information about even older techniques.
