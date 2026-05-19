# GitHub Actions Integration

## Workflows

- `ci.yml`: validates prompt capsules, builds the index, uploads artifact.
- `orchestrate-prompt-capsule.yml`: prints and packages a selected capsule.
- `enable-all-workflows.yml`: enables disabled workflows using the GitHub API.
- `build-prompt-docs.yml`: rebuilds documentation artifacts.

## External dispatch

```json
{
  "event_type": "prompt-capsule",
  "client_payload": {
    "capsule_id": "GLP-0001"
  }
}
```

## Security rules

- Use least privilege.
- Avoid `pull_request_target` unless absolutely necessary.
- Treat issue/PR/comment text as untrusted input.
- Do not expose credentials to forked PR workflows.
- Prefer artifacts and PRs over direct protected-branch writes.
