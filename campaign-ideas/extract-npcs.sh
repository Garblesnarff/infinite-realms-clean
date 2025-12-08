#!/bin/bash
# NPC Extractor - extracts NPCs from campaign bibles only

BASE_DIR="/Users/rob/Claude/workspaces/infinite-realms-clean/campaign-ideas"
OUTPUT_FILE="$BASE_DIR/all-npcs.md"

echo "# NPC Roster - All Campaign Bibles" > "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo "Generated: $(date)" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

total_npcs=0

# Find all campaign bible files
while IFS= read -r bible; do
    # Get campaign name from path
    dir=$(dirname "$bible")
    campaign=$(basename "$dir")
    genre=$(basename "$(dirname "$dir")")
    
    echo "## $campaign ($genre)" >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
    
    # Extract Tier 1 NPCs - numbered lists with **bold names**
    # Pattern: "1.  **Name** ..." or "1. **Name** ..."
    tier1=$(grep -E "^[0-9]+\.\s+\*\*" "$bible" | head -30)
    
    if [ -n "$tier1" ]; then
        echo "### Major NPCs" >> "$OUTPUT_FILE"
        echo "$tier1" >> "$OUTPUT_FILE"
        echo "" >> "$OUTPUT_FILE"
        count1=$(echo "$tier1" | wc -l)
        ((total_npcs += count1))
    fi
    
    # Extract Tier 2 NPCs from tables - look for | **Name** | or | Name |
    # Skip header rows (containing "Name" as header)
    tier2=$(grep -E "^\|[^|]+\|" "$bible" | grep -v "^|:--" | grep -v "| Name |" | grep -v "| ID |" | head -60)
    
    if [ -n "$tier2" ]; then
        # Count table rows (excluding headers)
        count2=$(echo "$tier2" | grep -cE "^\|")
        if [ "$count2" -gt 0 ]; then
            echo "### Minor NPCs (table)" >> "$OUTPUT_FILE"
            echo "$tier2" >> "$OUTPUT_FILE"
            echo "" >> "$OUTPUT_FILE"
            ((total_npcs += count2))
        fi
    fi
    
    echo "---" >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"

done < <(find "$BASE_DIR" -name "*campaign-bible*.md" -type f)

echo "" >> "$OUTPUT_FILE"
echo "**Total NPCs extracted: $total_npcs**" >> "$OUTPUT_FILE"

echo "=== NPC Extraction Complete ==="
echo "Total NPCs: $total_npcs"
echo "Output: $OUTPUT_FILE"
