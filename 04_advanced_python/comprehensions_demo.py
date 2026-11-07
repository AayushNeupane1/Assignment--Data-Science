"""Advanced - list comprehensions and functional tools (lambda, map, filter, zip, reduce).
Reworked from the lab exercises. Run: python comprehensions_demo.py
"""

from functools import reduce


def main():
    # --- list comprehension: build a list in one readable line ---
    evens = [i for i in range(1, 21) if i % 2 == 0]
    print("evens 1-20 :", evens)

    squares = [n * n for n in range(1, 6)]
    print("squares    :", squares)

    # --- lambda: a tiny anonymous function ---
    double = lambda x: x * 2
    print("double(5)  :", double(5))

    # --- map / filter with lambdas ---
    nums = [1, 2, 3, 4, 5, 6]
    print("map doubled:", list(map(lambda x: x * 2, nums)))
    print("filter even:", list(filter(lambda x: x % 2 == 0, nums)))

    # --- zip: pair two lists together ---
    students = ["Aayush", "Ram", "Smriti"]
    scores = [85, 90, 78]
    paired = list(zip(students, scores))
    print("zipped     :", paired)

    # --- reduce: fold a list down to one value ---
    total = reduce(lambda a, b: a + b, scores)
    print("total score:", total)


if __name__ == "__main__":
    main()
