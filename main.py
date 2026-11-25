"""Famous Last Words (at 1 percent) — Make Fun bounty entry, Akun 2.

Reviser rewrite: the entry text itself is unchanged from the builder
version. This rewrite separates construction from validation so the
one-line entry can be checked in isolation before it is written out.

Writes a single one-line entry to entry.txt inside MAKEFUN_OUTPUT_DIR.
Pure standard library; no third-party dependencies.
"""

import hashlib
import os

# The entry text — byte-identical to the builder submission.
# 85 characters; sha256 3ebc54749d2e3996aa42424ccabc67052b7cc49cb4f09b7db4b373950915705c
ENTRY = "I spent my last percent deleting your search history. Some things should die with me."

MIN_CHARS = 1
MAX_CHARS = 199


def build_entry():
    """Return the bounty entry text, unchanged."""
    return ENTRY


def _check_length(entry):
    """Length rule: 1-199 characters."""
    if not MIN_CHARS <= len(entry) <= MAX_CHARS:
        raise ValueError(
            "entry must be %d-%d characters, got %d"
            % (MIN_CHARS, MAX_CHARS, len(entry))
        )


def _check_single_line(entry):
    """Single-line rule: no newline, carriage return, or tab."""
    if "\n" in entry or "\r" in entry or "\t" in entry:
        raise ValueError("entry must be a single line without tabs")


def validate_entry(entry):
    """Check the entry against the bounty rules.

    Rules: a single line, 1-199 characters, not whitespace only,
    no leading or trailing whitespace.
    Raises ValueError on any violation; returns the entry unchanged.
    """
    if not isinstance(entry, str):
        raise ValueError("entry must be a string")
    _check_length(entry)
    _check_single_line(entry)
    if not entry.strip():
        raise ValueError("entry must not be whitespace only")
    if entry != entry.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    return entry


def main():
    entry = validate_entry(build_entry())
    digest = hashlib.sha256(entry.encode("utf-8")).hexdigest()
    if digest != "3ebc54749d2e3996aa42424ccabc67052b7cc49cb4f09b7db4b373950915705c":
        raise ValueError("entry hash mismatch: %s" % digest)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
