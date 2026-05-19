#!/usr/bin/env python3
import json
from collections import defaultdict
from pathlib import Path

data = json.loads(Path("prompt-capsules/prompt-capsules.json").read_text(encoding="utf-8"))
by = defaultdict(list)
for r in data:
    by[r["category"]].append(r)

lines = [
    "# Prompt Capsule Index",
    "",
    f"Total capsules: **{len(data)}**",
    "",
    "| Category | Count | Example |",
    "|---|---:|---|",
]
for cat in sorted(by):
    lines.append(f"| {cat} | {len(by[cat])} | `{by[cat][0]['command']}` |")

lines += ["", "## All Capsules", "", "| ID | Command | Category | Agent | Risk | Operation |", "|---|---|---|---|---|---|"]
for r in data:
    lines.append(f"| {r['id']} | `{r['command']}` | {r['category']} | {r['agent_role']} | {r['risk']} | {r['operation']} |")

Path("docs/PROMPT_INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("Built docs/PROMPT_INDEX.md")
