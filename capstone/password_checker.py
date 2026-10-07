"""Capstone part 1 - Password strength checker.

Uses only lessons 01-05: strings, conditionals, loops, functions, lists.

Run:  python -m capstone.password_checker "MyPassw0rd!"
"""
import math
import string
import sys

# A tiny sample of passwords that appear in every breach list.
COMMON_PASSWORDS = {
    "123456", "password", "123456789", "12345678", "qwerty", "111111",
    "abc123", "password1", "letmein", "admin", "welcome", "iloveyou",
    "monkey", "dragon", "football", "qwerty123", "000000", "passw0rd",
}


def character_pool_size(password):
    """How many different symbols an attacker must try per character."""
    pool = 0
    if any(c in string.ascii_lowercase for c in password):
        pool += 26
    if any(c in string.ascii_uppercase for c in password):
        pool += 26
    if any(c in string.digits for c in password):
        pool += 10
    if any(not c.isalnum() for c in password):
        pool += len(string.punctuation) + 1  # punctuation + space
    return pool


def estimate_entropy_bits(password):
    """Rough upper bound: length * log2(pool). Real attackers are smarter."""
    pool = character_pool_size(password)
    if not password or pool == 0:
        return 0.0
    return round(len(password) * math.log2(pool), 1)


def check_password(password):
    """Return (score 0-5, label, list of tips)."""
    tips = []
    if password.lower() in COMMON_PASSWORDS:
        return 0, "very weak", ["This password is in common breach lists - never use it."]

    score = 0
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
        tips.append("Use at least 12 characters (a passphrase is easiest).")
    else:
        tips.append("Too short: use at least 12 characters.")

    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        score += 1
    else:
        tips.append("Mix upper- and lower-case letters.")
    if any(c.isdigit() for c in password):
        score += 1
    else:
        tips.append("Add a digit.")
    if any(not c.isalnum() for c in password):
        score += 1
    else:
        tips.append("Add a symbol such as ! ? # or a space.")

    if has_repeated_run(password, 3):
        score = max(score - 1, 0)
        tips.append("Avoid repeating the same character 3+ times.")

    labels = ["very weak", "weak", "fair", "good", "strong", "very strong"]
    return score, labels[score], tips


def has_repeated_run(password, run_length):
    """True if any character repeats run_length times in a row (e.g. 'aaa')."""
    run = 1
    for previous, current in zip(password, password[1:]):
        run = run + 1 if current == previous else 1
        if run >= run_length:
            return True
    return False


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if not argv:
        print("usage: python -m capstone.password_checker <password>")
        return 2
    password = argv[0]
    score, label, tips = check_password(password)
    print(f"Score: {score}/5 ({label}), ~{estimate_entropy_bits(password)} bits")
    for tip in tips:
        print(" -", tip)
    return 0


if __name__ == "__main__":
    sys.exit(main())
