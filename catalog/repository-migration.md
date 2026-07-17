# Repository Migration Plan

## First-PR boundary

This PR is inventory and metadata only. It adds catalogs, reports, a schema, examples, and validation. It intentionally performs **no campaign-directory moves, merges, renames, or deletions**.

## Why movement is deferred

The generated catalog exposes exact-slug duplicates, inconsistent author length labels, divergent copies inside/outside `Completed`, and IP-heavy material. Those review decisions must precede physical reorganization.

## Second-PR sequence

1. Review duplicate groups file-by-file and designate canonical packages.
2. Confirm normalized length and legal/IP status.
3. Pilot `git mv` migrations for Eternal Feast, Porcelain Court, St. Mercy's, Godskin Atlas as a concept stub, and one resolved duplicate.
4. Test app ingestion, path redirects, and generated indexes.
5. Move remaining campaigns in small reviewed batches.

Proposed destination:

```text
campaigns/<slug>/{campaign.yaml,campaign.md,campaign-bible.md,world-building-spec.md,creative-brief.md,supporting/,assets/}
ideas/
catalog/
tools/
```

