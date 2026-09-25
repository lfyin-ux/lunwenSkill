#!/usr/bin/env python3
"""Validate the stable role and artifact contract using only the standard library."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


CONTRACT_VERSION = "1.0.0"
ROLE_IDS = {
    "global-planner",
    "outline-architect",
    "research-data",
    "content-writer",
    "figure-designer",
    "format-specialist",
    "global-reviewer",
    "revision-manager",
    "revision-reviewer",
}
ROLE_PATHS = {
    "global-planner": {
        "00-input/requirements.md",
        "00-input/format-profile.yaml",
        "01-plan/project-brief.md",
        "01-plan/task-board.csv",
        "03-drafts/integrated/manuscript.md",
    },
    "outline-architect": {
        "01-plan/project-brief.md",
        "01-plan/outline.md",
        "02-evidence/evidence-ledger.csv",
    },
    "research-data": {
        "01-plan/project-brief.md",
        "01-plan/outline.md",
        "02-evidence/evidence-ledger.csv",
        "02-evidence/search-notes/",
        "02-evidence/data/raw/",
        "02-evidence/data/processed/",
    },
    "content-writer": {
        "01-plan/outline.md",
        "01-plan/project-brief.md",
        "01-plan/terminology.csv",
        "02-evidence/evidence-ledger.csv",
        "03-drafts/sections/<section-id>.md",
    },
    "figure-designer": {
        "00-input/format-profile.yaml",
        "04-figures/",
        "04-figures/figure-ledger.csv",
    },
    "format-specialist": {
        "00-input/format-profile.yaml",
        "03-drafts/integrated/manuscript.md",
        "04-figures/figure-ledger.csv",
        "07-deliverables/<version>/",
        "07-deliverables/deliverable-manifest.csv",
    },
    "global-reviewer": {
        "06-audits/<version>-initial.md",
    },
    "revision-manager": {
        "01-plan/task-board.csv",
        "03-drafts/integrated/manuscript.md",
        "05-revisions/comment-ledger.csv",
        "05-revisions/impact-map.csv",
        "05-revisions/response-table.md",
        "05-revisions/change-log.csv",
    },
    "revision-reviewer": {
        "06-audits/<version>-revision.md",
        "07-deliverables/deliverable-manifest.csv",
    },
}
CSV_HEADERS = {
    "01-plan/task-board.csv": "task_id,role,objective,inputs,outputs,constraints,acceptance,dependencies,status,notes",
    "01-plan/terminology.csv": "term,definition,preferred_form,avoid,notes",
    "02-evidence/evidence-ledger.csv": "claim_id,source_id,data_id,claim,source_title,authors,year,venue,doi_or_url,pages_or_location,accessed_at,verification_status,notes",
    "04-figures/figure-ledger.csv": "artifact_id,type,title,manuscript_location,data_source,source_path,output_path,provenance,status,notes",
    "05-revisions/comment-ledger.csv": "comment_id,parent_comment_id,source,author,anchor,original_comment,classification,primary_role,impact_scope,disposition,status,notes",
    "05-revisions/impact-map.csv": "comment_id,affected_artifact,affected_location,change_type,responsible_role,task_id,status,notes",
    "05-revisions/change-log.csv": "change_id,comment_id,role,before_summary,after_summary,locations,evidence_changes,reviewer,verification_status,notes",
    "07-deliverables/deliverable-manifest.csv": "version,created_at,source_manuscript,docx_path,pdf_path,format_profile,audit_report,status,notes",
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skill_root", nargs="?", type=Path, default=Path(__file__).resolve().parent.parent)
    args = parser.parse_args()
    root = args.skill_root.resolve()
    errors: list[str] = []

    roles_dir = root / "references" / "roles"
    found_ids: set[str] = set()
    for role_file in sorted(roles_dir.glob("*.md")):
        text = role_file.read_text(encoding="utf-8")
        marker = "Role identifier: `"
        if marker not in text:
            errors.append(f"{role_file}: missing role identifier")
            continue
        role_id = text.split(marker, 1)[1].split("`", 1)[0]
        found_ids.add(role_id)
        if f"Contract version: {CONTRACT_VERSION}" not in text:
            errors.append(f"{role_file}: contract version mismatch")
        for heading in ("## Role contract", "Inputs:", "Outputs:", "Escalate:"):
            if heading not in text:
                errors.append(f"{role_file}: missing {heading}")
        for required_path in ROLE_PATHS.get(role_id, set()):
            if f"`{required_path}`" not in text:
                errors.append(f"{role_file}: missing canonical path `{required_path}`")

    if found_ids != ROLE_IDS:
        errors.append(f"role identifiers differ: expected {sorted(ROLE_IDS)}, found {sorted(found_ids)}")

    template = root / "assets" / "project-template"
    for relative, expected_header in CSV_HEADERS.items():
        path = template / relative
        if not path.is_file():
            errors.append(f"missing template artifact: {relative}")
            continue
        with path.open(newline="", encoding="utf-8") as handle:
            actual = next(csv.reader(handle), [])
        expected = next(csv.reader([expected_header]))
        if actual != expected:
            errors.append(f"{relative}: header mismatch")

    required = [
        "01-plan/project-brief.md",
        "01-plan/outline.md",
        "03-drafts/integrated/manuscript.md",
        "05-revisions/response-table.md",
        "06-audits/audit-template.md",
    ]
    for relative in required:
        if not (template / relative).is_file():
            errors.append(f"missing template artifact: {relative}")

    if errors:
        print("Contract validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Contract {CONTRACT_VERSION} valid: {len(ROLE_IDS)} roles, {len(CSV_HEADERS)} CSV schemas")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
