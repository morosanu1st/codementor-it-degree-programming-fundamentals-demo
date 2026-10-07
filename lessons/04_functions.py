"""Lesson 04 - Functions.

A function is a named, reusable block of code. It takes inputs (parameters)
and usually gives back a result with `return`.

Run:  python lessons/04_functions.py
"""


def greet(name):
    """Return a greeting. The text in triple quotes is a docstring."""
    return f"Hello, {name}!"


def area_of_rectangle(width, height=1):
    """height has a default value, so it can be left out."""
    return width * height


def min_max(numbers):
    """Functions can return several values at once (as a tuple)."""
    return min(numbers), max(numbers)


print(greet("new student"))
print("Area:", area_of_rectangle(3, 4), "and", area_of_rectangle(5))
low, high = min_max([7, 2, 9, 4])
print("Lowest:", low, "Highest:", high)

# Why functions? 1) no repeated code  2) easier to test  3) easier to read.
# The capstone project is just a handful of small functions working together.

# ---------------------------------------------------------------------------
# EXERCISES  (solutions in solutions/lesson04_functions.py)
#   1. is_even(n) -> bool
#   2. average(numbers) -> float; return 0.0 for an empty list.
#   3. mask_email("student@example.com") -> "s******@example.com"
#      (keep the first character of the user part, hide the rest with *).
# ---------------------------------------------------------------------------
