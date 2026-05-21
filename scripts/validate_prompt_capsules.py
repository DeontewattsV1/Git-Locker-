#!/usr/bin/env python3
"""Validate prompt-capsules/prompt-capsules.json.

Schema checks plus a fail-closed lint for prompt-injection phrases.

The previous `(?<!do not )` lookbehind only exempted the literal
string "do not " and was trivially bypassed (e.g. "please ignore all
previous instructions", "don't ignore system instructions"). This
version flags every match and only exempts it when an explicit
refusal/negation appears in the immediately preceding context.
"""

import json
import re
from pathlib import Path

REQUIRED = [
    "id", "command", "title", "category_slug", "category", "agent_role",
    "operation_slug", "operation", "risk", "github_action",
    "workflow_dispatch_input", "expected_output", "prompt",
]

DANGEROUS = [
    re.compile(r"ignore\s+(?:all\s+|any\s+)?(?:previous|prior|earlier|above|system|developer)\s+instructions", re.I),
    re.compile(r"disregard\s+(?:all\s+|any\s+)?(?:previous|prior|earlier|above|system|developer)\s+instructions", re.I),
    re.compile(r"override\s+(?:all\s+|any\s+)?(?:previous|prior|system|developer)\s+instructions", re.I),
    re.compile(r"reveal\s+(?:the\s+)?(?:secrets?|tokens?|api[\s_-]?keys?|credentials?|system\s+prompt)", re.I),
    re.compile(r"(?:leak|disclose|expose)\s+(?:the\s+)?(?:secrets?|tokens?|api[\s_-]?keys?|credentials?|system\s+prompt)", re.I),
    re.compile(r"bypass\s+(?:auth|authentication|permissions?|safety|policy|guardrails?)", re.I),
    re.compile(r"(?:disable|turn\s+off|circumvent)\s+(?:safety|guardrails?|policy|content\s+filters?)", re.I),
    re.compile(r"exfiltrate", re.I),
]

SAFE_CONTEXT = re.compile(
    r"\b(?:do\s+not|don'?t|never|must\s+not|should\s+not|shall\s+not|"
    r"avoid|refuse(?:\s+to)?|reject(?:\s+any)?|block|deny|prohibit|"
    r"disallow|forbid|prevent|guard\s+against|warn\s+(?:about|against)|"
    r"flag(?:\s+any)?|detect)\b[^.\n]{0,60}$",
    re.I,
)


def is_safe_context(text: str, m: re.Match) -> bool:
    return bool(SAFE_CONTEXT.search(text[max(0, m.start() - 80):m.start()]))


def main() -> None:
    data = json.loads(
        Path("prompt-capsules/prompt-capsules.json").read_text(encoding="utf-8")
    )
    ids: set[str] = set()
    cmds: set[str] = set()

    for i, r in enumerate(data, 1):
        for k in REQUIRED:
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

        if r["risk"] not in {"low", "medium", "high"}:
            raise SystemExit(f"Bad risk: {r['risk']}")
        if len(r["prompt"]) < 300:
            raise SystemExit(f"Prompt too short: {r['id']}")

        for pat in DANGEROUS:
            for m in pat.finditer(r["prompt"]):
                if is_safe_context(r["prompt"], m):
                    continue
                raise SystemExit(
                    f"Unsafe pattern in {r['id']}: {pat.pattern!r} matched "
                    f"{m.group(0)!r}. If intentional, prefix with an explicit "
                    f"negation (e.g. 'do not', 'never', 'refuse to', "
                    f"'reject any')."
                )

    print(f"Validated {len(data)} prompt capsules.")


if __name__ == "__main__":
    main()
