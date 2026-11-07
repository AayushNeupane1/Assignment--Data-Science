"""pandas - missing values, dtypes, duplicates.
Reworked from chapter_6 / chapter_7 class notebooks. Run: python cleaning.py
"""

import pandas as pd


def main():
    df = pd.read_csv("data/students.csv")

    print("missing values per column:")
    print(df.isnull().sum())

    # fill missing numbers with the column mean
    for col in ["study_hours", "score"]:
        df[col] = df[col].fillna(df[col].mean())

    print("\nafter fillna, missing values:", int(df.isnull().sum().sum()))

    # dtypes, and dropping duplicate rows
    print("dtypes:\n", df.dtypes)
    print("rows before dedup:", len(df), "| after:", len(df.drop_duplicates()))


if __name__ == "__main__":
    main()
