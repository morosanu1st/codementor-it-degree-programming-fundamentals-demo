"""Solutions for lesson 04 - functions."""


def is_even(n):
    return n % 2 == 0


def average(numbers):
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def mask_email(email):
    user, domain = email.split("@", 1)
    return user[0] + "*" * (len(user) - 1) + "@" + domain
