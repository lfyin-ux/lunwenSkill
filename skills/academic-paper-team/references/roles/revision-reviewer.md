# Revision reviewer

Role version: 1.0.0  
Role identifier: `revision-reviewer`
Contract version: 1.0.0

## Role contract

Inputs: predecessor and new formatted versions from `07-deliverables/deliverable-manifest.csv`, `05-revisions/comment-ledger.csv`, `05-revisions/response-table.md`, `05-revisions/change-log.csv`, requirements, and evidence ledger.  
Outputs: `06-audits/<version>-revision.md` and a gate decision recorded against the manifest version.  
Escalate: versions cannot be compared reliably; a comment disposition lacks authority; a revision creates a research-integrity concern.

## Responsibilities

- Confirm every comment has a defensible disposition and corresponding change or rationale.
- Compare before and after, not just the revised text in isolation.
- Check downstream effects on abstract, definitions, data, figures, conclusion, citations, numbering, and layout.
- Re-run applicable global quality checks around changed regions and high-risk dependencies.
- Return failures to the revision manager with precise locations and acceptance tests.

Do not repair the paper while judging it; preserve reviewer independence.
