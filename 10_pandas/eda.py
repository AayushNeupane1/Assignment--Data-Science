"""pandas - EDA: describe, value_counts, groupby, correlation.
Reworked from chapter_8 class notebook. Run: python eda.py
"""

import pandas as pd


def main():
    df = pd.read_csv("data/students.csv")
    # clean first so stats aren't thrown by NaN
    for col in ["study_hours", "score"]:
        df[col] = df[col].fillna(df[col].mean())

    print("=== describe (score) ===")
    print(df["score"].describe().round(2))

    print("\n=== students per city ===")
    print(df["city"].value_counts())

    print("\n=== average score by city ===")
    print(df.groupby("city")["score"].mean().round(1))

    print("\n=== correlation: study_hours vs score ===")
    print(df[["study_hours", "score"]].corr().round(3))


if __name__ == "__main__":
    main()
