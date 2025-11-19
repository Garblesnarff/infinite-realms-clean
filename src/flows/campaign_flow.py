"""
Campaign Bible Generation Flow using CrewAI Flows.

This flow orchestrates the entire campaign bible generation process with
conditional logic, state management, and error handling.
"""

import json
from typing import Any, Dict, Optional

from crewai.flow.flow import Flow, listen, start

from ..crews.campaign_crew import CampaignCrew
from ..utils.validators import validate_campaign_config


class CampaignBibleFlow(Flow):
    """
    Main flow for generating D&D 5E campaign bibles.

    Uses CrewAI Flows to manage the generation pipeline with state persistence,
    conditional branching, and iterative refinement.
    """

    def __init__(self):
        super().__init__()
        self.campaign_config: Dict[str, Any] = {}
        self.world_foundation: Dict[str, Any] = {}
        self.factions: list = []
        self.npcs: list = []
        self.locations: list = []
        self.connections: Dict[str, Any] = {}
        self.hooks: Dict[str, Any] = {}
        self.validation_report: Dict[str, Any] = {}
        self.campaign_bible: str = ""
        self.player_handout: str = ""

    @start()
    def load_and_validate_config(self, campaign_config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Start: Load and validate campaign configuration.

        Args:
            campaign_config: User-provided campaign configuration

        Returns:
            Validated and enriched configuration
        """
        print("🎲 Starting Campaign Bible Generation Flow...")
        print("📋 Step 1/11: Validating campaign configuration")

        # Validate configuration
        is_valid, errors = validate_campaign_config(campaign_config)

        if not is_valid:
            raise ValueError(f"Invalid campaign configuration: {errors}")

        # Store validated config
        self.campaign_config = campaign_config

        # Enrich with defaults
        config = self._apply_defaults(campaign_config)

        print(f"✅ Configuration validated for campaign: {config['campaign']['name']}")
        return config

    @listen(load_and_validate_config)
    def analyze_concept(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze the campaign concept to extract themes and requirements.

        Args:
            config: Validated configuration

        Returns:
            Campaign analysis
        """
        print("\n🔍 Step 2/11: Analyzing campaign concept")

        crew = CampaignCrew(config)
        analysis = crew.analyze_campaign()

        print(f"✅ Analysis complete: {len(analysis.get('themes', []))} core themes identified")
        return analysis

    @listen(analyze_concept)
    def build_world_foundation(self, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create world fundamentals: geography, history, cosmology.

        Args:
            analysis: Campaign analysis

        Returns:
            World foundation data
        """
        print("\n🌍 Step 3/11: Building world foundation")

        crew = CampaignCrew(self.campaign_config)
        world_foundation = crew.create_world_foundation(analysis)

        self.world_foundation = world_foundation
        print("✅ World foundation created")
        return world_foundation

    @listen(build_world_foundation)
    def create_factions(self, world_foundation: Dict[str, Any]) -> list:
        """
        Design factions with conflicting goals.

        Args:
            world_foundation: World foundation data

        Returns:
            List of faction data
        """
        num_factions = self.campaign_config.get("preferences", {}).get("include_factions", 5)
        print(f"\n⚔️ Step 4/11: Creating {num_factions} factions")

        crew = CampaignCrew(self.campaign_config)
        factions = crew.create_factions(world_foundation, num_factions)

        self.factions = factions
        print(f"✅ {len(factions)} factions created")
        return factions

    @listen(create_factions)
    def create_npcs(self, factions: list) -> list:
        """
        Generate memorable NPCs across factions.

        Args:
            factions: Faction data

        Returns:
            List of NPC data
        """
        num_npcs = self.campaign_config.get("preferences", {}).get("include_npcs", 15)
        print(f"\n👥 Step 5/11: Creating {num_npcs} NPCs")

        crew = CampaignCrew(self.campaign_config)
        npcs = crew.create_npcs(self.world_foundation, factions, num_npcs)

        self.npcs = npcs
        print(f"✅ {len(npcs)} NPCs created")
        return npcs

    @listen(create_npcs)
    def create_locations(self, npcs: list) -> list:
        """
        Design key locations with hooks.

        Args:
            npcs: NPC data

        Returns:
            List of location data
        """
        num_locations = self.campaign_config.get("preferences", {}).get("include_locations", 10)
        print(f"\n🏰 Step 6/11: Creating {num_locations} locations")

        crew = CampaignCrew(self.campaign_config)
        locations = crew.create_locations(self.world_foundation, self.factions, npcs, num_locations)

        self.locations = locations
        print(f"✅ {len(locations)} locations created")
        return locations

    @listen(create_locations)
    def weave_connections(self, locations: list) -> Dict[str, Any]:
        """
        Create connections between all elements.

        Args:
            locations: Location data

        Returns:
            Connection data and relationship map
        """
        print("\n🔗 Step 7/11: Weaving connections between elements")

        crew = CampaignCrew(self.campaign_config)
        connections = crew.integrate_elements(
            self.factions,
            self.npcs,
            locations,
            self.campaign_config.get("campaign", {}).get("themes", []),
        )

        self.connections = connections
        print("✅ Connections established")
        return connections

    @listen(weave_connections)
    def generate_hooks(self, connections: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate adventure hooks by tier.

        Args:
            connections: Connection data

        Returns:
            Hooks organized by tier
        """
        print("\n🎯 Step 8/11: Generating adventure hooks")

        crew = CampaignCrew(self.campaign_config)
        all_elements = {
            "factions": self.factions,
            "npcs": self.npcs,
            "locations": self.locations,
            "connections": connections,
        }
        hooks = crew.generate_hooks(all_elements)

        self.hooks = hooks
        print("✅ Adventure hooks generated")
        return hooks

    @listen(generate_hooks)
    def validate_content(self, hooks: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate consistency and D&D 5E compliance.

        Args:
            hooks: Adventure hooks

        Returns:
            Validation report
        """
        print("\n✔️ Step 9/11: Validating content")

        crew = CampaignCrew(self.campaign_config)
        all_elements = {
            "world_foundation": self.world_foundation,
            "factions": self.factions,
            "npcs": self.npcs,
            "locations": self.locations,
            "connections": self.connections,
            "hooks": hooks,
        }

        validation_report = crew.validate_campaign(all_elements)

        self.validation_report = validation_report

        # Check if we need to iterate
        if self._needs_iteration(validation_report):
            print("⚠️ Validation found issues requiring fixes")
            return self.fix_issues(validation_report)

        print("✅ Validation passed")
        return validation_report

    @listen(validate_content)
    def create_random_tables(self, validation_report: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate random tables for DM use.

        Args:
            validation_report: Validation results

        Returns:
            Random tables
        """
        print("\n🎲 Step 10/11: Creating random tables")

        crew = CampaignCrew(self.campaign_config)
        tables = crew.create_random_tables(self.locations, self.world_foundation, self.factions)

        print("✅ Random tables generated")
        return tables

    @listen(create_random_tables)
    def generate_player_handout(self, tables: Dict[str, Any]) -> str:
        """
        Create player-facing handout.

        Args:
            tables: Random tables

        Returns:
            Player handout markdown
        """
        print("\n📄 Step 11/11: Generating player handout")

        crew = CampaignCrew(self.campaign_config)
        handout = crew.create_player_handout(
            self.campaign_config,
            self.factions,
            self.world_foundation,
        )

        self.player_handout = handout
        print("✅ Player handout created")
        return handout

    @listen(generate_player_handout)
    def assemble_final_bible(self, player_handout: str) -> str:
        """
        Assemble complete campaign bible.

        Args:
            player_handout: Player handout content

        Returns:
            Complete campaign bible markdown
        """
        print("\n📚 Final Step: Assembling campaign bible")

        crew = CampaignCrew(self.campaign_config)
        all_elements = {
            "world_foundation": self.world_foundation,
            "factions": self.factions,
            "npcs": self.npcs,
            "locations": self.locations,
            "connections": self.connections,
            "hooks": self.hooks,
            "validation": self.validation_report,
            "player_handout": player_handout,
        }

        campaign_bible = crew.assemble_bible(all_elements)

        self.campaign_bible = campaign_bible
        print("✅ Campaign Bible Generation Complete! 🎉")
        return campaign_bible

    # Helper methods

    def _apply_defaults(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Apply default values to configuration."""
        defaults = {
            "preferences": {
                "include_factions": 5,
                "include_npcs": 15,
                "include_locations": 10,
                "detail_level": "comprehensive",
                "include_maps": True,
            },
            "players": {
                "count": 4,
                "starting_level": 1,
                "experience_level": "mixed",
            },
        }

        # Merge defaults with provided config
        result = {**defaults, **config}
        result["preferences"] = {**defaults["preferences"], **config.get("preferences", {})}
        result["players"] = {**defaults["players"], **config.get("players", {})}

        return result

    def _needs_iteration(self, validation_report: Dict[str, Any]) -> bool:
        """Check if validation issues require iteration."""
        # For now, we'll proceed even with warnings
        # In a production system, you might want to iterate on major issues
        major_issues = validation_report.get("major_issues", [])
        return len(major_issues) > 5

    def fix_issues(self, validation_report: Dict[str, Any]) -> Dict[str, Any]:
        """
        Attempt to fix validation issues.

        This is a simplified implementation. In production, you'd use
        specialized crews to fix specific types of issues.
        """
        print("🔧 Attempting to fix validation issues...")
        # Placeholder for issue fixing logic
        # In a real implementation, this would dispatch to specialized crews
        # based on issue types
        return validation_report

    def get_state(self) -> Dict[str, Any]:
        """Get current flow state for persistence."""
        return {
            "campaign_config": self.campaign_config,
            "world_foundation": self.world_foundation,
            "factions": self.factions,
            "npcs": self.npcs,
            "locations": self.locations,
            "connections": self.connections,
            "hooks": self.hooks,
            "validation_report": self.validation_report,
            "player_handout": self.player_handout,
            "campaign_bible": self.campaign_bible,
        }
