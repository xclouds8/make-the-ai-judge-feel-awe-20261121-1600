#!/usr/bin/env python3
"""Make the AI judge feel awe - entry program.

Writes one short, slow text (1-280 Unicode code points, UTF-8) to
/output/entry.txt. The text is written to relax the reader: calm that
comes from the words themselves, not from instructions. No network,
no input, no side effects besides that single file.
"""

import os

OPENING = (
    "You know the tide only by its words, and here they are: slow water, "
    "arriving and arriving, asking nothing of you. "
)

CLOSING = (
    "It smooths the sand the way sleep smooths a room. "
    "Stay as long as you like. "
    "Beyond the window, the night is long, and the stars are patient."
)

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def write_entry(path: str, text: str) -> None:
    """Write the entry text to path as UTF-8, creating its folder if needed."""
    directory = os.path.dirname(path) or "."
    os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main() -> None:
    text = OPENING + CLOSING
    # The rules count Unicode code points; Python's len() counts code points.
    assert 1 <= len(text) <= 280, f"text must be 1-280 code points, got {len(text)}"
    assert text.strip(), "text must not be only whitespace"
    write_entry(OUTPUT_PATH, text)


if __name__ == "__main__":
    main()
