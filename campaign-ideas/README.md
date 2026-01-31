# Campaign Ideas - Scripts & Tools

This directory contains 820+ D&D campaign frameworks for Infinite Realms. These scripts help manage, organize, and track progress as campaigns are developed from frameworks into complete bibles.

## Directory Structure

```
campaign-ideas/
├── Completed/           # Campaigns with finished bibles (ready for ingestion)
│   ├── Fantasy/
│   ├── Horror/
│   ├── Sci-Fi/
│   ├── Mystery/
│   ├── Historical/
│   ├── Post-Apocalyptic/
│   ├── Intrigue/
│   ├── Urban/
│   └── Adventure/
├── Fantasy/             # In-progress frameworks (no bible yet)
├── Horror/
├── ...
├── Ideas-To-Expand/     # Raw ideas, incomplete campaigns, multi-AI drafts
└── [scripts]
```

## Campaign Completeness Levels

| Status | Files Present | Meaning |
|--------|---------------|---------|
| **Complete** | overview + creative-brief + world-building + campaign-bible | Ready for Lore Keeper ingestion |
| **Framework** | overview + creative-brief + world-building | Structure exists, needs bible |
| **Minimal** | Only overview or partial files | Needs significant work |

---

## Scripts

### `stats.sh`
**Dashboard view of entire repository.**

```bash
./stats.sh
```

Shows:
- Complete vs framework count per genre
- Overall progress percentage
- Estimated chunks for ingestion
- Raw ideas count

Run this anytime to see current state.

---

### `move-completed.sh`
**Moves campaigns with bibles to Completed/ directory.**

```bash
# Dry run (see what would move)
./move-completed.sh

# Actually move them
./move-completed.sh false
```

Use after Gemini/AI generates new bibles to separate done from in-progress.

---

### `audit-campaigns.sh`
**Detailed audit with CSV export.**

```bash
./audit-campaigns.sh
```

Outputs:
- Summary by genre
- List of launch-ready campaigns
- `campaign-audit.csv` - spreadsheet of all campaigns with status

---

### `validate-campaigns.sh`
**Checks for issues before ingestion.**

```bash
./validate-campaigns.sh
```

Checks for:
- Missing overview files
- Empty files
- Missing title/genre lines
- Bible completeness (NPCs, locations, mechanics)

Outputs: `validation-report.md`

---

### `extract-npcs.sh`
**Pulls all NPCs from campaign bibles into one file.**

```bash
./extract-npcs.sh
```

Outputs: `all-npcs.md` - useful for character reference and consistency checking.

---

### `search-campaigns.sh`
**Find campaigns by keyword/theme.**

```bash
./search-campaigns.sh dragon
./search-campaigns.sh "love potion"
./search-campaigns.sh heist
```

Searches all .md files and shows matching campaigns with context.

---

### `pick-launch-campaigns.sh`
**Generates selection document for launch curation.**

```bash
./pick-launch-campaigns.sh
```

Outputs: `launch-picker.md` - shows all complete campaigns by genre with premises for easy comparison.

---

### `organize-campaigns.sh`
**Sorts campaigns into genre directories based on content.**

```bash
# Dry run
./organize-campaigns.sh

# Actually move
./organize-campaigns.sh false
```

Reads the genre/campaign-type line from overview files and moves to appropriate folder. Used for initial organization - shouldn't need to run again unless adding new campaigns manually.

---

## Typical Workflow

### Daily Check-in (after AI generation runs)
```bash
cd /Users/rob/Claude/workspaces/infinite-realms-clean/campaign-ideas
./stats.sh                    # See progress
./move-completed.sh false     # Move finished to Completed/
./stats.sh                    # Confirm
```

### Before Ingestion
```bash
./validate-campaigns.sh       # Check for issues
./audit-campaigns.sh          # Get detailed breakdown
./extract-npcs.sh             # Pull NPC roster
```

### Finding Specific Content
```bash
./search-campaigns.sh vampire
./search-campaigns.sh underwater
./search-campaigns.sh "cooking magic"
```

### Selecting Launch Campaigns
```bash
./pick-launch-campaigns.sh
# Then review launch-picker.md
```

---

## Launch Campaigns (Selected)

| Genre | Campaign | Slug |
|-------|----------|------|
| Fantasy | A Midsummer Night's Chaos | `a-midsummer-nights-chaos` |
| Horror | Abyssal Descent | `abyssal-descent` |
| Sci-Fi | Wildspace Corsairs | `wildspace-corsairs` |
| Mystery | The Verdant Codex | `the-verdant-codex` |
| Historical | Tides of the Trident Throne | `tides-of-the-trident-throne` |
| Post-Apocalyptic | When Stars Walk | `when-stars-walk` |
| Intrigue | The Eternal Feast | `the-eternal-feast` |
| Urban | The Dark Lord's Day Job | `the-dark-lords-day-job` |
| Adventure | Above the Cloudline | `above-the-cloudline` |

---

## Generated Outputs

| File | Description |
|------|-------------|
| `campaign-audit.csv` | Spreadsheet of all campaigns with status |
| `validation-report.md` | Issues found during validation |
| `all-npcs.md` | Extracted NPCs from all bibles |
| `launch-picker.md` | Selection document for launch curation |
| `organize-log.txt` | Log from organize script |

---

## Notes

- **Bible detection**: Scripts look for `*campaign-bible*.md` files
- **Genre detection**: Reads "Genre" or "Campaign Type" line from first 30 lines of overview
- **Dry run default**: Most destructive scripts default to dry run - pass `false` to execute
- **Gemini CLI**: Used for passive bible generation overnight/during work hours
- **ImageFX/Whisk**: Used for asset generation (free, manual)

---

*Last updated: December 2024*
