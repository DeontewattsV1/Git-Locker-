#!/usr/bin/env python3
"""Validate Git Locker CSV structure and uniqueness."""

from __future__ import annotations

import csv
import sys
from pathlib import Path

REQUIRED_FIELDS = [
    "id",
    "repo_name",
    "domain",
    "primitive_type",
    "concept",
    "foundational_primitive",
    "first_commit_mvp",
    "starter_command",
    "status",
    "license",
    "contribution_path",
]

VALID_STATUSES = {
    "open-seed-unverified",
    "research-needed",
    "validated-name",
    "claimed",
    "built",
    "deprecated",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    csv_path = Path("data/git-locker.csv")
    if not csv_path.exists():
        fail("Missing data/git-locker.csv")

    with csv_path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        if reader.fieldnames != REQUIRED_FIELDS:
            fail(f"CSV fields must be exactly: {', '.join(REQUIRED_FIELDS)}")

        ids: set[int] = set()
        names: set[str] = set()
        count = 0

        for line_number, row in enumerate(reader, start=2):
            count += 1

            for field in REQUIRED_FIELDS:
                if not row.get(field, "").strip():
                    fail(f"Line {line_number}: missing required field '{field}'")

            try:
                item_id = int(row["id"])
            except ValueError:
                fail(f"Line {line_number}: id must be an integer")

            if item_id in ids:
                fail(f"Line {line_number}: duplicate id {item_id}")
            ids.add(item_id)

            repo_name = row["repo_name"].strip()
            if repo_name in names:
                fail(f"Line {line_number}: duplicate repo_name {repo_name}")
            names.add(repo_name)

            if row["status"] not in VALID_STATUSES:
                fail(f"Line {line_number}: invalid status {row['status']}")

    print(f"Git Locker validation passed: {count} items.")


if __name__ == "__main__":
    main()
