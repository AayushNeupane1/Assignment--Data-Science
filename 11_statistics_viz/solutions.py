"""11 Statistics & Visualization - reference solutions. Run: python solutions.py"""

import math

import pandas as pd

df = pd.read_csv("data/students.csv")
scores = df["score"].dropna()


def average(series):
    return series.mean()


def middle(series):
    return series.median()


def spread(series):
    return series.std()


def chart_for_relationship():
    return "scatter"


def iqr_bounds(series):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    return q1 - 1.5 * iqr, q3 + 1.5 * iqr


if __name__ == "__main__":
    assert math.isclose(average(scores), scores.mean())
    assert math.isclose(middle(scores), scores.median())
    assert math.isclose(spread(scores), scores.std())
    assert chart_for_relationship() == "scatter"
    s = pd.Series([10, 12, 13, 12, 11, 100])
    lo, hi = iqr_bounds(s)
    assert 100 > hi and 10 >= lo
    print("All solutions pass.")
