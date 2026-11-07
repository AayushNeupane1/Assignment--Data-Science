"""
11 Statistics & Visualization - EXERCISES.
Replace every ____, then run:  python exercises.py
"""

import pandas as pd

df = pd.read_csv("data/students.csv")
scores = df["score"].dropna()


# Exercise 1 --------------------------------------------------------------
# Return the mean of a Series.
def average(series):
    return series.____()


# Exercise 2 --------------------------------------------------------------
# Return the median - the measure that resists outliers.
def middle(series):
    return series.____()


# Exercise 3 --------------------------------------------------------------
# Return the standard deviation (spread).
def spread(series):
    return series.____()


# Exercise 4 --------------------------------------------------------------
# Which chart answers "is there a relationship between two variables"?
# Return the matplotlib function name as a string: "hist", "boxplot" or "scatter".
def chart_for_relationship():
    return "____"


# ---------------------------------------------------------------------------
def _check():
    import math
    results = [
        ("ex1 mean",   math.isclose(average(scores), scores.mean())),
        ("ex2 median", math.isclose(middle(scores), scores.median())),
        ("ex3 std",    math.isclose(spread(scores), scores.std())),
        ("ex4 chart",  chart_for_relationship() == "scatter"),
    ]
    passed = 0
    for name, ok in results:
        print(f"{'PASS' if ok else 'FAIL'}  {name}")
        passed += ok
    print(f"\n{passed}/{len(results)} passed")


if __name__ == "__main__":
    _check()
