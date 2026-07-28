#!/usr/bin/env bun
/**
 * Simulate lore-keeper-ingest extractEncounters + production parser on the launch ten.
 * Reports which monsters would land as chunk_type=monster and whether they parse FULL.
 */
import { readdirSync, readFileSync } from 'fs';
import { join } from 'path';
import {
  gradeCoverage,
  parseAuthoredStatBlock,
} from '../../../infinite-realms-production/ai-adventure-scribe-main/server-bun/src/services/combat/authored-stat-block-parser.ts';

const BATCH1: Record<string, string> = {
  'the-eternal-feast': 'campaign-ideas/Completed/Intrigue/the-eternal-feast',
  'the-porcelain-court': 'campaign-ideas/Completed/Horror/the-porcelain-court',
  'abyssal-descent': 'campaign-ideas/Completed/Horror/abyssal-descent',
  'seven-swords-for-hire': 'campaign-ideas/Completed/Adventure/seven-swords-for-hire',
  'the-impossible-vault': 'campaign-ideas/Completed/Intrigue/the-impossible-vault',
  'academy-of-arcane-gastronomy': 'campaign-ideas/Completed/Fantasy/academy-of-arcane-gastronomy',
  'the-crimson-thread-of-silverport':
    'campaign-ideas/Completed/Urban/the-crimson-thread-of-silverport',
  'murder-on-the-astral-express':
    'campaign-ideas/Completed/Mystery/murder-on-the-astral-express',
  'the-weather-weavers': 'campaign-ideas/Completed/Historical/the-weather-weavers',
  'wings-of-the-void': 'campaign-ideas/Completed/Sci-Fi/wings-of-the-void',
};

const BATCH2: Record<string, string> = {
  'clash-of-olympus': 'campaign-ideas/Completed/Fantasy/clash-of-olympus',
  'chronicles-of-the-somnolent-oracle':
    'campaign-ideas/Completed/Fantasy/chronicles-of-the-somnolent-oracle',
  'ascension-protocol': 'campaign-ideas/Completed/Adventure/ascension-protocol',
  'against-the-titans': 'campaign-ideas/Completed/Adventure/against-the-titans',
  'way-of-the-fading-blade': 'campaign-ideas/Completed/Historical/way-of-the-fading-blade',
  'the-chosen-slayer': 'campaign-ideas/Completed/Urban/the-chosen-slayer',
  'calypsos-death-derby': 'campaign-ideas/Completed/Horror/calypsos-death-derby',
  'the-revolutionaries-anthem': 'campaign-ideas/Completed/Intrigue/the-revolutionaries-anthem',
  'the-verdant-codex': 'campaign-ideas/Completed/Mystery/the-verdant-codex',
  'see-you-space-cowboy': 'campaign-ideas/Completed/Sci-Fi/see-you-space-cowboy',
};

const batchArg = process.argv.includes('--batch2')
  ? 2
  : process.argv.includes('--batch1')
    ? 1
    : process.argv.includes('--all')
      ? 0
      : 2;
const TEN: Record<string, string> =
  batchArg === 1 ? BATCH1 : batchArg === 2 ? BATCH2 : { ...BATCH1, ...BATCH2 };

/** Mirrors chunker.ts extractSection exactly. */
function extractSection(content: string, headerName: string): string | undefined {
  const patterns = [
    new RegExp(`##\\s*\\d*\\.?\\s*${headerName}[^\\n]*\\n([\\s\\S]*?)(?=\\n##\\s|$)`, 'i'),
    new RegExp(`###\\s*${headerName}[^\\n]*\\n([\\s\\S]*?)(?=\\n###|\\n##|$)`, 'i'),
    new RegExp(
      `##\\s*Section\\s*\\d+:?\\s*[^\\n]*${headerName}[^\\n]*\\n([\\s\\S]*?)(?=\\n##\\s|$)`,
      'i',
    ),
    new RegExp(`\\*\\*${headerName}[^*]*\\*\\*:?\\s*\\n([\\s\\S]*?)(?=\\n\\*\\*|\\n##|$)`, 'i'),
  ];
  for (const pattern of patterns) {
    const match = content.match(pattern);
    if (match) return match[1];
  }
  return undefined;
}

/** Mirrors chunker.ts extractEncounters monster extraction. */
function extractEncounters(content: string): { entityName: string; content: string }[] {
  const encounterSection =
    extractSection(content, 'Bestiary') || extractSection(content, 'Encounter');
  if (!encounterSection) return [];

  const chunks: { entityName: string; content: string }[] = [];
  const monsterPatterns = [
    /\*\*(\d+)\.\s*(.+?)\s*\(CR\s*[\d/]+\)\*\*\s*([\s\S]*?)(?=\*\*\d+\.|##|$)/gi,
    /###\s*(\d+)\.\s*(.+?)\s*\(CR\s*[\d/]+\)\s*\n([\s\S]*?)(?=###\s*\d+\.|##|$|\[TAG)/gi,
  ];

  for (const monsterPattern of monsterPatterns) {
    for (const match of encounterSection.matchAll(monsterPattern)) {
      const [, , name, details] = match;
      if (!chunks.some((c) => c.entityName === name!.trim())) {
        chunks.push({
          entityName: name!.trim(),
          content: `**${name!.trim()}**\n\n${details}`,
        });
      }
    }
  }

  const statBlockPattern =
    /###\s*Custom Stat Block:?\s*\*\*(.+?)\*\*\s*([\s\S]*?)(?=###|##|$)/gi;
  for (const match of encounterSection.matchAll(statBlockPattern)) {
    const [, name, details] = match;
    if (!chunks.some((c) => c.entityName === name!.trim())) {
      chunks.push({
        entityName: name!.trim(),
        content: `**${name!.trim()}**\n\n${details}`,
      });
    }
  }

  return chunks;
}

for (const [id, dir] of Object.entries(TEN)) {
  const bible = readdirSync(dir).find((f) => /bible/i.test(f) && !f.startsWith('._'));
  if (!bible) {
    console.log(id, 'NO BIBLE');
    continue;
  }
  const text = readFileSync(join(dir, bible), 'utf8');
  const chunks = extractEncounters(text);
  let full = 0;
  const fails: string[] = [];
  for (const c of chunks) {
    const g = gradeCoverage(parseAuthoredStatBlock(c.content));
    if (g === 'full') full++;
    else fails.push(`${c.entityName}(${g})`);
  }
  console.log(
    `${id.padEnd(42)} chunker=${String(chunks.length).padStart(2)} full=${full}/${chunks.length}${fails.length ? ' FAIL ' + fails.join(', ') : ''}`,
  );
  if (chunks.length === 0) {
    const hasBestiary = /bestiary/i.test(text);
    const hpLines = (text.match(/\bHP\b/g) || []).length;
    const idx = text.search(/BESTIARY|Bestiary/i);
    const snip = idx >= 0 ? text.slice(idx, idx + 280).replace(/\n/g, ' | ') : '';
    console.log(`  (bestiary heading: ${hasBestiary}, HP mentions: ${hpLines})`);
    if (snip) console.log(`  snippet: ${snip}`);
  }
}
