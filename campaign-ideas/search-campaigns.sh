#!/bin/bash

# Campaign Search Script
# Find campaigns by keyword/theme

BASE_DIR="/Users/rob/Claude/workspaces/infinite-realms-clean/campaign-ideas"
GENRES=("Fantasy" "Horror" "Sci-Fi" "Mystery" "Historical" "Post-Apocalyptic" "Intrigue" "Urban" "Adventure")

if [ -z "$1" ]; then
    echo "Usage: ./search-campaigns.sh <keyword>"
    echo ""
    echo "Examples:"
    echo "  ./search-campaigns.sh dragon"
    echo "  ./search-campaigns.sh 'love potion'"
    echo "  ./search-campaigns.sh vampire"
    echo "  ./search-campaigns.sh heist"
    exit 1
fi

KEYWORD="$1"
echo "=== Searching for: $KEYWORD ==="
echo ""

found=0

for genre in "${GENRES[@]}"; do
    genre_dir="$BASE_DIR/$genre"
    [ -d "$genre_dir" ] || continue
    
    for dir in "$genre_dir"/*/; do
        [ -d "$dir" ] || continue
        
        dir_name=$(basename "$dir")
        
        # Search all .md files in the campaign
        if grep -rli "$KEYWORD" "$dir"/*.md 2>/dev/null > /dev/null; then
            # Get the title from the overview
            overview=$(find "$dir" -maxdepth 1 -name "*.md" ! -name "creative-brief.md" ! -name "world-building-spec.md" ! -name "*campaign-bible.md" | head -1)
            
            if [ -f "$overview" ]; then
                title=$(head -5 "$overview" | grep "^# " | head -1 | sed 's/^# //')
                [ -z "$title" ] && title="$dir_name"
            else
                title="$dir_name"
            fi
            
            # Check if it has a bible
            if ls "$dir"/*campaign-bible*.md 2>/dev/null | head -1 > /dev/null 2>&1; then
                status="✅"
            else
                status="📋"
            fi
            
            echo "$status $title"
            echo "   Genre: $genre"
            echo "   Path: $dir"
            
            # Show matching context
            echo "   Matches:"
            grep -rhi "$KEYWORD" "$dir"/*.md 2>/dev/null | head -3 | sed 's/^/      /'
            echo ""
            
            ((found++))
        fi
    done
done

echo "=== Found $found campaigns matching '$KEYWORD' ==="
