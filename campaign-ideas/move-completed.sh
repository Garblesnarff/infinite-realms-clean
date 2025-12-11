#!/bin/bash
# Move completed campaigns (with bibles) to Completed directory

BASE_DIR="/Users/rob/Claude/workspaces/infinite-realms-clean/campaign-ideas"
COMPLETED_DIR="$BASE_DIR/Completed"
GENRES=("Fantasy" "Horror" "Sci-Fi" "Mystery" "Historical" "Post-Apocalyptic" "Intrigue" "Urban" "Adventure")

# Dry run by default
DRY_RUN="${1:-true}"

echo "=== Move Completed Campaigns ==="
echo "Dry Run: $DRY_RUN"
echo ""

# Create Completed directory structure
if [ "$DRY_RUN" == "false" ]; then
    mkdir -p "$COMPLETED_DIR"
    for genre in "${GENRES[@]}"; do
        mkdir -p "$COMPLETED_DIR/$genre"
    done
    echo "Created: $COMPLETED_DIR with genre subdirectories"
    echo ""
fi

moved=0
skipped=0

for genre in "${GENRES[@]}"; do
    genre_dir="$BASE_DIR/$genre"
    [ -d "$genre_dir" ] || continue
    
    for dir in "$genre_dir"/*/; do
        [ -d "$dir" ] || continue
        
        name=$(basename "$dir")
        
        # Check if has bible
        if find "$dir" -maxdepth 1 -name "*campaign-bible*.md" -type f 2>/dev/null | grep -q .; then
            dest="$COMPLETED_DIR/$genre/$name"
            
            # Check if already exists in Completed
            if [ -d "$dest" ]; then
                echo "SKIP: $name (already in Completed/$genre)"
                ((skipped++))
                continue
            fi
            
            if [ "$DRY_RUN" == "false" ]; then
                mv "$dir" "$COMPLETED_DIR/$genre/"
                echo "MOVED: $name -> Completed/$genre"
            else
                echo "WOULD MOVE: $name -> Completed/$genre"
            fi
            ((moved++))
        fi
    done
done

echo ""
echo "=== Summary ==="
echo "Campaigns to move: $moved"
echo "Skipped (already moved): $skipped"

if [ "$DRY_RUN" == "true" ]; then
    echo ""
    echo "This was a DRY RUN. No files moved."
    echo "Run './move-completed.sh false' to actually move."
fi
