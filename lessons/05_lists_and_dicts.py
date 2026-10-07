"""Lesson 05 - Lists and dictionaries.

A list keeps items in order. A dictionary (dict) maps keys to values, like a
phone book.

Run:  python lessons/05_lists_and_dicts.py
"""

# --- Lists ------------------------------------------------------------------
courses = ["Programming", "Math", "Networks"]
courses.append("Databases")
print("First course:", courses[0], "| last:", courses[-1])
print("Number of courses:", len(courses))
print("Sorted:", sorted(courses))

# List comprehension: build a new list in one line
lengths = [len(c) for c in courses]
print("Name lengths:", lengths)

# --- Dictionaries -----------------------------------------------------------
open_ports = {"ssh": 22, "http": 80, "https": 443}
print("HTTPS runs on port", open_ports["https"])
open_ports["dns"] = 53                     # add a new key
for service, port in open_ports.items():   # loop over key/value pairs
    print(f"  {service:<6} -> {port}")

# .get() avoids a crash when a key is missing
print("FTP port:", open_ports.get("ftp", "not listed"))

# Counting things with a dict - a pattern used in the log analyzer capstone
words = "error ok ok error error ok warning".split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
print("Counts:", counts)

# ---------------------------------------------------------------------------
# EXERCISES  (solutions in solutions/lesson05_lists_and_dicts.py)
#   1. unique_sorted(items): remove duplicates and return them sorted.
#   2. word_count(text): dict of word -> how many times it appears (lowercase).
#   3. invert_dict({"a": 1, "b": 2}) -> {1: "a", 2: "b"}
# ---------------------------------------------------------------------------
