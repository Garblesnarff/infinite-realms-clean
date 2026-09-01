#!/usr/bin/env python3
import json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; rows=json.loads((ROOT/'catalog/campaigns.json').read_text()); errors=[]
for i,r in enumerate(rows,2):
 for k in ['campaign_id','title','slug','source','readiness_score','audit_confidence']:
  if r.get(k,'') in ('',None): errors.append(f'row {i}: missing {k}')
 try:
  if not 0<=int(r['readiness_score'])<=100: errors.append(f'row {i}: invalid score')
 except: errors.append(f'row {i}: nonnumeric score')
for p in (ROOT/'catalog/examples').glob('*.yaml'):
 for k in ['id','title','slug','status','genre','source','documents','ingestion_status','readiness','last_audited']:
  if not re.search(rf'(?m)^{k}:',p.read_text()): errors.append(f'{p}: missing {k}')
if errors: print('\n'.join(errors));sys.exit(1)
print(f'validated {len(rows)} catalog records')

