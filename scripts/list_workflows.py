#!/usr/bin/env python3
from pathlib import Path
print("| Workflow file | workflow_dispatch | repository_dispatch |")
print("|---|---:|---:|")
for p in sorted(Path(".github/workflows").glob("*.y*ml")):
    t = p.read_text(encoding="utf-8")
    print(f"| `{p}` | {'workflow_dispatch' in t} | {'repository_dispatch' in t} |")
