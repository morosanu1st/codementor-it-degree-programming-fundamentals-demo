"""Solutions for lesson 02 - conditionals."""


def grade_to_letter(points):
    if points >= 90:
        return "A"
    elif points >= 80:
        return "B"
    elif points >= 70:
        return "C"
    elif points >= 60:
        return "D"
    return "F"


def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def port_category(port):
    if 0 <= port <= 1023:
        return "well-known"
    if 1024 <= port <= 49151:
        return "registered"
    if 49152 <= port <= 65535:
        return "dynamic"
    return "invalid"
