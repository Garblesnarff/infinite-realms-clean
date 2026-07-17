# Pilot Campaign Migration

This stacked PR exercises the proposed structure on four campaign packages and one sheet-only concept. It is deliberately not a mass reorganization.

## Moved

- The Eternal Feast → `campaigns/the-eternal-feast/`
- The Porcelain Court → `campaigns/the-porcelain-court/`
- St. Mercy's Magical Menagerie → `campaigns/st-mercys-magical-menagerie/`
- Combat Healer Chronicles → `campaigns/combat-healer-chronicles/`
- The Godskin Atlas concept stub → `ideas/expansion-queue/the-godskin-atlas/`

## Duplicate resolution

Combat Healer Chronicles had a four-document, ~12,700-word package outside `Completed` and a distinct ~1,800-word RAG-tagged bible inside `Completed`. The richer package is canonical. The smaller file remains intact at `supporting/legacy-rag-campaign-bible.md`; it was not overwritten or discarded.

## Deferred

All other duplicate groups, IP transformations, and directory moves remain deferred until this pilot verifies app ingestion and path handling.

The first PR's JSON/CSV catalog remains an immutable audit snapshot. `path-migrations.csv` is the machine-readable overlay for this pilot; the catalog generator should fold these paths into the next full regeneration after the stacked PRs merge.
