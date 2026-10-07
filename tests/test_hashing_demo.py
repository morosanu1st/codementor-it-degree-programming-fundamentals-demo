from capstone.hashing_demo import hash_password, sha256_hex, verify_password


def test_sha256_known_value():
    assert sha256_hex("hello") == "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"


def test_hash_and_verify():
    stored = hash_password("s3cure pass", iterations=1_000)
    assert stored.startswith("pbkdf2_sha256$1000$")
    assert verify_password("s3cure pass", stored)
    assert not verify_password("wrong", stored)


def test_salt_makes_hashes_unique():
    a = hash_password("same", iterations=1_000)
    b = hash_password("same", iterations=1_000)
    assert a != b
    assert verify_password("same", a) and verify_password("same", b)


def test_verify_rejects_garbage():
    assert not verify_password("x", "not-a-hash")
    assert not verify_password("x", "md5$1$00$00")
