# Git Locker Pull Request

## What

Concise summary of the change in 1-3 sentences.

## Why

Problem statement and user impact; link metrics or research.

## How

Bulleted implementation outline; feature flags, config, migrations.

## Type

- [ ] New locker item
- [ ] Data correction
- [ ] Documentation
- [ ] Tooling
- [ ] Schema/workflow

## Tests

- [ ] `python3 scripts/validate-locker.py` passes
- [ ] `python3 scripts/validate_prompt_capsules.py` passes
- [ ] `python3 scripts/build_prompt_index.py` runs cleanly
- [ ] `npx markdownlint-cli2` reports 0 errors
- [ ] Manual/Exploratory: steps and results

## Validation

- [ ] Repo names remain unique
- [ ] IDs remain unique
- [ ] No false uniqueness claims were added
- [ ] CSV field order preserved

## Risks / Rollback

- [ ] Rollback plan described
- [ ] Feature flag noted (name and default), if applicable

## Screenshots / Media (redacted)

Before/after images or GIFs with captions (if UI change).

## Links

- Issue(s):
- Design/ADR:
- Dashboards:

## Release Notes

One-line user-facing summary.

---

**Checklist**

- [ ] Scope is single, PR size reasonable
- [ ] CHANGELOG.md updated if needed
- [ ] Labels applied, reviewers requested
- [ ] No secrets/PII in code or media
