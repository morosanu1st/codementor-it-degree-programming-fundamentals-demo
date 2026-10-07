"""Solutions for lesson 06 - files."""


def count_lines(path):
    with open(path, encoding="utf-8") as f:
        return sum(1 for _ in f)


def write_lines(path, lines):
    with open(path, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(f"{line}\n")


def find_lines(path, word):
    word = word.lower()
    with open(path, encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f if word in line.lower()]
