---
name: academic-paper-team
description: Orchestrate a reusable, traceable multi-agent workflow for planning, researching, drafting, illustrating, formatting, revising, and quality-checking academic papers. Use when creating or revising a thesis, dissertation, course paper, journal manuscript, or proposal with multiple specialist roles. Do not use to fabricate evidence, citations, data, or completed research.
---

# Academic Paper Team

Build the paper as a controlled artifact pipeline, not as nine agents editing one file concurrently.

## Start

1. Read `references/shared-contract.md` and `references/artifact-schemas.md`, then create or inspect the project workspace.
2. Read `references/workflow.md` to select the current phase and quality gate.
3. Load only the relevant role file under `references/roles/`.
4. If revising comments, also read `references/revision-protocol.md`.
5. If producing or checking DOCX/PDF formatting, also read `references/format-protocol.md`.

For a new workspace, run:

```bash
python3 scripts/init_paper_project.py /absolute/path/to/project
```

## Non-negotiable rules

- Treat `00-input/requirements.md` and `00-input/format-profile.yaml` as the user's source of truth. Never invent missing institutional requirements.
- Store claims, sources, data, and citation status in the evidence ledger. Never invent bibliographic metadata, quotations, page numbers, DOIs, URLs, statistics, or research results.
- The coordinator owns task routing and integration. Specialists write their assigned artifacts; they do not silently overwrite another role's output.
- Use parallel agents only for independent, bounded tasks. Serialize outline approval, global integration, formatting, and final acceptance.
- Preserve every substantive revision in the comment ledger and change log. Keep the original comment text.
- A checker reports issues and gate status; it does not silently rewrite the paper it is judging.
- Require human confirmation when a comment is ambiguous, two requirements conflict, or a change would alter the research question, methodology, findings, or claimed evidence.
- Academic integrity remains the user's responsibility. Label unverified or AI-generated material clearly and follow the user's institution and publication policies.

## Role routing

Load the matching file before assigning work:

- Overall coordination: `references/roles/global-planner.md`
- Outline design: `references/roles/outline-architect.md`
- Research and data: `references/roles/research-data.md`
- Drafting and substantive editing: `references/roles/content-writer.md`
- Figures and visual assets: `references/roles/figure-designer.md`
- Document formatting: `references/roles/format-specialist.md`
- First complete-paper audit: `references/roles/global-reviewer.md`
- Comment-driven revision routing: `references/roles/revision-manager.md`
- Post-revision regression audit: `references/roles/revision-reviewer.md`

Each role file is independently replaceable. Keep the shared artifact names, schemas, and `contract_version` stable unless a migration is intentionally applied across all affected roles. Run `python3 scripts/validate_contract.py .` after changing a role or shared artifact.

## Completion

Do not call a paper final until required quality gates in `references/quality-gates.md` pass. Deliver the manuscript together with the evidence ledger, comment-response table, change log, and latest audit report when those artifacts apply.
