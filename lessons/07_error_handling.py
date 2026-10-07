"""Lesson 07 - Error handling (try / except).

Errors (exceptions) are normal: users type letters instead of numbers, files go
missing, networks drop. Good programs expect this and react calmly.

Run:  python lessons/07_error_handling.py
"""

for text in ["42", "forty-two"]:
    try:
        number = int(text)
        print(f"'{text}' -> {number}")
    except ValueError:
        print(f"'{text}' is not a whole number")

try:
    with open("this_file_does_not_exist.txt", encoding="utf-8") as f:
        f.read()
except FileNotFoundError as error:
    print("Could not open the file:", error.filename)
finally:
    print("finally always runs - good place for clean-up")


# Raising your own errors makes bad input obvious early
def set_port(port):
    if not 0 < port < 65536:
        raise ValueError(f"port must be 1-65535, got {port}")
    return port


try:
    set_port(70000)
except ValueError as error:
    print("Rejected:", error)

# Security tip: never show full error details (stack traces, file paths,
# SQL) to end users - log them for yourself and show a friendly message.

# ---------------------------------------------------------------------------
# EXERCISES  (solutions in solutions/lesson07_error_handling.py)
#   1. safe_int(text, default=0): convert to int, return default on failure.
#   2. safe_divide(a, b): return a / b, or None when b is 0.
#   3. parse_port(text): return an int 1-65535, raise ValueError otherwise
#      (also for non-numbers).
# ---------------------------------------------------------------------------
