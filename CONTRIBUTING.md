# Contributing to Git Lockers

Git Lockers accepts new repository seeds, prompt capsules, refinements, domain
expansions, schemas, tooling, and validation workflows.

## Development Setup

Follow the [README Quickstart](./README.md#quickstart):

```bash
$ git clone https://github.com/DeontewattsV1/Git-Locker-.git
$ cd Git-Locker-
$ python3 scripts/validate-locker.py
$ python3 scripts/validate_prompt_capsules.py
```

## Good Locker Entries

A good entry is:

- Specific enough to build
- Broad enough to become reusable
- Clear about the primitive it introduces
- Not just a normal app idea
- Written with a first-commit MVP direction

## Add a New Locker Item

1. Fork the repo
2. Add a row to `data/git-locker.csv`
3. Add the same item to `data/git-locker.json`
4. Run validation:

```bash
$ python3 scripts/validate-locker.py
```

5. Open a pull request

## Add a New Prompt Capsule

1. Fork the repo
2. Add an entry to `prompt-capsules/prompt-capsules.json`
3. Add the same row to `prompt-capsules/prompt-capsules.csv`
4. Run validation:

```bash
$ python3 scripts/validate_prompt_capsules.py
```

5. Rebuild the index:

```bash
$ python3 scripts/build_prompt_index.py
```

6. Open a pull request

## Required Fields (Locker)

| Field | Description |
|---|---|
| `id` | Unique integer |
| `repo_name` | Lowercase, hyphenated |
| `domain` | Category domain |
| `primitive_type` | Type of primitive |
| `concept` | Description (min 20 chars) |
| `foundational_primitive` | Core primitive statement |
| `first_commit_mvp` | What the first commit proves |
| `starter_command` | Git init command |
| `status` | See status values below |
| `license` | License identifier |
| `contribution_path` | How to contribute |

## Status Values

| Status | Meaning |
|---|---|
| `open-seed-unverified` | New idea, not yet checked |
| `research-needed` | Needs investigation |
| `validated-name` | Name checked, available |
| `claimed` | Someone is building it |
| `built` | Repository exists |
| `deprecated` | No longer maintained |

## Coding Standards

- Format and lint before pushing
- Keep repo names lowercase and hyphenated
- Preserve CSV field order
- Never claim verified novelty without evidence
- Prefer small, composable primitives over broad app ideas
- Validate data before proposing commits

## Pull Requests

- Small, focused changes
- Include screenshots/logs for docs updates
- Link related issues
- Run validation scripts before submitting

## Branching

Create branches with descriptive names:

```bash
$ git checkout -b add/domain-name-primitive
```

## Expansion Ideas

Contributors can add:

- New domains
- Repo starter templates
- Validation scripts
- Project cards
- GitHub Actions workflows
- Examples of built projects
- Licensing improvements
- Issue templates
- Agent-readable metadata

## Ground Rule

Do not claim that an entry is "first ever" unless independent verification
has been done.
