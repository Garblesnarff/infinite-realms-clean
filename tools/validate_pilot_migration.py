#!/usr/bin/env python3
import csv, re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
errors=[]
for row in csv.DictReader((ROOT/'catalog/path-migrations.csv').open()):
    new=ROOT/row['new_path']
    if not new.exists(): errors.append(f"missing destination: {row['new_path']}")
    if row['old_path'] and (ROOT/row['old_path']).exists(): errors.append(f"old path still exists: {row['old_path']}")
for y in list((ROOT/'campaigns').glob('*/campaign.yaml'))+list((ROOT/'ideas/expansion-queue').glob('*/campaign.yaml')):
    text=y.read_text()
    for key in ['id','title','slug','status','genre','source','documents','ingestion_status','readiness','last_audited']:
        if not re.search(rf'(?m)^{key}:',text): errors.append(f'{y}: missing {key}')
if errors: print('\n'.join(errors));sys.exit(1)
print('pilot migration paths and metadata validated')
