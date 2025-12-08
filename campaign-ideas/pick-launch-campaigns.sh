#!/bin/bash
# Campaign Picker - shows complete campaigns by genre for launch selection

BASE_DIR="/Users/rob/Claude/workspaces/infinite-realms-clean/campaign-ideas"
GENRES=("Fantasy" "Horror" "Sci-Fi" "Mystery" "Historical" "Post-Apocalyptic" "Intrigue" "Urban" "Adventure")
OUTPUT="$BASE_DIR/launch-picker.md"

echo "# Launch Campaign Picker" > "$OUTPUT"
echo "" >> "$OUTPUT"
echo "**Pick 1 from each genre for your 9-campaign launch.**" >> "$OUTPUT"
echo "" >> "$OUTPUT"
echo "Generated: $(date)" >> "$OUTPUT"
echo "" >> "$OUTPUT"

for genre in "${GENRES[@]}"; do
    gdir="$BASE_DIR/$genre"
    [ -d "$gdir" ] || continue
    
    echo "---" >> "$OUTPUT"
    echo "" >> "$OUTPUT"
    echo "## $genre" >> "$OUTPUT"
    echo "" >> "$OUTPUT"
    
    count=0
    
    for dir in "$gdir"/*/; do
        [ -d "$dir" ] || continue
        
        # Check if has bible
        if ! find "$dir" -maxdepth 1 -name "*campaign-bible*.md" -type f 2>/dev/null | grep -q .; then
            continue
        fi
        
        ((count++))
        name=$(basename "$dir")
        
        # Find overview file
        overview=""
        if [ -f "$dir/$name.md" ]; then
            overview="$dir/$name.md"
        else
            for f in "$dir"/*.md; do
                fname=$(basename "$f")
                if [[ "$fname" != "creative-brief.md" && "$fname" != "world-building-spec.md" && "$fname" != *"campaign-bible"* ]]; then
                    overview="$f"
                    break
                fi
            done
        fi
        
        echo "### $count. $name" >> "$OUTPUT"
        echo "" >> "$OUTPUT"
        
        if [ -f "$overview" ]; then
            # Extract title (first # line)
            title=$(grep "^# " "$overview" | head -1 | sed 's/^# //')
            [ -n "$title" ] && echo "**Title:** $title" >> "$OUTPUT"
            
            # Extract genre/tone line
            genre_line=$(head -30 "$overview" | grep -i "genre\|tone\|campaign type" | head -1)
            [ -n "$genre_line" ] && echo "$genre_line" >> "$OUTPUT"
            
            # Extract premise - look for "Core Premise" or "Premise" section
            premise=$(awk '/[Cc]ore [Pp]remise|^## Premise|^\*\*Premise/,/^##|^---|^\*\*[A-Z]/' "$overview" | grep -v "^##" | grep -v "^---" | head -5)
            
            if [ -z "$premise" ]; then
                # Fallback: grab first paragraph after title
                premise=$(awk 'NR>3 && /^[A-Z]/' "$overview" | head -3)
            fi
            
            if [ -n "$premise" ]; then
                echo "" >> "$OUTPUT"
                echo "$premise" >> "$OUTPUT"
            fi
            
            # Extract unique mechanics if present
            mechanics=$(grep -i "unique mechanic\|special system\|core mechanic" "$overview" | head -2)
            if [ -n "$mechanics" ]; then
                echo "" >> "$OUTPUT"
                echo "*Mechanics:* $mechanics" >> "$OUTPUT"
            fi
        else
            echo "*No overview file found*" >> "$OUTPUT"
        fi
        
        echo "" >> "$OUTPUT"
        echo "📁 \`$name\`" >> "$OUTPUT"
        echo "" >> "$OUTPUT"
    done
    
    if [ $count -eq 0 ]; then
        echo "*No complete campaigns in this genre*" >> "$OUTPUT"
        echo "" >> "$OUTPUT"
    fi
done

echo "---" >> "$OUTPUT"
echo "" >> "$OUTPUT"
echo "## Your Selections" >> "$OUTPUT"
echo "" >> "$OUTPUT"
echo "| Genre | Selected Campaign |" >> "$OUTPUT"
echo "|-------|-------------------|" >> "$OUTPUT"
for genre in "${GENRES[@]}"; do
    echo "| $genre | _______________ |" >> "$OUTPUT"
done

echo "" >> "$OUTPUT"
echo "---" >> "$OUTPUT"
echo "*After selecting, these 9 campaigns will be ingested into the Lore Keeper.*" >> "$OUTPUT"

echo "=== Launch Picker Generated ==="
echo "Output: $OUTPUT"
echo ""
echo "Open it with: cat $OUTPUT"
echo "Or view in your editor for easier reading"
