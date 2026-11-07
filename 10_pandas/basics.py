"""pandas - Series/DataFrame, loading, selecting, filtering. Run: python basics.py"""

import pandas as pd


def main():
    df = pd.read_csv("data/students.csv")

    print("shape   :", df.shape)
    print("columns :", list(df.columns))
    print("\nfirst 3 rows:\n", df.head(3))

    print("\nscore column (first 3):\n", df["score"].head(3).tolist())

    high = df[df["score"] > 80]
    print(f"\nstudents scoring > 80: {len(high)}")

    syd_young = df[(df["city"] == "Sydney") & (df["age"] < 25)]
    print(f"young Sydney students: {len(syd_young)}")


if __name__ == "__main__":
    main()
