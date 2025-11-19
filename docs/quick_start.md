## Quick Start Guide

### Installation

1. **Clone and setup**:
```bash
git clone <repo-url>
cd infinite-realms-clean
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e .
```

2. **Configure API keys**:
```bash
cp .env.example .env
# Edit .env and add your OpenAI or Anthropic API key
```

### Generate Your First Campaign

#### Option 1: Use an Example

```bash
python src/main.py --campaign examples/shadow_empire.yaml
```

#### Option 2: Interactive Mode

```bash
python src/main.py --interactive
```

Follow the prompts to configure your campaign.

#### Option 3: Create Your Own Config

Create a YAML file:

```yaml
campaign:
  name: "My Amazing Campaign"
  pitch: "Your campaign concept here"
  themes:
    - "Theme 1"
    - "Theme 2"
  tone: "Describe the tone"
  setting_type: "Describe the setting"

players:
  count: 4
  starting_level: 1
  experience_level: "mixed"

preferences:
  include_factions: 5
  include_npcs: 15
  include_locations: 10
  detail_level: "comprehensive"
```

Then run:
```bash
python src/main.py --campaign my_campaign.yaml
```

### Output

By default, you'll get three outputs in the `./output` directory:

1. **Markdown** - Printable campaign bible
2. **JSON** - For importing into VTTs or databases
3. **Obsidian** - Interconnected vault with backlinks

Specify a single format:
```bash
python src/main.py --campaign my_campaign.yaml --format markdown
```

### What You Get

Your campaign bible includes:

- **Player Handout** (3-4 pages): What players need to know
- **World Foundation**: Geography, history, cosmology, magic system
- **Factions**: Detailed dossiers with goals, conflicts, and hooks
- **NPCs**: Character cards with motivations and secrets
- **Locations**: Detailed descriptions with adventure hooks
- **Adventure Hooks**: Organized by character tier (1-5, 6-10, 11-16, 17-20)
- **Random Tables**: Encounters, weather, rumors, events
- **Relationship Maps**: How everything connects

### Tips

1. **Start simple**: Use the minimal example and expand from there
2. **Be specific**: The more specific your themes and pitch, the better the output
3. **Iterate**: Generate multiple times with tweaks to find what works
4. **Customize**: Edit the YAML agent and task configs for your needs
5. **Use the tools**: The relationship mapper and consistency checker help maintain coherence

### Troubleshooting

**"No API key found"**: Make sure you've created `.env` and added your API key

**Generation is slow**: This is normal! Generating a comprehensive campaign bible takes 10-30 minutes depending on complexity

**Out of memory**: Reduce `detail_level` or number of NPCs/locations/factions

**Consistency issues**: The tools will flag these - use them to iterate and improve

### Next Steps

- Read the [Architecture Guide](architecture.md) to understand how it works
- Check [Best Practices](best_practices.md) for tips on getting better results
- Learn about [Custom Tools](tools.md) to extend functionality
