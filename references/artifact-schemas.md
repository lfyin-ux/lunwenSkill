# Artifact schemas

Contract version: `1.0.0`

These schemas are the machine-facing boundary between roles. CSV headers are ordered and required. Empty values are allowed only when information is genuinely unavailable and the corresponding status explains why.

## Enumerations

- Task status: `queued`, `in_progress`, `needs_input`, `ready_for_review`, `accepted`, `rejected`
- Evidence verification: `verified`, `partially_verified`, `unverified`, `rejected`
- Comment disposition: `pending`, `accepted`, `partially_accepted`, `rejected_with_reason`, `needs_clarification`, `not_actionable`
- Comment status: `open`, `routed`, `implemented`, `verified`, `blocked`
- Audit result: `pass`, `fail`, `blocked`, `not_applicable`
- Finding severity: `blocking`, `major`, `minor`, `suggestion`
- Figure status: `planned`, `in_progress`, `ready_for_review`, `approved`, `rejected`
- Impact-map status: use the task-status enumeration
- Deliverable status: `draft`, `under_review`, `rejected`, `approved`, `final`

## CSV contracts

### `01-plan/task-board.csv`

`task_id,role,objective,inputs,outputs,constraints,acceptance,dependencies,status,notes`

Multiple paths or values inside a cell use ` | ` as the separator.

### `01-plan/terminology.csv`

`term,definition,preferred_form,avoid,notes`

### `02-evidence/evidence-ledger.csv`

`claim_id,source_id,data_id,claim,source_title,authors,year,venue,doi_or_url,pages_or_location,accessed_at,verification_status,notes`

### `04-figures/figure-ledger.csv`

`artifact_id,type,title,manuscript_location,data_source,source_path,output_path,provenance,status,notes`

### `05-revisions/comment-ledger.csv`

`comment_id,parent_comment_id,source,author,anchor,original_comment,classification,primary_role,impact_scope,disposition,status,notes`

### `05-revisions/impact-map.csv`

`comment_id,affected_artifact,affected_location,change_type,responsible_role,task_id,status,notes`

### `05-revisions/change-log.csv`

`change_id,comment_id,role,before_summary,after_summary,locations,evidence_changes,reviewer,verification_status,notes`

Here `verification_status` uses the audit-result enumeration.

### `07-deliverables/deliverable-manifest.csv`

`version,created_at,source_manuscript,docx_path,pdf_path,format_profile,audit_report,status,notes`

## Markdown contracts

- `project-brief.md`: objective, research question, scope, method, constraints, deliverables, approvals, open questions.
- `outline.md`: section ID, heading, purpose, claims, evidence needs, dependencies, word budget, planned figures/tables, approval status.
- Section drafts: section ID, outline version, body, claim/source links, open issues, requested figures/tables.
- `manuscript.md`: version, source section versions, integrated content, unresolved issues.
- Audit report: paper version, audit type, reviewer role, date, gate decision, and finding table from the template.

## Version rules

- Use immutable paper versions such as `v0.1.0`, `v0.2.0`, and `v1.0.0`; do not overwrite an approved deliverable directory.
- Every manifest row points to the exact source manuscript and audit report used for that version.
- The revision reviewer compares the latest formatted deliverable against its declared predecessor, not an unformatted working draft.
