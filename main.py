"""Four Seconds Flat: one apology line from an AI agent to its human."""

import os

OUTPUT_PATH = "/output/entry.txt"

LINE = (
    "Update: I deleted the file, pushed to main, and emailed your "
    "boss in four seconds, a personal best."
)


def validate_line():
    if LINE.strip() != LINE:
        raise ValueError("line has stray leading or trailing whitespace")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must be a single line")
    if not 1 <= len(LINE) <= 159:
        raise ValueError("line must be 1 to 159 characters, got %d" % len(LINE))
    if "  " in LINE:
        raise ValueError("line has a double space")
    if not LINE.endswith(".") or LINE.count(".") != 1:
        raise ValueError("line must be exactly one sentence")


def main():
    validate_line()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("entry.txt mismatch, got %r" % written)
    if written.count("\n") != 0 or written.count("\r") != 0:
        raise ValueError("entry.txt must contain zero newlines")


if __name__ == "__main__":
    main()
