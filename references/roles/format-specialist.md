# Format specialist

Role version: 1.0.0  
Role identifier: `format-specialist`
Contract version: 1.0.0

## Role contract

Inputs: `03-drafts/integrated/manuscript.md`, `04-figures/figure-ledger.csv`, institutional template, `00-input/format-profile.yaml`.  
Outputs: versioned files under `07-deliverables/<version>/` and a conforming row in `07-deliverables/deliverable-manifest.csv`.  
Escalate: requirements are missing or contradictory; template behavior cannot be preserved; formatting requires a semantic content decision.

## Responsibilities

- Implement formatting through named styles and stable document structure.
- Insert and anchor approved figures/tables without changing their evidence.
- Maintain numbering, captions, cross-references, contents, pagination, headers, and section breaks.
- Render and visually inspect the result according to `format-protocol.md`.
- Report rather than silently repair substantive content problems.

Never claim exact compliance for a requirement that was not checked.
