from capstone.password_checker import (
    check_password,
    estimate_entropy_bits,
    has_repeated_run,
    main,
)


def test_common_password_is_rejected():
    score, label, tips = check_password("Password")
    assert score == 0 and label == "very weak"
    assert "breach" in tips[0]


def test_short_simple_password_is_weak():
    score, _, tips = check_password("abc")
    assert score <= 1
    assert any("12 characters" in t for t in tips)


def test_long_mixed_password_is_very_strong():
    score, label, tips = check_password("Blue-Coffee-Mug-42")
    assert score == 5 and label == "very strong"
    assert tips == []


def test_repeated_characters_lower_the_score():
    assert has_repeated_run("aaab", 3)
    assert not has_repeated_run("aabb", 3)
    strong, _, _ = check_password("Xk9!mQ2#pL7z")
    repeated, _, tips = check_password("Xk9!mmmm2#pL")
    assert repeated < strong
    assert any("repeating" in t for t in tips)


def test_entropy_grows_with_length_and_variety():
    assert estimate_entropy_bits("") == 0.0
    assert estimate_entropy_bits("abcdefgh") < estimate_entropy_bits("abcdefghijkl")
    assert estimate_entropy_bits("abcdefgh") < estimate_entropy_bits("aB3$efgh")


def test_cli(capsys):
    assert main(["Blue-Coffee-Mug-42"]) == 0
    assert "5/5" in capsys.readouterr().out
    assert main([]) == 2
