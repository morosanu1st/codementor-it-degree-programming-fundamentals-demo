"""Capstone part 3 - Hashing vs. encryption, and safe password storage.

See CYBERSECURITY_BASICS.md for the explanation.

Run:  python -m capstone.hashing_demo
"""
import hashlib
import hmac
import secrets

PBKDF2_ITERATIONS = 600_000  # OWASP 2023+ guidance for PBKDF2-HMAC-SHA256


def sha256_hex(text):
    """Plain SHA-256: great for checking file integrity, NOT for passwords."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def hash_password(password, salt=None, iterations=PBKDF2_ITERATIONS):
    """Return 'pbkdf2_sha256$iterations$salt_hex$hash_hex'.

    * A random salt makes identical passwords produce different hashes.
    * Many iterations make every guess slow for an attacker.
    """
    if salt is None:
        salt = secrets.token_bytes(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, iterations)
    return f"pbkdf2_sha256${iterations}${salt.hex()}${digest.hex()}"


def verify_password(password, stored):
    """Check a password against a value produced by hash_password()."""
    try:
        algorithm, iterations, salt_hex, hash_hex = stored.split("$")
    except ValueError:
        return False
    if algorithm != "pbkdf2_sha256":
        return False
    candidate = hash_password(password, bytes.fromhex(salt_hex), int(iterations))
    # compare_digest takes the same time whether the first or last byte
    # differs, so attackers cannot learn anything from response timing.
    return hmac.compare_digest(candidate.split("$")[3], hash_hex)


def main():
    print("SHA-256('hello')  =", sha256_hex("hello"))
    print("SHA-256('hello!') =", sha256_hex("hello!"), "<- one character, totally different")
    stored = hash_password("correct horse battery staple", iterations=100_000)
    print("Stored password  =", stored[:60] + "...")
    print("Right password?  ", verify_password("correct horse battery staple", stored))
    print("Wrong password?  ", verify_password("Tr0ub4dor&3", stored))


if __name__ == "__main__":
    main()
