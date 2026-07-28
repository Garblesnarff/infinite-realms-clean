import os
import json
import re
import csv
import io

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "campaign-assets")
SANITIZED_DIR = os.path.join(OUTPUT_DIR, "sanitized")
MANIFESTS_DIR = os.path.join(OUTPUT_DIR, "manifests")
LOGS_DIR = os.path.join(OUTPUT_DIR, "logs")

def aggregate_sanitization_logs():
    all_logs = []
    
    if not os.path.exists(SANITIZED_DIR):
        print("No sanitized directory found.")
        return

    for campaign_slug in os.listdir(SANITIZED_DIR):
        campaign_dir = os.path.join(SANITIZED_DIR, campaign_slug)
        if not os.path.isdir(campaign_dir):
            continue
            
        # Find clean file
        clean_file = os.path.join(campaign_dir, f"{campaign_slug}-campaign-bible-clean.md")
        if not os.path.exists(clean_file):
            continue
            
        with open(clean_file, 'r') as f:
            content = f.read()
            
        # Extract Log Table
        # Look for [SANITIZATION_LOG] followed by a table
        match = re.search(r'\[SANITIZATION_LOG\]\s*([\s\S]*)', content)
        if match:
            table_text = match.group(1).strip()
            # Simple markdown table parser
            rows = table_text.split('\n')
            # Skip header row (usually starts with | Original | ...)
            # And separator row (|---|...)
            
            for row in rows:
                if not row.strip().startswith('|'):
                    continue
                if 'Original' in row and 'Replacement' in row:
                    continue
                if '---' in row:
                    continue
                
                parts = [p.strip() for p in row.split('|') if p.strip()]
                if len(parts) >= 3:
                    all_logs.append({
                        "campaign": campaign_slug,
                        "original": parts[0],
                        "replacement": parts[1],
                        "reason": parts[2] if len(parts) > 2 else ""
                    })

    # Write to JSON
    os.makedirs(LOGS_DIR, exist_ok=True)
    with open(os.path.join(LOGS_DIR, "sanitization-log.json"), 'w') as f:
        json.dump(all_logs, f, indent=2)
    print(f"Aggregated {len(all_logs)} sanitization entries.")

def aggregate_manifest_logs():
    manifest_stats = []
    
    if not os.path.exists(MANIFESTS_DIR):
        print("No manifests directory found.")
        return

    for campaign_slug in os.listdir(MANIFESTS_DIR):
        campaign_dir = os.path.join(MANIFESTS_DIR, campaign_slug)
        if not os.path.isdir(campaign_dir):
            continue
            
        manifest_file = os.path.join(campaign_dir, "manifest.json")
        if not os.path.exists(manifest_file):
            continue
            
        try:
            with open(manifest_file, 'r') as f:
                data = json.load(f)
                
            stats = data.get("statistics", {})
            manifest_stats.append({
                "campaign": campaign_slug,
                "statistics": stats,
                "grok_queue_size": len(data.get("grok_queue", []))
            })
        except Exception as e:
            print(f"Error reading manifest for {campaign_slug}: {e}")

    # Write to JSON
    with open(os.path.join(LOGS_DIR, "manifest-log.json"), 'w') as f:
        json.dump(manifest_stats, f, indent=2)
    print(f"Aggregated stats for {len(manifest_stats)} manifests.")

if __name__ == "__main__":
    aggregate_sanitization_logs()
    aggregate_manifest_logs()
