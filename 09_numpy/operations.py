"""NumPy - vectorized math, boolean masking, np.where, axis aggregations.
Consolidated from NumPy/arrayOperation, booleanIndexing, operations/*. Run: python operations.py
"""

import numpy as np


def main():
    a = np.array([1, -2, 3, -4, 5])
    print("a           :", a)
    print("a * 2       :", a * 2)
    print("positives   :", a[a > 0])                 # boolean mask
    print("clip negs   :", np.where(a < 0, 0, a))    # replace negatives with 0

    m = np.array([[1, 2, 3], [4, 5, 6]])
    print("\nmatrix:\n", m)
    print("sum axis=0 (cols):", m.sum(axis=0))       # [5 7 9]
    print("sum axis=1 (rows):", m.sum(axis=1))       # [6 15]
    print("mean  :", m.mean(), "| std:", round(float(m.std()), 3))


if __name__ == "__main__":
    main()
