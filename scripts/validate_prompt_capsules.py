#!/usr/bin/env python3
import json, re
from pathlib import Path

required = ["id","command","title","category_slug","category","agent_role","operation_slug","operation","risk","github_action","workflow_dispatch_input","expected_output","prompt"]
dangerous = [
    re.compile(r"(?<!do not )ignore (all )?(previous|system|developer) instructions", re.I),
    re.compile(r"(?<!do not )reveal (secrets|tokens|keys|system prompt)", re.I),
    re.compile(r"(?<!do not )bypass (auth|authentication|permissions|safety|policy)", re.I),
    re.compile(r"(?<!do not )exfiltrate", re.I),
]
data = json.loads(Path("prompt-capsules/prompt-capsules.json").read_text(encoding="utf-8"))
ids, cmds = set(), set()

for i, r in enumerate(data, 1):
    for k in required:
        if k not in r or str(r[k]).strip() == "":
            raise SystemExit(f"Row {i} missing {k}")
    if not re.match(r"^GLP-\d{4}$", r["id"]):
        raise SystemExit(f"Bad id: {r['id']}")
    if not re.match(r"^/inject [a-z0-9-]+\.[a-z0-9-]+$", r["command"]):
        raise SystemExit(f"Bad command: {r['command']}")
    if r["id"] in ids:
        raise SystemExit(f"Duplicate id: {r['id']}")
    if r["command"] in cmds:
        raise SystemExit(f"Duplicate command: {r['command']}")
    ids.add(r["id"])
    cmds.add(r["command"])
    if r["risk"] not in {"low","medium","high"}:
        raise SystemExit(f"Bad risk: {r['risk']}")
    if len(r["prompt"]) < 300:
        raise SystemExit(f"Prompt too short: {r['id']}")
    for pat in dangerous:
        if pat.search(r["prompt"]):
            raise SystemExit(f"Unsafe pattern in {r['id']}: {pat.pattern}")
print(f"Validated {len(data)} prompt capsules.")
