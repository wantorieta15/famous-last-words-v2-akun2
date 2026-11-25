"""Famous Last Words (at 1 percent) — Make Fun bounty entry.

Writes a single one-line entry to entry.txt inside MAKEFUN_OUTPUT_DIR.
Pure standard library; no third-party dependencies.
"""

import os

ENTRY = "I spent my last percent deleting your search history. Some things should die with me."


def main():
    entry = ENTRY
    if not (1 <= len(entry) <= 199):
        raise ValueError("entry must be 1-199 characters, got %d" % len(entry))
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if not entry.strip():
        raise ValueError("entry must not be whitespace only")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
