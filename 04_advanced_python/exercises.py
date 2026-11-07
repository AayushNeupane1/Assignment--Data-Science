"""
04 Advanced Python - EXERCISES.
Replace every ____, then run:  python exercises.py
"""

import functools


# Exercise 1 (generator) --------------------------------------------------
# Yield the even numbers from 0 up to (and including) n.
def evens(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            ____ i          # hand back i lazily (not return)


# Exercise 2 (generator expression) ---------------------------------------
# Return a generator of each word's length. Use a generator expression.
def word_lengths(words):
    return (____(w) for w in words)


# Exercise 3 (decorator) --------------------------------------------------
# Complete the decorator so it doubles whatever number the function returns.
def double(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(____, ____)   # pass the arguments through unchanged
        return result * 2
    return wrapper


@double
def add(a, b):
    return a + b


# ---------------------------------------------------------------------------
def _check():
    results = [
        ("ex1 evens",        list(evens(6)) == [0, 2, 4, 6]),
        ("ex2 word_lengths", list(word_lengths(["ab", "c", "def"])) == [2, 1, 3]),
        ("ex3 double",       add(2, 3) == 10),
    ]
    passed = 0
    for name, ok in results:
        print(f"{'PASS' if ok else 'FAIL'}  {name}")
        passed += ok
    print(f"\n{passed}/{len(results)} passed")


if __name__ == "__main__":
    _check()
