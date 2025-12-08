#!/bin/bash

# Campaign Organizer Script
# Organizes campaign directories and files into genre folders

BASE_DIR="/Users/rob/Claude/workspaces/infinite-realms-clean/campaign-ideas"
LOG_FILE="$BASE_DIR/organize-log.txt"

# Genre folders (these should already exist)
GENRES=("Fantasy" "Horror" "Sci-Fi" "Mystery" "Historical" "Post-Apocalyptic" "Intrigue" "Urban" "Adventure")

# Dry run mode - set to "false" to actually move files
DRY_RUN="${1:-true}"

# Clear log
echo "Campaign Organization Log - $(date)" > "$LOG_FILE"
echo "Dry Run: $DRY_RUN" >> "$LOG_FILE"
echo "========================================" >> "$LOG_FILE"

# Counters
moved_dirs=0
moved_files=0
skipped=0
errors=0

# Function to determine genre from content
determine_genre() {
    local content="$1"
    local genre=""
    
    # Convert to lowercase for matching
    local lower_content=$(echo "$content" | tr '[:upper:]' '[:lower:]')
    
    # Check for genre keywords (order matters - more specific first)
    if echo "$lower_content" | grep -qE "horror|gothic|dread|terror|lovecraft|cthulhu|vampire|zombie|undead|nightmare|sanity|madness"; then
        genre="Horror"
    elif echo "$lower_content" | grep -qE "sci-fi|science fiction|space|cyber|android|robot|starship|galaxy|alien|future|dystopia|mech|tech"; then
        genre="Sci-Fi"
    elif echo "$lower_content" | grep -qE "post-apocal|wasteland|fallout|nuclear|survivor|collapse|ruins of civilization"; then
        genre="Post-Apocalyptic"
    elif echo "$lower_content" | grep -qE "mystery|detective|noir|investigation|whodunit|crime|sleuth"; then
        genre="Mystery"
    elif echo "$lower_content" | grep -qE "historical|ancient|medieval|renaissance|victorian|war of|dynasty|empire of|rome|egypt|viking|samurai"; then
        genre="Historical"
    elif echo "$lower_content" | grep -qE "intrigue|political|espionage|conspiracy|court|throne|noble|diplomat|spy"; then
        genre="Intrigue"
    elif echo "$lower_content" | grep -qE "urban|city|modern|contemporary|street|gang|underground"; then
        genre="Urban"
    elif echo "$lower_content" | grep -qE "fantasy|fae|fairy|dragon|magic|wizard|elf|dwarf|orc|kingdom|sword|sorcery|arcane|mythic|enchant"; then
        genre="Fantasy"
    else
        genre="Adventure"  # Default catch-all
    fi
    
    echo "$genre"
}

# Function to check if already in a genre folder
is_in_genre_folder() {
    local path="$1"
    local parent=$(dirname "$path")
    local parent_name=$(basename "$parent")
    
    for genre in "${GENRES[@]}"; do
        if [ "$parent_name" == "$genre" ]; then
            return 0  # true
        fi
    done
    return 1  # false
}

echo ""
echo "=== Campaign Organizer ==="
echo "Dry Run: $DRY_RUN (use './organize-campaigns.sh false' to actually move)"
echo ""

# ============================================
# PART 1: Handle campaign DIRECTORIES
# ============================================
echo "--- Processing Directories ---"

for dir in "$BASE_DIR"/*/; do
    dir_name=$(basename "$dir")
    
    # Skip genre folders, Tools, and hidden directories
    if [[ " ${GENRES[*]} " =~ " ${dir_name} " ]] || [ "$dir_name" == "Tools" ] || [[ "$dir_name" == .* ]]; then
        continue
    fi
    
    # Skip if already in a genre folder
    if is_in_genre_folder "$dir"; then
        continue
    fi
    
    # Find the main overview file
    overview=""
    
    # Try exact match first (directory-name.md)
    if [ -f "$dir/$dir_name.md" ]; then
        overview="$dir/$dir_name.md"
    else
        # Find any .md that's not a supporting file
        for f in "$dir"/*.md; do
            fname=$(basename "$f")
            if [[ "$fname" != "creative-brief.md" && "$fname" != "world-building-spec.md" && "$fname" != *"campaign-bible.md" ]]; then
                overview="$f"
                break
            fi
        done
    fi
    
    if [ -z "$overview" ] || [ ! -f "$overview" ]; then
        echo "  SKIP: $dir_name (no overview file found)"
        echo "SKIP: $dir_name - no overview file" >> "$LOG_FILE"
        ((skipped++))
        continue
    fi
    
    # Read first 50 lines and extract genre info
    content=$(head -50 "$overview")
    genre=$(determine_genre "$content")
    
    # Check if target directory exists
    target_dir="$BASE_DIR/$genre"
    if [ ! -d "$target_dir" ]; then
        echo "  ERROR: Target genre folder doesn't exist: $genre"
        echo "ERROR: $dir_name - genre folder $genre doesn't exist" >> "$LOG_FILE"
        ((errors++))
        continue
    fi
    
    # Check if destination already exists
    if [ -d "$target_dir/$dir_name" ]; then
        echo "  SKIP: $dir_name (already exists in $genre)"
        echo "SKIP: $dir_name - already exists in $genre" >> "$LOG_FILE"
        ((skipped++))
        continue
    fi
    
    # Move or report
    if [ "$DRY_RUN" == "false" ]; then
        mv "$dir" "$target_dir/"
        echo "  MOVED: $dir_name -> $genre"
        echo "MOVED: $dir_name -> $genre" >> "$LOG_FILE"
    else
        echo "  WOULD MOVE: $dir_name -> $genre"
        echo "WOULD MOVE: $dir_name -> $genre" >> "$LOG_FILE"
    fi
    ((moved_dirs++))
done

# ============================================
# PART 2: Handle standalone .md FILES
# ============================================
echo ""
echo "--- Processing Standalone Files ---"

# Create Ideas folder if it doesn't exist
IDEAS_DIR="$BASE_DIR/Ideas-To-Expand"
if [ ! -d "$IDEAS_DIR" ]; then
    if [ "$DRY_RUN" == "false" ]; then
        mkdir -p "$IDEAS_DIR"
        echo "  Created: Ideas-To-Expand folder"
    else
        echo "  WOULD CREATE: Ideas-To-Expand folder"
    fi
fi

for file in "$BASE_DIR"/*.md; do
    [ -f "$file" ] || continue  # Skip if no matches
    
    file_name=$(basename "$file")
    
    # Skip meta files
    if [[ "$file_name" == "README.md" || "$file_name" == "ideas-to-expand.md" || "$file_name" == "organize-log.txt" ]]; then
        continue
    fi
    
    # Read content and determine genre
    content=$(head -50 "$file")
    genre=$(determine_genre "$content")
    
    # Get the campaign name (without .md)
    campaign_name="${file_name%.md}"
    
    # Option 1: Move to genre folder as-is
    # Option 2: Create directory and move file into it
    # Going with Option 1 for now - just move to Ideas-To-Expand
    
    if [ "$DRY_RUN" == "false" ]; then
        mv "$file" "$IDEAS_DIR/"
        echo "  MOVED FILE: $file_name -> Ideas-To-Expand"
        echo "MOVED FILE: $file_name -> Ideas-To-Expand" >> "$LOG_FILE"
    else
        echo "  WOULD MOVE FILE: $file_name -> Ideas-To-Expand (detected genre: $genre)"
        echo "WOULD MOVE FILE: $file_name -> Ideas-To-Expand (genre: $genre)" >> "$LOG_FILE"
    fi
    ((moved_files++))
done

# ============================================
# SUMMARY
# ============================================
echo ""
echo "=== Summary ==="
echo "Directories to move: $moved_dirs"
echo "Files to move: $moved_files"
echo "Skipped: $skipped"
echo "Errors: $errors"
echo ""
echo "Log saved to: $LOG_FILE"

if [ "$DRY_RUN" == "true" ]; then
    echo ""
    echo "This was a DRY RUN. No files were moved."
    echo "Run './organize-campaigns.sh false' to actually move files."
fi
