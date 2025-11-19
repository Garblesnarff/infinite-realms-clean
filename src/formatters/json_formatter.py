"""JSON formatter for campaign bible output."""

import json
from pathlib import Path
from typing import Any, Dict


class JSONFormatter:
    """
    Formats campaign bible content as structured JSON.

    Suitable for importing into VTTs, databases, or other tools.
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
        Format complete campaign bible as JSON.

        Args:
            elements: All campaign elements

        Returns:
            JSON string
        """
        output = {
            "campaign_name": self.campaign_name,
            "version": "1.0",
            "data": elements,
        }

        return json.dumps(output, indent=2, ensure_ascii=False)

    def save_to_file(self, content: str, output_dir: Path):
        """
        Save JSON content to file.

        Args:
            content: JSON content
            output_dir: Output directory path
        """
        output_dir.mkdir(parents=True, exist_ok=True)
        filename = f"{self.campaign_name.lower().replace(' ', '_')}_campaign_bible.json"
        filepath = output_dir / filename

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"✅ JSON export saved to: {filepath}")
        return filepath
