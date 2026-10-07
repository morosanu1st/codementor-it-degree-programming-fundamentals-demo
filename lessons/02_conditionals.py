"""Lesson 02 - Conditionals (if / elif / else).

Programs make decisions by checking whether something is True or False.

Run:  python lessons/02_conditionals.py
"""

grade = 7

# Comparison operators: ==  !=  <  <=  >  >=
if grade >= 9:
    print("Excellent")
elif grade >= 5:
    print("Passed")
else:
    print("Failed - book the re-exam")

# Combining conditions with and / or / not
has_password = True
has_2fa_code = False
if has_password and has_2fa_code:
    print("Login allowed")
elif has_password and not has_2fa_code:
    print("Password OK, but the 2FA code is missing")

# 'in' checks membership - very handy
port = 22
if port in (22, 23, 3389):
    print(f"Port {port} is a remote-access port - keep it closed if unused")

# ---------------------------------------------------------------------------
# EXERCISES  (solutions in solutions/lesson02_conditionals.py)
#   1. grade_to_letter(points) for 0-100: >=90 "A", >=80 "B", >=70 "C",
#      >=60 "D", else "F".
#   2. is_leap_year(year): divisible by 4, except centuries, unless divisible
#      by 400.
#   3. port_category(port): 0-1023 "well-known", 1024-49151 "registered",
#      49152-65535 "dynamic", anything else "invalid".
# ---------------------------------------------------------------------------
