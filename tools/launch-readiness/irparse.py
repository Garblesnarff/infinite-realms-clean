"""Python port of production authored-stat-block-parser.ts + lore-keeper chunker extractEncounters.
Only the pieces needed for gradeCoverage (full/partial/none) are ported faithfully."""
import re

HP_LABELS=['HP','Hit Points','HitPoints','Health']
AC_LABELS=['AC','Armor Class','Armour Class']
SPEED_LABELS=['Speed','Movement','Move']
CR_LABELS=['CR','Challenge','Challenge Rating']
ATTACK_LABELS=['Attack Bonus','To Hit','Attack','Hit Bonus']
DAMAGE_LABELS=['Damage','Damage Dice','Dmg']
INTEGER=r'\d{1,4}(?!\d*\s*[dD]\d)'

def label_pattern(labels):
    return r'(?:^|[\s*_>|-])\**\s*(?:%s)\s*\**\s*:\s*\**\s*' % '|'.join(labels)

def read_labelled(content, labels, value_pattern):
    m=re.search(label_pattern(labels)+'('+value_pattern+')', content, re.I)
    return m.group(1) if m else None

def has_label(content, labels):
    return re.search(label_pattern(labels), content, re.I) is not None

def strip_embedded_tables(content):
    m=re.search(r'\[TAG:\s*[A-Z_]+\s*\]', content, re.I)
    return content[:m.start()] if m else content

def parse_stat_block(raw):
    """Returns dict with maxHp, armorClass, plus any_field bool."""
    out={'maxHp':None,'armorClass':None,'other':0}
    if not raw: return out
    c=strip_embedded_tables(raw)
    hp=read_labelled(c,HP_LABELS,INTEGER)
    if hp is not None:
        n=int(hp)
        if n>0: out['maxHp']=n
    ac=read_labelled(c,AC_LABELS,INTEGER)
    if ac is not None:
        n=int(ac)
        if 1<=n<=30: out['armorClass']=n
    for labels,pat in ((SPEED_LABELS,INTEGER),(CR_LABELS,r'\d{1,2}(?:\s*/\s*\d{1,2})?'),
                       (ATTACK_LABELS,r'\+\s*\d{1,2}\b'),(DAMAGE_LABELS,r'\d{1,2}\s*[dD]\s*\d{1,3}(?:\s*[+-]\s*\d{1,3})?')):
        if read_labelled(c,labels,pat) is not None: out['other']+=1
    return out

def grade(p):
    core=sum(1 for k in ('maxHp','armorClass') if p[k] is not None)
    if core==2: return 'full'
    return 'partial' if (core>0 or p['other']>0) else 'none'

# ---- chunker mirror ----
def extract_section(content, header):
    pats=[re.compile(r'##\s*\d*\.?\s*%s[^\n]*\n([\s\S]*?)(?=\n##\s|$)'%header, re.I),
          re.compile(r'###\s*%s[^\n]*\n([\s\S]*?)(?=\n###|\n##|$)'%header, re.I),
          re.compile(r'##\s*Section\s*\d+:?\s*[^\n]*%s[^\n]*\n([\s\S]*?)(?=\n##\s|$)'%header, re.I),
          re.compile(r'\*\*%s[^*]*\*\*:?\s*\n([\s\S]*?)(?=\n\*\*|\n##|$)'%header, re.I)]
    for p in pats:
        m=p.search(content)
        if m: return m.group(1)
    return None

MONSTER_PATTERNS=[re.compile(r'\*\*(\d+)\.\s*(.+?)\s*\(CR\s*[\d/]+\)\*\*\s*([\s\S]*?)(?=\*\*\d+\.|##|$)', re.I),
                  re.compile(r'###\s*(\d+)\.\s*(.+?)\s*\(CR\s*[\d/]+\)\s*\n([\s\S]*?)(?=###\s*\d+\.|##|$|\[TAG)', re.I)]
STATBLOCK_PATTERN=re.compile(r'###\s*Custom Stat Block:?\s*\*\*(.+?)\*\*\s*([\s\S]*?)(?=###|##|$)', re.I)

def extract_encounters(content):
    sec=extract_section(content,'Bestiary') or extract_section(content,'Encounter')
    if sec is None: return []
    chunks=[]; names=set()
    for p in MONSTER_PATTERNS:
        for m in p.finditer(sec):
            name=m.group(2).strip()
            if name not in names:
                names.add(name); chunks.append((name, '**%s**\n\n%s'%(name,m.group(3))))
    for m in STATBLOCK_PATTERN.finditer(sec):
        name=m.group(1).strip()
        if name not in names:
            names.add(name); chunks.append((name, '**%s**\n\n%s'%(name,m.group(2))))
    return chunks

def coverage(text):
    ch=extract_encounters(text)
    res=[(n,grade(parse_stat_block(c))) for n,c in ch]
    return res
