# Model Configuration Guide

## Overview

Infinite Realms supports **per-agent model configuration**, allowing you to optimize for quality, cost, and speed by using different models for different tasks.

## Quick Start

### 1. Simple (Use One Model for Everything)

```bash
# In .env
OPENAI_API_KEY=sk-...
DEFAULT_LLM=gpt-4-turbo-preview
```

All agents will use GPT-4 Turbo.

### 2. Mixed Providers (Recommended)

```bash
# In .env
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
```

Then configure per-agent in `src/config/agents.yaml`:

```yaml
master_worldbuilder:
  llm: "gpt-4-turbo-preview"
  temperature: 0.8
  # ... rest of config

character_dramatist:
  llm: "claude-3-5-sonnet-20241022"  # Claude excels at character writing
  temperature: 0.8
  # ... rest of config

lorekeeper:
  llm: "gpt-4-turbo-preview"
  temperature: 0.3  # Lower temp for validation
  # ... rest of config
```

### 3. Cost Optimized

Use cheaper models where quality isn't critical:

```yaml
lorekeeper:
  llm: "claude-3-haiku-20240307"  # Fast and cheap for validation
  temperature: 0.3
```

## Supported Models

### OpenAI Models

| Model | Best For | Cost (per 1M tokens) | Speed |
|-------|----------|----------------------|-------|
| `gpt-4-turbo-preview` | Creative tasks, worldbuilding | $10 in / $30 out | Medium |
| `gpt-4` | Highest quality | $30 in / $60 out | Slow |
| `gpt-3.5-turbo` | Fast iteration, testing | $0.50 in / $1.50 out | Fast |

**When to use OpenAI:**
- Need broad D&D knowledge
- Complex reasoning tasks
- Consistent output format

### Anthropic Models

| Model | Best For | Cost (per 1M tokens) | Speed |
|-------|----------|----------------------|-------|
| `claude-3-opus-20240229` | Highest quality creative | $15 in / $75 out | Medium |
| `claude-3-5-sonnet-20241022` | Best balance ⭐ | $3 in / $15 out | Fast |
| `claude-3-haiku-20240307` | Validation, fast tasks | $0.25 in / $1.25 out | Very Fast |

**When to use Anthropic:**
- Character writing and dialogue
- Seeing relationships/connections
- Concise, evocative prose
- Cost-effective validation

### Local Models (Ollama)

| Model | Best For | Cost | Speed |
|-------|----------|------|-------|
| `ollama/llama2` | Testing, development | Free | Depends on hardware |
| `ollama/mistral` | General tasks | Free | Depends on hardware |
| `ollama/codellama` | Structured output | Free | Depends on hardware |

**When to use Ollama:**
- Development and testing
- Privacy-sensitive campaigns
- No API costs
- Offline usage

**Setup:**
```bash
# Install Ollama
curl https://ollama.ai/install.sh | sh

# Pull a model
ollama pull llama2

# In .env
OLLAMA_BASE_URL=http://localhost:11434
```

## Recommended Configurations

### Best Quality (Cost: ~$1-2 per campaign)

```yaml
master_worldbuilder:
  llm: "gpt-4-turbo-preview"
  temperature: 0.8

character_dramatist:
  llm: "claude-3-opus-20240229"
  temperature: 0.8

lorekeeper:
  llm: "gpt-4-turbo-preview"
  temperature: 0.3

adventure_architect:
  llm: "gpt-4-turbo-preview"
  temperature: 0.7

integration_specialist:
  llm: "claude-3-opus-20240229"
  temperature: 0.7

player_facing_writer:
  llm: "claude-3-opus-20240229"
  temperature: 0.75
```

### Best Balance (Cost: ~$0.60-1.00 per campaign) ⭐

```yaml
master_worldbuilder:
  llm: "gpt-4-turbo-preview"
  temperature: 0.8

character_dramatist:
  llm: "claude-3-5-sonnet-20241022"
  temperature: 0.8

lorekeeper:
  llm: "claude-3-haiku-20240307"
  temperature: 0.3

adventure_architect:
  llm: "gpt-4-turbo-preview"
  temperature: 0.7

integration_specialist:
  llm: "claude-3-5-sonnet-20241022"
  temperature: 0.7

player_facing_writer:
  llm: "claude-3-5-sonnet-20241022"
  temperature: 0.75
```

### Budget (Cost: ~$0.10-0.30 per campaign)

```yaml
master_worldbuilder:
  llm: "gpt-3.5-turbo"
  temperature: 0.8

character_dramatist:
  llm: "claude-3-haiku-20240307"
  temperature: 0.8

lorekeeper:
  llm: "claude-3-haiku-20240307"
  temperature: 0.3

adventure_architect:
  llm: "gpt-3.5-turbo"
  temperature: 0.7

integration_specialist:
  llm: "claude-3-haiku-20240307"
  temperature: 0.7

player_facing_writer:
  llm: "claude-3-haiku-20240307"
  temperature: 0.75
```

### Local/Free (Cost: $0, requires Ollama)

```yaml
master_worldbuilder:
  llm: "ollama/llama2"
  temperature: 0.8

character_dramatist:
  llm: "ollama/llama2"
  temperature: 0.8

lorekeeper:
  llm: "ollama/llama2"
  temperature: 0.3

adventure_architect:
  llm: "ollama/llama2"
  temperature: 0.7

integration_specialist:
  llm: "ollama/llama2"
  temperature: 0.7

player_facing_writer:
  llm: "ollama/llama2"
  temperature: 0.75
```

## Temperature Settings

Temperature controls randomness (0.0-1.0):

- **0.0-0.3**: Deterministic, factual (validation, rules)
- **0.4-0.6**: Balanced (general tasks)
- **0.7-0.9**: Creative (worldbuilding, characters)
- **1.0+**: Very random (not recommended)

## Per-Agent Recommendations

### Master Worldbuilder
**Best model**: GPT-4 Turbo or Claude Opus
**Temperature**: 0.7-0.8
**Why**: Needs broad knowledge and creativity

### Character Dramatist
**Best model**: Claude 3.5 Sonnet or Opus ⭐
**Temperature**: 0.8
**Why**: Claude excels at character voice and motivation

### Lorekeeper
**Best model**: Claude Haiku or GPT-3.5
**Temperature**: 0.3
**Why**: Validation doesn't need top-tier creativity

### Adventure Architect
**Best model**: GPT-4 Turbo
**Temperature**: 0.7
**Why**: Needs D&D knowledge + creativity

### Integration Specialist
**Best model**: Claude 3.5 Sonnet ⭐
**Temperature**: 0.7
**Why**: Claude sees relationships exceptionally well

### Player-Facing Writer
**Best model**: Claude 3.5 Sonnet ⭐
**Temperature**: 0.75
**Why**: Claude writes concise, evocative prose

## Cost Tracking

Enable cost tracking in `.env`:

```bash
ENABLE_COST_TRACKING=true
```

After generation, you'll see:

```
💰 Estimated Cost Breakdown:
  Master Worldbuilder (gpt-4-turbo): $0.15
  Character Dramatist (claude-3-5-sonnet): $0.12
  Lorekeeper (claude-3-haiku): $0.03
  ...
  Total: $0.78
```

## Environment Variable Substitution

You can use environment variables in `agents.yaml`:

```yaml
master_worldbuilder:
  llm: "${CREATIVE_LLM}"  # Will use value from .env
```

Then in `.env`:
```bash
CREATIVE_LLM=gpt-4-turbo-preview
```

This allows easy switching without editing YAML.

## Testing Different Models

Create multiple agent config files:

```bash
cp src/config/agents.yaml src/config/agents.budget.yaml
cp src/config/agents.yaml src/config/agents.premium.yaml
```

Then specify which to use:

```bash
python src/main.py --config my_campaign.yaml --agents src/config/agents.premium.yaml
```

(Note: This requires adding the `--agents` flag - future enhancement)

## Troubleshooting

### "No API key found"

Make sure you have the appropriate API key in `.env`:
- OpenAI models → `OPENAI_API_KEY`
- Anthropic models → `ANTHROPIC_API_KEY`
- Ollama models → Ollama running locally

### "Rate limit exceeded"

Add delays between requests or use cheaper/faster models:

```yaml
lorekeeper:
  llm: "claude-3-haiku-20240307"  # Faster, less likely to hit limits
```

### "Model not found"

Check that you're using the correct model identifier:
- ✅ `gpt-4-turbo-preview`
- ❌ `gpt-4-turbo` (might not work, depends on provider)
- ✅ `claude-3-5-sonnet-20241022`
- ❌ `claude-3.5-sonnet` (use the full version string)

## Advanced: Provider-Specific Settings

You can pass provider-specific kwargs:

```python
# In llm_factory.py or custom code
llm = create_llm(
    "gpt-4-turbo-preview",
    temperature=0.7,
    max_tokens=4000,  # Limit output
    top_p=0.9,  # Nucleus sampling
)
```

---

**Recommended starting point**: Use the **Best Balance** configuration. It provides excellent results at reasonable cost (~$0.60-1.00 per campaign).
