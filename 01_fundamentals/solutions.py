"""01 Fundamentals - reference solutions. Run: python solutions.py"""

import string


def describe(name, age):
    return f"{name} is {age} years old"


def even_or_odd(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"


def sum_to(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def validate_password(password):
    if len(password) >= 8:
        for char in password:
            if char in string.punctuation:
                return True
    return False


def count_valid(names):
    count = 0
    for name in names:
        if 3 <= len(name) <= 20 and name.isalnum():
            count += 1
    return count


if __name__ == "__main__":
    assert describe("Ram", 24) == "Ram is 24 years old"
    assert even_or_odd(4) == "even" and even_or_odd(7) == "odd"
    assert sum_to(5) == 15
    assert validate_password("Nepal@2026") is True
    assert validate_password("abcdefgh") is False
    assert count_valid(["ab", "ram", "bad name!"]) == 1
    print("All solutions pass.")
