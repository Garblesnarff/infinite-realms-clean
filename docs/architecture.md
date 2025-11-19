# Architecture Overview

## System Design Philosophy

Infinite Realms follows a **multi-agent orchestration** architecture where specialized AI agents collaborate to create comprehensive campaign content. This design is inspired by how professional creative teams work: different specialists handling different aspects, coordinated by a project manager.

## High-Level Architecture

```
┌─────────────────────────────────────────────────┐
│              User Input (YAML)                  │
│  Campaign concept, themes, preferences          │
└─────────────────┬───────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────┐
│          CampaignBibleFlow (Orchestrator)       │
│  Manages state, coordinates crews, handles      │
│  conditional logic and iterative refinement     │
└─────────────────┬───────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────┐
│            CampaignCrew (Coordinator)           │
│  Creates agents, assigns tasks, manages tools   │
└─────────────────┬───────────────────────────────┘
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
┌───────────────┐    ┌───────────────┐
│    Agents     │    │     Tools     │
│               │    │               │
│ • Worldbuild  │    │ • Consistency │
│ • Character   │    │ • D&D Valid.  │
│ • Lorekeeper  │    │ • Rel. Map    │
│ • Adventure   │    │ • Hook Gen    │
│ • Integration │    │ • Random Tbl  │
│ • Player Face │    │               │
└───────┬───────┘    └───────────────┘
        │
        ▼
┌─────────────────────────────────────────────────┐
│              Output Formatters                  │
│  Markdown | JSON | Obsidian Vault               │
└─────────────────────────────────────────────────┘
```

## Core Components

### 1. CampaignBibleFlow

**File**: `src/flows/campaign_flow.py`

**Purpose**: Orchestrates the entire generation pipeline using CrewAI Flows.

**Key Features**:
- **State Management**: Maintains campaign state across all generation steps
- **Conditional Logic**: Makes decisions based on validation results
- **Error Handling**: Gracefully handles failures and retries
- **Progress Tracking**: Provides user feedback throughout generation

**Flow Steps**:
1. Load and validate configuration
2. Analyze campaign concept
3. Build world foundation
4. Create factions
5. Create NPCs
6. Create locations
7. Weave connections
8. Generate adventure hooks
9. Validate content (consistency + D&D rules)
10. Create random tables
11. Generate player handout
12. Assemble final campaign bible

Each step uses the `@listen` decorator to create dependencies.

### 2. CampaignCrew

**File**: `src/crews/campaign_crew.py`

**Purpose**: Coordinates specialized agents to execute tasks.

**Key Features**:
- **Agent Management**: Creates and configures all specialized agents
- **Task Assignment**: Maps tasks to appropriate agents
- **Tool Provisioning**: Gives agents access to relevant tools
- **Process Control**: Uses sequential or hierarchical processes

**Methods**:
- `analyze_campaign()` - Extract themes and requirements
- `create_world_foundation()` - Build setting fundamentals
- `create_factions()` - Design faction politics
- `create_npcs()` - Generate memorable characters
- `create_locations()` - Design key places
- `integrate_elements()` - Weave connections
- `generate_hooks()` - Create adventure seeds
- `validate_campaign()` - Check consistency and rules
- `create_random_tables()` - Generate DM tools
- `create_player_handout()` - Write player-facing content
- `assemble_bible()` - Compile everything

### 3. Specialized Agents

**File**: `src/config/agents.yaml`

Each agent has a specialized role:

#### Master Worldbuilder
- **Focus**: Geography, history, cosmology, magic systems
- **Expertise**: World-building, setting design, consistency
- **Output**: Foundation documents that other agents build upon

#### Character Dramatist
- **Focus**: NPCs, factions, political dynamics
- **Expertise**: Character writing, motivation, conflict creation
- **Output**: Memorable characters and faction politics

#### Lorekeeper
- **Focus**: Consistency validation, D&D 5E rules compliance
- **Expertise**: Rules knowledge, continuity checking
- **Output**: Validation reports and recommendations

#### Adventure Architect
- **Focus**: Plot hooks, encounters, quest lines
- **Expertise**: Encounter design, pacing, challenge balance
- **Output**: Adventure hooks and random tables

#### Integration Specialist
- **Focus**: Connections, relationships, network effects
- **Expertise**: Systems thinking, relationship mapping
- **Output**: Integration reports and connection data

#### Player-Facing Writer
- **Focus**: Player handouts, marketing copy
- **Expertise**: Evocative writing, conciseness
- **Output**: Player-ready campaign primer

### 4. Custom Tools

**Directory**: `src/tools/`

Tools extend agent capabilities with specialized functions:

#### ConsistencyCheckerTool
- **Technology**: ChromaDB vector database
- **Function**: Stores all generated facts, queries for similar content
- **Purpose**: Prevent contradictions and plot holes
- **Usage**: Called before finalizing any element

#### DnD5EValidatorTool
- **Technology**: Rule-based validation
- **Function**: Checks spells, CR, encounters, lore against D&D 5E
- **Purpose**: Ensure campaign fits D&D conventions
- **Usage**: Validates all mechanical content

#### RelationshipMapperTool
- **Technology**: NetworkX graph analysis
- **Function**: Creates relationship networks, identifies key nodes
- **Purpose**: Ensure interconnected world
- **Usage**: Analyzes all elements after generation

#### HookGeneratorTool
- **Technology**: Template-based generation
- **Function**: Creates plot hooks from campaign elements
- **Purpose**: Give DMs ready-to-use adventure seeds
- **Usage**: Generates hooks for each element

#### RandomTableCreatorTool
- **Technology**: Procedural generation
- **Function**: Creates setting-specific random tables
- **Purpose**: Support DM improvisation
- **Usage**: Generates tables for each location type

### 5. Output Formatters

**Directory**: `src/formatters/`

#### MarkdownFormatter
- Structured, printable document
- Table of contents with sections
- Easy to read and reference

#### JSONFormatter
- Machine-readable data export
- For VTT import (Foundry, Roll20)
- For custom tools and databases

#### ObsidianFormatter
- Interconnected note vault
- Backlinks between elements
- Ideal for DM campaign management

## Data Flow

### Generation Pipeline

```
Input YAML
    ↓
Validation
    ↓
Concept Analysis
    ↓
World Foundation ──→ [Consistency DB]
    ↓                       ↓
Factions ──────────→ [Consistency DB]
    ↓                       ↓
NPCs ──────────────→ [Consistency DB]
    ↓                       ↓
Locations ─────────→ [Consistency DB]
    ↓
Integration ────────→ [Relationship Graph]
    ↓
Adventure Hooks ────→ [Hook Templates]
    ↓
Validation ─────────→ [D&D Rules + Consistency]
    ↓
Random Tables
    ↓
Player Handout
    ↓
Assembly
    ↓
Output (MD/JSON/Obsidian)
```

### State Management

The `CampaignBibleFlow` maintains state across all steps:

```python
{
    "campaign_config": {...},
    "world_foundation": {...},
    "factions": [...],
    "npcs": [...],
    "locations": [...],
    "connections": {...},
    "hooks": {...},
    "validation_report": {...},
    "player_handout": "...",
    "campaign_bible": "..."
}
```

This state is:
- Built incrementally through the flow
- Available to all agents via context
- Persisted for resume capability (future feature)
- Passed to formatters for output

## Design Patterns

### 1. Multi-Agent Collaboration

Each agent is a **specialist** with:
- Defined role and expertise
- Specific tools access
- Clear output expectations
- Limited scope (no delegation)

**Why**: Mirrors how creative teams work. Better output quality than a single general-purpose agent.

### 2. Flows for Orchestration

Using CrewAI Flows (v0.98.0+) provides:
- **Conditional branching**: Different paths based on validation
- **State persistence**: Resume from any step
- **Error handling**: Graceful failures
- **Progress tracking**: User feedback

**Why**: Complex multi-step processes need coordination beyond simple sequential execution.

### 3. Tool Augmentation

Agents use tools for:
- **Deterministic operations**: Rule checking, validation
- **Data persistence**: Vector database, graph storage
- **Specialized computation**: Relationship mapping, CR calculation

**Why**: LLMs excel at creative generation, struggle with precise computation. Tools provide precision.

### 4. Separation of Concerns

- **Agents**: Creative generation
- **Tools**: Validation and computation
- **Flows**: Orchestration and control
- **Formatters**: Output presentation
- **Crews**: Coordination

**Why**: Each component has a single responsibility, making the system maintainable and extensible.

### 5. Configuration-Driven

Agents and tasks defined in YAML:
- Easy to modify without code changes
- Version control for different styles
- A/B testing of prompts
- Community sharing of configs

**Why**: Non-programmers can customize agent behavior.

## Extension Points

### Adding New Agents

1. Define in `agents.yaml`
2. Create tasks in `tasks.yaml`
3. Add to crew initialization
4. Update flow if needed

### Adding New Tools

1. Implement `BaseTool` subclass
2. Add to `tools/__init__.py`
3. Provide to relevant agents
4. Document usage

### Adding New Output Formats

1. Create formatter class
2. Implement `format_full_bible()` and `save_to_file()`
3. Add to CLI options
4. Update documentation

### Custom Flows

1. Subclass `Flow`
2. Define steps with `@start()` and `@listen()`
3. Manage state in instance variables
4. Call from `main.py`

## Performance Considerations

### Token Usage

Estimated tokens per campaign (comprehensive):
- World foundation: ~2,000 tokens
- Factions (5): ~5,000 tokens
- NPCs (15): ~8,000 tokens
- Locations (10): ~6,000 tokens
- Integration: ~3,000 tokens
- Validation: ~2,000 tokens
- Assembly: ~4,000 tokens

**Total**: ~30,000-50,000 tokens

**Cost** (GPT-4 Turbo at $0.01/1K tokens):
- Input: ~$0.30-0.50
- Output: ~$0.30-0.50
- **Total**: ~$0.60-1.00 per campaign

### Generation Time

Depends on:
- Number of elements (factions, NPCs, locations)
- Detail level (basic, moderate, comprehensive)
- LLM model (GPT-4 is slower than GPT-3.5)
- API rate limits

Typical: **15-30 minutes** for comprehensive campaign

### Optimization Strategies

1. **Use GPT-3.5 Turbo** for non-creative tasks (validation)
2. **Parallel task execution** where possible
3. **Caching** of world foundation for iterations
4. **Incremental generation** - start small, expand
5. **Local LLMs** (Ollama) for cost-sensitive users

## Future Enhancements

### Planned Features

1. **Resume capability**: Save and resume long generations
2. **Incremental updates**: Modify existing campaigns
3. **Multiplayer mode**: Collaborative campaign building
4. **Version control**: Track campaign changes over time
5. **Custom agent marketplace**: Share and download agent configs
6. **Web UI**: Browser-based interface
7. **Real-time collaboration**: Multiple DMs working together

### Technical Debt

- Add comprehensive test coverage
- Implement proper logging
- Add telemetry for debugging
- Improve error messages
- Add progress bars
- Implement retry logic for API failures

---

For implementation details, see the source code and inline documentation.
