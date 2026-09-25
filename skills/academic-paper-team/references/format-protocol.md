# Format protocol

The format profile is data, not prose. Populate `00-input/format-profile.yaml` from the user's instructions or institutional template. Leave unknown values empty and report them.

## Required domains

- page size, margins, orientation, columns;
- title page and front matter;
- heading levels, numbering, font, size, weight, spacing, breaks;
- body font, size, line spacing, indentation, paragraph spacing;
- headers, footers, page-number scheme and section breaks;
- figures, tables, equations, notes and caption rules;
- table of contents, lists of figures/tables and cross-references;
- citation and bibliography style;
- appendix rules;
- output filename and required formats.

## Implementation rules

- Prefer named document styles and template inheritance over direct per-paragraph formatting.
- Preserve semantic heading levels so navigation and the table of contents work.
- Do not alter scholarly meaning while formatting. Report content defects separately.
- Recalculate fields, references, numbering, and the table of contents before delivery when the document tooling supports it.
- Render the final document to pages and visually inspect representative and risk-heavy pages: title page, contents, first page of each heading level, dense tables, figures, equations, references, and appendices.
- Record any format requirement that could not be verified automatically.
