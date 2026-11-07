"""Statistics - detecting outliers with the IQR method.
Reworked from the lab exercise, applied to the students dataset.
Run: python outliers.py
"""

import pandas as pd


def iqr_bounds(series):
    """Return the (lower, upper) fences for outliers using the IQR rule."""
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return lower, upper


def main():
    df = pd.read_csv("data/students.csv").dropna(subset=["score"])
    scores = df["score"]

    lower, upper = iqr_bounds(scores)
    print(f"Q1 - 1.5*IQR = {lower:.1f}")
    print(f"Q3 + 1.5*IQR = {upper:.1f}")

    outliers = df[(scores < lower) | (scores > upper)]
    clean = df[(scores >= lower) & (scores <= upper)]

    print(f"\noutliers found: {len(outliers)}")
    print(outliers[["id", "score"]].to_string(index=False) if len(outliers) else "  (none)")
    print(f"\nrows kept after removing outliers: {len(clean)} of {len(df)}")


if __name__ == "__main__":
    main()
