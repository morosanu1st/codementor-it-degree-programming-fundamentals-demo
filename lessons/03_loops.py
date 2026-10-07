"""Lesson 03 - Loops (for / while).

Loops repeat work so you don't have to copy-paste code.

Run:  python lessons/03_loops.py
"""

# for: repeat once for every item
for week in range(1, 4):            # 1, 2, 3  (the end value is not included)
    print(f"Week {week}: practise 30 minutes")

# Looping over text, one character at a time
password = "Secr3t!"
digits = 0
for ch in password:
    if ch.isdigit():
        digits += 1
print(f"'{password}' contains {digits} digit(s)")

# while: repeat as long as a condition is True
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    attempts += 1
    print(f"Login attempt {attempts} failed")
print("Account locked after", attempts, "attempts")

# break stops a loop early, continue skips to the next round
for n in range(10):
    if n % 2 == 0:
        continue          # skip even numbers
    if n > 7:
        break             # stop completely
    print("odd:", n)

# ---------------------------------------------------------------------------
# EXERCISES  (solutions in solutions/lesson03_loops.py)
#   1. sum_to(n): add up 1 + 2 + ... + n using a loop.
#   2. count_vowels(text): how many of a, e, i, o, u (any case) are in text.
#   3. fizzbuzz(n): return a list for 1..n where multiples of 3 are "Fizz",
#      of 5 "Buzz", of both "FizzBuzz", otherwise the number as a string.
# ---------------------------------------------------------------------------
