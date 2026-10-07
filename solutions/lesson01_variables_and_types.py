"""Solutions for lesson 01 - variables and types."""


def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32


def describe_host(name, ip, port):
    return f"{name} ({ip}:{port})"


def bytes_to_megabytes(n):
    return round(n / (1024 * 1024), 2)
