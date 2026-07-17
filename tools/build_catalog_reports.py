#!/usr/bin/env python3
"""Generate additive inventory reports from catalog/campaigns.json."""
import json
from collections import Counter, defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; CAT=ROOT/'catalog'
rows=json.loads((CAT/'campaigns.json').read_text())
repo=[r for r in rows if r['source']=='GitHub']; ideas=[r for r in rows if r['source']=='Ideas sheet']
groups=defaultdict(list)
for r in repo: groups[r['slug']].append(r)
dupes={k:v for k,v in groups.items() if len(v)>1}

audit=['# Campaign Audit','',f'- GitHub packages inspected: **{len(repo)}**',f'- Ideas-sheet concepts reconciled: **{len(ideas)}**',f'- Total catalog records: **{len(rows)}**',f'- Packages under `Completed`: **{sum(r["status_directory"]=="Completed" for r in repo)}**',f'- Packages outside `Completed`: **{sum(r["status_directory"]!="Completed" for r in repo)}**',f'- Exact-slug duplicate groups: **{len(dupes)}**','','Every Markdown file was included in the structural inventory. Text-derived fields are conservative signals and preserve audit confidence. `Completed` placement is not treated as readiness evidence.','', '## Categories','']
audit += [f'- {k}: {v}' for k,v in sorted(Counter(r['category'] for r in repo).items())]
(CAT/'campaign-audit.md').write_text('\n'.join(audit)+'\n')

lines=['# Duplicate Review','','Candidates only. Nothing was merged, moved, or deleted.','']
for slug,rs in sorted(dupes.items()):
 lines += [f'## {slug}','']+[f'- `{r["github_path"]}` — score {r["readiness_score"]}' for r in rs]+['']
(CAT/'duplicate-review.md').write_text('\n'.join(lines))

ip=[r for r in repo if r['ip_status']=='Needs transformation']
lines=['# IP / Commercial-Safety Review','','Automated triage only; obtain legal/editorial review before commercial release.','']+[f'- **{r["title"]}** — {r["ip_notes"]} — `{r["github_path"]}`' for r in ip]
(CAT/'ip-review.md').write_text('\n'.join(lines)+'\n')

lines=['# Sheet-Only Ideas','','No sheet row was merged automatically with a GitHub package.','']+[f'- **{r["title"]}** — {r["duplicate_status"]}' for r in ideas]
(CAT/'sheet-only-ideas.md').write_text('\n'.join(lines)+'\n')

idx=['# Campaign Index','',f'- GitHub packages: **{len(repo)}**',f'- Ideas concepts: **{len(ideas)}**',f'- Total records: **{len(rows)}**','','## Length distribution','']+[f'- {k}: {v}' for k,v in sorted(Counter(r['normalized_length'] for r in repo).items())]
(CAT/'campaign-index.md').write_text('\n'.join(idx)+'\n')

