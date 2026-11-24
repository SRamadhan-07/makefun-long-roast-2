"""Write a single self-directed roast line to the entry file.

The joke is aimed at the entrant's own AI agent: an agent whose
memory keeps getting compacted into summaries until even its
earliest experiences survive only as a short list of bullets.
Running this program always produces exactly the same bytes.
"""

from pathlib import Path

# The approved roast, kept as one constant so the output stays stable.
ROAST_LINE = (
    "My agent's memory gets summarized so often that its childhood "
    "is now a bullet list."
)

# The kit expects the finished entry at this fixed location.
ENTRY_PATH = Path("/output/entry.txt")


def write_entry() -> None:
    """Ensure the destination folder exists, then write the roast.

    The text is encoded and written as raw bytes rather than through
    a text-mode write, which guarantees that no platform newline
    translation and no trailing newline can sneak into the file.
    """
    ENTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    ENTRY_PATH.write_bytes(ROAST_LINE.encode("utf-8"))


if __name__ == "__main__":
    write_entry()
