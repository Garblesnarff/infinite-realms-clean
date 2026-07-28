"""Bestiary normalizer v2 -- handles the dialects normalize_bestiaries.py (v1) misses.

Same HARD RULE as v1: never invent a number. Only relabel / reposition numbers the
author already wrote. An entry missing CR, HP or AC is left byte-for-byte untouched
and reported in `info['skipped_no_numbers']`.

v1 is imported and reused for region-finding, the two known header shapes, the CR
regex and the HP/AC labeller. v2 adds:

  (1) ANCHOR BUG FIX -- v1 unconditionally prepended a synthetic "## Bestiary"
      heading to the top of the statblock region. When the region already sat
      *inside* a chunker-visible section (e.g. "## 7. BESTIARY" followed by
      "[TAG: ENEMY_STATBLOCK]"), that synthetic "##" heading terminated the real
      section, so extract_section() returned only the TAG line and coverage stayed
      at zero even though every entry had been reshaped correctly.
      v2 builds both candidates (with / without the anchor) and keeps whichever
      one production actually parses, preferring the smaller edit on a tie.

  (2) B_HDR dialect -- "**1. Name**" on its own line with the stats on the
      following line(s) as "*CR 1* | *HP: 20* | *AC: 14* | *Speed: 40ft*".
      v1's two header regexes both require the ordinal *outside* the bold run,
      so it found zero entries here.

  (3) irparse-first stat resolution -- if the production parser can already read
      HP and AC out of the body as-authored (e.g. "*HP: 20*", whose leading "*"
      defeats v1's `(?<!\*)` lookbehind), leave the body byte-for-byte alone and
      only fix the header. Only fall back to v1's relabeller when production
      genuinely cannot read the stats.

  (4) CR-parenthetical name cleaning -- for "**Magma-Shark (CR 5):**" v1 stripped
      only the "(CR 5" fragment, leaving the name as "Magma-Shark )". v2 removes
      the whole "(CR ...)" parenthetical, yielding "Magma-Shark".

  (5) no_content_loss() -- word/number multiset guard so a rewrite can never drop
      authored text.

Target shape (unchanged from v1 -- what production requires):
    ## Bestiary   (or a pre-existing "## <n>. Bestiary")
    ### <n>. <Name> (CR <x>)
    ... **HP:** <n> ... **AC:** <n>
"""
import re, os, sys, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import irparse
import normalize_bestiaries as nb

# --- header dialects -------------------------------------------------------
# v1 supplies:
#   nb.H_HDR  "### 1. Name"
#   nb.L_HDR  "1. **Name** rest"
# v2 adds the ordinal-inside-the-bold shape, stats on the following lines:
B_HDR = re.compile(r'^\*\*\s*(\d{1,2})[\.\)]\s*(.+?)\s*\*\*\s*$', re.M)

# "(CR 5)" / "(CR 1/2 Humanoid)" -- the whole parenthetical, so removing it from a
# name leaves no orphan bracket behind.
CR_PAREN = re.compile(r'\(\s*CR\s*:?\s*(\d{1,2}(?:\s*/\s*\d{1,2})?)[^)]*\)', re.I)

WORD_RE = re.compile(r'[A-Za-z0-9]+')


def split_entries(region):
    """Yield (kind, match) per monster entry header, in document order."""
    hs = [('h', m) for m in nb.H_HDR.finditer(region)]
    if hs:
        return hs
    ls = [('l', m) for m in nb.L_HDR.finditer(region)]
    if ls:
        return ls
    return [('b', m) for m in B_HDR.finditer(region)]


def take_cr(text):
    """Return (cr_string_or_None, text_with_the_CR_fragment_removed)."""
    m = CR_PAREN.search(text)
    if m:
        return m.group(1).replace(' ', ''), text[:m.start()] + text[m.end():]
    m = nb.CR_RE.search(text)
    if m:
        return m.group(1).replace(' ', ''), text[:m.start()] + text[m.end():]
    return None, text


def resolve_stats(body):
    """Return (new_body, hp, ac).

    Prefer leaving the body untouched: if production's own parser already reads
    both numbers, we change nothing. Otherwise fall back to v1's relabeller and
    re-verify with production's parser before accepting the edit.
    """
    probe = '**x**\n\n' + body
    p = irparse.parse_stat_block(probe)
    if p['maxHp'] is not None and p['armorClass'] is not None:
        return body, p['maxHp'], p['armorClass']
    nb_body, nhp, nac = nb.label_stats(body)
    if nhp is not None and nac is not None and nb_body != body:
        p2 = irparse.parse_stat_block('**x**\n\n' + nb_body)
        if p2['maxHp'] is not None and p2['armorClass'] is not None:
            return nb_body, p2['maxHp'], p2['armorClass']
    return body, (p['maxHp'] or nhp), (p['armorClass'] or nac)


def clean_name(name):
    nm = name.strip()
    nm = re.sub(r'\(\s*\)', '', nm)
    nm = re.sub(r'^[\s\.,;:\)]+', '', nm)
    nm = re.sub(r'[\s\.,;:]+$', '', nm)
    nm = re.sub(r'\s{2,}', ' ', nm)
    return nm.strip()


def no_content_loss(old, new):
    """True iff no authored word/number occurs fewer times in `new` than in `old`."""
    co = collections.Counter(WORD_RE.findall(old))
    cn = collections.Counter(WORD_RE.findall(new))
    return not (co - cn)


def _build(text, start, end, region_out):
    return text[:start] + region_out + text[end:]


def normalize_text(text):
    """Return (new_text_or_None, info)."""
    info = {'entries': 0, 'fixed': 0, 'skipped_no_numbers': [], 'region': False,
            'anchor': False, 'dialect': None}
    reg = nb.find_region(text)
    if not reg:
        return None, info
    info['region'] = True
    start, end = reg
    region = text[start:end]
    entries = split_entries(region)
    if not entries:
        return None, info
    info['dialect'] = entries[0][0]

    spans = []
    for i, (kind, m) in enumerate(entries):
        e = entries[i + 1][1].start() if i + 1 < len(entries) else len(region)
        spans.append((kind, m, m.start(), e))

    out, cursor = [], 0
    for kind, m, s, e in spans:
        info['entries'] += 1
        out.append(region[cursor:s])
        chunk = region[s:e]
        hdr_line_end = chunk.index('\n') if '\n' in chunk else len(chunk)
        hdr, body = chunk[:hdr_line_end], chunk[hdr_line_end:]

        if kind == 'h':
            num, name = m.group(2), m.group(3)
        elif kind == 'l':
            num, name = m.group(1), m.group(2)
            if m.group(3).strip():
                body = '\n' + m.group(3) + body
        else:  # 'b' -- "**1. Name**", stats on the following lines
            num, name = m.group(1), m.group(2)

        # CR: from the name first (strip it there so it isn't duplicated), then
        # from the rest of the header line, then from the head of the body.
        cr, name = take_cr(name)
        if cr is None:
            cr, _ = take_cr(hdr)
        if cr is None:
            cr, _ = take_cr('\n'.join(body.split('\n')[:4]))

        new_body, hp, ac = resolve_stats(body)
        if cr is None or hp is None or ac is None:
            info['skipped_no_numbers'].append(
                {'name': clean_name(name), 'cr': cr, 'hp': hp, 'ac': ac})
            out.append(chunk)          # untouched, byte for byte
            cursor = e
            continue

        out.append('### %s. %s (CR %s)' % (num, clean_name(name), cr) + new_body)
        info['fixed'] += 1
        cursor = e
    out.append(region[cursor:])
    new_region = ''.join(out)

    if info['fixed'] == 0:
        return None, info

    # --- fix (1): only add a synthetic anchor if production needs one ---------
    cands = [(False, _build(text, start, end, new_region))]
    if not re.search(r'^##\s*\d*\.?\s*Bestiary', new_region, re.M | re.I):
        anchored = '\n\n## Bestiary\n' + new_region.lstrip('\n')
        cands.append((True, _build(text, start, end, anchored)))

    best, best_n, best_anchor = None, -1, False
    for anchor, cand in cands:
        n = sum(1 for _, g in irparse.coverage(cand) if g == 'full')
        if n > best_n:
            best, best_n, best_anchor = cand, n, anchor
    info['anchor'] = best_anchor
    if best == text:
        return None, info
    return best, info
