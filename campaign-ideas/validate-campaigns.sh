#!/bin/bash
# Campaign Validation - checks for issues before ingestion

BASE_DIR="/Users/rob/Claude/workspaces/infinite-realms-clean/campaign-ideas"
GENRES=("Fantasy" "Horror" "Sci-Fi" "Mystery" "Historical" "Post-Apocalyptic" "Intrigue" "Urban" "Adventure")
REPORT="$BASE_DIR/validation-report.md"

echo "# Validation Report" > "$REPORT"
echo "Generated: $(date)" >> "$REPORT"
echo "" >> "$REPORT"

errors=0; warnings=0

for genre in "${GENRES[@]}"; do
    gdir="$BASE_DIR/$genre"; [ -d "$gdir" ] || continue
    
    genre_issues=""
    
    for dir in "$gdir"/*/; do
        [ -d "$dir" ] || continue
        name=$(basename "$dir")
        issues=""
        
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
        
        # Check overview
        if [ -z "$overview" ] || [ ! -f "$overview" ]; then
            issues+="  - ERROR: Missing overview file\n"
            ((errors++))
        elif [ ! -s "$overview" ]; then
            issues+="  - ERROR: Overview is empty\n"
            ((errors++))
        else
            # Check for key sections
            if ! head -10 "$overview" | grep -q "^# "; then
                issues+="  - WARN: Missing title\n"
                ((warnings++))
            fi
            if ! grep -qi "genre\|campaign type" "$overview"; then
                issues+="  - WARN: Missing genre line\n"
                ((warnings++))
            fi
        fi
        
        # Check if bible exists - validate its content
        bible=$(find "$dir" -maxdepth 1 -name "*campaign-bible*.md" -type f 2>/dev/null | head -1)
        if [ -f "$bible" ]; then
            if ! grep -qi "npc\|character" "$bible"; then
                issues+="  - WARN: Bible missing NPC section\n"
                ((warnings++))
            fi
            if ! grep -qi "location\|zone" "$bible"; then
                issues+="  - WARN: Bible missing locations\n"
                ((warnings++))
            fi
        fi
        
        if [ -n "$issues" ]; then
            genre_issues+="### $name\n$issues\n"
        fi
    done
    
    if [ -n "$genre_issues" ]; then
        echo "## $genre" >> "$REPORT"
        echo "" >> "$REPORT"
        echo -e "$genre_issues" >> "$REPORT"
    fi
done

echo "---" >> "$REPORT"
echo "## Summary" >> "$REPORT"
echo "- Errors: $errors" >> "$REPORT"
echo "- Warnings: $warnings" >> "$REPORT"

echo "=== Validation Complete ==="
echo "Errors: $errors"
echo "Warnings: $warnings"
echo "Report: $REPORT"
