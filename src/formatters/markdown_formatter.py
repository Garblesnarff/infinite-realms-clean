"""Markdown formatter for campaign bible output."""

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List


class MarkdownFormatter:
    """
    Formats campaign bible content as well-structured Markdown.

    Creates a comprehensive, printable document suitable for DM reference.
    """

    def __init__(self, campaign_name: str):
        """
        Initialize the formatter.

        Args:
            campaign_name: Name of the campaign
        """
        self.campaign_name = campaign_name

    def format_full_bible(self, elements: Dict[str, Any]) -> str:
        """
        Format complete campaign bible.

        Args:
            elements: All campaign elements

        Returns:
            Complete markdown document
        """
        sections = []

        # Title and metadata
        sections.append(self._format_title())
        sections.append(self._format_toc())

        # Player handout
        if "player_handout" in elements:
            sections.append("\n---\n\n# Player Handout\n\n")
            sections.append(elements["player_handout"])

        # DM content
        sections.append("\n---\n\n# Dungeon Master's Reference\n\n")

        # World foundation
        if "world_foundation" in elements:
            sections.append(self._format_world_foundation(elements["world_foundation"]))

        # Factions
        if "factions" in elements:
            sections.append(self._format_factions(elements["factions"]))

        # NPCs
        if "npcs" in elements:
            sections.append(self._format_npcs(elements["npcs"]))

        # Locations
        if "locations" in elements:
            sections.append(self._format_locations(elements["locations"]))

        # Adventure hooks
        if "hooks" in elements:
            sections.append(self._format_hooks(elements["hooks"]))

        # Connections
        if "connections" in elements:
            sections.append(self._format_connections(elements["connections"]))

        return "\n".join(sections)

    def _format_title(self) -> str:
        """Format title page."""
        return f"""# {self.campaign_name}
## Campaign Bible

*Generated on {datetime.now().strftime("%B %d, %Y")}*

---
"""

    def _format_toc(self) -> str:
        """Format table of contents."""
        return """## Table of Contents

1. [Player Handout](#player-handout)
2. [World Foundation](#world-foundation)
3. [Factions](#factions)
4. [NPCs](#npcs)
5. [Locations](#locations)
6. [Adventure Hooks](#adventure-hooks)
7. [Connections & Relationships](#connections--relationships)

---
"""

    def _format_world_foundation(self, foundation: Dict[str, Any]) -> str:
        """Format world foundation section."""
        md = ["## World Foundation\n"]

        if "geography" in foundation:
            md.append("### Geography\n")
            geography = foundation["geography"]
            if isinstance(geography, dict):
                for key, value in geography.items():
                    md.append(f"**{key.replace('_', ' ').title()}**: {value}\n")
            else:
                md.append(f"{geography}\n")
            md.append("\n")

        if "history" in foundation:
            md.append("### History & Timeline\n")
            history = foundation["history"]
            if isinstance(history, list):
                for event in history:
                    if isinstance(event, dict):
                        md.append(f"- **{event.get('year', 'Unknown')}**: {event.get('event', '')}\n")
                    else:
                        md.append(f"- {event}\n")
            else:
                md.append(f"{history}\n")
            md.append("\n")

        if "cosmology" in foundation:
            md.append("### Cosmology & Planes\n")
            cosmology = foundation["cosmology"]
            if isinstance(cosmology, dict):
                for plane, description in cosmology.items():
                    md.append(f"**{plane}**: {description}\n")
            else:
                md.append(f"{cosmology}\n")
            md.append("\n")

        if "magic_system" in foundation:
            md.append("### Magic System\n")
            magic = foundation["magic_system"]
            if isinstance(magic, dict):
                for key, value in magic.items():
                    md.append(f"**{key.replace('_', ' ').title()}**: {value}\n")
            else:
                md.append(f"{magic}\n")
            md.append("\n")

        md.append("---\n\n")
        return "".join(md)

    def _format_factions(self, factions: List[Dict]) -> str:
        """Format factions section."""
        md = ["## Factions\n\n"]

        for faction in factions:
            name = faction.get("name", "Unknown Faction")
            md.append(f"### {name}\n\n")

            if "description" in faction:
                md.append(f"{faction['description']}\n\n")

            if "goal" in faction:
                md.append(f"**Primary Goal**: {faction['goal']}\n\n")

            if "resources" in faction:
                md.append(f"**Resources**: {faction['resources']}\n\n")

            if "leadership" in faction:
                md.append(f"**Leadership**: {faction['leadership']}\n\n")

            if "allies" in faction:
                allies = faction['allies']
                if isinstance(allies, list):
                    md.append(f"**Allies**: {', '.join(allies)}\n\n")
                else:
                    md.append(f"**Allies**: {allies}\n\n")

            if "enemies" in faction or "rivals" in faction:
                rivals = faction.get("enemies", faction.get("rivals", []))
                if isinstance(rivals, list):
                    md.append(f"**Rivals/Enemies**: {', '.join(rivals)}\n\n")
                else:
                    md.append(f"**Rivals/Enemies**: {rivals}\n\n")

            if "hooks" in faction:
                md.append("**Plot Hooks**:\n")
                hooks = faction["hooks"]
                if isinstance(hooks, list):
                    for hook in hooks:
                        md.append(f"- {hook}\n")
                else:
                    md.append(f"- {hooks}\n")
                md.append("\n")

            md.append("---\n\n")

        return "".join(md)

    def _format_npcs(self, npcs: List[Dict]) -> str:
        """Format NPCs section."""
        md = ["## NPCs\n\n"]

        for npc in npcs:
            name = npc.get("name", "Unknown NPC")
            md.append(f"### {name}\n\n")

            # Basic info
            info_parts = []
            if "race" in npc:
                info_parts.append(npc["race"])
            if "role" in npc or "occupation" in npc:
                info_parts.append(npc.get("role", npc.get("occupation", "")))

            if info_parts:
                md.append(f"*{' '.join(info_parts)}*\n\n")

            if "faction" in npc or "affiliation" in npc:
                faction = npc.get("faction", npc.get("affiliation", ""))
                md.append(f"**Faction**: {faction}\n\n")

            # Wants/Fears/Offers framework
            if "wants" in npc:
                md.append(f"**Wants**: {npc['wants']}\n\n")

            if "fears" in npc:
                md.append(f"**Fears**: {npc['fears']}\n\n")

            if "offers" in npc:
                md.append(f"**Offers**: {npc['offers']}\n\n")

            if "secrets" in npc:
                md.append(f"**Secrets**: {npc['secrets']}\n\n")

            # Personality
            if "personality" in npc or "trait" in npc:
                trait = npc.get("personality", npc.get("trait", ""))
                md.append(f"**Personality**: {trait}\n\n")

            if "quirk" in npc:
                md.append(f"**Quirk**: {npc['quirk']}\n\n")

            # Stats
            if "stat_block" in npc or "cr" in npc or "level" in npc:
                stats = npc.get("stat_block", npc.get("cr", npc.get("level", "")))
                md.append(f"**Stats**: {stats}\n\n")

            md.append("---\n\n")

        return "".join(md)

    def _format_locations(self, locations: List[Dict]) -> str:
        """Format locations section."""
        md = ["## Locations\n\n"]

        for location in locations:
            name = location.get("name", "Unknown Location")
            md.append(f"### {name}\n\n")

            if "type" in location:
                md.append(f"*{location['type']}*\n\n")

            if "description" in location:
                md.append(f"{location['description']}\n\n")

            if "features" in location or "key_features" in location:
                features = location.get("features", location.get("key_features", []))
                md.append("**Key Features**:\n")
                if isinstance(features, list):
                    for feature in features:
                        md.append(f"- {feature}\n")
                else:
                    md.append(f"- {features}\n")
                md.append("\n")

            if "factions" in location or "factions_present" in location:
                factions = location.get("factions", location.get("factions_present", []))
                if isinstance(factions, list):
                    md.append(f"**Factions Present**: {', '.join(factions)}\n\n")
                else:
                    md.append(f"**Factions Present**: {factions}\n\n")

            if "npcs" in location or "important_npcs" in location:
                npcs = location.get("npcs", location.get("important_npcs", []))
                if isinstance(npcs, list):
                    md.append(f"**Important NPCs**: {', '.join(npcs)}\n\n")
                else:
                    md.append(f"**Important NPCs**: {npcs}\n\n")

            if "secrets" in location:
                md.append(f"**Secrets**: {location['secrets']}\n\n")

            if "hooks" in location or "adventure_hooks" in location:
                hooks = location.get("hooks", location.get("adventure_hooks", []))
                md.append("**Adventure Hooks**:\n")
                if isinstance(hooks, list):
                    for hook in hooks:
                        md.append(f"- {hook}\n")
                else:
                    md.append(f"- {hooks}\n")
                md.append("\n")

            md.append("---\n\n")

        return "".join(md)

    def _format_hooks(self, hooks: Dict[str, Any]) -> str:
        """Format adventure hooks section."""
        md = ["## Adventure Hooks by Tier\n\n"]

        for tier in ["tier_1", "tier_2", "tier_3", "tier_4"]:
            if tier in hooks:
                tier_name = {
                    "tier_1": "Tier 1 (Levels 1-5)",
                    "tier_2": "Tier 2 (Levels 6-10)",
                    "tier_3": "Tier 3 (Levels 11-16)",
                    "tier_4": "Tier 4 (Levels 17-20)",
                }[tier]

                md.append(f"### {tier_name}\n\n")

                tier_hooks = hooks[tier]
                if isinstance(tier_hooks, list):
                    for hook in tier_hooks:
                        if isinstance(hook, dict):
                            hook_type = hook.get("type", "General")
                            hook_text = hook.get("hook", "")
                            md.append(f"**[{hook_type.title()}]** {hook_text}\n\n")
                        else:
                            md.append(f"- {hook}\n\n")
                else:
                    md.append(f"{tier_hooks}\n\n")

        md.append("---\n\n")
        return "".join(md)

    def _format_connections(self, connections: Dict[str, Any]) -> str:
        """Format connections and relationships section."""
        md = ["## Connections & Relationships\n\n"]

        if "key_nodes" in connections:
            md.append("### Central Figures\n\n")
            md.append("Elements with the most connections:\n\n")
            for node in connections["key_nodes"]:
                if isinstance(node, dict):
                    md.append(f"- **{node.get('name', 'Unknown')}**: {node.get('connections', 0)} connections\n")
                else:
                    md.append(f"- {node}\n")
            md.append("\n")

        if "orphaned_elements" in connections:
            orphans = connections["orphaned_elements"]
            if orphans:
                md.append("### Isolated Elements\n\n")
                md.append("⚠️ These elements need more connections:\n\n")
                for orphan in orphans:
                    md.append(f"- {orphan}\n")
                md.append("\n")

        if "relationships" in connections:
            md.append("### Key Relationships\n\n")
            relationships = connections["relationships"]
            if isinstance(relationships, list):
                for rel in relationships:
                    if isinstance(rel, dict):
                        source = rel.get("source", "Unknown")
                        target = rel.get("target", "Unknown")
                        rel_type = rel.get("type", "connected to")
                        md.append(f"- **{source}** {rel_type} **{target}**\n")
                    else:
                        md.append(f"- {rel}\n")
            md.append("\n")

        md.append("---\n\n")
        return "".join(md)

    def save_to_file(self, content: str, output_dir: Path):
        """
        Save markdown content to file.

        Args:
            content: Markdown content
            output_dir: Output directory path
        """
        output_dir.mkdir(parents=True, exist_ok=True)
        filename = f"{self.campaign_name.lower().replace(' ', '_')}_campaign_bible.md"
        filepath = output_dir / filename

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"✅ Campaign bible saved to: {filepath}")
        return filepath
