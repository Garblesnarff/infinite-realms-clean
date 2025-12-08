#!/bin/bash
BASE_DIR="/Users/rob/Claude/workspaces/infinite-realms-clean/campaign-ideas"
GENRES=("Fantasy" "Horror" "Sci-Fi" "Mystery" "Historical" "Post-Apocalyptic" "Intrigue" "Urban" "Adventure")
CSV_FILE="$BASE_DIR/campaign-audit.csv"

echo "campaign,genre,status" > "$CSV_FILE"

complete=0; framework=0; minimal=0

for genre in "${GENRES[@]}"; do
    gdir="$BASE_DIR/$genre"; [ -d "$gdir" ] || continue
    
    for dir in "$gdir"/*/; do
        [ -d "$dir" ] || continue
        name=$(basename "$dir")
        
        if find "$dir" -maxdepth 1 -name "*campaign-bible*.md" -type f 2>/dev/null | grep -q .; then
            echo "$name,$genre,COMPLETE" >> "$CSV_FILE"
            ((complete++))
        elif [ -f "$dir/creative-brief.md" ] && [ -f "$dir/world-building-spec.md" ]; then
            echo "$name,$genre,FRAMEWORK" >> "$CSV_FILE"
            ((framework++))
        else
            echo "$name,$genre,MINIMAL" >> "$CSV_FILE"
            ((minimal++))
        fi
    done
done

echo "=== AUDIT COMPLETE ==="
echo "Complete: $complete"
echo "Framework: $framework"
echo "Minimal: $minimal"
echo ""
echo "Launch-ready campaigns:"
grep ",COMPLETE" "$CSV_FILE" | cut -d',' -f1,2
