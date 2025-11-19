# Best Practices for Using Infinite Realms

## Campaign Configuration

### Writing a Good Campaign Pitch

**Good Pitches**:
- ✅ "A fallen empire rises from shadow, corrupting the land with dark magic as fractured kingdoms must unite or fall"
- ✅ "Swashbuckling pirates uncover ancient sea god conspiracies in a world of endless archipelagos"
- ✅ "In a steampunk city powered by magic clockwork, a missing inventor sparks a war for control"

**Bad Pitches**:
- ❌ "Fantasy campaign with dragons" (too vague)
- ❌ "My players will explore a world" (no hook or conflict)
- ❌ 5 paragraphs of backstory (too much detail, be concise)

**Key Elements**:
1. **Central Conflict**: What's the main problem?
2. **Stakes**: What happens if players fail?
3. **Unique Hook**: What makes this different?

### Choosing Themes

Pick 3-5 themes that will recur throughout the campaign:

**Strong Themes**:
- Corruption vs. redemption
- Power and its cost
- Unity vs. division
- Secrets and revelation
- Freedom vs. order

**Use themes to guide**:
- Faction conflicts
- NPC motivations
- Location design
- Plot hooks

### Setting the Right Tone

Be specific about tone to guide agent creativity:

**Examples**:
- "Dark fantasy with moments of hope, morally gray villains"
- "Heroic epic, players are legendary heroes, high magic spectacle"
- "Gritty low-magic survival, realistic consequences"
- "Gonzo weird fantasy, surreal and humorous, anything goes"

## Optimizing Generation

### Start Small, Scale Up

1. First run: Use minimal config to test
2. Review output for quality and style
3. Adjust config and regenerate
4. Add more NPCs/factions/locations incrementally

### Balance Detail vs. Speed

| Detail Level | Generation Time | Use When |
|-------------|-----------------|-----------|
| Basic | 5-10 min | Quick ideas, testing |
| Moderate | 15-20 min | Standard campaigns |
| Comprehensive | 30-45 min | Epic campaigns, lots of prep time |

### Faction Count Guidelines

- **3 Factions**: Minimal, good for focused stories
- **5 Factions**: Sweet spot for most campaigns
- **7+ Factions**: Complex political intrigue, experienced DMs only

More factions = more connections = more complexity = longer generation time

### NPC Count Guidelines

- **10 NPCs**: Minimal cast
- **15 NPCs**: Recommended starting point
- **20+ NPCs**: Large campaign with lots of social interaction

**Pro tip**: Start with fewer major NPCs, use the random NPC tables for improvisation

## Getting Better Results

### Theme Consistency

Ensure your themes align:

**Aligned**:
```yaml
themes:
  - Ancient evils awakening
  - Corruption spreading
  - Heroes rising to challenge
tone: "Dark fantasy with hope"
```

**Misaligned**:
```yaml
themes:
  - Comedy and humor
  - Grimdark horror
  - Cute woodland creatures
tone: "Serious political drama"
```

### Faction Design

Great factions need:
1. **Clear Goal**: What do they want?
2. **Opposition**: Who stands in their way?
3. **Resources**: How will they achieve their goal?
4. **Player Hook**: Why should players care?

The AI will generate these, but guide it with good themes.

### Location Variety

Mix location types:
- **Cities**: Social, political, resource hubs
- **Dungeons**: Combat, exploration, treasure
- **Wilderness**: Travel, survival, discovery
- **Special**: Unique magical locations

Don't make 10 cities or 10 dungeons - variety creates better gameplay.

## Working with Output

### Iteration Strategy

1. **First Pass**: Generate full bible, read through
2. **Identify Gaps**: What's missing? What doesn't fit?
3. **Adjust Config**: Tweak themes, add specific requests
4. **Regenerate**: Try again with improvements
5. **Manual Polish**: Edit the markdown/JSON directly

### Using Multiple Formats

- **Markdown**: For reading, printing, sharing with players
- **JSON**: For importing into Foundry VTT, Roll20, etc.
- **Obsidian**: For DM notes, linking ideas, campaign management

### Player Handout Tips

The generated player handout is DM-approved by default. Before sharing:

1. Read it for accidentally revealed secrets
2. Customize for your table's style
3. Add/remove details as needed
4. Consider player questions and add FAQ section

### Random Tables Usage

Random tables are for **improvisation**, not planning:

- Roll when players go off-script
- Use to add unexpected twists
- Combine multiple table results for creativity
- Let results inspire you, don't be bound by them

## Advanced Tips

### Custom Agent Personalities

Edit `src/config/agents.yaml` to adjust agent behavior:

```yaml
character_dramatist:
  backstory: >
    You create NPCs inspired by [favorite media].
    You emphasize [specific traits].
```

### Custom Task Instructions

Edit `src/config/tasks.yaml` for specific outputs:

```yaml
create_npcs:
  description: >
    Create NPCs with [your specific requirements].
    Focus on [your priorities].
```

### Extending Tools

Create custom tools in `src/tools/`:

```python
class MyCustomTool(BaseTool):
    name: str = "My Tool"
    description: str = "What it does"

    def _run(self, input: str) -> str:
        # Your implementation
        return result
```

Then add to crew initialization in `campaign_crew.py`.

### Combining Campaigns

Generate multiple smaller campaigns and merge:

1. Generate Campaign A with 3 factions
2. Generate Campaign B with different 3 factions
3. Manually merge JSON outputs
4. Use relationship mapper to connect them

## Common Pitfalls

❌ **Too Many Elements**: 10 factions, 50 NPCs, 30 locations = overwhelming
✅ **Start Focused**: 5 factions, 15 NPCs, 10 locations = manageable

❌ **Vague Themes**: "Adventure" and "Magic"
✅ **Specific Themes**: "Redemption through sacrifice" and "Ancient sins revisited"

❌ **Ignoring Player Level**: Starting at level 1 with cosmic threats
✅ **Appropriate Scale**: Level 1 = local threats, scale up as they level

❌ **No Central Conflict**: Random factions with unrelated goals
✅ **Unified Conflict**: All factions care about the same MacGuffin/territory/threat

❌ **Static World**: Nothing changes if players don't act
✅ **Dynamic World**: Factions pursue goals, timelines matter

## Quality Checklist

Before finalizing your campaign bible:

- [ ] All factions have clear, conflicting goals
- [ ] Every NPC has wants, fears, and offers
- [ ] Every location has 3 adventure hooks
- [ ] Player handout doesn't reveal secrets
- [ ] Themes recur throughout content
- [ ] At least 3 connections per major element
- [ ] Random tables reflect setting
- [ ] Consistency validation passed
- [ ] D&D 5E rules compliance verified
- [ ] You're excited to run this campaign!

---

**Remember**: The AI generates scaffolding. Your creativity and table's style make it come alive!
