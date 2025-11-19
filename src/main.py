#!/usr/bin/env python3
"""
Infinite Realms - AI-Powered D&D 5E Campaign Bible Generator

Main entry point for the application.
"""

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Dict, Any

import yaml
from dotenv import load_dotenv

from flows.campaign_flow import CampaignBibleFlow
from formatters import MarkdownFormatter, JSONFormatter, ObsidianFormatter
from utils.validators import validate_campaign_config


def load_campaign_config(config_path: str) -> Dict[str, Any]:
    """
    Load campaign configuration from YAML file.

    Args:
        config_path: Path to configuration file

    Returns:
        Configuration dictionary
    """
    with open(config_path, "r") as f:
        if config_path.endswith(".yaml") or config_path.endswith(".yml"):
            return yaml.safe_load(f)
        elif config_path.endswith(".json"):
            return json.load(f)
        else:
            raise ValueError("Configuration must be YAML or JSON format")


def interactive_mode() -> Dict[str, Any]:
    """
    Run interactive configuration mode.

    Returns:
        Configuration dictionary
    """
    print("🎲 Welcome to Infinite Realms Campaign Bible Generator!\n")
    print("Let's create your campaign configuration...\n")

    config = {"campaign": {}, "players": {}, "preferences": {}}

    # Campaign basics
    config["campaign"]["name"] = input("Campaign name: ").strip()
    config["campaign"]["pitch"] = input("Campaign pitch (1-2 sentences): ").strip()

    # Themes
    print("\nEnter campaign themes (comma-separated):")
    themes = input("Themes: ").strip()
    config["campaign"]["themes"] = [t.strip() for t in themes.split(",")]

    config["campaign"]["tone"] = input("Campaign tone (e.g., 'dark fantasy', 'heroic epic'): ").strip()
    config["campaign"]["setting_type"] = input("Setting type (e.g., 'high magic', 'low magic'): ").strip()

    # Players
    config["players"]["count"] = int(input("\nNumber of players: ").strip() or "4")
    config["players"]["starting_level"] = int(input("Starting character level (1-20): ").strip() or "1")
    config["players"]["experience_level"] = input("Player experience (beginner/intermediate/advanced/mixed): ").strip() or "mixed"

    # Preferences
    config["preferences"]["include_factions"] = int(input("\nNumber of factions to generate: ").strip() or "5")
    config["preferences"]["include_npcs"] = int(input("Number of NPCs to generate: ").strip() or "15")
    config["preferences"]["include_locations"] = int(input("Number of locations to generate: ").strip() or "10")
    config["preferences"]["detail_level"] = input("Detail level (basic/moderate/comprehensive): ").strip() or "comprehensive"

    return config


def main():
    """Main entry point."""
    # Load environment variables
    load_dotenv()

    # Parse arguments
    parser = argparse.ArgumentParser(
        description="Generate D&D 5E campaign bibles using AI multi-agent systems"
    )
    parser.add_argument(
        "--campaign",
        "-c",
        type=str,
        help="Path to campaign configuration file (YAML or JSON)",
    )
    parser.add_argument(
        "--interactive",
        "-i",
        action="store_true",
        help="Run in interactive configuration mode",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=str,
        default="./output",
        help="Output directory for generated campaign bible",
    )
    parser.add_argument(
        "--format",
        "-f",
        type=str,
        choices=["markdown", "json", "obsidian", "all"],
        default="all",
        help="Output format (default: all)",
    )
    parser.add_argument(
        "--skip-validation",
        action="store_true",
        help="Skip configuration validation (not recommended)",
    )

    args = parser.parse_args()

    # Check for API keys
    if not os.getenv("OPENAI_API_KEY") and not os.getenv("ANTHROPIC_API_KEY"):
        print("❌ Error: No API keys found!")
        print("Please set OPENAI_API_KEY or ANTHROPIC_API_KEY in your .env file")
        sys.exit(1)

    # Get configuration
    if args.interactive:
        campaign_config = interactive_mode()
    elif args.campaign:
        try:
            campaign_config = load_campaign_config(args.campaign)
        except Exception as e:
            print(f"❌ Error loading configuration: {e}")
            sys.exit(1)
    else:
        print("❌ Error: Either --campaign or --interactive must be specified")
        parser.print_help()
        sys.exit(1)

    # Validate configuration
    if not args.skip_validation:
        is_valid, errors = validate_campaign_config(campaign_config)
        if not is_valid:
            print("❌ Configuration validation failed:")
            for error in errors:
                print(f"  - {error}")
            sys.exit(1)

    print(f"\n🎲 Generating campaign bible for: {campaign_config['campaign']['name']}")
    print(f"📂 Output directory: {args.output}\n")

    try:
        # Create and run flow
        flow = CampaignBibleFlow()
        result = flow.kickoff(campaign_config=campaign_config)

        # Get final campaign bible
        campaign_bible = flow.campaign_bible
        campaign_name = campaign_config["campaign"]["name"]

        # Get all elements for formatters
        elements = flow.get_state()

        # Create output directory
        output_dir = Path(args.output)
        output_dir.mkdir(parents=True, exist_ok=True)

        # Format and save outputs
        if args.format in ["markdown", "all"]:
            print("\n📝 Formatting Markdown...")
            md_formatter = MarkdownFormatter(campaign_name)
            md_content = md_formatter.format_full_bible(elements)
            md_formatter.save_to_file(md_content, output_dir)

        if args.format in ["json", "all"]:
            print("\n📦 Exporting JSON...")
            json_formatter = JSONFormatter(campaign_name)
            json_content = json_formatter.format_full_bible(elements)
            json_formatter.save_to_file(json_content, output_dir)

        if args.format in ["obsidian", "all"]:
            print("\n📚 Creating Obsidian vault...")
            obsidian_formatter = ObsidianFormatter(campaign_name)
            obsidian_formatter.create_vault(elements, output_dir)

        print("\n✅ Campaign Bible Generation Complete! 🎉\n")
        print(f"📂 Your campaign materials are in: {output_dir.absolute()}")
        print("\nHappy adventuring! ⚔️🐉\n")

    except KeyboardInterrupt:
        print("\n\n⚠️ Generation interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error during generation: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
