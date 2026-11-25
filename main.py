"""One Line, Big Laugh — entry program.

Writes one funny line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Python 3.13, stdlib only, deterministic.
"""

import os

# The joke: a smoke detector's 3 a.m. beep is every homeowner's
# least favourite sound. The turn reframes it — not a warning at
# all, but a polite ghost doing a welfare check, and the punch is
# that the human is awake enough to ignore it anyway. One line,
# 133 chars, inside the 1-200 gate, no trailing newline.
LINE = (
    "My smoke detector beeps once at 3 a.m. every night \u2014 "
    "not a warning, just a polite ghost checking I'm still "
    "awake enough to ignore it."
)


def main() -> None:
    # Deterministic: same bytes on every run, no randomness, no I/O
    # besides the single output file.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
