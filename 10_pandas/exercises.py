"""
10 pandas - EXERCISES.
Replace every ____, then run:  python exercises.py  (uses data/students.csv)
"""

import pandas as pd

df = pd.read_csv("data/students.csv")


# Exercise 1 --------------------------------------------------------------
# Return the number of rows and columns as a (rows, cols) tuple.
def dimensions(frame):
    return frame.____


# Exercise 2 --------------------------------------------------------------
# Return the rows where score is greater than 80 (a filtered DataFrame).
def high_scorers(frame):
    return frame[frame["score"] ____ 80]


# Exercise 3 --------------------------------------------------------------
# Return how many values are missing in the 'score' column.
def missing_scores(frame):
    return int(frame["score"].____().sum())    # method that flags NaN


# Exercise 4 --------------------------------------------------------------
# Return the average score for each city (a Series indexed by city).
def avg_by_city(frame):
    return frame.____("city")["score"].mean()  # split-apply-combine method


# ---------------------------------------------------------------------------
def _check():
    results = [
        ("ex1 dimensions", dimensions(df) == (200, 5)),
        ("ex2 high_scorers", (high_scorers(df)["score"] > 80).all()),
        ("ex3 missing", missing_scores(df) == int(df["score"].isnull().sum())),
        ("ex4 avg_by_city", set(avg_by_city(df).index) ==
                            set(df["city"].dropna().unique())),
    ]
    passed = 0
    for name, ok in results:
        print(f"{'PASS' if ok else 'FAIL'}  {name}")
        passed += ok
    print(f"\n{passed}/{len(results)} passed")


if __name__ == "__main__":
    _check()
