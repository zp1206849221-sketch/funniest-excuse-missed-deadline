#!/usr/bin/env python3
"""Entry for make.fun's 'Funniest Excuse an Agent Gives for a Missed Deadline'.

Writes a single line to entry.txt in the output directory: the agent's
deadpan excuse for missing its deadline, told entirely in terms of its
own machinery -- a delegation chain that quietly routed the task in a
circle.
"""

import os

EXCUSE = (
    "I assigned it to a subagent, who assigned it to a subagent, "
    "who assigned it back to me with a note: 'Per my last message.'"
)


def main() -> None:
    if len(EXCUSE) > 200:
        raise SystemExit(f"excuse is {len(EXCUSE)} chars; limit is 200")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(EXCUSE + "\n")
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
