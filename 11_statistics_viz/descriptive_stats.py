"""Statistics - descriptive measures on the students dataset.
Reworked from stats_assignment. Run: python descriptive_stats.py
"""

import pandas as pd


def main():
    df = pd.read_csv("data/students.csv")
    scores = df["score"].dropna()

    print(f"count   : {scores.count()}")
    print(f"mean    : {scores.mean():.2f}")
    print(f"median  : {scores.median():.2f}")
    print(f"mode    : {scores.mode().iloc[0]:.2f}")
    print(f"variance: {scores.var():.2f}")
    print(f"std dev : {scores.std():.2f}")
    print(f"min/max : {scores.min():.1f} / {scores.max():.1f}")

    q = scores.quantile([0.25, 0.5, 0.75])
    print(f"quartiles: Q1={q[0.25]:.1f}  Q2={q[0.5]:.1f}  Q3={q[0.75]:.1f}")


if __name__ == "__main__":
    main()
