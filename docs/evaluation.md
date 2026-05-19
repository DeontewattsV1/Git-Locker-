# Evaluation

## What this package does well

- Converts loose prompts into auditable work packets.
- Supports JEAI-style separation of evidence, preference, dissent, and audit.
- Makes Git Locker expandable through prompt capsules.
- Adds GitHub Actions validation and guarded workflow enablement.
- Treats issue bodies, PR descriptions, and comments as untrusted unless validated.

## Risks and controls

| Risk | Control |
|---|---|
| Prompt-injection ambiguity | Publicly call them prompt capsules; internally use `/inject`. |
| Over-permissioned workflows | Default to `contents: read`; use job-level `actions: write` only where needed. |
| Agentic workflow injection | Never pipe untrusted issue/PR text into scripts without validation. |
| Repository bloat | Split by category and generate indexes. |
| False novelty claims | Mark generated ideas as unverified until checked. |
