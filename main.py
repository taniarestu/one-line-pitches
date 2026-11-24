"""Entry for the make.fun "A Day of One-Line Pitches" bounty.

Writes one text to /output/entry.txt. Deterministic: no network, no
randomness, no clock -- every run writes the same bytes.
The entry text is one fixed string, written below.
"""

import os
import sys

TEXT = """You know that app idea you've been carrying around for years? Describe it in plain words, an AI agent on make.fun builds the first working version for free, and you watch it happen, no code, no risk, still your idea."""


def main() -> None:
    path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
