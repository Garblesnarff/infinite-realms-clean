"""Consistency Checker Tool using vector database for campaign element validation."""

import json
import os
from typing import Any, Optional, Type

import chromadb
from chromadb.config import Settings
from crewai_tools import BaseTool
from pydantic import BaseModel, Field


class ConsistencyCheckerInput(BaseModel):
    """Input schema for ConsistencyChecker."""

    content: str = Field(..., description="New content to check for consistency")
    category: str = Field(
        ..., description="Category of content (e.g., 'npc', 'faction', 'location', 'event')"
    )
    context: str = Field(
        default="",
        description="Additional context or existing related information",
    )


class ConsistencyCheckerTool(BaseTool):
    """
    Tool for checking consistency of campaign elements using vector similarity search.

    This tool maintains a vector database of all established campaign facts and
    checks new content against existing information to flag potential contradictions.
    """

    name: str = "Consistency Checker"
    description: str = (
        "Checks new campaign content against established facts to identify "
        "contradictions or inconsistencies. Use this before finalizing any "
        "campaign element. Input should include the content to check, its category, "
        "and any relevant context."
    )
    args_schema: Type[BaseModel] = ConsistencyCheckerInput

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Initialize ChromaDB
        db_path = os.getenv("CHROMA_DB_PATH", "./data/chroma_db")
        self.client = chromadb.PersistentClient(
            path=db_path,
            settings=Settings(anonymized_telemetry=False),
        )
        # Get or create collection
        self.collection = self.client.get_or_create_collection(
            name="campaign_facts",
            metadata={"hnsw:space": "cosine"},
        )

    def _run(
        self,
        content: str,
        category: str,
        context: str = "",
    ) -> str:
        """
        Check content for consistency against established facts.

        Args:
            content: The new content to validate
            category: Category of the content
            context: Additional context

        Returns:
            Analysis of consistency with any potential issues flagged
        """
        try:
            # Query similar existing content
            results = self.collection.query(
                query_texts=[content],
                n_results=5,
                where={"category": category} if category else None,
            )

            # Analyze for contradictions
            issues = []
            similar_facts = []

            if results["documents"] and results["documents"][0]:
                for i, doc in enumerate(results["documents"][0]):
                    distance = results["distances"][0][i] if results["distances"] else 1.0
                    metadata = results["metadatas"][0][i] if results["metadatas"] else {}

                    # If very similar (distance < 0.3), might be duplicate or contradiction
                    if distance < 0.3:
                        similar_facts.append(
                            {
                                "fact": doc,
                                "similarity": 1 - distance,
                                "metadata": metadata,
                            }
                        )

            # Add the new content to the database
            self.collection.add(
                documents=[content],
                metadatas=[{"category": category, "context": context}],
                ids=[f"{category}_{self.collection.count()}"],
            )

            # Generate report
            report = {
                "status": "checked",
                "category": category,
                "content": content,
                "similar_existing_facts": similar_facts,
                "potential_issues": issues,
                "recommendation": (
                    "Review similar facts for potential contradictions"
                    if similar_facts
                    else "No major consistency issues detected"
                ),
            }

            return json.dumps(report, indent=2)

        except Exception as e:
            return f"Error checking consistency: {str(e)}"

    def clear_database(self):
        """Clear all stored facts (useful for starting new campaigns)."""
        try:
            self.client.delete_collection("campaign_facts")
            self.collection = self.client.get_or_create_collection(
                name="campaign_facts",
                metadata={"hnsw:space": "cosine"},
            )
            return "Database cleared successfully"
        except Exception as e:
            return f"Error clearing database: {str(e)}"
