---
name: testing-git-locker
description: End-to-end testing procedure for Git-Locker- repository. Use when validating data integrity, README rendering, or documentation quality.
---

# Testing Git-Locker-

## Overview

Git-Locker- is a static data repository containing 1,000 locker seeds and 1,000 prompt capsules. Testing focuses on data validation, visual rendering, and documentation quality — there is no server or API to test.

## Prerequisites

- Python 3.10+ (for validation scripts)
- Node.js (for `npx markdownlint-cli2`)
- Browser access to GitHub (for visual rendering tests)

## Devin Secrets Needed

None — this is a public repository with no authentication required for testing.

## Test Procedure

### 1. Data Validation (Shell)

```bash
cd /home/ubuntu/repos/Git-Locker-

# Validate locker data — expect "Git Locker validation passed: 1000 items."
python3 scripts/validate-locker.py

# Validate prompt capsules — expect "Validated 1000 prompt capsules."
python3 scripts/validate_prompt_capsules.py

# Build prompt index — expect "Built docs/PROMPT_INDEX.md"
python3 scripts/build_prompt_index.py
```

### 2. Count Consistency (Shell)

```bash
# Locker CSV should have 1001 lines (1 header + 1000 data)
wc -l data/git-locker.csv

# Locker JSON should have 1000 entries
python3 -c "import json; print(len(json.load(open('data/git-locker.json'))))"

# Capsule JSON should have 1000 entries
python3 -c "import json; print(len(json.load(open('prompt-capsules/prompt-capsules.json'))))"

# Capsule CSV line count
wc -l prompt-capsules/prompt-capsules.csv
```

### 3. Brand Assets (Shell)

Verify all 6 files exist and are non-empty:
- `assets/git-lockers-logo.{svg,png}`
- `assets/git-lockers-readme-hero.{svg,png}`
- `assets/git-lockers-social-preview-1280x640.{svg,png}`

```bash
for f in assets/git-lockers-logo.svg assets/git-lockers-logo.png assets/git-lockers-readme-hero.svg assets/git-lockers-readme-hero.png assets/git-lockers-social-preview-1280x640.svg assets/git-lockers-social-preview-1280x640.png; do
  if [ -s "$f" ]; then echo "OK: $f ($(wc -c < "$f") bytes)"; else echo "FAIL: $f"; fi
done
```

### 4. README Visual Rendering (Browser)

Open `https://github.com/${GITHUB_OWNER}/Git-Locker-` and verify:
- Hero banner image renders (not broken)
- CI badges render (Validate Git Locker, Prompt Capsule CI, License)
- Table of Contents links are present
- All tables render correctly (What's Inside, Core Concepts, Configuration, Categories, Troubleshooting)
- Mermaid architecture diagram renders
- Support section shows 10 donation badge images
- Footer logo renders with tagline

Record this test if making visual verification.

### 5. Markdown Lint (Shell)

```bash
npx markdownlint-cli2 "README.md" "CONTRIBUTING.md" "SUPPORT.md"
# Expect: Summary: 0 error(s)
```

### 6. Internal File References (Shell)

Verify all files referenced in README.md exist:

```bash
for f in LOCKER.md CONTRIBUTING.md LICENSE CODE_OF_CONDUCT.md CLAUDE.md SUPPORT.md docs/BRAND_IDENTITY.md docs/ROADMAP.md docs/ARTIFACT_INDEX.md assets/git-lockers-readme-hero.svg assets/git-lockers-logo.svg; do
  if [ -f "$f" ]; then echo "OK: $f"; else echo "MISSING: $f"; fi
done
```

## Known Issues

- `scripts/build_prompt_index.py` previously had a bug where line 26 used escaped `"\\n"` instead of real `"\n"`, producing single-line output. This was fixed — if the issue recurs, check that line uses real newlines.
- The "Devin Review" status context may show as "failed" on PRs — this is just the review bot completing analysis, not an actual CI failure. The real CI jobs are "Validate Git Locker" and "Prompt Capsule CI".
- The `.markdownlint.json` config disables MD033 (inline HTML) and MD041 (first-line heading) to allow the branded hero image and badge HTML.

## Tips

- Shell tests (validation, counts, assets, lint, file references) can all run without browser interaction.
- Only the visual rendering test requires a browser — record it for user evidence.
- CSV field order matters for locker validation — check `schema/git-locker.schema.json` if validation fails.
- Prompt capsules require `id` format `GLP-NNNN`, `command` format `/inject category.operation`, `risk` one of `low/medium/high`, and `prompt` minimum 300 characters.
