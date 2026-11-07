"""04 Advanced Python - reference solutions. Run: python solutions.py"""

import functools
import re


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


def squares(n):
    return [i * i for i in range(1, n + 1)]


def total_score(names, scores):
    paired = list(zip(names, scores))
    return functools.reduce(lambda a, b: a + b, scores)


def capitalised_words(text):
    return re.findall(r"[A-Z][a-z]+", text)


if __name__ == "__main__":
    assert list(evens(6)) == [0, 2, 4, 6]
    assert list(word_lengths(["ab", "c", "def"])) == [2, 1, 3]
    assert add(2, 3) == 10
    assert squares(4) == [1, 4, 9, 16]
    assert total_score(["a", "b"], [10, 25]) == 35
    assert capitalised_words("Hi there London and Paris") == ["Hi", "London", "Paris"]
    print("All solutions pass.")
