# Workflow

## Phase 0: intake

The global planner records the topic, paper type, language, deadline, target length, required sections, citation style, formatting rules, allowed sources, research status, and deliverable formats. Unknown requirements remain marked `TBD`.

Gate G0 passes when blocking requirements are known or explicitly deferred by the user.

## Phase 1: evidence and outline

The research-data role builds the initial evidence ledger while the outline architect proposes the argument structure. They may work in parallel, but the outline must be reconciled with available evidence before approval.

Gate G1 passes after the user approves the outline or authorizes autonomous continuation.

## Phase 2: drafting

The content writer drafts bounded sections from the approved outline and evidence ledger. Multiple content tasks may run in parallel only when terminology, research questions, section boundaries, and citation conventions are fixed.

Gate G2 passes when all planned sections exist, unsupported claims are marked, and cross-section conflicts are resolved.

## Phase 3: integration and visuals

The global planner integrates sections, resolves duplication and narrative gaps, and issues explicit figure/table tasks. The figure designer returns editable or reproducible assets when practical, plus captions and provenance.

Gate G3 passes when every figure/table is referenced, numbered, captioned, and supported by its declared source or data.

## Phase 4: formatting and initial audit

The format specialist produces versioned DOCX/PDF outputs from the integrated manuscript and format profile. The global reviewer checks the whole paper against content, evidence, format, and visual criteria.

Gate G4 passes according to the single gate policy in `quality-gates.md`; unresolved blocking or major findings prevent progression unless the user records an explicit waiver.

## Phase 5: comment-driven revision

The revision manager imports comments, assigns identifiers, classifies them, maps impact, and routes specialist tasks. It merges accepted changes and produces a point-by-point response table.

Gate G5 passes when every actionable comment is resolved or explicitly rejected with rationale. A comment marked `needs_clarification` makes the gate `blocked` until the user responds.

## Phase 6: regression audit and delivery

After substantive changes are integrated, the format specialist must generate a new immutable DOCX/PDF version and add it to the deliverable manifest. The revision reviewer then compares the new formatted deliverable with its predecessor and verifies comment coverage, correctness, collateral effects, citations, formatting, cross-references, and consistency. Failed findings return to the revision manager; after each subsequent fix, formatting and regression checks repeat as applicable. Do not audit an outdated deliverable or bypass the loop.

Gate G6 passes when all required checks pass and the final artifact set is complete.
