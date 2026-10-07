# 8-Week Study Plan - Programming from Zero

Designed to run alongside a typical first semester of an IT / Computer Science
degree (Intro to Programming, Computer Systems, Discrete Math, Networks &
Security intro). Expect **4-6 hours per week**: one live session, the lesson
script, the exercises, and a little reading.

| Week | Lesson(s) | Goal | Links to first-year courses | Homework |
|-----:|-----------|------|-----------------------------|----------|
| 1 | Setup + `01_variables_and_types` | Install Python & VS Code, run a script, understand types | Intro to Programming: data types; Computer Systems: binary, bytes, KB/MB | Exercises 01; write a script that prints your timetable |
| 2 | `02_conditionals` | Make decisions with `if/elif/else`, boolean logic | Discrete Math: logic, truth tables (`and`, `or`, `not`) | Exercises 02; truth table for `has_password and has_2fa` |
| 3 | `03_loops` | Repeat work with `for`/`while`, trace loops on paper | Algorithms basics: iteration, counting | Exercises 03; FizzBuzz without looking |
| 4 | `04_functions` | Split problems into small functions; parameters & return values | Software Engineering: modularity, docstrings | Exercises 04; refactor week 1-3 code into functions |
| 5 | `05_lists_and_dicts` | Store and look up data; counting pattern | Data Structures preview: arrays, hash maps; Networks: ports & services | Exercises 05; port → service lookup table |
| 6 | `06_files` + `07_error_handling` | Read/write files safely; handle bad input without crashing | Operating Systems: files & paths; Security: input validation | Exercises 06-07; read a CSV of grades and compute averages |
| 7 | `08_intro_to_classes` + capstone part 1 | Model things with classes; build the password checker | OOP fundamentals; Security: authentication | Exercises 08; extend the checker with a "contains your username" rule |
| 8 | Capstone part 2-3 + `CYBERSECURITY_BASICS.md` | Log analyzer, hashing, safe password storage; run the test suite | Security intro: CIA triad, hashing vs. encryption, logging | Add a new rule to the log analyzer (e.g. flag a SUCCESS right after many FAILEDs) |

## After week 8

* Learn Git properly (commit, branch, pull request) - every course project will need it.
* Write your own `pytest` tests for every homework (see `tests/` for examples).
* Next topics: recursion, sorting & searching, Big-O, SQL basics, networking with sockets.
* Optional security practice: OverTheWire *Bandit*, TryHackMe "Pre Security" path.

## How to know you're on track

You can, without help: explain what each line of a lesson does, solve the
exercises, and change the capstone to add a new rule and a test for it.
