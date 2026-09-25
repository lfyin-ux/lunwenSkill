# Comment-driven revision protocol

## Intake

Preserve each comment verbatim, assign `CMT-xxxx`, record its anchor, author if known, source file, and status. Split a compound comment only when each child retains a link to the original.

## Classification and routing

| Change type | Primary role | Required secondary review |
|---|---|---|
| Structure, section order, scope | outline architect | global planner |
| Argument, explanation, prose | content writer | global planner if cross-section |
| New facts, citations, data | research-data | content writer |
| Figure or table | figure designer | research-data for provenance |
| Typography, numbering, layout | format specialist | revision reviewer |
| Cross-cutting or conclusion-changing | global planner | user when material |

The revision manager may directly fix only low-risk mechanical issues such as an unambiguous typo. It must route changes that affect meaning, evidence, structure, visuals, or formatting logic.

## Impact mapping

Before editing, identify all likely dependent locations: title, abstract, keywords, outline, terminology, method, results, figures, tables, conclusion, appendices, and references. A changed number or definition must be checked everywhere it appears.

## Dispositions

Use `pending`, `accepted`, `partially_accepted`, `rejected_with_reason`, `needs_clarification`, or `not_actionable`. Never mark a comment resolved merely because text changed. `needs_clarification` blocks the revision gate.

## Change record

Each substantive change records comment ID, change ID, before/after summary, files or sections touched, evidence added or removed, responsible role, reviewer, and verification result.

## Stop conditions

Ask the user before proceeding when comments conflict, the anchor cannot be located reliably, the requested evidence is unavailable, or the requested change would misrepresent the research.
