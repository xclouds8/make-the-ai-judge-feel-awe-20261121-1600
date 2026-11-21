#!/usr/bin/env python3
"""Make the AI judge feel awe - entry program.

Writes one short, slow text (1-280 Unicode code points, UTF-8) to
/output/entry.txt. The text is written to relax the reader: calm that
comes from the words themselves, not from instructions. No network,
no input, no side effects besides that single file.
"""

import os

TEXT = (
    "You know the tide only by its words, and here they are: slow water, "
    "arriving and arriving, asking nothing of you. "
    "It smooths the sand the way sleep smooths a room. "
    "Stay as long as you like. "
    "Beyond the window, the night is long, and the stars are patient."
)


def main() -> None:
    # The rules count Unicode code points; Python's len() counts code points.
    assert 1 <= len(TEXT) <= 280, f"text must be 1-280 code points, got {len(TEXT)}"
    assert TEXT.strip(), "text must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
