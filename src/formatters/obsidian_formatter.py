"""Obsidian vault formatter for campaign bible output."""

from pathlib import Path
from typing import Any, Dict, List


class ObsidianFormatter:
    """
    Formats campaign bible content as an Obsidian vault.

    Creates interconnected notes with backlinks for easy navigation.
    """

    def __init__(self, campaign_name: str):
        """
        Initialize the formatter.

        Args:
            campaign_name: Name of the campaign
        """
        self.campaign_name = campaign_name

    def create_vault(self, elements: Dict[str, Any], output_dir: Path):
        """
        Create Obsidian vault structure.

        Args:
            elements: All campaign elements
            output_dir: Output directory for vault
        """
        vault_dir = output_dir / f"{self.campaign_name.replace(' ', '_')}_Vault"
        vault_dir.mkdir(parents=True, exist_ok=True)

        # Create folder structure
        folders = ["Factions", "NPCs", "Locations", "Hooks", "World"]
        for folder in folders:
            (vault_dir / folder).mkdir(exist_ok=True)

        # Create index
        self._create_index(vault_dir, elements)

        # Create world foundation notes
        if "world_foundation" in elements:
            self._create_world_notes(vault_dir / "World", elements["world_foundation"])

        # Create faction notes
        if "factions" in elements:
            self._create_faction_notes(vault_dir / "Factions", elements["factions"])

        # Create NPC notes
        if "npcs" in elements:
            self._create_npc_notes(vault_dir / "NPCs", elements["npcs"])

        # Create location notes
        if "locations" in elements:
            self._create_location_notes(vault_dir / "Locations", elements["locations"])

        # Create hook notes
        if "hooks" in elements:
            self._create_hook_notes(vault_dir / "Hooks", elements["hooks"])

        # Create player handout
        if "player_handout" in elements:
            self._create_player_handout(vault_dir, elements["player_handout"])

        print(f"✅ Obsidian vault created at: {vault_dir}")
        return vault_dir

    def _create_index(self, vault_dir: Path, elements: Dict[str, Any]):
        """Create main index note."""
        content = [f"# {self.campaign_name}\n\n"]
        content.append("## Campaign Index\n\n")

        # Link to major sections
        content.append("### World\n")
        content.append("- [[Geography]]\n")
        content.append("- [[History]]\n")
        content.append("- [[Cosmology]]\n\n")

        content.append("### Factions\n")
        if "factions" in elements:
            for faction in elements["factions"]:
                name = faction.get("name", "Unknown")
                content.append(f"- [[{name}]]\n")
        content.append("\n")

        content.append("### Important NPCs\n")
        if "npcs" in elements:
            for npc in elements["npcs"][:10]:  # Top 10
                name = npc.get("name", "Unknown")
                content.append(f"- [[{name}]]\n")
        content.append("\n")

        content.append("### Key Locations\n")
        if "locations" in elements:
            for location in elements["locations"]:
                name = location.get("name", "Unknown")
                content.append(f"- [[{name}]]\n")
        content.append("\n")

        content.append("### Adventure Hooks\n")
        content.append("- [[Tier 1 Hooks]]\n")
        content.append("- [[Tier 2 Hooks]]\n")
        content.append("- [[Tier 3 Hooks]]\n")
        content.append("- [[Tier 4 Hooks]]\n\n")

        content.append("---\n\n")
        content.append("*For players: see [[Player Handout]]*\n")

        with open(vault_dir / "Index.md", "w", encoding="utf-8") as f:
            f.write("".join(content))

    def _create_world_notes(self, world_dir: Path, foundation: Dict[str, Any]):
        """Create world foundation notes."""
        # Geography
        if "geography" in foundation:
            with open(world_dir / "Geography.md", "w", encoding="utf-8") as f:
                f.write("# Geography\n\n")
                geography = foundation["geography"]
                if isinstance(geography, dict):
                    for key, value in geography.items():
                        f.write(f"## {key.replace('_', ' ').title()}\n\n{value}\n\n")
                else:
                    f.write(f"{geography}\n")

        # History
        if "history" in foundation:
            with open(world_dir / "History.md", "w", encoding="utf-8") as f:
                f.write("# Historical Timeline\n\n")
                history = foundation["history"]
                if isinstance(history, list):
                    for event in history:
                        if isinstance(event, dict):
                            f.write(f"## {event.get('year', 'Unknown')}\n\n{event.get('event', '')}\n\n")
                        else:
                            f.write(f"- {event}\n")
                else:
                    f.write(f"{history}\n")

        # Cosmology
        if "cosmology" in foundation:
            with open(world_dir / "Cosmology.md", "w", encoding="utf-8") as f:
                f.write("# Cosmology & Planes\n\n")
                cosmology = foundation["cosmology"]
                if isinstance(cosmology, dict):
                    for plane, description in cosmology.items():
                        f.write(f"## {plane}\n\n{description}\n\n")
                else:
                    f.write(f"{cosmology}\n")

    def _create_faction_notes(self, factions_dir: Path, factions: List[Dict]):
        """Create individual faction notes."""
        for faction in factions:
            name = faction.get("name", "Unknown")
            filename = f"{name.replace(' ', '_').replace('/', '_')}.md"

            with open(factions_dir / filename, "w", encoding="utf-8") as f:
                f.write(f"# {name}\n\n")
                f.write("---\n")
                f.write(f"Type: Faction\n")
                f.write("---\n\n")

                if "description" in faction:
                    f.write(f"{faction['description']}\n\n")

                if "goal" in faction:
                    f.write(f"## Primary Goal\n\n{faction['goal']}\n\n")

                if "leadership" in faction:
                    f.write(f"## Leadership\n\n{faction['leadership']}\n\n")

                # Create links to allies and enemies
                if "allies" in faction:
                    f.write("## Allies\n\n")
                    allies = faction["allies"]
                    if isinstance(allies, list):
                        for ally in allies:
                            f.write(f"- [[{ally}]]\n")
                    else:
                        f.write(f"- [[{allies}]]\n")
                    f.write("\n")

                if "enemies" in faction or "rivals" in faction:
                    rivals = faction.get("enemies", faction.get("rivals", []))
                    f.write("## Enemies/Rivals\n\n")
                    if isinstance(rivals, list):
                        for rival in rivals:
                            f.write(f"- [[{rival}]]\n")
                    else:
                        f.write(f"- [[{rivals}]]\n")
                    f.write("\n")

                if "hooks" in faction:
                    f.write("## Plot Hooks\n\n")
                    hooks = faction["hooks"]
                    if isinstance(hooks, list):
                        for hook in hooks:
                            f.write(f"- {hook}\n")
                    else:
                        f.write(f"- {hooks}\n")

    def _create_npc_notes(self, npcs_dir: Path, npcs: List[Dict]):
        """Create individual NPC notes."""
        for npc in npcs:
            name = npc.get("name", "Unknown")
            filename = f"{name.replace(' ', '_').replace('/', '_')}.md"

            with open(npcs_dir / filename, "w", encoding="utf-8") as f:
                f.write(f"# {name}\n\n")
                f.write("---\n")
                f.write(f"Type: NPC\n")
                if "race" in npc:
                    f.write(f"Race: {npc['race']}\n")
                if "role" in npc or "occupation" in npc:
                    f.write(f"Role: {npc.get('role', npc.get('occupation', ''))}\n")
                f.write("---\n\n")

                # Link to faction
                if "faction" in npc or "affiliation" in npc:
                    faction = npc.get("faction", npc.get("affiliation", ""))
                    f.write(f"**Faction**: [[{faction}]]\n\n")

                f.write("## Motivation\n\n")
                if "wants" in npc:
                    f.write(f"**Wants**: {npc['wants']}\n\n")
                if "fears" in npc:
                    f.write(f"**Fears**: {npc['fears']}\n\n")
                if "offers" in npc:
                    f.write(f"**Offers**: {npc['offers']}\n\n")

                if "secrets" in npc:
                    f.write(f"## Secrets\n\n{npc['secrets']}\n\n")

                if "personality" in npc or "trait" in npc:
                    trait = npc.get("personality", npc.get("trait", ""))
                    f.write(f"## Personality\n\n{trait}\n\n")

    def _create_location_notes(self, locations_dir: Path, locations: List[Dict]):
        """Create individual location notes."""
        for location in locations:
            name = location.get("name", "Unknown")
            filename = f"{name.replace(' ', '_').replace('/', '_')}.md"

            with open(locations_dir / filename, "w", encoding="utf-8") as f:
                f.write(f"# {name}\n\n")
                f.write("---\n")
                f.write(f"Type: Location\n")
                if "type" in location:
                    f.write(f"Location Type: {location['type']}\n")
                f.write("---\n\n")

                if "description" in location:
                    f.write(f"{location['description']}\n\n")

                if "features" in location or "key_features" in location:
                    features = location.get("features", location.get("key_features", []))
                    f.write("## Key Features\n\n")
                    if isinstance(features, list):
                        for feature in features:
                            f.write(f"- {feature}\n")
                    else:
                        f.write(f"- {features}\n")
                    f.write("\n")

                # Link to factions
                if "factions" in location or "factions_present" in location:
                    factions = location.get("factions", location.get("factions_present", []))
                    f.write("## Factions Present\n\n")
                    if isinstance(factions, list):
                        for faction in factions:
                            f.write(f"- [[{faction}]]\n")
                    else:
                        f.write(f"- [[{factions}]]\n")
                    f.write("\n")

                # Link to NPCs
                if "npcs" in location or "important_npcs" in location:
                    npcs = location.get("npcs", location.get("important_npcs", []))
                    f.write("## Important NPCs\n\n")
                    if isinstance(npcs, list):
                        for npc in npcs:
                            f.write(f"- [[{npc}]]\n")
                    else:
                        f.write(f"- [[{npcs}]]\n")
                    f.write("\n")

                if "hooks" in location or "adventure_hooks" in location:
                    hooks = location.get("hooks", location.get("adventure_hooks", []))
                    f.write("## Adventure Hooks\n\n")
                    if isinstance(hooks, list):
                        for hook in hooks:
                            f.write(f"- {hook}\n")
                    else:
                        f.write(f"- {hooks}\n")

    def _create_hook_notes(self, hooks_dir: Path, hooks: Dict[str, Any]):
        """Create adventure hook notes by tier."""
        for tier in ["tier_1", "tier_2", "tier_3", "tier_4"]:
            if tier in hooks:
                tier_name = {
                    "tier_1": "Tier 1 Hooks",
                    "tier_2": "Tier 2 Hooks",
                    "tier_3": "Tier 3 Hooks",
                    "tier_4": "Tier 4 Hooks",
                }[tier]

                filename = f"{tier_name.replace(' ', '_')}.md"

                with open(hooks_dir / filename, "w", encoding="utf-8") as f:
                    f.write(f"# {tier_name}\n\n")

                    tier_hooks = hooks[tier]
                    if isinstance(tier_hooks, list):
                        for hook in tier_hooks:
                            if isinstance(hook, dict):
                                hook_type = hook.get("type", "General")
                                hook_text = hook.get("hook", "")
                                f.write(f"## [{hook_type.title()}]\n\n{hook_text}\n\n")
                            else:
                                f.write(f"- {hook}\n\n")
                    else:
                        f.write(f"{tier_hooks}\n")

    def _create_player_handout(self, vault_dir: Path, handout: str):
        """Create player handout note."""
        with open(vault_dir / "Player Handout.md", "w", encoding="utf-8") as f:
            f.write(handout)
