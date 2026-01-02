# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Infinite Realms is building the "YouTube of AI-Generated Entertainment" starting with solo AI D&D experiences. The platform uses AI to generate and manage TTRPG campaigns, with plans to expand into campaign sharing, auto-generated publishing, 3D assets, and shared virtual worlds.

**Current stack**: React/TypeScript frontend, Supabase backend, CrewAI agents, Gemini 2.5 Flash, ElevenLabs for audio.

## Repository Structure

This is a monorepo with four main components:

### `/crewai-dnd-expander/`
Python-based CrewAI pipeline that expands campaign ideas into full 5E-compatible content. Uses multiple AI agents via OpenRouter to parse markdown campaign ideas and generate structured data (NPCs, quests, locations, worlds) for Supabase import.

**Key commands:**
```bash
cd crewai-dnd-expander
source venv/bin/activate
pip install -r requirements.txt

# Single campaign expansion
python main.py path/to/campaign.md --output-dir output

# Batch process all campaigns
python main.py --batch --input-dir ../campaign-ideas/ --output-dir output

# Dry run (no LLM calls)
python main.py --batch --dry-run
```

**Environment**: Requires `OPENROUTER_API_KEY` in `.env`. Models configured via `MODELS` JSON env var.

### `/campaign-ideas/`
820+ D&D campaign frameworks organized by genre (Fantasy, Horror, Sci-Fi, Mystery, Historical, Post-Apocalyptic, Intrigue, Urban, Adventure). Each campaign can have: overview, creative-brief, world-building, and campaign-bible files.

**Shell scripts for campaign management:**
```bash
cd campaign-ideas

./stats.sh                    # Dashboard view of repository state
./move-completed.sh           # Dry run - move completed campaigns
./move-completed.sh false     # Actually move completed campaigns
./validate-campaigns.sh       # Check for issues before ingestion
./audit-campaigns.sh          # Detailed audit with CSV export
./search-campaigns.sh dragon  # Find campaigns by keyword
./extract-npcs.sh             # Pull all NPCs into one file
./pick-launch-campaigns.sh    # Generate selection document
```

**Completeness levels:**
- **Complete**: Has overview + creative-brief + world-building + campaign-bible (ready for ingestion)
- **Framework**: Has overview + creative-brief + world-building (needs bible)
- **Minimal**: Only overview or partial files

### `/infinite-realms-research/`
Business intelligence and strategic planning documents covering market research, competitive analysis, technical architecture, financial modeling, and roadmap strategy.

### `/ai-world-forge-dashboard/`
React frontend (currently contains only node_modules from a previous CRA setup).

### `/test/`
Sample expanded campaign markdown files for testing the expander output.

## Campaign Content Schema

Campaigns follow a Pydantic-validated schema mapping to Supabase tables:
- `campaigns`: name, description, genre, difficulty_level, campaign_length, tone, setting_details, thematic_elements
- `worlds`: climate_type, magic_level, technology_level
- `npcs`: race, class, level, personality, stats (5E stat blocks as JSON)
- `quests`: difficulty, quest_type, prerequisites, rewards
- `locations`: location_type, parent_location_id, coordinates

## CrewAI Agent Pipeline

The expansion pipeline uses 7 sequential agents via OpenRouter:
1. **Idea Parser**: Extracts structured data from markdown
2. **Campaign Architect**: Designs 5E-compatible structure with level progression
3. **World Builder**: Creates worlds, locations, factions
4. **NPC Designer**: Generates full 5E stat blocks
5. **Encounter Planner**: Designs balanced quests and combats
6. **Rules Validator**: Validates 5E compliance and schema integrity
7. **DB Compiler**: Assembles import-ready JSON/SQL

Output formats: JSON bundle, SQL INSERT statements, Markdown campaign book.

## D&D 5E Constraints

When generating or validating content:
- Level progression typically 1-5 starting, scaling to 15+ for full campaigns
- CR-appropriate encounters based on party level
- Standard 5E stat block format (ability scores, HP, AC, skills)
- Difficulty levels: easy, medium, hard, deadly
- Campaign lengths: one-shot, short (6-8 sessions), full
