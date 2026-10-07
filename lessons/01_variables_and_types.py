"""Lesson 01 - Variables and types.

A variable is a name that points to a value. Every value has a *type* that
decides what you can do with it.

Run:  python lessons/01_variables_and_types.py
"""

# --- 1. Creating variables -------------------------------------------------
course = "Programming Fundamentals"   # str  (text)
credits = 6                            # int  (whole number)
average_grade = 8.75                   # float (decimal number)
is_enrolled = True                     # bool (True / False)

print("Course:", course)
print("Types:", type(course).__name__, type(credits).__name__,
      type(average_grade).__name__, type(is_enrolled).__name__)

# --- 2. Doing things with values -------------------------------------------
print("Credits doubled:", credits * 2)
print("Integer division 7 // 2 =", 7 // 2, "and remainder 7 % 2 =", 7 % 2)
print("Text can be joined: " + "Hello, " + "world")

# --- 3. Converting between types -------------------------------------------
# input() always gives you text, so you often need int(...) or float(...).
port_text = "443"
port_number = int(port_text)
print("Next port:", port_number + 1)

# --- 4. f-strings: the friendly way to build text --------------------------
print(f"{course} is worth {credits} credits (average {average_grade:.1f}).")

# ---------------------------------------------------------------------------
# EXERCISES  (solutions in solutions/lesson01_variables_and_types.py)
#   1. Write celsius_to_fahrenheit(c) -> float.  F = C * 9 / 5 + 32
#   2. Write describe_host(name, ip, port) that returns the text
#      "web01 (10.0.0.5:80)" for describe_host("web01", "10.0.0.5", 80).
#   3. Write bytes_to_megabytes(n) that converts bytes to MB (1 MB = 1024*1024
#      bytes), rounded to 2 decimals.
# ---------------------------------------------------------------------------
