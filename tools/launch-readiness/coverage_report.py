#!/usr/bin/env python3
"""Library-wide parser coverage for campaign bibles.

Mirrors production `extractEncounters` (lore-keeper chunker) + `parseAuthoredStatBlock`
/ `gradeCoverage` (server-bun combat). Verified to reproduce the TypeScript results
exactly on all 20 launch-batch campaigns.

  python3 coverage_report.py            # per-campaign table
  python3 coverage_report.py --summary  # totals only
  python3 coverage_report.py --failing  # only campaigns with unparsed monsters
"""
import os, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import irparse

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'campaign-ideas')

def bibles():
    for dp, dn, fn in os.walk(ROOT):
        for f in sorted(fn):
            if ('campaign-bible' in f.lower() and f.endswith('.md')
                    and not f.startswith('._') and '.OLD' not in f):
                yield os.path.join(dp, f)

def main():
    summary = '--summary' in sys.argv
    failing_only = '--failing' in sys.argv
    tot = full = 0
    allfull = nomonsters = 0
    rows = []
    for p in bibles():
        text = open(p, encoding='utf-8', errors='replace').read()
        res = irparse.coverage(text)
        f = sum(1 for _, g in res if g == 'full')
        tot += len(res); full += f
        if not res: nomonsters += 1
        elif f == len(res): allfull += 1
        rows.append((os.path.basename(os.path.dirname(p)), f, len(res)))
    if not summary:
        for name, f, n in rows:
            if failing_only and (n and f == n): continue
            flag = '  ok' if n and f == n else ('  NO MONSTERS' if not n else '  PARTIAL')
            print('  %-48s %2d/%-2d%s' % (name, f, n, flag))
        print()
    print('   bibles scanned:        %d' % len(rows))
    print('   fully parsing:         %d' % allfull)
    print('   no extractable monsters: %d' % nomonsters)
    print('   monster blocks:        %d   grading FULL: %d (%.1f%%)'
          % (tot, full, 100.0 * full / tot if tot else 0))

if __name__ == '__main__':
    main()
