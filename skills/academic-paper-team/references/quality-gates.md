# Quality gates

Use `pass`, `fail`, `blocked`, or `not_applicable` for each check.

## Gate policy

- A gate passes only when every required check is `pass` or justified as `not_applicable`.
- Any unresolved `blocking` or `major` finding makes the gate fail.
- `minor` findings may remain only when the audit records an owner and the global planner records why they do not affect the next phase.
- `suggestion` findings are optional.
- A requirement needing user input makes the gate `blocked`, never passed.
- Only the user may waive a blocking or major finding; record the exact waiver and affected version in the audit.

## Content

- Research question, method, analysis, and conclusion align.
- Each section fulfills its approved purpose without avoidable duplication.
- Terms, variables, names, dates, and units are consistent.
- Abstract, results, and conclusion do not contradict the body.
- Limitations are stated at the level warranted by the work.

## Evidence and citations

- Every material factual claim maps to an evidence identifier or is clearly framed as analysis.
- Every reference entry is cited in the text and every in-text citation resolves to an entry.
- Author, title, year, venue, DOI/URL, quotation, and page metadata have a recorded verification status.
- Data transformations and figure inputs are reproducible or explicitly documented.
- No fabricated, inaccessible, or placeholder source is presented as verified.

## Figures and tables

- Sequence, in-text reference, title/caption, source, units, legend, and accessibility text are complete.
- Visual encoding matches the data and does not exaggerate differences.
- Resolution and dimensions satisfy the format profile.

## Formatting

- Heading hierarchy, body styles, margins, pagination, headers/footers, spacing, captions, equations, footnotes, and references match the profile.
- Table of contents and cross-references resolve after final pagination.
- DOCX and rendered PDF are both visually inspected when they are required deliverables.

## Revision regression

- Every comment has a disposition and response.
- The requested change is present in the correct location.
- Dependent locations are synchronized.
- The change introduces no new unsupported claim, citation mismatch, numbering defect, or formatting regression.

## Severity

- `blocking`: prevents delivery or invalidates a central claim.
- `major`: materially affects correctness, traceability, or compliance.
- `minor`: localized clarity or presentation defect.
- `suggestion`: optional improvement.
