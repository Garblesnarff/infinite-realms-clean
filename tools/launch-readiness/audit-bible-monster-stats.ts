#!/usr/bin/env bun
/**
 * Filesystem coverage audit for campaign-authored monster stat blocks.
 *
 * Imports the PRODUCTION parser (read-only path) — never reimplements its rules.
 * Extracts monster blocks with the same patterns as lore-keeper-ingest chunker.ts
 * so numbers here match what combat would see after ingest.
 *
 * Usage:
 *   bun tools/launch-readiness/audit-bible-monster-stats.ts
 *   bun tools/launch-readiness/audit-bible-monster-stats.ts --json
 *   bun tools/launch-readiness/audit-bible-monster-stats.ts --campaign the-eternal-feast
 */
import { readdirSync, readFileSync, statSync, existsSync, writeFileSync, mkdirSync } from 'fs';
import { join, basename, dirname } from 'path';

import {
  gradeCoverage,
  parseAuthoredStatBlock,
  type ParseCoverage,
} from '../../../infinite-realms-production/ai-adventure-scribe-main/server-bun/src/services/combat/authored-stat-block-parser.ts';

const REPO_ROOT = join(import.meta.dir, '../..');
const CAMPAIGN_IDEAS = join(REPO_ROOT, 'campaign-ideas');
const COMPLETED = join(CAMPAIGN_IDEAS, 'Completed');
const GENRES = [
  'Adventure',
  'Fantasy',
  'Historical',
  'Horror',
  'Intrigue',
  'Mystery',
  'Post-Apocalyptic',
  'Sci-Fi',
  'Urban',
] as const;

const args = process.argv.slice(2);
const flag = (name: string) => args.includes(name);
const option = (name: string): string | undefined => {
  const i = args.indexOf(name);
  return i >= 0 ? args[i + 1] : undefined;
};

interface CreatureResult {
  name: string;
  coverage: ParseCoverage;
  maxHp?: number;
  armorClass?: number;
  unparsedLabels: string[];
  parsedFields: string[];
  /** True when raw text has HP/AC numbers but parser missed them (colon/format issue). */
  hasLooseStats: boolean;
  snippet: string;
}

interface CampaignResult {
  id: string;
  genre: string;
  path: string;
  files: {
    overview: boolean;
    creativeBrief: boolean;
    worldBuilding: boolean;
    bible: boolean;
  };
  wordCount: number;
  monsterCount: number;
  full: number;
  partial: number;
  none: number;
  fullPct: number;
  creatures: CreatureResult[];
  hasBestiaryHeading: boolean;
  productIdentityHits: string[];
  trademarkHits: string[];
  lengthHint: string;
  score: number;
  scoreNotes: string[];
}

/** Same extraction patterns as lore-keeper-ingest/src/chunker.ts extractEncounters. */
function extractMonsterBlocks(bible: string): { name: string; content: string }[] {
  const section =
    extractSection(bible, 'Bestiary') ||
    extractSection(bible, 'Encounter') ||
    extractSection(bible, 'BESTIARY') ||
    extractSection(bible, 'Monsters') ||
    // Fall back: whole bible if it has numbered CR blocks
    (/\(CR\s*[\d/]+\)/i.test(bible) ? bible : '');

  if (!section) return [];

  const found: { name: string; content: string }[] = [];
  const seen = new Set<string>();

  // Patterns mirror lore-keeper-ingest chunker.ts, plus common bible dialects the
  // chunker currently misses (Porcelain Court one-liners, Wings compact lists).
  // Each pattern yields {name, details} via named capture groups.
  type Hit = { name: string; details: string };
  const hits: Hit[] = [];

  // Format A (Abyssal): **1. The Chiropteran Hulk (CR 5)**
  for (const m of section.matchAll(
    /\*\*(\d+)\.\s*(.+?)\s*\(CR\s*[\d/]+\)\*\*\s*([\s\S]*?)(?=\*\*\d+\.|##|$)/gi,
  )) {
    hits.push({ name: m[2]!, details: m[3] ?? '' });
  }

  // Format B (Eternal Feast): ### 1. Gluten Golem (CR 5)
  for (const m of section.matchAll(
    /###\s*(\d+)\.\s*(.+?)\s*\(CR\s*[\d/]+\)\s*\n([\s\S]*?)(?=###\s*\d+\.|##|$|\[TAG)/gi,
  )) {
    hits.push({ name: m[2]!, details: m[3] ?? '' });
  }

  // Format C: ### Custom Stat Block: **Name**
  for (const m of section.matchAll(
    /###\s*Custom Stat Block:?\s*\*\*(.+?)\*\*\s*([\s\S]*?)(?=###|##|$)/gi,
  )) {
    hits.push({ name: m[1]!, details: m[2] ?? '' });
  }

  // Format D (Porcelain / Astral / Ascension):
  // 1. **Chipped Hound** (CR 3 Beast Construct). HP: 50, AC: 16. ...
  for (const m of section.matchAll(
    /^\d+\.\s+\*\*(.+?)\*\*\s*\(CR\s*[\d/]+[^)]*\)\.?\s*(.+)$/gim,
  )) {
    hits.push({ name: m[1]!, details: m[2] ?? '' });
  }

  // Format E (Wings of the Void):
  // 1. **Void Glider (CR 2):** HP 30, AC 14, ...
  for (const m of section.matchAll(
    /^\d+\.\s+\*\*(.+?)\s*\(CR\s*[\d/]+\)\*\*:?\s*(.+)$/gim,
  )) {
    hits.push({ name: m[1]!, details: m[2] ?? '' });
  }

  // Format F: bare bold name with CR on same/next line and HP nearby
  // 1. **Name** ... HP ... (only if nothing else found for that name)
  for (const m of section.matchAll(
    /^\d+\.\s+\*\*([^*]+?)\*\*[^\n]{0,80}(?:\n[^\n]{0,200})?/gim,
  )) {
    const block = m[0];
    if (!/HP|Hit Points|AC|Armor Class/i.test(block)) continue;
    hits.push({ name: m[1]!, details: block });
  }

  for (const hit of hits) {
    let name = hit.name.trim();
    name = name.replace(/\s*\(CR\s*[\d/]+\)\s*$/i, '').trim();
    name = name.replace(/\*+/g, '').trim();
    if (!name || seen.has(name.toLowerCase())) continue;
    seen.add(name.toLowerCase());
    found.push({ name, content: `**${name}**\n\n${hit.details.trim()}` });
  }

  return found;
}

function extractSection(content: string, heading: string): string | null {
  // From a ##/### heading containing `heading` through the next ##-level heading or EOF.
  // Index-based: multiline `$` matches EOL and would empty a non-greedy body.
  const startRe = new RegExp(`^#{1,3}\\s+[^\\n]*${heading}[^\\n]*`, 'im');
  const start = startRe.exec(content);
  if (!start || start.index === undefined) return null;
  const from = start.index;
  const afterHeading = from + start[0].length;
  const rest = content.slice(afterHeading);
  const nextH2 = /^#{1,2}\s+(?!#)[^\n]+/im.exec(rest);
  // Prefer next ## (not ###) as section end; if none, take to EOF
  if (!nextH2 || nextH2.index === undefined) return content.slice(from);
  return content.slice(from, afterHeading + nextH2.index);
}

const LOOSE_HP = /(?:HP|Hit Points|Health)\s*[:*]?\s*\**\s*(\d{1,4})\b/i;
const LOOSE_AC = /(?:AC|Armor Class|Armour Class)\s*[:*]?\s*\**\s*(\d{1,2})\b/i;

const PI_PATTERNS: { label: string; re: RegExp }[] = [
  { label: 'beholder', re: /\bbeholders?\b/i },
  { label: 'spectator', re: /\bspectators?\b(?!\s+of)/i }, // careful: "spectator" as sports
  { label: 'death tyrant', re: /\bdeath\s+tyrants?\b/i },
  { label: 'gauth', re: /\bgauths?\b/i },
  { label: 'mind flayer', re: /\bmind\s+flayers?\b/i },
  { label: 'illithid', re: /\billithids?\b/i },
  { label: 'elder brain', re: /\belder\s+brains?\b/i },
  { label: 'intellect devourer', re: /\bintellect\s+devourers?\b/i },
  { label: 'displacer beast', re: /\bdisplacer\s+beasts?\b/i },
  { label: 'githyanki', re: /\bgithyanki\b/i },
  { label: 'githzerai', re: /\bgithzerai\b/i },
  { label: 'umber hulk', re: /\bumber\s+hulks?\b/i },
  { label: 'carrion crawler', re: /\bcarrion\s+crawlers?\b/i },
  { label: 'yuan-ti', re: /\byuan[-\s]?ti\b/i },
  { label: 'slaad', re: /\bslaadi?\b/i },
  { label: 'kuo-toa', re: /\bkuo[-\s]?toa\b/i },
  { label: 'blink dog', re: /\bblink\s+dogs?\b/i },
  { label: 'hook horror', re: /\bhook\s+horrors?\b/i },
];

const TM_PATTERNS = [
  /Dungeons\s*&\s*Dragons/gi,
  /\bD&D\b/g,
  /\bDnD\b/g,
  /\bDungeons and Dragons\b/gi,
];

function findFiles(dir: string): {
  overview: string | null;
  creativeBrief: string | null;
  worldBuilding: string | null;
  bible: string | null;
} {
  const files = readdirSync(dir).filter((f) => f.endsWith('.md'));
  const slug = basename(dir);
  const bible =
    files.find((f) => /campaign-bible/i.test(f)) ||
    files.find((f) => /bible/i.test(f)) ||
    null;
  const creativeBrief = files.find((f) => /creative-brief/i.test(f)) || null;
  const worldBuilding = files.find((f) => /world-building/i.test(f)) || null;
  const overview =
    files.find((f) => f === `${slug}.md`) ||
    files.find(
      (f) =>
        !/creative-brief|world-building|campaign-bible|bible/i.test(f) && f.endsWith('.md'),
    ) ||
    null;
  return {
    overview: overview ? join(dir, overview) : null,
    creativeBrief: creativeBrief ? join(dir, creativeBrief) : null,
    worldBuilding: worldBuilding ? join(dir, worldBuilding) : null,
    bible: bible ? join(dir, bible) : null,
  };
}

function lengthHint(text: string, wordCount: number): string {
  const sessionMatch =
    text.match(/(\d+)\s*[–-]\s*(\d+)\s+sessions?/i) ||
    text.match(/(\d+)\s+sessions?/i) ||
    text.match(/campaign length[:\s*]+([^\n]+)/i);
  const raw = sessionMatch ? sessionMatch[0] : '';
  if (/one[-\s]?shot/i.test(text) || /one shot/i.test(text)) return 'one-shot';
  if (/\b(short|6\s*[–-]\s*8|8\s*[–-]\s*10|10\s*sessions)/i.test(text) || wordCount < 2500)
    return 'short';
  if (/\b(long|30\+|35\s*sessions|full campaign)/i.test(text) || wordCount > 5500) return 'long';
  if (raw) return raw.slice(0, 40);
  if (wordCount < 3500) return 'medium-short';
  return 'medium';
}

function scoreCampaign(r: CampaignResult): { score: number; notes: string[] } {
  let score = 0;
  const notes: string[] = [];

  // Completeness (0-25)
  const fileScore =
    (r.files.overview ? 4 : 0) +
    (r.files.creativeBrief ? 5 : 0) +
    (r.files.worldBuilding ? 5 : 0) +
    (r.files.bible ? 11 : 0);
  score += fileScore;
  if (fileScore < 25) notes.push(`incomplete package (${fileScore}/25 files)`);

  // Parser full coverage (0-35) — the hard requirement for launch
  if (r.monsterCount === 0) {
    notes.push('no extractable monster blocks');
  } else {
    const cov = r.fullPct;
    const covScore = Math.round((cov / 100) * 35);
    score += covScore;
    if (cov < 100) notes.push(`parser full coverage ${cov.toFixed(0)}% (${r.full}/${r.monsterCount})`);
    else notes.push(`100% full parse (${r.monsterCount} monsters)`);
  }

  // Has a real bestiary section
  if (r.hasBestiaryHeading) score += 5;
  else notes.push('no Bestiary heading');

  // Depth / arc signal via word count (0-10)
  if (r.wordCount >= 4000) score += 10;
  else if (r.wordCount >= 2500) score += 7;
  else if (r.wordCount >= 1500) score += 4;
  else {
    score += 1;
    notes.push(`thin package (${r.wordCount} words)`);
  }

  // Length preference for new-subscriber conversion: short/medium > epic (0-8)
  if (r.lengthHint === 'short' || r.lengthHint === 'one-shot') {
    score += 8;
    notes.push('short/one-shot length (good for trial conversion)');
  } else if (r.lengthHint.includes('medium') || r.lengthHint === 'medium-short') {
    score += 6;
  } else if (r.lengthHint === 'long') {
    score += 3;
    notes.push('long campaign — flagship, not trial');
  } else {
    score += 4;
  }

  // Legal cleanliness (0-10 subtracted for hits)
  if (r.productIdentityHits.length === 0) score += 7;
  else {
    score += Math.max(0, 7 - r.productIdentityHits.length * 2);
    notes.push(`Product Identity: ${r.productIdentityHits.join(', ')}`);
  }
  if (r.trademarkHits.length === 0) score += 5;
  else {
    score += Math.max(0, 5 - r.trademarkHits.length);
    notes.push(`trademark: ${r.trademarkHits.join(', ')}`);
  }

  // Prefer 5+ monsters for combat depth
  if (r.monsterCount >= 8) score += 5;
  else if (r.monsterCount >= 5) score += 3;
  else if (r.monsterCount >= 1) score += 1;

  return { score, notes };
}

function scanCampaign(genre: string, dir: string): CampaignResult | null {
  const id = basename(dir);
  const files = findFiles(dir);
  if (!files.bible) return null;

  const bibleText = readFileSync(files.bible, 'utf8');
  const extraTexts = [files.overview, files.creativeBrief, files.worldBuilding]
    .filter(Boolean)
    .map((p) => readFileSync(p!, 'utf8'));
  const allText = [bibleText, ...extraTexts].join('\n');
  const wordCount = bibleText.split(/\s+/).length;

  const blocks = extractMonsterBlocks(bibleText);
  const creatures: CreatureResult[] = blocks.map((b) => {
    const parsed = parseAuthoredStatBlock(b.content);
    const coverage = gradeCoverage(parsed);
    const hasLooseStats = LOOSE_HP.test(b.content) && LOOSE_AC.test(b.content);
    return {
      name: b.name,
      coverage,
      maxHp: parsed.maxHp,
      armorClass: parsed.armorClass,
      unparsedLabels: parsed.unparsedLabels,
      parsedFields: parsed.parsedFields,
      hasLooseStats,
      snippet: b.content.replace(/\s+/g, ' ').slice(0, 120),
    };
  });

  const full = creatures.filter((c) => c.coverage === 'full').length;
  const partial = creatures.filter((c) => c.coverage === 'partial').length;
  const none = creatures.filter((c) => c.coverage === 'none').length;
  const monsterCount = creatures.length;
  const fullPct = monsterCount === 0 ? 0 : (full / monsterCount) * 100;

  const productIdentityHits: string[] = [];
  for (const { label, re } of PI_PATTERNS) {
    if (re.test(allText)) productIdentityHits.push(label);
  }

  const trademarkHits: string[] = [];
  for (const re of TM_PATTERNS) {
    re.lastIndex = 0;
    if (re.test(allText)) {
      const sample = allText.match(re)?.[0];
      if (sample && !trademarkHits.includes(sample)) trademarkHits.push(sample);
    }
  }

  const result: CampaignResult = {
    id,
    genre,
    path: dir,
    files: {
      overview: !!files.overview,
      creativeBrief: !!files.creativeBrief,
      worldBuilding: !!files.worldBuilding,
      bible: !!files.bible,
    },
    wordCount,
    monsterCount,
    full,
    partial,
    none,
    fullPct,
    creatures,
    hasBestiaryHeading: /#{1,3}\s+[^\n]*bestiary/i.test(bibleText),
    productIdentityHits,
    trademarkHits,
    lengthHint: lengthHint(allText, wordCount),
    score: 0,
    scoreNotes: [],
  };

  const scored = scoreCampaign(result);
  result.score = scored.score;
  result.scoreNotes = scored.notes;
  return result;
}

function listCampaignDirs(): { genre: string; dir: string }[] {
  const out: { genre: string; dir: string }[] = [];
  for (const genre of GENRES) {
    const gdir = join(COMPLETED, genre);
    if (!existsSync(gdir)) continue;
    for (const name of readdirSync(gdir)) {
      const dir = join(gdir, name);
      try {
        if (statSync(dir).isDirectory()) out.push({ genre, dir });
      } catch {
        /* skip */
      }
    }
  }
  return out;
}

const single = option('--campaign');
const dirs = listCampaignDirs().filter((d) => !single || basename(d.dir) === single);
const results: CampaignResult[] = [];

for (const { genre, dir } of dirs) {
  const r = scanCampaign(genre, dir);
  if (r) results.push(r);
}

results.sort((a, b) => b.score - a.score || b.fullPct - a.fullPct || b.wordCount - a.wordCount);

const totals = results.reduce(
  (acc, r) => ({
    campaigns: acc.campaigns + 1,
    monsters: acc.monsters + r.monsterCount,
    full: acc.full + r.full,
    partial: acc.partial + r.partial,
    none: acc.none + r.none,
    withMonsters: acc.withMonsters + (r.monsterCount > 0 ? 1 : 0),
    perfect: acc.perfect + (r.monsterCount > 0 && r.full === r.monsterCount ? 1 : 0),
  }),
  { campaigns: 0, monsters: 0, full: 0, partial: 0, none: 0, withMonsters: 0, perfect: 0 },
);

if (flag('--json')) {
  console.log(JSON.stringify({ totals, campaigns: results }, null, 2));
  process.exit(0);
}

const pct = (n: number, t: number) => (t === 0 ? 'n/a' : `${((n / t) * 100).toFixed(1)}%`);

console.log('Filesystem bible monster coverage (production parser)');
console.log('='.repeat(100));
console.log(
  `${'score'.padStart(5)} ${'genre'.padEnd(18)} ${'campaign'.padEnd(36)} ${'mons'.padStart(4)} ${'full'.padStart(4)} ${'part'.padStart(4)} ${'none'.padStart(4)} ${'full%'.padStart(6)} ${'words'.padStart(6)} ${'len'.padEnd(12)}`,
);
console.log('-'.repeat(100));

for (const r of results) {
  console.log(
    `${String(r.score).padStart(5)} ${r.genre.padEnd(18)} ${r.id.slice(0, 36).padEnd(36)} ${String(r.monsterCount).padStart(4)} ${String(r.full).padStart(4)} ${String(r.partial).padStart(4)} ${String(r.none).padStart(4)} ${r.fullPct.toFixed(0).padStart(5)}% ${String(r.wordCount).padStart(6)} ${r.lengthHint.slice(0, 12).padEnd(12)}`,
  );
}

console.log('-'.repeat(100));
console.log(
  `TOTAL campaigns ${totals.campaigns}  with monsters ${totals.withMonsters}  perfect-full ${totals.perfect}`,
);
console.log(
  `TOTAL monsters ${totals.monsters}  full ${totals.full} (${pct(totals.full, totals.monsters)})  partial ${totals.partial}  none ${totals.none}`,
);

// Top candidates per genre for selection
console.log('\n\nTOP BY GENRE (score ≥ 50 or full coverage)');
console.log('='.repeat(80));
for (const genre of GENRES) {
  const top = results.filter((r) => r.genre === genre).slice(0, 5);
  console.log(`\n## ${genre}`);
  for (const r of top) {
    const pi = r.productIdentityHits.length ? ` PI:[${r.productIdentityHits.join(',')}]` : '';
    const tm = r.trademarkHits.length ? ` TM:[${r.trademarkHits.join(',')}]` : '';
    console.log(
      `  ${r.score}  ${r.id}  monsters ${r.full}/${r.monsterCount} full  words ${r.wordCount}  ${r.lengthHint}${pi}${tm}`,
    );
    console.log(`       ${r.scoreNotes.join('; ')}`);
  }
}

// Write machine-readable report for selection
const outDir = join(REPO_ROOT, 'tools/launch-readiness/reports');
mkdirSync(outDir, { recursive: true });
const outPath = join(outDir, 'bible-monster-coverage.json');
writeFileSync(outPath, JSON.stringify({ totals, generatedAt: new Date().toISOString(), campaigns: results }, null, 2));
console.log(`\nWrote ${outPath}`);
