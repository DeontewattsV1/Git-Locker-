#!/usr/bin/env bash
set -euo pipefail
: "${GITHUB_REPOSITORY:?GITHUB_REPOSITORY is required}"
: "${GH_TOKEN:?GH_TOKEN is required}"

echo "Listing workflows in ${GITHUB_REPOSITORY}"
gh workflow list --repo "$GITHUB_REPOSITORY" --all || true

mapfile -t workflows < <(gh workflow list --repo "$GITHUB_REPOSITORY" --all --json id,state --jq '.[] | select(.state != "active") | .id')
for wf in "${workflows[@]}"; do
  [[ -z "$wf" ]] && continue
  echo "Enabling workflow id: $wf"
  gh api --method PUT "repos/${GITHUB_REPOSITORY}/actions/workflows/${wf}/enable" >/dev/null
done

echo "Workflow enable pass complete."
gh workflow list --repo "$GITHUB_REPOSITORY" --all || true
