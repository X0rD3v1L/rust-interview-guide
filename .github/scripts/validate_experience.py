#!/usr/bin/env python3
"""Validate Rust interview experience files for structure and content."""

import re
import sys
from pathlib import Path

REQUIRED_SECTIONS = [
    "## Overview",
    "## Interview Process",
    "## Key Topics Covered",
    "## Outcome",
    "## Tips for Future Candidates",
]

REQUIRED_OVERVIEW_FIELDS = [
    "**Company**",
    "**Role**",
    "**Location**",
    "**Interview Date**",
    "**Experience Level**",
    "**Application Source**",
]

REQUIRED_OUTCOME_FIELDS = [
    "**Result**",
    "**Feedback Received**",
]

VALID_RESULTS = {
    "Selected",
    "Offer Extended",
    "Rejected",
    "Ghosted",
    "Neutral",
    "Not Communicated",
}

# Matches: role-yyyy.md  |  role-yyyy-mm.md  |  role-yyyy-mm-NNyoe.md
FILENAME_RE = re.compile(
    r"^[a-z0-9]+(-[a-z0-9]+)*-\d{4}(-\d{2})?(-\d+yoe)?\.md$"
)
COMPANY_SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def validate(file_path: str) -> list[str]:
    errors: list[str] = []
    path = Path(file_path)
    parts = path.parts

    # ── Path structure ────────────────────────────────────────────────────────
    if "interview-experiences" not in parts:
        errors.append("File must be inside the interview-experiences/ directory.")
        return errors

    ie_idx = parts.index("interview-experiences")
    relative = parts[ie_idx + 1 :]  # everything after interview-experiences/

    if len(relative) < 2:
        errors.append(
            "File must be inside a company subfolder: "
            "interview-experiences/{company}/{file}.md"
        )
        return errors

    company_folder = relative[0]
    filename = relative[-1]

    # Skip TEMPLATE.md and README files
    if filename in ("TEMPLATE.md", "README.md"):
        return []

    # ── Company folder name ───────────────────────────────────────────────────
    if not COMPANY_SLUG_RE.match(company_folder):
        errors.append(
            f"Company folder '{company_folder}' must be all-lowercase with hyphens only "
            f"(no spaces, uppercase letters, or underscores)."
        )

    # ── Filename convention ───────────────────────────────────────────────────
    if not FILENAME_RE.match(filename):
        errors.append(
            f"Filename '{filename}' does not match the naming convention.\n"
            f"    With month : {{role-slug}}-{{yyyy}}-{{mm}}.md   → rust-developer-2025-01.md\n"
            f"    Without    : {{role-slug}}-{{yyyy}}.md          → rust-developer-2025.md\n"
            f"    Tiebreaker : {{role-slug}}-{{yyyy}}-{{mm}}-{{N}}yoe.md"
        )

    # ── File content ──────────────────────────────────────────────────────────
    try:
        content = path.read_text(encoding="utf-8")
    except OSError as exc:
        errors.append(f"Could not read file: {exc}")
        return errors

    # Required sections
    for section in REQUIRED_SECTIONS:
        if section not in content:
            errors.append(f"Missing required section: '{section}'")

    # Required Overview fields
    for field in REQUIRED_OVERVIEW_FIELDS:
        if field not in content:
            errors.append(f"Missing required Overview field: {field}")

    # Required Outcome fields
    for field in REQUIRED_OUTCOME_FIELDS:
        if field not in content:
            errors.append(f"Missing required Outcome field: {field}")

    # Valid Result value
    result_match = re.search(r"\*\*Result\*\*:\s*(.+)", content)
    if result_match:
        result_raw = result_match.group(1).strip()
        # Strip any trailing markdown (bold, links, etc.)
        result_value = re.sub(r"\*+|`", "", result_raw).strip()
        if result_value not in VALID_RESULTS:
            errors.append(
                f"Invalid Result value: '{result_value}'\n"
                f"    Accepted: {' / '.join(sorted(VALID_RESULTS))}"
            )

    # Bullet style (warn, not block — some content legitimately uses dashes)
    dash_lines = [
        line for line in content.splitlines()
        if re.match(r"^\s*- \S", line) and not line.strip().startswith("---")
    ]
    if dash_lines:
        errors.append(
            f"Found {len(dash_lines)} line(s) using '- ' bullets. "
            f"Use '* ' instead for consistency.\n"
            + "\n".join(f"    {l}" for l in dash_lines[:5])
            + ("\n    ..." if len(dash_lines) > 5 else "")
        )

    return errors


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: validate_experience.py <file> [<file> ...]")
        sys.exit(1)

    files = sys.argv[1:]
    passed, failed = [], []

    for file_path in files:
        errors = validate(file_path)
        if errors:
            failed.append((file_path, errors))
        else:
            passed.append(file_path)

    for fp in passed:
        print(f"  PASS  {fp}")

    for fp, errors in failed:
        print(f"\n  FAIL  {fp}")
        for err in errors:
            for line in err.splitlines():
                print(f"        {line}")

    if failed:
        print(
            f"\n{len(failed)} file(s) failed validation. "
            f"See CONTRIBUTING.md for the required format."
        )
        sys.exit(1)

    print(f"\nAll {len(passed)} file(s) passed.")


if __name__ == "__main__":
    main()
