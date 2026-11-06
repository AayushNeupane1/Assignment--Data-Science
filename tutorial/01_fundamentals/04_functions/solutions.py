"""Fundamentals > Functions - reference solutions. Run: python solutions.py"""

import string


def validate_password(password):
    if len(password) >= 8:
        for char in password:
            if char in string.punctuation:
                return True
    return False


def area(length, width=1):
    return length * width


def greet(name):
    return f"Hello, {name}!"


def count_even(numbers):
    count = 0
    for n in numbers:
        if n % 2 == 0:
            count += 1
    return count


if __name__ == "__main__":
    assert validate_password("Nepal@2026") is True
    assert validate_password("a@1") is False
    assert validate_password("abcdefgh") is False
    assert area(5) == 5
    assert area(3, 4) == 12
    assert greet("Sam") == "Hello, Sam!"
    assert count_even([1, 2, 3, 4, 6]) == 3
    print("All solutions pass.")
