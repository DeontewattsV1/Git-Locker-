# Artifact Index

This repository was developed alongside several generated artifact packages. Some packages were produced in the ChatGPT sandbox and may need to be uploaded manually if not already committed.

## Generated packages

| Artifact | Purpose | Status |
|---|---|---|
| `git-locker-repo.zip` | Initial Git Locker repository scaffold with 1,000 repo concepts | Generated externally |
| `git-locker-prompt-capsules.zip` | 1,000 controlled `/inject` prompt capsules with GitHub Actions | Generated externally |
| `git-lockers-brand-assets.zip` | Logo, social preview, README hero banner | Generated externally |

## Recommended repository placement

```text
assets/
  git-lockers-logo.svg
  git-lockers-logo.png
  git-lockers-social-preview-1280x640.png
  git-lockers-readme-hero.svg
  git-lockers-readme-hero.png

docs/
  BRAND_IDENTITY.md
  ARTIFACT_INDEX.md
  PRIVACY_REDACTIONS.md
  ROADMAP.md

prompt-capsules/
  prompt-capsules.json
  prompt-capsules.csv
  PROMPT_CAPSULES.md

.github/workflows/
  ci.yml
  orchestrate-prompt-capsule.yml
  enable-all-workflows.yml
  build-prompt-docs.yml
```

## Next manual upload checklist

- [ ] Upload brand assets into `assets/`
- [ ] Upload prompt capsule package contents into `prompt-capsules/`, `scripts/`, `schema/`, and `.github/workflows/`
- [ ] Upload Git Locker data into `data/` and `LOCKER.md`
- [ ] Enable GitHub Actions after reviewing permissions
- [ ] Set GitHub social preview using `git-lockers-social-preview-1280x640.png`
