"""
01 Fundamentals - EXERCISES.

Replace every ____ with the correct code, then run:  python exercises.py
The checks at the bottom report PASS/FAIL. Try before peeking at solutions.py.
"""

import string


# Exercise 1 (variables) --------------------------------------------------
# Return a sentence like "Ram is 24 years old" using an f-string.
def describe(name, age):
    return f"____ is ____ years old"


# Exercise 2 (conditions) -------------------------------------------------
# Return "even" if n is divisible by 2, otherwise "odd".
def even_or_odd(n):
    if n ____ 2 == 0:       # operator that gives the remainder
        return "even"
    ____:
        return "odd"


# Exercise 3 (loops) ------------------------------------------------------
# Return the sum of all numbers from 1 to n (inclusive) using a loop.
def sum_to(n):
    total = 0
    for i in range(1, ____):    # what stop value includes n?
        total ____ i
    return total


# Exercise 4 (functions) --------------------------------------------------
# Complete the password check: at least 8 chars AND contains a special char.
def validate_password(password):
    if ____(____) >= 8:
        for char in password:
            if char in string.____:
                return True
    return False


# Exercise 5 (combine) ----------------------------------------------------
# Count how many names in a list are "valid": 3-20 chars, letters/digits/_ only.
def count_valid(names):
    count = 0
    for name in names:
        if 3 <= len(name) <= 20 and name.____():   # method: all chars alphanumeric?
            count += 1
    return count


# ---------------------------------------------------------------------------
# Checks - do not edit.
# ---------------------------------------------------------------------------
def _check():
    results = [
        ("ex1 describe",    describe("Ram", 24) == "Ram is 24 years old"),
        ("ex2 even",        even_or_odd(4) == "even"),
        ("ex2 odd",         even_or_odd(7) == "odd"),
        ("ex3 sum_to",      sum_to(5) == 15),
        ("ex4 strong",      validate_password("Nepal@2026") is True),
        ("ex4 weak",        validate_password("abcdefgh") is False),
        ("ex5 count_valid", count_valid(["ab", "ram", "bad name!"]) == 1),
    ]
    passed = 0
    for name, ok in results:
        print(f"{'PASS' if ok else 'FAIL'}  {name}")
        passed += ok
    print(f"\n{passed}/{len(results)} passed")


if __name__ == "__main__":
    _check()
