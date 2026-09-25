# Shared artifact contract

Contract version: `1.0.0`

This contract isolates role implementations from one another. A role may be optimized independently as long as it continues to read and write the declared artifacts. Exact paths, columns, and enumerations are defined in `artifact-schemas.md`.

## Workspace layout

```text
00-input/       user requirements, source material, institutional template
01-plan/        project brief, outline, terminology, task board
02-evidence/    source and data ledgers, downloaded or supplied evidence
03-drafts/      section drafts and integrated manuscript source
04-figures/     figures, tables, captions, provenance
05-revisions/   comments, routing, response table, change log
06-audits/      initial and post-revision audit reports
07-deliverables/ versioned DOCX/PDF and final package
```

## Artifact ownership

- One role owns each artifact during an assigned task.
- The global planner may integrate copies into `03-drafts/integrated/`; it must not erase specialist source artifacts.
- The format specialist alone produces formatted deliverables in `07-deliverables/`.
- Reviewers write reports in `06-audits/`; they do not edit the artifact under review.
- The revision manager writes the revision plan, assembles accepted outputs, and maintains the change log.

## Canonical cross-role artifacts

- `01-plan/project-brief.md`
- `01-plan/outline.md`
- `01-plan/terminology.csv`
- `01-plan/task-board.csv`
- `02-evidence/evidence-ledger.csv`
- `02-evidence/search-notes/`
- `02-evidence/data/raw/`
- `02-evidence/data/processed/`
- `03-drafts/sections/<section-id>.md`
- `03-drafts/integrated/manuscript.md`
- `04-figures/figure-ledger.csv`
- `05-revisions/comment-ledger.csv`
- `05-revisions/impact-map.csv`
- `05-revisions/change-log.csv`
- `05-revisions/response-table.md`
- `06-audits/<version>-<audit-type>.md`
- `07-deliverables/deliverable-manifest.csv`
- `07-deliverables/<version>/`

## Task envelope

Every delegated task must contain:

```yaml
task_id: T-001
role: content-writer
objective: "Concrete, bounded outcome"
inputs:
  - "relative/path"
outputs:
  - "relative/path"
constraints:
  - "Relevant user or format requirement"
acceptance:
  - "Observable pass condition"
dependencies:
  - "T-000"
status: queued
```

Allowed task status values: `queued`, `in_progress`, `needs_input`, `ready_for_review`, `accepted`, `rejected`.

## Evidence identifiers

- Sources: `SRC-0001`
- Claims: `CLM-0001`
- Data items: `DAT-0001`
- Figures/tables: `FIG-001`, `TAB-001`
- Comments: `CMT-0001`
- Changes: `CHG-0001`
- Audit findings: `FND-0001`

Use these identifiers across ledgers so a claim can be traced to evidence, revisions, and audit findings.

## Role module compatibility

Each role file begins with a `Role contract` block. Future role-specific optimization may change reasoning, checks, tools, or internal workflow, but must preserve:

1. role identifier;
2. required inputs;
3. required outputs;
4. escalation conditions;
5. shared identifiers and status vocabulary;
6. `Contract version: 1.0.0` until an intentional migration.

If an optimization changes one of these, update this contract and every affected role in the same commit and record the migration in `CHANGELOG.md`.
