# 🎲 Infinite Realms - AI-Powered D&D Campaign Bible Generator

> Transform your campaign ideas into comprehensive, living campaign bibles using state-of-the-art multi-agent AI orchestration.

## 🌟 What Makes This Special

This isn't just another content generator. Infinite Realms creates **interconnected, consistent, and usable** campaign reference materials that DMs actually want to use at the table.

### Key Features

- 🤖 **Multi-Agent Architecture**: 6 specialized AI agents working in harmony
- 🔗 **Relationship Mapping**: Every element connects to create organic storytelling
- ✅ **Consistency Checking**: Vector database ensures no contradictions
- 📊 **Hierarchical Workflow**: Manager agent coordinates specialized crews
- 🎯 **D&D 5E Native**: Built specifically for Fifth Edition rules and lore
- 📤 **Multiple Outputs**: Markdown, PDF, JSON, Obsidian vault-ready
- 🔄 **Iterative Refinement**: Multiple passes for depth and consistency

## 🏗️ Architecture

### The Agent Crew

1. **Master Worldbuilder** - Creates setting fundamentals (geography, history, cosmology)
2. **Character Dramatist** - Designs complex NPCs and faction politics
3. **Lorekeeper** - Validates consistency and D&D 5E compliance
4. **Adventure Architect** - Generates plot hooks and quest lines
5. **Integration Specialist** - Weaves connections between all elements
6. **Player-Facing Writer** - Creates compelling player handouts

### Custom Tools

- **Consistency Checker**: Vector database validation
- **D&D 5E Validator**: Rules and lore compliance
- **Relationship Mapper**: Network graph generation
- **Hook Generator**: Plot thread creation
- **Random Table Creator**: Setting-specific tables

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone <repo-url>
cd infinite-realms-clean

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e .

# Copy environment template and add your API keys
cp .env.example .env
# Edit .env with your API keys
```

### Basic Usage

```bash
# Run with example campaign
python src/main.py --campaign examples/shadow_empire.yaml

# Interactive mode
python src/main.py --interactive

# Custom configuration
python src/main.py --campaign my_campaign.yaml --output ./my_bible
```

### Campaign Configuration

Create a YAML file with your campaign concept:

```yaml
campaign:
  name: "The Shadow Empire"
  pitch: "A fallen empire rises from the shadows, corrupting the land with dark magic"
  themes:
    - "Corruption and redemption"
    - "Ancient evils awakening"
    - "Political intrigue"
  tone: "Dark fantasy with moments of hope"
  setting_type: "High magic, low tech"

players:
  count: 4
  starting_level: 3
  experience_level: "intermediate"

preferences:
  include_maps: true
  include_npcs: 15
  include_factions: 5
  include_locations: 10
  detail_level: "comprehensive"
```

## 📂 Project Structure

```
infinite-realms-clean/
├── src/
│   ├── agents/              # Agent implementations
│   ├── tools/               # Custom CrewAI tools
│   ├── crews/               # Crew configurations
│   ├── flows/               # CrewAI Flows
│   ├── formatters/          # Output formatters
│   ├── config/              # YAML configurations
│   │   ├── agents.yaml      # Agent definitions
│   │   └── tasks.yaml       # Task definitions
│   ├── templates/           # Output templates
│   └── main.py              # Entry point
├── examples/                # Example campaign configs
├── output/                  # Generated campaign bibles
├── tests/                   # Unit tests
├── docs/                    # Documentation
└── README.md
```

## 📖 Output Structure

Each campaign bible includes:

1. **Player Handout** (3-4 pages)
   - World primer and tone
   - Major factions overview
   - Character creation guidance

2. **DM Reference** (Comprehensive)
   - Detailed faction information
   - NPC cards with motivations
   - Location descriptions with hooks
   - Plot threads by tier
   - Timeline and cosmology

3. **Session Prep Tools**
   - Random encounter tables
   - Quick NPC generator
   - Location-specific prep sheets

4. **Digital Exports**
   - JSON for VTT import
   - Obsidian vault with backlinks
   - Relationship graph visualization

## 🎯 Design Philosophy

### The "Angry GM Principle"
Campaign bibles should be **fact sheets, not prose**. Quick, scannable, actionable.

### The "Rule of Three"
Every element has:
- 3 plot hooks
- 3 connections to other elements
- 3 secrets to reveal

### Player Impact
Static worlds are boring. Everything has goals that players can influence.

## 🛠️ Advanced Usage

### Custom Agents

Add your own specialized agents by extending the base configuration:

```yaml
# config/agents.yaml
custom_agent:
  role: "Magic System Designer"
  goal: "Create unique, balanced magic systems"
  backstory: "You are an expert in game design..."
  llm: "gpt-4-turbo-preview"
```

### Custom Tools

Create specialized tools for your needs:

```python
from crewai_tools import BaseTool

class MyCustomTool(BaseTool):
    name: str = "My Tool"
    description: str = "What it does"

    def _run(self, input: str) -> str:
        # Your implementation
        return result
```

### Flows and Conditional Logic

Use CrewAI Flows for complex workflows:

```python
from crewai.flow import Flow, start, listen

class CampaignFlow(Flow):
    @start()
    def analyze_input(self):
        # Process campaign concept
        pass

    @listen(analyze_input)
    def generate_world(self, context):
        # Conditional logic based on setting type
        pass
```

## 🧪 Testing

```bash
# Run all tests
pytest

# Run specific test
pytest tests/test_tools.py

# With coverage
pytest --cov=src tests/
```

## 📚 Documentation

- [Agent Architecture](docs/architecture.md)
- [Custom Tools Guide](docs/tools.md)
- [Output Formats](docs/outputs.md)
- [Best Practices](docs/best_practices.md)
- [API Reference](docs/api.md)

## 🤝 Contributing

Contributions welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📝 License

MIT License - see [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

- Built with [CrewAI](https://crewai.com)
- Inspired by [The Angry GM](https://theangrygm.com)
- D&D 5E by Wizards of the Coast

## 🐛 Troubleshooting

### Common Issues

**API Rate Limits**: Adjust delays in `config/crew_config.yaml`

**Memory Issues**: Reduce `detail_level` in campaign config

**Consistency Errors**: Clear ChromaDB cache: `rm -rf data/chroma_db`

## 🗺️ Roadmap

- [ ] Web UI for campaign creation
- [ ] Integration with D&D Beyond
- [ ] Support for other RPG systems
- [ ] Collaborative editing features
- [ ] AI-powered session prep assistant
- [ ] Mobile app for table reference

---

**Made with ⚔️ for DMs who want to focus on storytelling, not spreadsheets.**
