"""
Fundamentals > Functions - EXERCISES.

Replace every ____ with the correct code, then run:  python exercises.py
The checks at the bottom will tell you which pass. (The file won't run until
you've filled the blanks - that's expected.) Peek at solutions.py only after.
"""

import string


# Exercise 1 --------------------------------------------------------------
# Complete the function so it returns True when the password is at least
# 8 characters long AND contains a special character.
def validate_password(password):
    # Check if password is at least 8 characters long
    if ____(____) >= 8:
        # Check if password contains a special character
        for char in password:
            if char in string.____:
                return True
    return False


# Exercise 2 --------------------------------------------------------------
# Write a function that returns the area of a rectangle.
# It should have a default `width` of 1 so make_area(5) == 5.
def area(length, width=____):
    return ____ * ____


# Exercise 3 --------------------------------------------------------------
# Fix the return-vs-print trap: make this function RETURN the greeting
# (as a string) instead of printing it.
def greet(name):
    ____ f"Hello, {name}!"


# Exercise 4 --------------------------------------------------------------
# Count how many numbers in a list are even. Fill the blanks.
def count_even(numbers):
    count = 0
    for n in numbers:
        if n ____ 2 == 0:      # which operator gives the remainder?
            count ____ 1        # add one to count
    return count


# ---------------------------------------------------------------------------
# Checks - do not edit.
# ---------------------------------------------------------------------------
def _check():
    results = [
        ("ex1 strong pass", validate_password("Nepal@2026") is True),
        ("ex1 too short",   validate_password("a@1") is False),
        ("ex1 no symbol",   validate_password("abcdefgh") is False),
        ("ex2 default",     area(5) == 5),
        ("ex2 both args",   area(3, 4) == 12),
        ("ex3 returns",     greet("Sam") == "Hello, Sam!"),
        ("ex4 count",       count_even([1, 2, 3, 4, 6]) == 3),
    ]
    passed = 0
    for name, ok in results:
        print(f"{'PASS' if ok else 'FAIL'}  {name}")
        passed += ok
    print(f"\n{passed}/{len(results)} passed")


if __name__ == "__main__":
    _check()
