"""
09 NumPy - EXERCISES.
Replace every ____, then run:  python exercises.py
"""

import numpy as np


# Exercise 1 --------------------------------------------------------------
# Return an array of the even numbers 0..20 inclusive (use arange).
def evens_to_20():
    return np.arange(0, ____, 2)        # what stop includes 20?


# Exercise 2 --------------------------------------------------------------
# Return the shape of a matrix as a tuple.
def shape_of(matrix):
    return matrix.____


# Exercise 3 --------------------------------------------------------------
# Return only the positive numbers from the array (boolean masking).
def positives(arr):
    return arr[arr ____ 0]


# Exercise 4 --------------------------------------------------------------
# Replace every negative number with 0, keep the rest (use np.where).
def clip_negatives(arr):
    return np.____(arr < 0, 0, arr)


# Exercise 5 --------------------------------------------------------------
# Return the column sums of a 2D array (sum down the rows).
def column_sums(matrix):
    return matrix.sum(axis=____)


# ---------------------------------------------------------------------------
def _check():
    m = np.array([[1, 2, 3], [4, 5, 6]])
    arr = np.array([1, -2, 3, -4])
    results = [
        ("ex1 evens",   np.array_equal(evens_to_20(), np.arange(0, 21, 2))),
        ("ex2 shape",   shape_of(m) == (2, 3)),
        ("ex3 positives", np.array_equal(positives(arr), np.array([1, 3]))),
        ("ex4 clip",    np.array_equal(clip_negatives(arr), np.array([1, 0, 3, 0]))),
        ("ex5 colsums", np.array_equal(column_sums(m), np.array([5, 7, 9]))),
    ]
    passed = 0
    for name, ok in results:
        print(f"{'PASS' if ok else 'FAIL'}  {name}")
        passed += ok
    print(f"\n{passed}/{len(results)} passed")


if __name__ == "__main__":
    _check()
