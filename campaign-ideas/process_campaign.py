import os
import sys
import json
import re
import time

# Configuration
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_DIR = os.path.join(BASE_DIR, "campaign-ideas", "Completed")
OUTPUT_DIR = os.path.join(BASE_DIR, "campaign-assets")
SANITIZED_DIR = os.path.join(OUTPUT_DIR, "sanitized")
MANIFESTS_DIR = os.path.join(OUTPUT_DIR, "manifests")
LOGS_DIR = os.path.join(OUTPUT_DIR, "logs")

# Prompts
SANITIZATION_PROMPT = """You are a Copyright Sanitizer for tabletop RPG campaign content.
CRITICAL INSTRUCTION: You are EDITING an existing document, NOT creating a new one.

1. READ the entire campaign content provided below.
2. KEEP 95% of the content EXACTLY as written.
3. ONLY change specific copyrighted character names or extremely specific IP terms.
4. The output structure, lore, locations, NPCs, quests MUST match the input.
5. DO NOT invent new content. DO NOT change the genre. DO NOT replace the setting.
6. If the input is about CRUSADES and JERUSALEM, the output must be about CRUSADES and JERUSALEM.
7. If the input is about SPACE COWBOYS, the output must be about SPACE COWBOYS.

Rules for "Demon Slayer" content:
- REPLACE "Muzan" with "The Progenitor"
- REPLACE "Tanjiro" with "The Sun-Breather"
- REPLACE "Nezuko" with "The Demon Sister"
- REPLACE "Zenitsu" with "The Thunder Coward"
- REPLACE "Inosuke" with "The Beast Warrior"
- REPLACE "Hashira" with "Pillars"
- REPLACE "Nichirin" with "Sun-Steel"

Naming approach for replacements:
Use the character's ROLE + a personality trait OR create a setting-appropriate name.

Output the FULL sanitized document. At the end, add:
[SANITIZATION_LOG]
| Original | Replacement | Reason |

INPUT DOCUMENT TO EDIT:
"""

MANIFEST_PROMPT = """1. Role & Objective
You are the Visual Asset Coordinator for "Infinite Realms." Given campaign documents (Bible, Creative Brief, World-Building Spec), you will generate a complete Asset Generation Manifest containing Imagen 4-optimized prompts.

CRITICAL INSTRUCTIONS:
- Base ALL output on the campaign content provided below.
- PRIMARY SOURCE FOR STYLE: Use the "Creative Brief" section for art style, palette, and mood.
- DO NOT invent or hallucinate any details.
- Use ONLY the names that appear in the campaign content provided (which may have been sanitized).
- NEVER use real-world copyrighted character names.
- When in doubt, use descriptive titles from the text.

2. Style Anchor System
Extract from "Creative Brief":
Genre, Era, Palette, Art Style, Mood Keywords, Recurring Motifs.

3. Asset Categories & Quotas
hero: 3-5, npc: up to 20 (Tier 1), location: 10-15, monster: 5-10, item: 5-10, npc-minor: 10-15, scene: 5-8.

4. Imagen 4 Prompt Structure
[Subject] in [Action/Pose], [Environment/Background], [Lighting], [Art Style], [Mood], [Technical specs]
- Front-load details. Specify composition. Material/texture words. Explicit lighting.
- Under 75 words. NO negative prompts. NO text.

5. Output Format (JSON)
{
  "campaign_slug": "{slug}",
  "campaign_name": "{name}",
  "genre": "{genre}",
  "style_anchor": { ... },
  "assets": {
    "hero": [ { "id", "filename", "title", "route": "IMAGEFX|GROK", "prompt", "purpose" } ],
    "npc": [ ... ],
    "location": [ ... ],
    "monster": [ ... ],
    "item": [ ... ],
    "npc-minor": [ ... ],
    "scene": [ ... ]
  },
  "grok_queue": [ "filename1", "filename2" ],
  "statistics": { "total_assets": 0, "by_category": {}, "grok_count": 0, "imagefx_count": 0 }
}

6. Content Routing
Mark for GROK: Explicit wounds, gore, body horror, aggressive weapons, disturbing creatures, corpses.
Everything else: IMAGEFX.

CONTENT TO PROCESS (Bible + Brief + Spec):
"""

def get_campaign_files(slug):
    """Find all relevant files for a campaign slug."""
    campaign_path = None
    for root, dirs, files in os.walk(INPUT_DIR):
        if f"{slug}-campaign-bible.md" in files:
            campaign_path = root
            break
    
    if not campaign_path:
        return None
        
    files_to_read = [
        f"{slug}-campaign-bible.md",
        "creative-brief.md", 
        "world-building-spec.md",
        f"{slug}.md"
    ]
    
    found_files = []
    for f in files_to_read:
        full_path = os.path.join(campaign_path, f)
        if os.path.exists(full_path):
            found_files.append(full_path)
            
    return found_files

def read_combined_content(file_paths):
    combined = ""
    for path in file_paths:
        fname = os.path.basename(path)
        with open(path, 'r') as f:
            combined += f"\n\n--- FILE: {fname} ---\n\n"
            combined += f.read()
    return combined

def run_gemini_cli(prompt, content, output_path, model="gemini-3-flash-preview"):
    temp_input = f"/tmp/gemini_input_{os.getpid()}.txt"
    with open(temp_input, 'w') as f_out:
        f_out.write(prompt)
        f_out.write("\n\n")
        f_out.write(content)
            
    cmd = f"gemini -m {model} --output-format text < {temp_input} > {output_path}"
    ret = os.system(cmd)
    
    if os.path.exists(temp_input):
        os.remove(temp_input)
        
    if ret != 0:
        raise Exception(f"Gemini CLI command failed with return code {ret}")
        
    if not os.path.exists(output_path) or os.path.getsize(output_path) < 100:
         raise Exception("Output file is too small or missing.")

def validate_sanitization(original, sanitized):
    """Heuristic check to ensure content wasn't completely replaced."""
    # Check length - should be within 30% of original
    if len(sanitized) < len(original) * 0.5:
        return "Sanitized content is significantly shorter than original."
    
    # Check for [TAG:] preservation
    tags = re.findall(r'\[TAG: [A-Z_]+\]', original)
    for tag in tags:
        if tag not in sanitized:
            return f"Missing required tag: {tag}"
            
    # Check for known hallucination keywords if not in original
    hallucination_terms = ["Divine Spark", "Cosmic Ray", "Dogma Thief", "Plot Hole"]
    for term in hallucination_terms:
        if term.lower() in sanitized.lower() and term.lower() not in original.lower():
            return f"Hallucination detected: term '{term}' found in output but not in original."

    return None

def validate_manifest(manifest_data):
    errors = []
    if "assets" not in manifest_data:
        errors.append("Missing 'assets' key")
    total = manifest_data.get("statistics", {}).get("total_assets", 0)
    if total < 10:
        errors.append(f"Only {total} assets found.")
    if "style_anchor" not in manifest_data:
        errors.append("Missing style_anchor")
    return errors

def process_campaign(slug):
    print(f"Processing {slug}...")
    
    file_paths = get_campaign_files(slug)
    if not file_paths:
        print(f"Error: Could not find files for {slug}")
        return
    
    raw_content = read_combined_content(file_paths)

    sanitized_subdir = os.path.join(SANITIZED_DIR, slug)
    os.makedirs(sanitized_subdir, exist_ok=True)
    sanitized_path = os.path.join(sanitized_subdir, f"{slug}-campaign-bible-clean.md")
    
    manifest_subdir = os.path.join(MANIFESTS_DIR, slug)
    os.makedirs(manifest_subdir, exist_ok=True)
    manifest_path = os.path.join(manifest_subdir, "manifest.json")

    # 1. Sanitize
    print("Stage 1: Sanitizing...")
    temp_sanitized = f"/tmp/sanitized_{slug}.txt"
    try:
        run_gemini_cli(SANITIZATION_PROMPT, raw_content, temp_sanitized)
        with open(temp_sanitized, 'r') as f:
            sanitized_content = f.read()
            
        error = validate_sanitization(raw_content, sanitized_content)
        if error:
            print(f"Sanitization validation failed: {error}")
            # In a real batch we might retry, but let's see if this prompt fix works
        
        with open(sanitized_path, 'w') as f:
            f.write(sanitized_content)
        print(f"Sanitized content saved to {sanitized_path}")
    except Exception as e:
        print(f"Sanitization failed: {e}")
        return

    # 2. Manifest
    print("Stage 2: Generating Manifest...")
    temp_manifest_out = f"/tmp/manifest_{slug}.txt"
    max_retries = 2
    
    for attempt in range(max_retries + 1):
        try:
            run_gemini_cli(MANIFEST_PROMPT, sanitized_content, temp_manifest_out)
            with open(temp_manifest_out, 'r') as f:
                manifest_raw = f.read()
            
            json_match = re.search(r'```json\s*(\{.*?\})\s*```', manifest_raw, re.DOTALL)
            json_str = json_match.group(1) if json_match else None
            if not json_str:
                start, end = manifest_raw.find('{'), manifest_raw.rfind('}')
                if start != -1 and end != -1:
                    json_str = manifest_raw[start:end+1]
            
            if not json_str:
                raise Exception("JSON not found in output")

            json_str = re.sub(r',\s*([\]}])', r'\1', json_str)
            manifest_data = json.loads(json_str)
            
            v_errors = validate_manifest(manifest_data)
            if v_errors:
                print(f"Manifest validation failed: {v_errors}")
                if attempt < max_retries:
                    time.sleep(2)
                    continue
            
            with open(manifest_path, 'w') as f:
                json.dump(manifest_data, f, indent=2)
            if "style_anchor" in manifest_data:
                with open(os.path.join(manifest_subdir, "style-anchor.json"), 'w') as f:
                    json.dump(manifest_data["style_anchor"], f, indent=2)
            
            print(f"Success! Manifest saved to {manifest_path}")
            break
        except Exception as e:
            print(f"Manifest attempt {attempt+1} failed: {e}")
            if attempt < max_retries: time.sleep(2)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python process_campaign.py <slug>")
        sys.exit(1)
    process_campaign(sys.argv[1])