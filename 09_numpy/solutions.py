"""09 NumPy - reference solutions. Run: python solutions.py"""

import numpy as np


def evens_to_20():
    return np.arange(0, 21, 2)


def shape_of(matrix):
    return matrix.shape


def positives(arr):
    return arr[arr > 0]


def clip_negatives(arr):
    return np.where(arr < 0, 0, arr)


def column_sums(matrix):
    return matrix.sum(axis=0)


if __name__ == "__main__":
    m = np.array([[1, 2, 3], [4, 5, 6]])
    arr = np.array([1, -2, 3, -4])
    assert np.array_equal(evens_to_20(), np.arange(0, 21, 2))
    assert shape_of(m) == (2, 3)
    assert np.array_equal(positives(arr), [1, 3])
    assert np.array_equal(clip_negatives(arr), [1, 0, 3, 0])
    assert np.array_equal(column_sums(m), [5, 7, 9])
    print("All solutions pass.")
