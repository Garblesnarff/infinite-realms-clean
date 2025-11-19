"""
Main Campaign Crew implementation.

This module orchestrates all agents to generate a complete campaign bible.
"""

import json
import os
from pathlib import Path
from typing import Any, Dict, List

import yaml
from crewai import Agent, Crew, Process, Task
from langchain_openai import ChatOpenAI

from ..tools import (
    ConsistencyCheckerTool,
    DnD5EValidatorTool,
    HookGeneratorTool,
    RandomTableCreatorTool,
    RelationshipMapperTool,
)


class CampaignCrew:
    """
    Main crew for generating D&D 5E campaign bibles.

    Coordinates multiple specialized agents using hierarchical process
    to create comprehensive, consistent campaign content.
    """

    def __init__(self, campaign_config: Dict[str, Any]):
        """
        Initialize the campaign crew.

        Args:
            campaign_config: Campaign configuration dictionary
        """
        self.campaign_config = campaign_config
        self.agents_config = self._load_config("agents.yaml")
        self.tasks_config = self._load_config("tasks.yaml")

        # Initialize LLM
        self.llm = ChatOpenAI(
            model=os.getenv("DEFAULT_LLM", "gpt-4-turbo-preview"),
            temperature=0.7,
        )

        # Initialize tools
        self.tools = {
            "consistency_checker": ConsistencyCheckerTool(),
            "dnd_validator": DnD5EValidatorTool(),
            "relationship_mapper": RelationshipMapperTool(),
            "hook_generator": HookGeneratorTool(),
            "random_table_creator": RandomTableCreatorTool(),
        }

        # Initialize agents
        self.agents = self._create_agents()

    def _load_config(self, filename: str) -> Dict:
        """Load YAML configuration file."""
        config_path = Path(__file__).parent.parent / "config" / filename
        with open(config_path, "r") as f:
            return yaml.safe_load(f)

    def _create_agents(self) -> Dict[str, Agent]:
        """Create all specialized agents from YAML config."""
        agents = {}

        for agent_name, config in self.agents_config.items():
            agents[agent_name] = Agent(
                role=config["role"],
                goal=config["goal"],
                backstory=config["backstory"],
                verbose=config.get("verbose", True),
                allow_delegation=config.get("allow_delegation", False),
                llm=self.llm,
            )

        return agents

    def _create_task(
        self,
        task_name: str,
        agent: Agent,
        context_vars: Dict[str, Any],
        tools: List = None,
    ) -> Task:
        """Create a task from YAML config with variable substitution."""
        task_config = self.tasks_config[task_name]

        # Substitute variables in description and expected_output
        description = task_config["description"].format(**context_vars)
        expected_output = task_config["expected_output"].format(**context_vars)

        return Task(
            description=description,
            expected_output=expected_output,
            agent=agent,
            tools=tools or [],
        )

    # Campaign generation methods

    def analyze_campaign(self) -> Dict[str, Any]:
        """Analyze campaign concept and extract key themes."""
        task = self._create_task(
            "analyze_campaign_concept",
            self.agents["master_worldbuilder"],
            {"campaign_input": json.dumps(self.campaign_config)},
        )

        crew = Crew(
            agents=[self.agents["master_worldbuilder"]],
            tasks=[task],
            process=Process.sequential,
            verbose=True,
        )

        result = crew.kickoff()
        try:
            return json.loads(str(result))
        except json.JSONDecodeError:
            # Fallback to structured dict
            return {
                "themes": self.campaign_config.get("campaign", {}).get("themes", []),
                "tone": self.campaign_config.get("campaign", {}).get("tone", ""),
                "unique_elements": [],
            }

    def create_world_foundation(self, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Create world foundation: geography, history, cosmology."""
        task = self._create_task(
            "create_world_foundation",
            self.agents["master_worldbuilder"],
            {
                "campaign_analysis": json.dumps(analysis),
                "player_info": json.dumps(self.campaign_config.get("players", {})),
            },
            tools=[self.tools["consistency_checker"]],
        )

        crew = Crew(
            agents=[self.agents["master_worldbuilder"]],
            tasks=[task],
            process=Process.sequential,
            verbose=True,
        )

        result = crew.kickoff()
        try:
            return json.loads(str(result))
        except json.JSONDecodeError:
            return {"geography": {}, "history": [], "cosmology": {}, "magic_system": {}}

    def create_factions(self, world_foundation: Dict[str, Any], num_factions: int) -> List[Dict]:
        """Design factions with conflicting goals."""
        task = self._create_task(
            "design_factions",
            self.agents["character_dramatist"],
            {
                "num_factions": num_factions,
                "world_foundation": json.dumps(world_foundation),
                "campaign_themes": json.dumps(
                    self.campaign_config.get("campaign", {}).get("themes", [])
                ),
            },
            tools=[self.tools["consistency_checker"]],
        )

        crew = Crew(
            agents=[self.agents["character_dramatist"]],
            tasks=[task],
            process=Process.sequential,
            verbose=True,
        )

        result = crew.kickoff()
        try:
            parsed = json.loads(str(result))
            return parsed if isinstance(parsed, list) else []
        except json.JSONDecodeError:
            return []

    def create_npcs(
        self,
        world_foundation: Dict[str, Any],
        factions: List[Dict],
        num_npcs: int,
    ) -> List[Dict]:
        """Create memorable NPCs across factions."""
        task = self._create_task(
            "create_npcs",
            self.agents["character_dramatist"],
            {
                "num_npcs": num_npcs,
                "factions": json.dumps(factions),
                "world_foundation": json.dumps(world_foundation),
            },
            tools=[self.tools["consistency_checker"]],
        )

        crew = Crew(
            agents=[self.agents["character_dramatist"]],
            tasks=[task],
            process=Process.sequential,
            verbose=True,
        )

        result = crew.kickoff()
        try:
            parsed = json.loads(str(result))
            return parsed if isinstance(parsed, list) else []
        except json.JSONDecodeError:
            return []

    def create_locations(
        self,
        world_foundation: Dict[str, Any],
        factions: List[Dict],
        npcs: List[Dict],
        num_locations: int,
    ) -> List[Dict]:
        """Design key locations with hooks."""
        task = self._create_task(
            "create_locations",
            self.agents["master_worldbuilder"],
            {
                "num_locations": num_locations,
                "world_foundation": json.dumps(world_foundation),
                "factions": json.dumps(factions),
                "npcs": json.dumps(npcs),
            },
            tools=[self.tools["consistency_checker"], self.tools["hook_generator"]],
        )

        crew = Crew(
            agents=[self.agents["master_worldbuilder"]],
            tasks=[task],
            process=Process.sequential,
            verbose=True,
        )

        result = crew.kickoff()
        try:
            parsed = json.loads(str(result))
            return parsed if isinstance(parsed, list) else []
        except json.JSONDecodeError:
            return []

    def integrate_elements(
        self,
        factions: List[Dict],
        npcs: List[Dict],
        locations: List[Dict],
        themes: List[str],
    ) -> Dict[str, Any]:
        """Weave connections between all elements."""
        task = self._create_task(
            "weave_connections",
            self.agents["integration_specialist"],
            {
                "factions": json.dumps(factions),
                "npcs": json.dumps(npcs),
                "locations": json.dumps(locations),
                "campaign_themes": json.dumps(themes),
            },
            tools=[self.tools["relationship_mapper"], self.tools["consistency_checker"]],
        )

        crew = Crew(
            agents=[self.agents["integration_specialist"]],
            tasks=[task],
            process=Process.sequential,
            verbose=True,
        )

        result = crew.kickoff()
        try:
            return json.loads(str(result))
        except json.JSONDecodeError:
            return {"relationships": [], "key_nodes": [], "orphaned_elements": []}

    def generate_hooks(self, all_elements: Dict[str, Any]) -> Dict[str, Any]:
        """Generate adventure hooks by tier."""
        player_level = self.campaign_config.get("players", {}).get("starting_level", 1)

        task = self._create_task(
            "generate_adventure_hooks",
            self.agents["adventure_architect"],
            {
                "all_elements": json.dumps(all_elements),
                "player_levels": f"1-20",
                "hooks_per_tier": 5,
            },
            tools=[self.tools["hook_generator"], self.tools["dnd_validator"]],
        )

        crew = Crew(
            agents=[self.agents["adventure_architect"]],
            tasks=[task],
            process=Process.sequential,
            verbose=True,
        )

        result = crew.kickoff()
        try:
            return json.loads(str(result))
        except json.JSONDecodeError:
            return {"tier_1": [], "tier_2": [], "tier_3": [], "tier_4": []}

    def validate_campaign(self, all_elements: Dict[str, Any]) -> Dict[str, Any]:
        """Validate consistency and D&D 5E compliance."""
        # Consistency validation
        consistency_task = self._create_task(
            "validate_consistency",
            self.agents["lorekeeper"],
            {"all_elements": json.dumps(all_elements)},
            tools=[self.tools["consistency_checker"]],
        )

        # D&D rules validation
        dnd_task = self._create_task(
            "validate_dnd_compliance",
            self.agents["lorekeeper"],
            {"all_elements": json.dumps(all_elements)},
            tools=[self.tools["dnd_validator"]],
        )

        crew = Crew(
            agents=[self.agents["lorekeeper"]],
            tasks=[consistency_task, dnd_task],
            process=Process.sequential,
            verbose=True,
        )

        result = crew.kickoff()
        try:
            return json.loads(str(result))
        except json.JSONDecodeError:
            return {"consistency_issues": [], "dnd_issues": [], "recommendations": []}

    def create_random_tables(
        self,
        locations: List[Dict],
        world_foundation: Dict[str, Any],
        factions: List[Dict],
    ) -> Dict[str, Any]:
        """Create random tables for DM use."""
        task = self._create_task(
            "create_random_tables",
            self.agents["adventure_architect"],
            {
                "locations": json.dumps(locations),
                "world_foundation": json.dumps(world_foundation),
                "factions": json.dumps(factions),
            },
            tools=[self.tools["random_table_creator"]],
        )

        crew = Crew(
            agents=[self.agents["adventure_architect"]],
            tasks=[task],
            process=Process.sequential,
            verbose=True,
        )

        result = crew.kickoff()
        try:
            return json.loads(str(result))
        except json.JSONDecodeError:
            return {"encounter_tables": [], "weather_tables": [], "rumor_tables": []}

    def create_player_handout(
        self,
        campaign_config: Dict[str, Any],
        factions: List[Dict],
        world_foundation: Dict[str, Any],
    ) -> str:
        """Create player-facing handout."""
        task = self._create_task(
            "create_player_handout",
            self.agents["player_facing_writer"],
            {
                "campaign_concept": json.dumps(campaign_config.get("campaign", {})),
                "factions": json.dumps(factions),
                "world_foundation": json.dumps(world_foundation),
                "campaign_themes": json.dumps(
                    campaign_config.get("campaign", {}).get("themes", [])
                ),
            },
        )

        crew = Crew(
            agents=[self.agents["player_facing_writer"]],
            tasks=[task],
            process=Process.sequential,
            verbose=True,
        )

        result = crew.kickoff()
        return str(result)

    def assemble_bible(self, all_elements: Dict[str, Any]) -> str:
        """Assemble complete campaign bible."""
        task = self._create_task(
            "assemble_campaign_bible",
            self.agents["integration_specialist"],
            {
                "all_elements": json.dumps(all_elements),
                "player_handout": all_elements.get("player_handout", ""),
            },
        )

        crew = Crew(
            agents=[self.agents["integration_specialist"]],
            tasks=[task],
            process=Process.sequential,
            verbose=True,
        )

        result = crew.kickoff()
        return str(result)
