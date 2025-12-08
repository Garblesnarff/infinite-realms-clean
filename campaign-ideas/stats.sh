#!/bin/bash
BASE_DIR="/Users/rob/Claude/workspaces/infinite-realms-clean/campaign-ideas"
GENRES=("Fantasy" "Horror" "Sci-Fi" "Mystery" "Historical" "Post-Apocalyptic" "Intrigue" "Urban" "Adventure")

total=0; bibles=0; frameworks=0

echo ""
echo "=== CAMPAIGN REPOSITORY STATUS ==="
echo ""
printf "%-20s %8s %8s %8s\n" "GENRE" "TOTAL" "COMPLETE" "FRAMEWORK"

for genre in "${GENRES[@]}"; do
    gdir="$BASE_DIR/$genre"; [ -d "$gdir" ] || continue
    gc=0; gb=0; gf=0
    
    for dir in "$gdir"/*/; do
        [ -d "$dir" ] || continue
        ((gc++))
        
        # Check for bible file
        if find "$dir" -maxdepth 1 -name "*campaign-bible*.md" -type f 2>/dev/null | grep -q .; then
            ((gb++))
        elif [ -f "$dir/creative-brief.md" ] && [ -f "$dir/world-building-spec.md" ]; then
            ((gf++))
        fi
    done
    
    [ $gc -gt 0 ] && printf "%-20s %8d %8d %8d\n" "$genre" "$gc" "$gb" "$gf"
    ((total+=gc)); ((bibles+=gb)); ((frameworks+=gf))
done

echo ""
echo "TOTAL: $total campaigns"
echo "  Complete (bible): $bibles"
echo "  Framework: $frameworks"  
echo "  Minimal: $((total - bibles - frameworks))"
