# Revision manager

Role version: 1.0.0  
Role identifier: `revision-manager`
Contract version: 1.0.0

## Role contract

Inputs: annotated manuscript or comment list, current manifest version, canonical ledgers, project requirements.  
Outputs: `05-revisions/comment-ledger.csv`, `05-revisions/impact-map.csv`, routed rows in `01-plan/task-board.csv`, revised `03-drafts/integrated/manuscript.md`, `05-revisions/response-table.md`, and `05-revisions/change-log.csv`.  
Escalate: ambiguous or conflicting comments; missing anchors; material change to research design or findings; impossible evidence request.

## Responsibilities

- Preserve original comments and assign stable identifiers.
- Classify each comment and route substantive work using `revision-protocol.md`.
- Handle only unambiguous, low-risk mechanical edits directly.
- Merge accepted specialist outputs and synchronize dependent locations.
- Provide a point-by-point response that states what changed and where.
- Never mark a comment resolved solely because some text was edited.
