"""Lesson 06 - Reading and writing files.

Real programs read configuration, data and logs from files. Always open files
with `with` - Python closes them for you, even if something goes wrong.

Run:  python lessons/06_files.py
"""
import tempfile
from pathlib import Path

# We use a temporary folder so the lesson does not leave files behind.
with tempfile.TemporaryDirectory() as folder:
    notes = Path(folder) / "notes.txt"

    # Writing ("w" replaces the file, "a" appends to it)
    with open(notes, "w", encoding="utf-8") as f:
        f.write("week 1: variables\n")
        f.write("week 2: conditionals\n")
    with open(notes, "a", encoding="utf-8") as f:
        f.write("week 3: loops\n")

    # Reading line by line - memory friendly, works for huge log files too
    with open(notes, encoding="utf-8") as f:
        for number, line in enumerate(f, start=1):
            print(number, line.strip())

    # pathlib shortcut for small files
    print("Characters in file:", len(notes.read_text(encoding="utf-8")))

# ---------------------------------------------------------------------------
# EXERCISES  (solutions in solutions/lesson06_files.py)
#   1. count_lines(path): number of lines in a text file.
#   2. write_lines(path, lines): write each item of the list on its own line.
#   3. find_lines(path, word): list of lines (without "\n") containing word,
#      case-insensitive.
# ---------------------------------------------------------------------------
