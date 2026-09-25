#!/usr/bin/env python3
"""Create a paper workspace from this skill's reusable template."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path, help="New or empty project directory")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Copy missing template files into a non-empty directory; never overwrite existing files",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    destination = args.destination.expanduser().resolve()
    template = Path(__file__).resolve().parent.parent / "assets" / "project-template"

    if not template.is_dir():
        raise SystemExit(f"Template not found: {template}")

    if destination.exists() and any(destination.iterdir()) and not args.force:
        raise SystemExit(
            f"Destination is not empty: {destination}\n"
            "Use a new directory or pass --force to add only missing files."
        )

    destination.mkdir(parents=True, exist_ok=True)
    created = 0
    skipped = 0
    for source in sorted(template.rglob("*")):
        relative = source.relative_to(template)
        target = destination / relative
        if source.is_dir():
            target.mkdir(parents=True, exist_ok=True)
            continue
        if target.exists():
            skipped += 1
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        created += 1

    print(f"Initialized paper workspace: {destination}")
    print(f"Created {created} files; skipped {skipped} existing files.")
    print("Next: complete 00-input/requirements.md and 00-input/format-profile.yaml")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
