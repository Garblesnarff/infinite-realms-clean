#!/bin/bash
# Campaign Stats - counts both Completed and In-Progress campaigns

BASE_DIR="/Users/rob/Claude/workspaces/infinite-realms-clean/campaign-ideas"
COMPLETED_DIR="$BASE_DIR/Completed"
GENRES=("Fantasy" "Horror" "Sci-Fi" "Mystery" "Historical" "Post-Apocalyptic" "Intrigue" "Urban" "Adventure")

echo ""
echo "╔══════════════════════════════════════════════════════════╗"
echo "║           INFINITE REALMS CAMPAIGN REPOSITORY            ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""

total_complete=0
total_framework=0

printf "%-20s %10s %10s %10s\n" "GENRE" "COMPLETE" "FRAMEWORK" "TOTAL"
printf "%-20s %10s %10s %10s\n" "--------------------" "----------" "----------" "----------"

for genre in "${GENRES[@]}"; do
    complete=0
    framework=0
    
    # Count completed (in Completed directory)
    if [ -d "$COMPLETED_DIR/$genre" ]; then
        for dir in "$COMPLETED_DIR/$genre"/*/; do
            [ -d "$dir" ] && ((complete++))
        done
    fi
    
    # Count in-progress (in main genre directory)
    genre_dir="$BASE_DIR/$genre"
    if [ -d "$genre_dir" ]; then
        for dir in "$genre_dir"/*/; do
            [ -d "$dir" ] || continue
            
            # Check if has bible (shouldn't after move, but just in case)
            if find "$dir" -maxdepth 1 -name "*campaign-bible*.md" -type f 2>/dev/null | grep -q .; then
                ((complete++))
            else
                ((framework++))
            fi
        done
    fi
    
    genre_total=$((complete + framework))
    
    if [ $genre_total -gt 0 ]; then
        printf "%-20s %10d %10d %10d\n" "$genre" "$complete" "$framework" "$genre_total"
    fi
    
    ((total_complete += complete))
    ((total_framework += framework))
done

total=$((total_complete + total_framework))

printf "%-20s %10s %10s %10s\n" "--------------------" "----------" "----------" "----------"
printf "%-20s %10d %10d %10d\n" "TOTAL" "$total_complete" "$total_framework" "$total"

echo ""
echo "📊 Repository Status:"
echo "   ✅ Complete (with bible): $total_complete"
echo "   📋 Frameworks (need bible): $total_framework"

# Calculate percentage
if [ $total -gt 0 ]; then
    pct=$((total_complete * 100 / total))
    echo "   📈 Progress: $pct%"
fi

echo ""

# Ideas folder count
if [ -d "$BASE_DIR/Ideas-To-Expand" ]; then
    ideas_count=$(find "$BASE_DIR/Ideas-To-Expand" -maxdepth 1 -name "*.md" -type f 2>/dev/null | wc -l | tr -d ' ')
    ideas_dirs=$(find "$BASE_DIR/Ideas-To-Expand" -maxdepth 1 -type d 2>/dev/null | wc -l | tr -d ' ')
    ideas_dirs=$((ideas_dirs - 1))  # Subtract the directory itself
    echo "   💡 Raw ideas: $ideas_count files, $ideas_dirs folders"
    echo ""
fi

echo "📦 Ingestion Ready:"
echo "   Campaigns in Completed/: $total_complete"
echo "   Est. chunks: ~$((total_complete * 50))"
echo ""
