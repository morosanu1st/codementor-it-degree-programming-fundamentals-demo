# Cybersecurity Basics for First-Year IT Students

Short, plain-language notes that go with the capstone code in `capstone/`.

## 1. The CIA triad

Almost every security question comes back to three goals:

| Goal | Plain words | Example threat | Example defence |
|------|-------------|----------------|-----------------|
| **Confidentiality** | Only the right people can *read* it | Stolen laptop, leaked database | Encryption, access control, strong passwords + 2FA |
| **Integrity** | Nobody can *change* it unnoticed | Tampered download, edited grades | Hashes/checksums, digital signatures, audit logs |
| **Availability** | It *works* when you need it | DDoS, ransomware, failed disk | Backups, redundancy, rate limiting, patching |

When you read about any attack, ask: *which of the three did it break?*

## 2. Hashing vs. encryption

| | Hashing | Encryption |
|---|---------|------------|
| Direction | **One-way** - you cannot get the input back | **Two-way** - with the key you can decrypt |
| Output | Fixed length (SHA-256 is always 64 hex chars) | About as long as the input |
| Key? | No key | Needs a key |
| Used for | Integrity checks, password *storage*, fingerprints | Keeping data secret (HTTPS, disk encryption, messaging) |

```python
import hashlib

print(hashlib.sha256(b"hello").hexdigest())
# 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
print(hashlib.sha256(b"hello!").hexdigest())
# ce06092fb948d9ffac7d1a376e404b26b7575bcc11ee05a4615fef4fec3a308b
```

One extra character gives a completely different hash (the *avalanche effect*).
That is why a published SHA-256 checksum lets you verify a download wasn't
tampered with.

> Encoding (Base64, hex) is **neither** - it is just another way of writing the
> same data, anyone can reverse it. Never call Base64 "encryption".

## 3. Storing passwords safely

**Never** store passwords as plain text, and never encrypt them (whoever gets
the key gets every password). Store a **slow, salted hash**:

1. **Salt** - a random value per user, stored next to the hash. Two users with
   the same password get different hashes, and pre-computed "rainbow tables"
   become useless.
2. **Slow on purpose** - plain SHA-256 is designed to be fast, so attackers can
   try billions of guesses per second. Password hashing functions (PBKDF2,
   bcrypt, scrypt, **Argon2**) repeat the work many times.
3. **Constant-time comparison** - `hmac.compare_digest` avoids leaking
   information through response timing.

See [`capstone/hashing_demo.py`](capstone/hashing_demo.py):

```python
import hashlib, hmac, secrets

salt = secrets.token_bytes(16)
digest = hashlib.pbkdf2_hmac("sha256", b"my password", salt, 600_000)
stored = f"pbkdf2_sha256$600000${salt.hex()}${digest.hex()}"
```

In real projects use a well-tested library (`argon2-cffi`, `bcrypt`, or your
web framework's built-in password hasher) instead of rolling your own.

## 4. Spotting brute-force attacks in logs

Attackers who don't know a password just try many. In a log this looks like
lots of `FAILED` lines from the same IP in a short time.
[`capstone/log_analyzer.py`](capstone/log_analyzer.py) uses a **sliding time
window** to flag those IPs - the same idea behind tools like fail2ban and SIEM
alert rules. Defences: account lockout/back-off, rate limiting, 2FA, and
alerting.

## 5. Everyday habits

* Use a password manager and a unique passphrase per site; turn on 2FA.
* Update your OS and software - most attacks use known, already-fixed bugs.
* Think before clicking links (phishing is still the #1 way in).
* Back up important files (3-2-1 rule: 3 copies, 2 media, 1 off-site).
* Only test security tools on systems you own or have written permission to test.
