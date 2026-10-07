# Programming Fundamentals from Zero - IT Degree Starter (Python)

A beginner-friendly path for someone starting an **IT / Computer Science degree**
with no programming experience: 8 short runnable Python lessons with exercises
and solutions, a small **cybersecurity capstone**, plain-language security notes
and an 8-week study plan aligned with first-year courses.

## What's inside

```
lessons/                 01_variables_and_types ... 08_intro_to_classes (run each one)
solutions/               Solutions to every lesson's exercises (checked by tests)
capstone/
  password_checker.py    Password strength score, entropy estimate, tips
  log_analyzer.py        Flags IPs with repeated failed logins (sliding time window)
  hashing_demo.py        SHA-256 vs. salted PBKDF2 password hashing
sample_data/auth.log     Example authentication log
tests/                   pytest suite (41 tests)
CYBERSECURITY_BASICS.md  CIA triad, hashing vs. encryption, safe password storage
STUDY_PLAN.md            8-week plan mapped to first-year IT courses
```

| # | Lesson | Key ideas |
|---|--------|-----------|
| 01 | Variables and types | `str`, `int`, `float`, `bool`, conversions, f-strings |
| 02 | Conditionals | `if/elif/else`, `and/or/not`, `in` |
| 03 | Loops | `for`, `while`, `range`, `break`, `continue` |
| 04 | Functions | parameters, defaults, `return`, docstrings |
| 05 | Lists and dicts | indexing, comprehensions, counting with dicts |
| 06 | Files | `with open(...)`, reading line by line, `pathlib` |
| 07 | Error handling | `try/except/finally`, raising `ValueError` |
| 08 | Intro to classes | `__init__`, attributes, methods, `__repr__` |

## How to run

Requires Python 3.9+.

```bash
git clone https://github.com/morosanu1st/codementor-it-degree-programming-fundamentals-demo.git
cd codementor-it-degree-programming-fundamentals-demo

# run a lesson
python lessons/01_variables_and_types.py

# capstone tools
python -m capstone.password_checker "Blue-Coffee-Mug-42"
python -m capstone.log_analyzer sample_data/auth.log --threshold 3 --window 300
python -m capstone.hashing_demo

# tests
python -m pip install -r requirements-dev.txt
python -m pytest
```

Example output of the log analyzer:

```
Parsed 12 events (1 malformed lines skipped)
Failed logins per IP:
  203.0.113.7     5
  198.51.100.23   3
  192.0.2.10      1
ALERT - 3+ failures within 300s:
  203.0.113.7     5 failures
```

## How I'd tutor

I'm **Mihai Chindris**, a software engineer (BSc Computer Science, Technical
University of Cluj-Napoca, 2019; MSc Business Informatics at TU Wien in progress).
I remember what the first semester feels like, and I like explaining things
without jargon.

* **1:1 live sessions, under an hour.** One topic per session; you type the code,
  I explain and ask questions so it sticks.
* **Plain words first, terms second.** "A dictionary is a phone book" before
  "a hash map with O(1) lookups".
* **Homework review.** You do the exercises between sessions; I review your code,
  point out one or two improvements and explain *why* - never just paste a fix.
* **Linked to your degree.** We follow the [study plan](STUDY_PLAN.md) and adapt
  it to your actual course schedule, assignments and exams.
* **Security mindset from day one.** Small, practical habits (input validation,
  password storage, reading logs) that pay off in later cybersecurity courses.

## License

[MIT](LICENSE)
