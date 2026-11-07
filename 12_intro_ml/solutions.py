"""12 Intro ML - reference solutions. Run: python solutions.py"""

import numpy as np


def slope(x, y):
    x_mean, y_mean = x.mean(), y.mean()
    return np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean) ** 2)


def intercept(x, y, m):
    return y.mean() - m * x.mean()


def predict(x, m, c):
    return m * x + c


if __name__ == "__main__":
    x = np.array([1, 2, 3, 4, 5], dtype=float)
    y = 2 * x + 1
    m = slope(x, y)
    c = intercept(x, y, m)
    assert abs(m - 2) < 1e-9
    assert abs(c - 1) < 1e-9
    assert abs(predict(10, m, c) - 21) < 1e-9
    print("All solutions pass.")
