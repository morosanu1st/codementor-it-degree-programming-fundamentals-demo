"""Solutions for lesson 05 - lists and dictionaries."""


def unique_sorted(items):
    return sorted(set(items))


def word_count(text):
    counts = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def invert_dict(d):
    return {value: key for key, value in d.items()}
