"""
Intro ML - linear regression FROM SCRATCH with NumPy (no sklearn).
Predicts score from study_hours. Extends your LinearRegression.ipynb to real data.
Run:  python linear_regression_scratch.py
"""

import numpy as np
import pandas as pd


def fit(x, y):
    """Return (slope m, intercept c) of the least-squares line y = m*x + c."""
    x_mean, y_mean = x.mean(), y.mean()
    m = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean) ** 2)
    c = y_mean - m * x_mean
    return m, c


def r_squared(y, y_pred):
    ss_res = np.sum((y - y_pred) ** 2)
    ss_tot = np.sum((y - y.mean()) ** 2)
    return 1 - ss_res / ss_tot


def main():
    df = pd.read_csv("data/students.csv").dropna(subset=["study_hours", "score"])
    x = df["study_hours"].to_numpy()
    y = df["score"].to_numpy()

    m, c = fit(x, y)
    y_pred = m * x + c
    mse = np.mean((y - y_pred) ** 2)

    print(f"slope (m)   : {m:.3f}")
    print(f"intercept(c): {c:.3f}")
    print(f"=> score ~= {m:.2f} * study_hours + {c:.1f}")
    print(f"MSE         : {mse:.2f}")
    print(f"R^2         : {r_squared(y, y_pred):.3f}")

    for hrs in (2, 6, 10):
        print(f"predict {hrs:>2}h study -> score {m * hrs + c:.1f}")


if __name__ == "__main__":
    main()
