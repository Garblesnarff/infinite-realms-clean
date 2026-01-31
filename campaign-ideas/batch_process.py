import os
import subprocess
import time
import sys

BASE_DIR = "/Users/rob/Claude/workspaces/infinite-realms-clean"
INPUT_DIR = os.path.join(BASE_DIR, "campaign-ideas", "Completed")
OUTPUT_DIR = os.path.join(BASE_DIR, "campaign-assets")
MANIFESTS_DIR = os.path.join(OUTPUT_DIR, "manifests")
SCRIPT_PATH = os.path.join(BASE_DIR, "campaign-ideas", "process_campaign.py")

def get_all_campaigns():
    campaigns = []
    for root, dirs, files in os.walk(INPUT_DIR):
        for file in files:
            if file.endswith("-campaign-bible.md"):
                # Extract slug: {slug}-campaign-bible.md
                slug = file.replace("-campaign-bible.md", "")
                campaigns.append(slug)
    return sorted(list(set(campaigns)))

def get_processed_campaigns():
    if not os.path.exists(MANIFESTS_DIR):
        return []
    return [d for d in os.listdir(MANIFESTS_DIR) if os.path.isdir(os.path.join(MANIFESTS_DIR, d))]

def run_batch(limit=None):
    all_campaigns = get_all_campaigns()
    processed = get_processed_campaigns()
    
    to_process = [c for c in all_campaigns if c not in processed]
    
    print(f"Total campaigns found: {len(all_campaigns)}")
    print(f"Already processed: {len(processed)}")
    print(f"Remaining to process: {len(to_process)}")
    
    if limit:
        to_process = to_process[:limit]
        print(f"Limited to first {limit} campaigns.")

    count = 0
    for slug in to_process:
        count += 1
        print(f"\n--- [{count}/{len(to_process)}] Processing: {slug} ---")
        
        try:
            # We call the script as a subprocess to keep memory clean and handle crashes
            result = subprocess.run([sys.executable, SCRIPT_PATH, slug], capture_output=True, text=True)
            print(result.stdout)
            if result.stderr:
                print(f"Errors:\n{result.stderr}")
        except Exception as e:
            print(f"Failed to launch process for {slug}: {e}")
            
        # Inter-campaign delay to respect rate limits
        # gemini-3-flash-preview usually has generous limits but sequential processing is safer
        print("Waiting 10 seconds before next campaign...")
        time.sleep(10)

if __name__ == "__main__":
    # Optional: pass a number to limit the run (e.g. python3 batch_process.py 5)
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else None
    run_batch(limit)
