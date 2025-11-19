"""D&D 5E Validator Tool for rules and lore compliance."""

import json
import re
from typing import Any, Dict, List, Optional, Type

from crewai_tools import BaseTool
from pydantic import BaseModel, Field


class DnD5EValidatorInput(BaseModel):
    """Input schema for D&D 5E Validator."""

    content: str = Field(..., description="Content to validate against D&D 5E rules")
    validation_type: str = Field(
        ...,
        description="Type of validation: 'mechanics', 'lore', 'balance', 'encounter', or 'all'",
    )


class DnD5EValidatorTool(BaseTool):
    """
    Tool for validating campaign content against D&D 5E rules and conventions.

    Checks for:
    - Spell/ability mechanics compliance
    - CR and encounter balance
    - Lore consistency with official D&D settings
    - Game balance issues
    """

    name: str = "D&D 5E Validator"
    description: str = (
        "Validates campaign content against D&D 5th Edition rules, mechanics, "
        "and lore. Checks for rule compliance, game balance, and encounter difficulty. "
        "Specify validation type: 'mechanics', 'lore', 'balance', 'encounter', or 'all'."
    )
    args_schema: Type[BaseModel] = DnD5EValidatorInput

    # D&D 5E Reference Data
    SPELL_LEVELS = list(range(0, 10))  # Cantrips (0) through 9th level
    DAMAGE_TYPES = [
        "acid",
        "bludgeoning",
        "cold",
        "fire",
        "force",
        "lightning",
        "necrotic",
        "piercing",
        "poison",
        "psychic",
        "radiant",
        "slashing",
        "thunder",
    ]
    ABILITY_SCORES = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
    CREATURE_TYPES = [
        "aberration",
        "beast",
        "celestial",
        "construct",
        "dragon",
        "elemental",
        "fey",
        "fiend",
        "giant",
        "humanoid",
        "monstrosity",
        "ooze",
        "plant",
        "undead",
    ]

    # CR to XP mapping
    CR_XP = {
        "0": 10,
        "1/8": 25,
        "1/4": 50,
        "1/2": 100,
        "1": 200,
        "2": 450,
        "3": 700,
        "4": 1100,
        "5": 1800,
        "6": 2300,
        "7": 2900,
        "8": 3900,
        "9": 5000,
        "10": 5900,
        "11": 7200,
        "12": 8400,
        "13": 10000,
        "14": 11500,
        "15": 13000,
        "16": 15000,
        "17": 18000,
        "18": 20000,
        "19": 22000,
        "20": 25000,
        "21": 33000,
        "22": 41000,
        "23": 50000,
        "24": 62000,
        "25": 75000,
        "26": 90000,
        "27": 105000,
        "28": 120000,
        "29": 135000,
        "30": 155000,
    }

    def _run(self, content: str, validation_type: str = "all") -> str:
        """
        Validate content against D&D 5E rules.

        Args:
            content: The content to validate
            validation_type: Type of validation to perform

        Returns:
            Validation report with findings and recommendations
        """
        results = {
            "validation_type": validation_type,
            "issues": [],
            "warnings": [],
            "suggestions": [],
            "compliant": True,
        }

        if validation_type in ["mechanics", "all"]:
            self._validate_mechanics(content, results)

        if validation_type in ["lore", "all"]:
            self._validate_lore(content, results)

        if validation_type in ["balance", "all"]:
            self._validate_balance(content, results)

        if validation_type in ["encounter", "all"]:
            self._validate_encounter(content, results)

        results["compliant"] = len(results["issues"]) == 0

        return json.dumps(results, indent=2)

    def _validate_mechanics(self, content: str, results: Dict):
        """Check for mechanical rule compliance."""
        content_lower = content.lower()

        # Check for invalid spell levels
        spell_level_pattern = r"(\d+)(?:st|nd|rd|th)[\s-]level spell"
        matches = re.findall(spell_level_pattern, content_lower)
        for match in matches:
            level = int(match)
            if level not in self.SPELL_LEVELS:
                results["issues"].append(
                    f"Invalid spell level: {level}. D&D 5E spells range from 0 (cantrips) to 9."
                )

        # Check for invalid ability scores
        for ability in ["str", "dex", "con", "int", "wis", "cha"]:
            pattern = rf"{ability}(?:ength|terity|stitution|elligence|dom|risma)?\s*(?:score|modifier)?\s*(?:of\s*)?(\d+)"
            matches = re.findall(pattern, content_lower)
            for match in matches:
                score = int(match)
                if score > 30:
                    results["warnings"].append(
                        f"Ability score of {score} is extremely high. "
                        f"Consider if this is intentional (typical max is 20 for PCs, 30 for gods)."
                    )

        # Check damage types
        damage_pattern = r"(\w+)\s+damage"
        matches = re.findall(damage_pattern, content_lower)
        for match in matches:
            if match not in self.DAMAGE_TYPES and match not in ["magical", "nonmagical"]:
                results["suggestions"].append(
                    f"'{match}' damage type found. "
                    f"Verify this is a valid D&D 5E damage type: {', '.join(self.DAMAGE_TYPES)}"
                )

    def _validate_lore(self, content: str, results: Dict):
        """Check for lore consistency."""
        content_lower = content.lower()

        # Check creature types
        creature_pattern = r"(\w+)\s+(?:creature|monster|enemy|being)"
        matches = re.findall(creature_pattern, content_lower)
        for match in matches:
            if match in self.CREATURE_TYPES:
                results["suggestions"].append(
                    f"Creature type '{match}' detected. "
                    f"Ensure it aligns with D&D 5E creature type conventions."
                )

        # Detect common lore conflicts
        if "tarrasque" in content_lower and "multiple" in content_lower:
            results["warnings"].append(
                "Multiple Tarrasques mentioned. "
                "In standard D&D lore, there is typically only one Tarrasque."
            )

    def _validate_balance(self, content: str, results: Dict):
        """Check for game balance issues."""
        content_lower = content.lower()

        # Check for overpowered items
        legendary_pattern = r"legendary\s+(?:item|weapon|armor|artifact)"
        if re.search(legendary_pattern, content_lower):
            results["suggestions"].append(
                "Legendary item detected. Ensure it's appropriate for the party level "
                "and doesn't overshadow other players."
            )

        # Check for resistance/immunity stacking
        if "resistance" in content_lower and "immunity" in content_lower:
            results["warnings"].append(
                "Both resistance and immunity mentioned. "
                "Verify these don't stack inappropriately (immunity supersedes resistance)."
            )

    def _validate_encounter(self, content: str, results: Dict):
        """Validate encounter difficulty."""
        # Look for CR mentions
        cr_pattern = r"CR\s*(\d+|1/\d+)"
        matches = re.findall(cr_pattern, content, re.IGNORECASE)

        if matches:
            total_xp = 0
            for cr in matches:
                cr_str = cr.replace(" ", "")
                if cr_str in self.CR_XP:
                    total_xp += self.CR_XP[cr_str]

            if total_xp > 0:
                results["suggestions"].append(
                    f"Encounter XP budget: {total_xp} XP. "
                    f"For a party of 4, this is appropriate for: "
                    f"Level 1 (Deadly: 400), Level 5 (Deadly: 4400), "
                    f"Level 10 (Deadly: 10400), Level 15 (Deadly: 18000), Level 20 (Deadly: 28800)"
                )

        # Check for action economy
        if "legendary action" in content_lower or "lair action" in content_lower:
            results["suggestions"].append(
                "Legendary/Lair actions detected. These help balance solo monsters "
                "against multiple PCs. Ensure boss fights include these."
            )

    def validate_stat_block(self, stat_block: Dict[str, Any]) -> str:
        """
        Validate a creature stat block.

        Args:
            stat_block: Dictionary containing creature statistics

        Returns:
            Validation report
        """
        # This could be expanded significantly
        issues = []

        required_fields = ["name", "type", "armor_class", "hit_points", "speed"]
        for field in required_fields:
            if field not in stat_block:
                issues.append(f"Missing required field: {field}")

        if stat_block.get("type") and stat_block["type"].lower() not in self.CREATURE_TYPES:
            issues.append(f"Invalid creature type: {stat_block['type']}")

        return json.dumps({"issues": issues, "valid": len(issues) == 0}, indent=2)
