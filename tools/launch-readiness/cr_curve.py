#!/usr/bin/env python3
"""House HP/AC curve for Infinite Realms, derived from the library's own authored
stat blocks (not from SRD 5.1, and not from anybody's judgement).

Provenance: 589 authored (CR, HP, AC) triples from 99 non-clone campaign bibles,
extracted with tools/launch-readiness/irparse.py (the verified port of the
production authored-stat-block-parser). Template-clone campaigns -- those sharing
an identical stat signature with 4 or more peers, per depth_score.py -- were
excluded before any median was taken. Full method, sample sizes, SRD comparison
and the list of situations where this curve must NOT be used:
    tools/launch-readiness/HOUSE-STAT-CURVE.md

    from cr_curve import hp_for_cr, ac_for_cr
    hp_for_cr('1/2') -> 15
    ac_for_cr(8)     -> 18

    python3 cr_curve.py --table

Every value returned here is a *median of what the authors already wrote*. It is
a starting point for a human to adjust, never a substitute for one.
"""
from __future__ import annotations

import sys

__all__ = ['hp_for_cr', 'ac_for_cr', 'confidence_for_cr', 'curve_row',
           'parse_cr', 'format_cr', 'OBSERVED', 'MIN_CR', 'MAX_CR']

# --- observed data -----------------------------------------------------------
# cr: (blocks, distinct source campaigns, hp_median, hp_q1, hp_q3,
#      ac_median, ac_min, ac_max)
# Clone-corrected cohort only. CR 30 is deliberately absent: its single
# observation (a 5000 HP kaiju) is a set piece, not a data point.
OBSERVED = {
    0.0:   (1,  1,    1,    1,    1,  10, 10, 10),
    0.125: (1,  1,    5,    5,    5,  12, 12, 12),
    0.25:  (4,  4,   12,   10,   15,  10, 10, 12),
    0.5:   (19, 19,  15,   12,   15,  12, 11, 18),
    1.0:   (31, 27,  18,   15,   20,  12, 10, 18),
    2.0:   (74, 61,  30,   30,   40,  13,  5, 18),
    3.0:   (84, 69,  45,   45,   50,  14, 10, 22),
    4.0:   (58, 44,  60,   55,   65,  15,  8, 20),
    5.0:   (94, 75,  80,   75,   80,  16,  9, 18),
    6.0:   (44, 38,  90,   90,   96,  16,  8, 18),
    7.0:   (27, 27, 110,  105,  118,  17,  7, 20),
    8.0:   (44, 44, 120,  120,  150,  18, 13, 20),
    9.0:   (12, 12, 140,  139,  142,  17, 12, 20),
    10.0:  (33, 33, 150,  150,  180,  18, 10, 22),
    12.0:  (27, 27, 180,  180,  180,  18, 16, 22),
    15.0:  (25, 25, 250,  250,  250,  20, 18, 25),
    18.0:  (1,   1, 250,  250,  250,  20, 20, 20),
    20.0:  (7,   7, 400,  400,  400,  22, 20, 25),
    25.0:  (2,   2, 600,  600,  600,  22, 22, 22),
}

# A CR is trustworthy only if enough *separate* campaigns voted on it.
MIN_SOURCES = 5

# Anchors that drive interpolation. Thin CRs (fewer than MIN_SOURCES distinct
# campaigns) are reported but are NOT allowed to bend the curve -- with two
# exceptions at the ends of the range, where there is nothing to interpolate
# from and refusing outright would be less useful than a flagged guess.
_ANCHOR_EXCEPTIONS = {0.0, 0.125, 0.25, 25.0}

ANCHORS = sorted(cr for cr, row in OBSERVED.items()
                 if row[1] >= MIN_SOURCES or cr in _ANCHOR_EXCEPTIONS)

MIN_CR = ANCHORS[0]    # 0
MAX_CR = ANCHORS[-1]   # 25

_FRACTIONS = {'0': 0.0, '1/8': 0.125, '1/4': 0.25, '1/2': 0.5}


def parse_cr(cr):
    """Accept 5, '5', 0.5, '1/2', 'CR 1/2'. Returns a float."""
    if isinstance(cr, (int, float)):
        return float(cr)
    s = str(cr).strip().upper().removeprefix('CR').strip()
    s = s.replace(' ', '')
    if s in _FRACTIONS:
        return _FRACTIONS[s]
    if '/' in s:
        num, den = s.split('/', 1)
        den = float(den)
        if den == 0:
            raise ValueError('bad CR %r' % (cr,))
        return float(num) / den
    return float(s)


def format_cr(cr):
    v = parse_cr(cr)
    for label, val in _FRACTIONS.items():
        if abs(v - val) < 1e-9:
            return label
    if abs(v - round(v)) < 1e-9:
        return str(int(round(v)))
    return '%g' % v


def _check_range(v, cr):
    if v < MIN_CR or v > MAX_CR:
        raise ValueError(
            'CR %s is outside the evidence base (CR %s-%s). The library contains '
            'no usable authored sample there, so this curve will not invent one. '
            'See HOUSE-STAT-CURVE.md.' % (format_cr(cr), format_cr(MIN_CR),
                                          format_cr(MAX_CR)))


def _interp(v, index, round_to):
    """Linear interpolation between the two surrounding anchors."""
    lo = max(a for a in ANCHORS if a <= v)
    hi = min(a for a in ANCHORS if a >= v)
    if lo == hi:
        return int(OBSERVED[lo][index])
    a, b = OBSERVED[lo][index], OBSERVED[hi][index]
    val = a + (b - a) * (v - lo) / (hi - lo)
    return int(round(val / round_to) * round_to)


def confidence_for_cr(cr):
    """How much to trust the returned number.

    'observed'     -- median of >= MIN_SOURCES distinct campaigns.
    'thin'         -- median of a handful of campaigns; treat as a hint only.
    'interpolated' -- no usable sample here; value interpolated from neighbours.
    """
    v = parse_cr(cr)
    _check_range(v, cr)
    row = OBSERVED.get(v)
    if row is None:
        return 'interpolated'
    if row[1] >= MIN_SOURCES:
        return 'observed'
    # thin samples at the ends of the range are used (nothing to interpolate
    # from); thin samples in the middle are recorded but overridden.
    return 'thin' if v in _ANCHOR_EXCEPTIONS else 'interpolated'


def hp_for_cr(cr):
    """Median authored HP for this CR. Raises ValueError outside CR 0-25."""
    v = parse_cr(cr)
    _check_range(v, cr)
    row = OBSERVED.get(v)
    if row is not None and (row[1] >= MIN_SOURCES or v in _ANCHOR_EXCEPTIONS):
        return int(row[2])
    return _interp(v, 2, 5)


def ac_for_cr(cr):
    """Median authored AC for this CR. Raises ValueError outside CR 0-25."""
    v = parse_cr(cr)
    _check_range(v, cr)
    row = OBSERVED.get(v)
    if row is not None and (row[1] >= MIN_SOURCES or v in _ANCHOR_EXCEPTIONS):
        return int(row[5])
    return _interp(v, 5, 1)


def curve_row(cr):
    """Everything known about one CR, for callers that need to show their work."""
    v = parse_cr(cr)
    _check_range(v, cr)
    row = OBSERVED.get(v)
    conf = confidence_for_cr(v)
    out = dict(cr=format_cr(v), hp=hp_for_cr(v), ac=ac_for_cr(v),
               confidence=conf, blocks=0, sources=0,
               hp_iqr=None, ac_range=None, overridden_sample=None)
    if row:
        if conf == 'interpolated':
            # a thin mid-range sample the curve deliberately does not follow
            out['overridden_sample'] = dict(blocks=row[0], sources=row[1],
                                            hp=row[2], ac=row[5])
        else:
            out.update(blocks=row[0], sources=row[1], hp_iqr=(row[3], row[4]),
                       ac_range=(row[6], row[7]))
    return out


_TABLE_CRS = ['0', '1/8', '1/4', '1/2'] + [str(i) for i in range(1, 26)]


def _print_table():
    print('Infinite Realms house stat curve -- medians of authored values')
    print('source: 589 triples / 99 non-clone bibles. See HOUSE-STAT-CURVE.md')
    print()
    print('%-5s %6s %5s %-14s %-9s %6s %5s' %
          ('CR', 'HP', 'AC', 'HP IQR', 'AC range', 'blocks', 'srcs'))
    print('-' * 62)
    for label in _TABLE_CRS:
        r = curve_row(label)
        iqr = '%g-%g' % r['hp_iqr'] if r['hp_iqr'] else '-'
        acr = '%d-%d' % r['ac_range'] if r['ac_range'] else '-'
        flag = {'observed': '', 'thin': '  THIN', 'interpolated': '  interp'}[r['confidence']]
        ov = r['overridden_sample']
        if ov:
            flag += ' (overrides %d thin sample%s: HP %d / AC %d)' % (
                ov['sources'], '' if ov['sources'] == 1 else 's', ov['hp'], ov['ac'])
        print('%-5s %6d %5d %-14s %-9s %6s %5s%s' %
              (r['cr'], r['hp'], r['ac'], iqr, acr,
               r['blocks'] or '-', r['sources'] or '-', flag))
    print()
    print('THIN   = fewer than %d distinct source campaigns; do not lean on it.' % MIN_SOURCES)
    print('interp = no authored sample at this CR; linearly interpolated.')
    print('CR 26+ raises ValueError -- the library has no evidence up there.')


if __name__ == '__main__':
    if '--table' in sys.argv:
        _print_table()
    else:
        print(__doc__.strip())
        print()
        print('Run with --table to print the curve.')
