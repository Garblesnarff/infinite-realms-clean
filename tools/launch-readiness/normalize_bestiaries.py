"""Mechanically reshape campaign bible bestiaries to the production chunker + parser contract.

HARD RULE: never invent a number. Only relabel/reposition numbers the author already wrote.
An entry missing HP or AC is left untouched and reported.

Target shape (what production extractEncounters + parseAuthoredStatBlock require):
    ## Bestiary                      <- section anchor extract_section() can find
    ### <n>. <Name> (CR <x>)         <- monster header
    ... **HP:** <n> ... **AC:** <n>  <- labelled stats
"""
import re, os, sys

TAG_RE   = re.compile(r'`?\[TAG:\s*ENEMY_STATBLOCK\s*\]`?', re.I)
NEXTTAG  = re.compile(r'`?\[TAG:\s*[A-Z_]+\s*\]`?')
HEAD_RE  = re.compile(r'^#{1,4}[^\n]*(bestiar|custom stat block|unique monster)[^\n]*$', re.I | re.M)

def find_region(text):
    """Return (start, end) of the statblock region, or None."""
    m = TAG_RE.search(text)
    if m:
        start = m.end()
        nxt = NEXTTAG.search(text, start)
        return (start, nxt.start() if nxt else len(text))
    m = HEAD_RE.search(text)
    if m:
        start = m.end()
        nxt = re.compile(r'^##\s', re.M).search(text, start)
        return (start, nxt.start() if nxt else len(text))
    return None

# --- entry splitting -------------------------------------------------------
H_HDR = re.compile(r'^(#{3,4})\s*(\d{1,2})[\.\)]\s*(.+?)\s*$', re.M)   # ### 1. Name
L_HDR = re.compile(r'^\s*(\d{1,2})[\.\)]\s+\*\*(.+?)\*\*\s*(.*)$', re.M)  # 1. **Name** rest

def split_entries(region):
    """Yield (kind, match) for each monster entry header, in document order."""
    hs = [('h', m) for m in H_HDR.finditer(region)]
    if hs:
        return hs
    return [('l', m) for m in L_HDR.finditer(region)]

CR_RE = re.compile(r'\(?\bCR\s*:?\s*(\d{1,2}(?:\s*/\s*\d{1,2})?)', re.I)
# HP/AC with or without colon, not already bold-labelled
HP_RE = re.compile(r'(?<!\*)\b(HP|Hit Points|Health)\b\s*:?\s*(\d{1,4})(?!\s*[dD]\d)', re.I)
AC_RE = re.compile(r'(?<!\*)\b(AC|Armor Class|Armour Class)\b\s*:?\s*(\d{1,3})\b', re.I)

def already_labelled(s, which):
    pat = r'\*\*\s*(?:HP|Hit Points|Health)\s*\*?\*?\s*:' if which=='hp' else r'\*\*\s*(?:AC|Armor Class|Armour Class)\s*\*?\*?\s*:'
    return re.search(pat, s, re.I) is not None

def label_stats(body):
    """Add **HP:** / **AC:** labels in place. Returns (new_body, hp, ac)."""
    hp = ac = None
    m = HP_RE.search(body)
    if m:
        hp = int(m.group(2))
        if hp <= 0: hp = None
    m2 = AC_RE.search(body)
    if m2:
        ac = int(m2.group(2))
        if not (1 <= ac <= 30): ac = None
    if hp is None or ac is None:
        return body, hp, ac
    if not already_labelled(body, 'hp'):
        body = HP_RE.sub(lambda x: '**HP:** %s' % x.group(2), body, count=1)
    if not already_labelled(body, 'ac'):
        body = AC_RE.sub(lambda x: '**AC:** %s' % x.group(2), body, count=1)
    return body, hp, ac

def normalize_text(text):
    """Return (new_text, stats_dict) or (None, stats_dict) if nothing changed."""
    info = {'entries': 0, 'fixed': 0, 'skipped_no_numbers': [], 'region': False}
    reg = find_region(text)
    if not reg:
        return None, info
    info['region'] = True
    start, end = reg
    region = text[start:end]
    entries = split_entries(region)
    if not entries:
        return None, info

    # build entry spans
    spans = []
    for i, (kind, m) in enumerate(entries):
        e = entries[i+1][1].start() if i+1 < len(entries) else len(region)
        spans.append((kind, m, m.start(), e))

    out = []
    cursor = 0
    for kind, m, s, e in spans:
        info['entries'] += 1
        out.append(region[cursor:s])
        chunk = region[s:e]
        hdr_line_end = chunk.index('\n') if '\n' in chunk else len(chunk)
        hdr = chunk[:hdr_line_end]
        body = chunk[hdr_line_end:]

        if kind == 'h':
            num, name = m.group(2), m.group(3)
        else:
            num, name = m.group(1), m.group(2)
            body = ('\n' + m.group(3) + body) if m.group(3).strip() else body

        # CR: from header first, else from the first 3 lines of body
        cr = None
        cm = CR_RE.search(hdr)
        if cm:
            cr = cm.group(1).replace(' ', '')
            # strip the CR fragment out of the name so it isn't duplicated
            name = CR_RE.sub('', name)
        else:
            head_of_body = '\n'.join(body.split('\n')[:4])
            cm = CR_RE.search(head_of_body)
            if cm: cr = cm.group(1).replace(' ', '')

        new_body, hp, ac = label_stats(body)
        if cr is None or hp is None or ac is None:
            # never invent — leave this entry exactly as it was
            info['skipped_no_numbers'].append({
                'name': name.strip(' .*()'), 'cr': cr, 'hp': hp, 'ac': ac})
            out.append(chunk)
            cursor = e
            continue

        # clean the name: drop trailing punctuation and dangling empty parens
        nm = name.strip()
        nm = re.sub(r'\(\s*\)', '', nm)
        nm = re.sub(r'[\s\.,;:]+$', '', nm).strip()
        nm = re.sub(r'\s{2,}', ' ', nm)
        new_hdr = '### %s. %s (CR %s)' % (num, nm, cr)
        out.append(new_hdr + new_body)
        info['fixed'] += 1
        cursor = e
    out.append(region[cursor:])
    new_region = ''.join(out)

    if info['fixed'] == 0:
        return None, info

    # ensure a chunker-visible section anchor exists right at the top of the region
    if not re.search(r'^##\s*\d*\.?\s*Bestiary', new_region, re.M | re.I):
        new_region = '\n\n## Bestiary\n' + new_region.lstrip('\n')

    return text[:start] + new_region + text[end:], info
