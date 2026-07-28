#!/bin/bash
# Campaign Stats — counts packages by completeness and reports parser coverage.
# Path is derived from the script's own location so it works from any checkout.

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
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

    # Completed/<genre>/* — a package counts as complete only if it really has a bible
    if [ -d "$COMPLETED_DIR/$genre" ]; then
        for dir in "$COMPLETED_DIR/$genre"/*/; do
            [ -d "$dir" ] || continue
            if find "$dir" -maxdepth 1 -name "*campaign-bible*.md" -type f 2>/dev/null | grep -q .; then
                ((complete++))
            else
                ((framework++))
            fi
        done
    fi

    # In-progress genre folder
    genre_dir="$BASE_DIR/$genre"
    if [ -d "$genre_dir" ]; then
        for dir in "$genre_dir"/*/; do
            [ -d "$dir" ] || continue
            if find "$dir" -maxdepth 1 -name "*campaign-bible*.md" -type f 2>/dev/null | grep -q .; then
                ((complete++))
            else
                ((framework++))
            fi
        done
    fi

    genre_total=$((complete + framework))
    [ $genre_total -gt 0 ] && printf "%-20s %10d %10d %10d\n" "$genre" "$complete" "$framework" "$genre_total"

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
if [ $total -gt 0 ]; then
    echo "   📈 Progress: $((total_complete * 100 / total))%"
fi
echo ""

if [ -d "$BASE_DIR/Ideas-To-Expand" ]; then
    ideas_count=$(find "$BASE_DIR/Ideas-To-Expand" -maxdepth 1 -name "*.md" -type f 2>/dev/null | wc -l | tr -d ' ')
    ideas_dirs=$(( $(find "$BASE_DIR/Ideas-To-Expand" -maxdepth 1 -type d 2>/dev/null | wc -l | tr -d ' ') - 1 ))
    echo "   💡 Raw ideas: $ideas_count files, $ideas_dirs folders"
    echo ""
fi

# Parser coverage — the metric that decides whether monsters fight at authored stats.
COV="$BASE_DIR/../tools/launch-readiness/coverage_report.py"
if [ -f "$COV" ] && command -v python3 >/dev/null 2>&1; then
    echo "🎲 Parser coverage (production chunker + authored-stat-block-parser):"
    python3 "$COV" --summary
    echo ""
fi

echo "📦 Ingestion Ready:"
echo "   Campaigns with bibles: $total_complete"
echo "   Est. chunks: ~$((total_complete * 50))"
echo ""
