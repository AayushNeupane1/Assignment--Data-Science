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
# Return "hist", "boxplot" or "scatter".
def chart_for_relationship():
    return "____"


# Exercise 5 (IQR outliers) -----------------------------------------------
# Return the (lower, upper) outlier fences using the 1.5*IQR rule.
def iqr_bounds(series):
    q1 = series.quantile(0.25)
    q3 = series.quantile(____)        # the 75th percentile
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 ____ 1.5 * iqr          # upper fence is Q3 PLUS 1.5*IQR
    return lower, upper


# ---------------------------------------------------------------------------
def _check():
    import math
    s = pd.Series([10, 12, 13, 12, 11, 100])   # 100 is the outlier
    lo, hi = iqr_bounds(s)
    results = [
        ("ex1 mean",   math.isclose(average(scores), scores.mean())),
        ("ex2 median", math.isclose(middle(scores), scores.median())),
        ("ex3 std",    math.isclose(spread(scores), scores.std())),
        ("ex4 chart",  chart_for_relationship() == "scatter"),
        ("ex5 iqr",    100 > hi and 10 >= lo),   # 100 is flagged, 10 is not
    ]
    passed = 0
    for name, ok in results:
        print(f"{'PASS' if ok else 'FAIL'}  {name}")
        passed += ok
    print(f"\n{passed}/{len(results)} passed")


if __name__ == "__main__":
    _check()
