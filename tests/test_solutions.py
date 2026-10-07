import pytest

from solutions import (
    lesson01_variables_and_types as l01,
    lesson02_conditionals as l02,
    lesson03_loops as l03,
    lesson04_functions as l04,
    lesson05_lists_and_dicts as l05,
    lesson06_files as l06,
    lesson07_error_handling as l07,
    lesson08_intro_to_classes as l08,
)


def test_lesson01():
    assert l01.celsius_to_fahrenheit(100) == 212
    assert l01.celsius_to_fahrenheit(-40) == -40
    assert l01.describe_host("web01", "10.0.0.5", 80) == "web01 (10.0.0.5:80)"
    assert l01.bytes_to_megabytes(5 * 1024 * 1024) == 5.0
    assert l01.bytes_to_megabytes(1536 * 1024) == 1.5


@pytest.mark.parametrize("points,letter", [(95, "A"), (90, "A"), (85, "B"), (72, "C"), (60, "D"), (10, "F")])
def test_lesson02_grade(points, letter):
    assert l02.grade_to_letter(points) == letter


def test_lesson02_leap_and_ports():
    assert l02.is_leap_year(2024)
    assert not l02.is_leap_year(1900)
    assert l02.is_leap_year(2000)
    assert not l02.is_leap_year(2026)
    assert l02.port_category(443) == "well-known"
    assert l02.port_category(8080) == "registered"
    assert l02.port_category(50000) == "dynamic"
    assert l02.port_category(70000) == "invalid"
    assert l02.port_category(-1) == "invalid"


def test_lesson03():
    assert l03.sum_to(10) == 55
    assert l03.sum_to(0) == 0
    assert l03.count_vowels("Information Technology") == 8
    assert l03.fizzbuzz(15)[-1] == "FizzBuzz"
    assert l03.fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]


def test_lesson04():
    assert l04.is_even(4) and not l04.is_even(7)
    assert l04.average([2, 4, 6]) == 4
    assert l04.average([]) == 0.0
    assert l04.mask_email("student@example.com") == "s******@example.com"


def test_lesson05():
    assert l05.unique_sorted([3, 1, 3, 2, 1]) == [1, 2, 3]
    assert l05.word_count("Error ok error") == {"error": 2, "ok": 1}
    assert l05.invert_dict({"a": 1, "b": 2}) == {1: "a", 2: "b"}


def test_lesson06(tmp_path):
    path = tmp_path / "log.txt"
    l06.write_lines(path, ["boot ok", "Login FAILED", "login ok"])
    assert l06.count_lines(path) == 3
    assert l06.find_lines(path, "login") == ["Login FAILED", "login ok"]


def test_lesson07():
    assert l07.safe_int("12") == 12
    assert l07.safe_int("abc", default=-1) == -1
    assert l07.safe_int(None) == 0
    assert l07.safe_divide(10, 4) == 2.5
    assert l07.safe_divide(1, 0) is None
    assert l07.parse_port("22") == 22
    for bad in ["0", "65536", "ssh", ""]:
        with pytest.raises(ValueError):
            l07.parse_port(bad)


def test_lesson08_bank_account():
    acc = l08.BankAccount()
    acc.deposit(100)
    acc.withdraw(30)
    assert acc.balance == 70
    with pytest.raises(ValueError):
        acc.withdraw(1000)
    with pytest.raises(ValueError):
        acc.deposit(-5)


def test_lesson08_course():
    c = l08.Course("Programming")
    assert c.average() == 0.0
    c.add_grade(8)
    c.add_grade(10)
    assert c.average() == 9
