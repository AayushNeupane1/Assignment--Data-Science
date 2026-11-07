"""
12 Intro ML - EXERCISES (from scratch, needs only numpy).
Replace every ____, then run:  python exercises.py
"""

import numpy as np


# Exercise 1 --------------------------------------------------------------
# Return the slope m = cov(x, y) / var(x) for the least-squares line.
def slope(x, y):
    x_mean, y_mean = x.mean(), y.mean()
    numerator = np.sum((x - x_mean) * (y - y_mean))
    denominator = np.sum((x - x_mean) ____ 2)     # squared distances
    return numerator / denominator


# Exercise 2 --------------------------------------------------------------
# Return the intercept c = mean(y) - m * mean(x).
def intercept(x, y, m):
    return y.mean() ____ m * x.mean()             # the operator in c = ȳ - m·x̄


# Exercise 3 --------------------------------------------------------------
# Predict y for a given x using the line parameters.
def predict(x, m, c):
    return m * x ____ c                            # y = m*x + c


# ---------------------------------------------------------------------------
def _check():
    # perfect line y = 2x + 1
    x = np.array([1, 2, 3, 4, 5], dtype=float)
    y = 2 * x + 1
    m = slope(x, y)
    c = intercept(x, y, m)
    results = [
        ("ex1 slope",     abs(m - 2) < 1e-9),
        ("ex2 intercept", abs(c - 1) < 1e-9),
        ("ex3 predict",   abs(predict(10, m, c) - 21) < 1e-9),
    ]
    passed = 0
    for name, ok in results:
        print(f"{'PASS' if ok else 'FAIL'}  {name}")
        passed += ok
    print(f"\n{passed}/{len(results)} passed")


if __name__ == "__main__":
    _check()
