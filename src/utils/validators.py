"""Validation utilities for campaign configurations."""

from typing import Any, Dict, List, Tuple


def validate_campaign_config(config: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """
    Validate campaign configuration.

    Args:
        config: Campaign configuration dictionary

    Returns:
        Tuple of (is_valid, list_of_errors)
    """
    errors = []

    # Check required top-level keys
    if "campaign" not in config:
        errors.append("Missing required 'campaign' section")
    else:
        campaign = config["campaign"]

        # Check required campaign fields
        if "name" not in campaign:
            errors.append("Missing required field: campaign.name")
        if "pitch" not in campaign:
            errors.append("Missing required field: campaign.pitch")

    # Validate preferences if present
    if "preferences" in config:
        prefs = config["preferences"]

        if "include_factions" in prefs:
            if not isinstance(prefs["include_factions"], int) or prefs["include_factions"] < 1:
                errors.append("include_factions must be a positive integer")

        if "include_npcs" in prefs:
            if not isinstance(prefs["include_npcs"], int) or prefs["include_npcs"] < 1:
                errors.append("include_npcs must be a positive integer")

        if "include_locations" in prefs:
            if not isinstance(prefs["include_locations"], int) or prefs["include_locations"] < 1:
                errors.append("include_locations must be a positive integer")

        if "detail_level" in prefs:
            valid_levels = ["basic", "moderate", "comprehensive"]
            if prefs["detail_level"] not in valid_levels:
                errors.append(
                    f"detail_level must be one of: {', '.join(valid_levels)}"
                )

    # Validate players if present
    if "players" in config:
        players = config["players"]

        if "count" in players:
            if not isinstance(players["count"], int) or players["count"] < 1:
                errors.append("players.count must be a positive integer")

        if "starting_level" in players:
            level = players["starting_level"]
            if not isinstance(level, int) or level < 1 or level > 20:
                errors.append("players.starting_level must be between 1 and 20")

        if "experience_level" in players:
            valid_exp = ["beginner", "intermediate", "advanced", "mixed"]
            if players["experience_level"] not in valid_exp:
                errors.append(
                    f"players.experience_level must be one of: {', '.join(valid_exp)}"
                )

    is_valid = len(errors) == 0
    return is_valid, errors
