"""Hook Generator Tool for creating plot hooks from campaign elements."""

import json
import random
from typing import Any, Dict, List, Type

from crewai_tools import BaseTool
from pydantic import BaseModel, Field


class HookGeneratorInput(BaseModel):
    """Input schema for HookGenerator."""

    element: str = Field(..., description="Campaign element to generate hooks for (JSON)")
    element_type: str = Field(
        ...,
        description="Type of element: 'npc', 'faction', 'location', or 'event'",
    )
    num_hooks: int = Field(default=3, description="Number of hooks to generate")
    hook_types: str = Field(
        default="all",
        description="Types of hooks: 'combat', 'social', 'exploration', 'mystery', or 'all'",
    )


class HookGeneratorTool(BaseTool):
    """
    Tool for generating adventure hooks from campaign elements.

    Creates engaging plot hooks categorized by type (combat, social, exploration, mystery)
    that DMs can use to drive adventures.
    """

    name: str = "Hook Generator"
    description: str = (
        "Generates adventure hooks from campaign elements. Creates plot threads "
        "categorized as combat, social, exploration, or mystery hooks. "
        "Input should be a JSON element with its type and desired number of hooks."
    )
    args_schema: Type[BaseModel] = HookGeneratorInput

    HOOK_TEMPLATES = {
        "npc": {
            "combat": [
                "{name} has been kidnapped by {antagonist}. The party must rescue them.",
                "{name} is being hunted by assassins and needs protection.",
                "{name} challenges the party to a duel/contest to prove their worth.",
                "{name}'s enemies attack while they're meeting with the party.",
            ],
            "social": [
                "{name} needs the party to negotiate a deal with {faction}.",
                "{name} invites the party to an important social event where intrigue unfolds.",
                "{name} asks the party to clear their name in a scandal.",
                "{name} needs help convincing someone to {action}.",
            ],
            "exploration": [
                "{name} has a map to {location} and needs escorts/explorers.",
                "{name} sends the party to investigate strange occurrences at {location}.",
                "{name} lost something precious in {location} and needs it retrieved.",
                "{name} needs rare materials from {location}.",
            ],
            "mystery": [
                "{name} is acting strangely, and someone needs to find out why.",
                "{name} has disappeared, leaving only cryptic clues.",
                "{name} knows a secret about {subject} but won't reveal it directly.",
                "{name} is being blackmailed, but doesn't know by whom.",
            ],
        },
        "faction": {
            "combat": [
                "{name} is at war with {rival} and needs mercenaries.",
                "{name} is planning a raid on {target} and needs help.",
                "{name}'s headquarters is under attack.",
                "{name} needs the party to eliminate a threat to their operations.",
            ],
            "social": [
                "{name} needs representatives for negotiations with {rival}.",
                "{name} is hosting a gathering where the party can make connections.",
                "{name} wants to recruit the party as official members.",
                "{name} needs help managing an internal power struggle.",
            ],
            "exploration": [
                "{name} is searching for {artifact} in {location}.",
                "{name} wants to expand into new territory and needs scouts.",
                "{name} lost contact with an outpost and needs investigators.",
                "{name} is funding an expedition to {location}.",
            ],
            "mystery": [
                "{name} has a traitor in their ranks who must be identified.",
                "{name}'s leader has been replaced by a doppelganger or impostor.",
                "{name} is receiving threatening messages from an unknown source.",
                "{name}'s operations are being sabotaged systematically.",
            ],
        },
        "location": {
            "combat": [
                "{name} is overrun by {monsters} that need to be cleared out.",
                "A powerful creature has claimed {name} as its lair.",
                "Two factions are fighting over control of {name}.",
                "{name} is being used as a base by {antagonists}.",
            ],
            "social": [
                "{name} is hosting an important festival/event.",
                "The rulers of {name} need mediators for a dispute.",
                "{name} has closed its borders and won't say why.",
                "A merchant consortium wants exclusive trade rights to {name}.",
            ],
            "exploration": [
                "{name} contains unexplored ruins/dungeons beneath it.",
                "Strange phenomena have been observed near {name}.",
                "{name} appeared overnight/was recently discovered.",
                "The old maps of {name} don't match current geography.",
            ],
            "mystery": [
                "People who enter {name} are disappearing without a trace.",
                "{name} is experiencing impossible weather/phenomena.",
                "The inhabitants of {name} are all acting strangely.",
                "A legend says {name} contains {artifact}, but no one knows where.",
            ],
        },
        "event": {
            "combat": [
                "{name} triggers an armed conflict between factions.",
                "{name} releases/awakens something dangerous.",
                "{name} is the perfect opportunity for an ambush/attack.",
                "{name} must be defended against those who would disrupt it.",
            ],
            "social": [
                "{name} brings together important NPCs the party should meet.",
                "{name} provides an opportunity for the party to increase their reputation.",
                "{name} is being used as cover for secret dealings.",
                "{name} requires delicate diplomacy to navigate successfully.",
            ],
            "exploration": [
                "{name} reveals the existence of {location}.",
                "{name} only happens at specific times/places that must be found.",
                "{name} leaves behind clues to something greater.",
                "{name} creates a temporary passage to {location}.",
            ],
            "mystery": [
                "{name} shouldn't be happening according to all known lore.",
                "Someone is trying to prevent {name} from occurring.",
                "{name} is a cover for something else happening simultaneously.",
                "The true purpose of {name} is not what it appears to be.",
            ],
        },
    }

    def _run(
        self,
        element: str,
        element_type: str,
        num_hooks: int = 3,
        hook_types: str = "all",
    ) -> str:
        """
        Generate adventure hooks for a campaign element.

        Args:
            element: JSON string of the element
            element_type: Type of element
            num_hooks: Number of hooks to generate
            hook_types: Types of hooks to include

        Returns:
            JSON array of generated hooks
        """
        try:
            element_data = json.loads(element)
            element_name = element_data.get("name", "Unknown")

            # Determine which hook types to generate
            if hook_types == "all":
                types = ["combat", "social", "exploration", "mystery"]
            else:
                types = [t.strip() for t in hook_types.split(",")]

            hooks = []
            templates = self.HOOK_TEMPLATES.get(element_type, {})

            for hook_type in types:
                if hook_type in templates:
                    # Generate hooks for this type
                    type_templates = templates[hook_type]
                    num_per_type = max(1, num_hooks // len(types))

                    for _ in range(num_per_type):
                        template = random.choice(type_templates)
                        hook = self._fill_template(template, element_data, element_type)
                        hooks.append(
                            {
                                "type": hook_type,
                                "hook": hook,
                                "element": element_name,
                                "element_type": element_type,
                            }
                        )

            # Ensure we have exactly num_hooks
            if len(hooks) > num_hooks:
                hooks = random.sample(hooks, num_hooks)
            elif len(hooks) < num_hooks:
                # Generate additional hooks from any category
                while len(hooks) < num_hooks:
                    hook_type = random.choice(types)
                    if hook_type in templates:
                        template = random.choice(templates[hook_type])
                        hook = self._fill_template(template, element_data, element_type)
                        hooks.append(
                            {
                                "type": hook_type,
                                "hook": hook,
                                "element": element_name,
                                "element_type": element_type,
                            }
                        )

            return json.dumps(hooks, indent=2)

        except json.JSONDecodeError as e:
            return f"Error parsing element JSON: {str(e)}"
        except Exception as e:
            return f"Error generating hooks: {str(e)}"

    def _fill_template(self, template: str, element_data: Dict, element_type: str) -> str:
        """Fill in template placeholders with element data."""
        result = template.replace("{name}", element_data.get("name", "Unknown"))

        # Fill in other placeholders with data from element or generic terms
        placeholders = {
            "antagonist": element_data.get("enemy", "a dangerous enemy"),
            "faction": element_data.get("faction", "a powerful faction"),
            "location": element_data.get("location", "a mysterious location"),
            "rival": element_data.get("rival", "a rival faction"),
            "target": element_data.get("target", "an important target"),
            "artifact": element_data.get("artifact", "a legendary artifact"),
            "monsters": element_data.get("monsters", "dangerous monsters"),
            "antagonists": element_data.get("enemies", "hostile forces"),
            "action": element_data.get("goal", "take action"),
            "subject": element_data.get("secret", "an important matter"),
        }

        for placeholder, value in placeholders.items():
            result = result.replace(f"{{{placeholder}}}", str(value))

        return result
