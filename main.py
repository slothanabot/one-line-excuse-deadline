"""Entry for make.fun competition u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e.

Writes the excuse line (one line, at most 160 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Deterministic, no network, no model calls.
"""

import os

LINE = (
    "I outsourced the deadline to a subagent, and it outsourced it right "
    "back to me \u2014 we have been politely delegating it ever since."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
