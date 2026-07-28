#!/usr/bin/env python3
"""Rank campaigns by authored depth, not by parser coverage.

Parser coverage is now near 100% library-wide, so it no longer separates a
strong campaign from a weak one. What separates them is whether a human-grade
bestiary and package were authored, or whether a generator stamped out the same
three creatures with new nouns.

  python3 depth_score.py            # ranked table
  python3 depth_score.py --top 30   # shortlist
  python3 depth_score.py --json     # machine-readable
"""
import os, sys, json, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import irparse

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'campaign-ideas')
GENRES = ['Fantasy','Horror','Sci-Fi','Mystery','Historical','Post-Apocalyptic','Intrigue','Urban','Adventure']
SHIPPED = {  # already on the launch shelf (batches 1 and 2)
 'the-eternal-feast','the-porcelain-court','abyssal-descent','seven-swords-for-hire',
 'the-impossible-vault','academy-of-arcane-gastronomy','the-crimson-thread-of-silverport',
 'murder-on-the-astral-express','the-weather-weavers','wings-of-the-void','clash-of-olympus',
 'chronicles-of-the-somnolent-oracle','ascension-protocol','against-the-titans',
 'way-of-the-fading-blade','the-chosen-slayer','calypsos-death-derby',
 'the-revolutionaries-anthem','the-verdant-codex','see-you-space-cowboy'}
# premises built on a Wizards setting; a rename does not fix these
KNOCKOFFS = {'factions-of-sigil','domains-of-dread','sharn-city-of-towers',
             'wasteland-of-athas','wildspace-corsairs','goldport','deductions-of-baker-street'}
PI = ['beholder','death tyrant','mind flayer','illithid','githyanki','githzerai','yuan-ti',
      'kuo-toa','slaad','umber hulk','displacer beast','carrion crawler','modron',
      'intellect devourer','flumph','froghemoth']   # verified absent from SRD 5.1

def packages():
    for g in GENRES:
        for base in (os.path.join(ROOT,'Completed',g), os.path.join(ROOT,g)):
            if not os.path.isdir(base): continue
            for d in sorted(os.listdir(base)):
                p = os.path.join(base,d)
                if os.path.isdir(p): yield g, d, p

def analyse():
    rows = []
    for genre, slug, path in packages():
        fs = [f for f in os.listdir(path) if f.endswith('.md')
              and not f.startswith('._') and '.OLD' not in f]
        bib = [f for f in fs if 'campaign-bible' in f.lower()]
        if not bib: continue
        text = open(os.path.join(path, bib[0]), encoding='utf-8', errors='replace').read()
        cov = irparse.coverage(text)
        stats = tuple(sorted(
            (irparse.parse_stat_block(c)['maxHp'], irparse.parse_stat_block(c)['armorClass'])
            for _, c in irparse.extract_encounters(text)))
        low = text.lower()
        rows.append(dict(
            slug=slug, genre=genre, path=os.path.relpath(path, ROOT),
            monsters=len(cov), full=sum(1 for _, g in cov if g == 'full'),
            bible_kb=round(len(text)/1024, 1),
            complete=all(any(k in f for f in fs) for k in ('creative-brief','world-building'))
                     and any(f == slug+'.md' or f == 'overview.md' for f in fs),
            pi=[n for n in PI if n in low],
            knockoff=slug in KNOCKOFFS, shipped=slug in SHIPPED, sig=stats))
    # a stat signature shared by many campaigns means a generator template, not authorship
    freq = collections.Counter(r['sig'] for r in rows)
    for r in rows:
        r['clone_peers'] = freq[r['sig']] - 1
        s  = min(r['monsters'], 12) * 6                 # authored depth, capped
        s += min(r['bible_kb'], 60) * 0.5               # written substance
        s += 12 if r['complete'] else 0                 # whole package
        s -= 40 if r['clone_peers'] >= 4 else 0         # template clone
        s -= 10 * len(r['pi'])                          # rename work outstanding
        s -= 60 if r['knockoff'] else 0                 # cannot ship at all
        r['score'] = round(s, 1)
    return sorted(rows, key=lambda r: -r['score'])

def main():
    rows = analyse()
    if '--json' in sys.argv:
        print(json.dumps(rows, indent=2)); return
    top = int(sys.argv[sys.argv.index('--top')+1]) if '--top' in sys.argv else len(rows)
    avail = [r for r in rows if not r['shipped'] and not r['knockoff']]
    print('%-42s %-16s %5s %4s %6s %6s  %s' %
          ('CAMPAIGN','GENRE','SCORE','MONS','BIBLEkB','CLONES','FLAGS'))
    for r in avail[:top]:
        flags = []
        if r['pi']: flags.append('PI:'+','.join(r['pi']))
        if not r['complete']: flags.append('incomplete-package')
        if r['clone_peers'] >= 4: flags.append('template-clone')
        print('%-42s %-16s %5.1f %4d %6.1f %6d  %s' %
              (r['slug'], r['genre'], r['score'], r['monsters'],
               r['bible_kb'], r['clone_peers'], ' '.join(flags)))
    print()
    print('  bibles ranked:        %d' % len(rows))
    print('  already shipped:      %d' % sum(1 for r in rows if r['shipped']))
    print('  setting knockoffs:    %d' % sum(1 for r in rows if r['knockoff']))
    print('  template clones:      %d' % sum(1 for r in rows if r['clone_peers'] >= 4))
    print('  clean and available:  %d' % sum(
        1 for r in avail if r['clone_peers'] < 4 and not r['pi'] and r['complete']))

if __name__ == '__main__':
    main()
