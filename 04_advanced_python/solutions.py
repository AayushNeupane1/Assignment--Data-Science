"""04 Advanced Python - reference solutions. Run: python solutions.py"""

import functools


def evens(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i


def word_lengths(words):
    return (len(w) for w in words)


def double(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    return wrapper


@double
def add(a, b):
    return a + b


if __name__ == "__main__":
    assert list(evens(6)) == [0, 2, 4, 6]
    assert list(word_lengths(["ab", "c", "def"])) == [2, 1, 3]
    assert add(2, 3) == 10
    print("All solutions pass.")
