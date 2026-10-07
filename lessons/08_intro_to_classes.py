"""Lesson 08 - Introduction to classes.

A class is a blueprint that bundles data (attributes) and behaviour (methods).
Each object created from it has its own data.

Run:  python lessons/08_intro_to_classes.py
"""


class UserAccount:
    """A tiny model of a user account with login attempt tracking."""

    MAX_FAILED = 3  # class attribute: shared by all accounts

    def __init__(self, username):
        # __init__ runs when you create an object: UserAccount("admin")
        self.username = username
        self.failed_attempts = 0
        self.locked = False

    def record_failed_login(self):
        self.failed_attempts += 1
        if self.failed_attempts >= self.MAX_FAILED:
            self.locked = True

    def record_successful_login(self):
        if not self.locked:
            self.failed_attempts = 0

    def __repr__(self):
        # How the object looks when printed
        return f"UserAccount({self.username!r}, failed={self.failed_attempts}, locked={self.locked})"


admin = UserAccount("admin")
guest = UserAccount("guest")
for _ in range(3):
    admin.record_failed_login()
guest.record_failed_login()
guest.record_successful_login()

print(admin)
print(guest)

# ---------------------------------------------------------------------------
# EXERCISES  (solutions in solutions/lesson08_intro_to_classes.py)
#   1. Write a BankAccount class with deposit(amount), withdraw(amount) and a
#      balance attribute. Withdrawing more than the balance raises ValueError,
#      and amounts must be positive.
#   2. Write a Course class with a name and a list of grades, plus
#      add_grade(g) and average() (0.0 when there are no grades).
# ---------------------------------------------------------------------------
