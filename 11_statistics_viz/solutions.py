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


if __name__ == "__main__":
    assert math.isclose(average(scores), scores.mean())
    assert math.isclose(middle(scores), scores.median())
    assert math.isclose(spread(scores), scores.std())
    assert chart_for_relationship() == "scatter"
    print("All solutions pass.")
