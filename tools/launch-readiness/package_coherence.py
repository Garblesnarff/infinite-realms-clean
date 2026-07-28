#!/usr/bin/env python3
"""Detect campaign packages whose files describe DIFFERENT campaigns.

The batch-3 audit found six of ten shortlisted campaigns where the bible was an
original story but the overview / creative-brief / world-building-spec belonged to
a borrowed one (Tarzan, Doc Savage, Initial D, Into the Woods...). The four-file
completeness check passed all of them, because it only counts files.

This compares the proper nouns each file actually uses. A package where the bible
and the overview share almost no names is not one campaign; it is two documents in
one folder, and shipping it means shipping whichever one the ingest pipeline reads.

  python3 package_coherence.py            # ranked worst-first
  python3 package_coherence.py --json
"""
import os, re, sys, json, collections

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'campaign-ideas')
GENRES = ['Fantasy','Horror','Sci-Fi','Mystery','Historical','Post-Apocalyptic',
          'Intrigue','Urban','Adventure']

# Words that are capitalised for grammar or genre reasons, not because they name
# something specific to this campaign. Without this the score is mostly noise.
STOP = set('''The A An And Or But If Then When While As At By For From In Into Of On To With
Act Acts Session Sessions Chapter Part Tier Level Levels Player Players Character Characters
Campaign Bible Overview Brief Spec World Building Creative Genre Tone Theme Themes Setting
Hook Hooks Quest Quests NPC NPCs Location Locations Faction Factions Item Items Monster
Monsters Bestiary Encounter Encounters Combat Skill Ability Abilities HP AC CR DC STR DEX
CON INT WIS CHA Str Dex Con Int Wis Cha Fantasy Horror Mystery Adventure Urban Historical
Intrigue Apocalyptic Sci Fi Epic Dark High Low Medium Short Long One Two Three Four Five
Six Seven Eight Nine Ten Difficulty Easy Hard Deadly Secret Goal Voice Type Leader Name
Description Summary Notes Note Example Prompt Style Art Palette Mood Motif Motifs Key
Primary Secondary Major Minor North South East West God Gods King Queen Lord Lady Captain
Doctor Dr Professor Prof Mr Mrs Ms Sir Saint St Day Night Dawn Dusk Winter Summer Spring
Autumn Fall East West Great Old New First Last Final Grand Deep Red Blue Green Black White
Gold Silver Iron Stone Blood Fire Ice Storm Shadow Light Dark'''.split())

PROPER = re.compile(r'\b([A-Z][a-z]{2,})\b')

def names(text):
    """Proper-noun-ish tokens, minus grammar capitalisation."""
    out = collections.Counter()
    for line in text.split('\n'):
        # drop the first word of each sentence: capitalised by grammar, not meaning
        for m in re.finditer(r'(?<![.!?]\s)(?<!^)' + PROPER.pattern, line):
            w = m.group(1)
            if w not in STOP:
                out[w] += 1
    return out

def packages():
    for g in GENRES:
        for base in (os.path.join(ROOT, 'Completed', g), os.path.join(ROOT, g)):
            if not os.path.isdir(base):
                continue
            for d in sorted(os.listdir(base)):
                p = os.path.join(base, d)
                if os.path.isdir(p):
                    yield g, d, p

def analyse():
    rows = []
    for genre, slug, path in packages():
        fs = [f for f in os.listdir(path)
              if f.endswith('.md') and not f.startswith('._') and '.OLD' not in f]
        bib = [f for f in fs if 'campaign-bible' in f.lower()]
        sup = [f for f in fs if f not in bib]
        if not bib or not sup:
            continue
        btext = open(os.path.join(path, bib[0]), encoding='utf-8', errors='replace').read()
        stext = '\n'.join(open(os.path.join(path, f), encoding='utf-8', errors='replace').read()
                          for f in sup)
        bn, sn = names(btext), names(stext)
        # only names used more than once: a single mention is often incidental
        bset = {w for w, c in bn.items() if c >= 2}
        sset = {w for w, c in sn.items() if c >= 2}
        if len(bset) < 12 or len(sset) < 12:
            continue                     # too little text to judge
        overlap = bset & sset
        # Jaccard against the smaller set: asymmetric doc lengths shouldn't punish
        share = len(overlap) / min(len(bset), len(sset))
        rows.append(dict(
            slug=slug, genre=genre, share=round(share, 3),
            bible_names=len(bset), support_names=len(sset), shared=len(overlap),
            only_bible=sorted(bset - sset, key=lambda w: -bn[w])[:8],
            only_support=sorted(sset - bset, key=lambda w: -sn[w])[:8]))
    return sorted(rows, key=lambda r: r['share'])

def main():
    rows = analyse()
    if '--json' in sys.argv:
        print(json.dumps(rows, indent=2)); return
    print('%-42s %-16s %6s %7s %7s' % ('CAMPAIGN', 'GENRE', 'SHARE', 'BIBLE', 'SUPPORT'))
    for r in rows[:40]:
        print('%-42s %-16s %6.2f %7d %7d' % (
            r['slug'], r['genre'], r['share'], r['bible_names'], r['support_names']))
        print('      bible only : %s' % ', '.join(r['only_bible'][:6]))
        print('      support only: %s' % ', '.join(r['only_support'][:6]))
    print()
    print('  packages compared: %d' % len(rows))
    for lbl, lo, hi in (('severe  (<0.15)', 0, .15), ('suspect (0.15-0.30)', .15, .30),
                        ('ok      (>=0.30)', .30, 9)):
        print('  %-20s %d' % (lbl, sum(1 for r in rows if lo <= r['share'] < hi)))

if __name__ == '__main__':
    main()
