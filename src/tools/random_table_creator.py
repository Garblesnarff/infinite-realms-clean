"""Random Table Creator Tool for generating setting-specific random encounter tables."""

import json
import random
from typing import Any, Dict, List, Type

from crewai_tools import BaseTool
from pydantic import BaseModel, Field


class RandomTableCreatorInput(BaseModel):
    """Input schema for RandomTableCreator."""

    table_type: str = Field(
        ...,
        description="Type of table: 'encounters', 'weather', 'rumors', 'events', 'treasure', or 'npcs'",
    )
    setting_context: str = Field(
        ..., description="JSON context about the setting/location for this table"
    )
    num_entries: int = Field(default=20, description="Number of table entries to generate")


class RandomTableCreatorTool(BaseTool):
    """
    Tool for creating random tables specific to the campaign setting.

    Generates contextual random tables for encounters, weather, rumors, events,
    treasure, and quick NPCs based on the campaign setting.
    """

    name: str = "Random Table Creator"
    description: str = (
        "Creates random tables customized for your campaign setting. "
        "Generates encounters, weather, rumors, random events, treasure, and quick NPCs. "
        "Input should include table type and setting context (JSON)."
    )
    args_schema: Type[BaseModel] = RandomTableCreatorInput

    def _run(
        self,
        table_type: str,
        setting_context: str,
        num_entries: int = 20,
    ) -> str:
        """
        Generate a random table for the campaign.

        Args:
            table_type: Type of random table
            setting_context: JSON context about the setting
            num_entries: Number of entries to generate

        Returns:
            Formatted random table (JSON)
        """
        try:
            context = json.loads(setting_context)

            if table_type == "encounters":
                table = self._create_encounter_table(context, num_entries)
            elif table_type == "weather":
                table = self._create_weather_table(context, num_entries)
            elif table_type == "rumors":
                table = self._create_rumor_table(context, num_entries)
            elif table_type == "events":
                table = self._create_event_table(context, num_entries)
            elif table_type == "treasure":
                table = self._create_treasure_table(context, num_entries)
            elif table_type == "npcs":
                table = self._create_npc_table(context, num_entries)
            else:
                return json.dumps({"error": f"Unknown table type: {table_type}"})

            return json.dumps(table, indent=2)

        except json.JSONDecodeError as e:
            return f"Error parsing context JSON: {str(e)}"
        except Exception as e:
            return f"Error creating random table: {str(e)}"

    def _create_encounter_table(self, context: Dict, num_entries: int) -> Dict:
        """Create random encounter table."""
        setting = context.get("setting", "generic")
        danger_level = context.get("danger_level", "moderate")

        entries = []
        for i in range(1, num_entries + 1):
            # Mix of combat, social, and environmental encounters
            encounter_type = random.choice(["combat", "combat", "social", "environmental"])

            if encounter_type == "combat":
                entry = self._generate_combat_encounter(setting, danger_level)
            elif encounter_type == "social":
                entry = self._generate_social_encounter(setting)
            else:
                entry = self._generate_environmental_encounter(setting)

            entries.append({"roll": i, "encounter": entry})

        return {
            "title": f"Random Encounters - {context.get('location', 'Unknown')}",
            "type": "encounters",
            "dice": f"d{num_entries}",
            "entries": entries,
            "context": context,
        }

    def _create_weather_table(self, context: Dict, num_entries: int) -> Dict:
        """Create weather table."""
        climate = context.get("climate", "temperate")
        season = context.get("season", "summer")

        weather_options = {
            "temperate": ["Clear skies", "Partly cloudy", "Overcast", "Light rain", "Heavy rain", "Fog", "Wind"],
            "cold": ["Clear and cold", "Snowing lightly", "Heavy snowfall", "Blizzard", "Ice storm", "Freezing fog"],
            "hot": ["Scorching sun", "Heat wave", "Dust storm", "Brief rain", "Humid and oppressive"],
            "magical": ["Aurora dancing", "Arcane lightning", "Mana storm", "Reality shimmer", "Floating rain"],
        }

        options = weather_options.get(climate, weather_options["temperate"])
        entries = []

        for i in range(1, num_entries + 1):
            weather = random.choice(options)
            effect = self._generate_weather_effect(weather)
            entries.append({"roll": i, "weather": weather, "effect": effect})

        return {
            "title": f"Weather Table - {climate.title()} Climate",
            "type": "weather",
            "dice": f"d{num_entries}",
            "entries": entries,
            "context": context,
        }

    def _create_rumor_table(self, context: Dict, num_entries: int) -> Dict:
        """Create rumor table."""
        factions = context.get("factions", [])
        locations = context.get("locations", [])

        rumor_templates = [
            "They say {faction} is planning something big...",
            "A traveler swears they saw {creature} near {location}",
            "The {npc} hasn't been seen in days. Some say they've fled the region",
            "Strange lights were spotted over {location} last night",
            "A merchant claims {faction} is secretly allied with {faction2}",
            "Local children have been singing a creepy song about {location}",
            "A dying man's last words mentioned {artifact}",
            "The {npc} is offering a huge reward for {item}",
        ]

        entries = []
        for i in range(1, num_entries + 1):
            template = random.choice(rumor_templates)
            rumor = self._fill_rumor_template(template, context)
            truth = random.choice(["True", "Partially true", "False", "Misleading"])
            entries.append({"roll": i, "rumor": rumor, "truth": truth})

        return {
            "title": f"Rumors - {context.get('location', 'The Region')}",
            "type": "rumors",
            "dice": f"d{num_entries}",
            "entries": entries,
            "context": context,
        }

    def _create_event_table(self, context: Dict, num_entries: int) -> Dict:
        """Create random event table."""
        events = [
            "A messenger arrives with urgent news",
            "A fight breaks out nearby",
            "Unexpected weather change",
            "A pickpocket tries their luck",
            "A street performer gathers a crowd",
            "City guards rush past toward an emergency",
            "A noble's procession blocks the street",
            "A merchant offers a special deal",
            "Distant screams echo through the area",
            "A mysterious cloaked figure watches the party",
        ]

        entries = []
        for i in range(1, min(num_entries, len(events)) + 1):
            event = events[i - 1] if i <= len(events) else random.choice(events)
            entries.append({"roll": i, "event": event})

        return {
            "title": f"Random Events - {context.get('location', 'Urban')}",
            "type": "events",
            "dice": f"d{len(entries)}",
            "entries": entries,
            "context": context,
        }

    def _create_treasure_table(self, context: Dict, num_entries: int) -> Dict:
        """Create treasure table."""
        value_level = context.get("value_level", "moderate")

        treasure_types = [
            "Coins",
            "Gems",
            "Art object",
            "Mundane item",
            "Minor magic item",
            "Rare material",
        ]

        entries = []
        for i in range(1, num_entries + 1):
            treasure_type = random.choice(treasure_types)
            item = self._generate_treasure_item(treasure_type, value_level, context)
            entries.append({"roll": i, "treasure": item})

        return {
            "title": f"Treasure - {value_level.title()} Value",
            "type": "treasure",
            "dice": f"d{num_entries}",
            "entries": entries,
            "context": context,
        }

    def _create_npc_table(self, context: Dict, num_entries: int) -> Dict:
        """Create quick NPC table."""
        races = ["Human", "Elf", "Dwarf", "Halfling", "Gnome", "Half-elf", "Dragonborn", "Tiefling"]
        occupations = ["Merchant", "Guard", "Scholar", "Artisan", "Farmer", "Noble", "Priest", "Sellsword"]
        traits = ["Nervous", "Friendly", "Suspicious", "Greedy", "Honest", "Secretive", "Cheerful", "Grumpy"]

        entries = []
        for i in range(1, num_entries + 1):
            npc = {
                "race": random.choice(races),
                "occupation": random.choice(occupations),
                "trait": random.choice(traits),
                "quirk": self._generate_quirk(),
            }
            entries.append({"roll": i, "npc": npc})

        return {
            "title": f"Quick NPCs - {context.get('location', 'Generic')}",
            "type": "npcs",
            "dice": f"d{num_entries}",
            "entries": entries,
            "context": context,
        }

    # Helper methods
    def _generate_combat_encounter(self, setting: str, danger_level: str) -> str:
        """Generate a combat encounter description."""
        creatures = {
            "low": ["bandits", "wolves", "goblins", "skeletons"],
            "moderate": ["orcs", "gnolls", "cultists", "wights"],
            "high": ["trolls", "elementals", "assassins", "demons"],
        }
        numbers = ["a pair of", "a small group of", "several", "many"]
        situations = [
            "ambush from cover",
            "patrol the area",
            "guard their camp",
            "hunt for prey",
        ]

        creature_list = creatures.get(danger_level, creatures["moderate"])
        return f"{random.choice(numbers)} {random.choice(creature_list)} {random.choice(situations)}"

    def _generate_social_encounter(self, setting: str) -> str:
        """Generate a social encounter description."""
        npcs = ["traveling merchant", "lost child", "wandering bard", "injured soldier", "mysterious stranger"]
        situations = [
            "asks for directions",
            "seeks help with a problem",
            "offers information for a price",
            "warns of danger ahead",
        ]
        return f"A {random.choice(npcs)} {random.choice(situations)}"

    def _generate_environmental_encounter(self, setting: str) -> str:
        """Generate an environmental encounter."""
        events = [
            "Difficult terrain slows travel",
            "A sudden weather change",
            "Evidence of a recent battle",
            "An interesting landmark",
            "Animal tracks crossing the path",
            "A hidden cache is discovered",
        ]
        return random.choice(events)

    def _generate_weather_effect(self, weather: str) -> str:
        """Generate mechanical effect for weather."""
        effects = {
            "rain": "Disadvantage on Perception checks relying on sight",
            "fog": "Heavily obscured beyond 20 feet",
            "wind": "Disadvantage on ranged attacks",
            "snow": "Difficult terrain",
            "storm": "Loud noise, limited visibility",
        }
        for key in effects:
            if key in weather.lower():
                return effects[key]
        return "No mechanical effect"

    def _fill_rumor_template(self, template: str, context: Dict) -> str:
        """Fill in rumor template with context."""
        result = template
        if "{faction}" in template:
            factions = context.get("factions", ["a secret society"])
            result = result.replace("{faction}", random.choice(factions), 1)
        if "{faction2}" in result:
            factions = context.get("factions", ["unknown forces"])
            result = result.replace("{faction2}", random.choice(factions))
        if "{location}" in result:
            locations = context.get("locations", ["the old ruins"])
            result = result.replace("{location}", random.choice(locations))
        result = result.replace("{creature}", "a mysterious creature")
        result = result.replace("{npc}", "local notable")
        result = result.replace("{artifact}", "an ancient artifact")
        result = result.replace("{item}", "a rare item")
        return result

    def _generate_treasure_item(self, treasure_type: str, value_level: str, context: Dict) -> str:
        """Generate specific treasure item."""
        if treasure_type == "Coins":
            amounts = {"low": "2d6", "moderate": "4d6 × 10", "high": "2d6 × 100"}
            return f"{amounts.get(value_level, '3d6 × 10')} gp"
        elif treasure_type == "Gems":
            return f"A {random.choice(['sapphire', 'ruby', 'emerald', 'diamond'])} worth {random.choice(['50', '100', '500'])} gp"
        elif treasure_type == "Minor magic item":
            return random.choice(["Potion of healing", "Spell scroll", "+1 ammunition (10)", "Mystery potion"])
        return treasure_type

    def _generate_quirk(self) -> str:
        """Generate NPC quirk."""
        quirks = [
            "Speaks in rhyme",
            "Has a pet rat",
            "Missing a finger",
            "Always eating",
            "Extremely tall/short",
            "Colorful clothes",
            "Talks to themselves",
            "Fidgets constantly",
        ]
        return random.choice(quirks)
