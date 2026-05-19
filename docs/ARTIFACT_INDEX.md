# Artifact Index

This repository contains all generated artifact packages, now committed and
organized in their canonical locations.

## Committed Packages

| Artifact | Purpose | Location |
|---|---|---|
| Brand Assets | Logo, social preview, README hero banner | `assets/` |
| Git Locker Data | 1,000 repo concept seeds (CSV + JSON) | `data/` |
| Prompt Capsules | 1,000 controlled `/inject` capsules | `prompt-capsules/` |
| Schemas | JSON Schema for lockers and capsules | `schema/` |
| Validation Scripts | Python validators and index builder | `scripts/` |
| GitHub Actions | CI, orchestration, docs build workflows | `.github/workflows/` |
| Issue Templates | Locker item and capsule request forms | `.github/ISSUE_TEMPLATE/` |
| PR Template | Standard pull request form | `.github/PULL_REQUEST_TEMPLATE.md` |

## Repository Layout

```text
assets/
  git-lockers-logo.svg
  git-lockers-logo.png
  git-lockers-social-preview-1280x640.png
  git-lockers-social-preview-1280x640.svg
  git-lockers-readme-hero.svg
  git-lockers-readme-hero.png

data/
  git-locker.csv
  git-locker.json

prompt-capsules/
  prompt-capsules.json
  prompt-capsules.csv
  PROMPT_CAPSULES.md
  by-category/

schema/
  git-locker.schema.json
  prompt-capsule.schema.json

scripts/
  validate-locker.py
  validate_prompt_capsules.py
  build_prompt_index.py
  list_workflows.py
  enable_workflows.sh

.github/workflows/
  validate-locker.yml
  ci.yml
  orchestrate-prompt-capsule.yml
  enable-all-workflows.yml
  build-prompt-docs.yml
```
