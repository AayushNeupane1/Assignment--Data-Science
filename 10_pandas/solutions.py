"""10 pandas - reference solutions. Run: python solutions.py"""

import pandas as pd

df = pd.read_csv("data/students.csv")


def dimensions(frame):
    return frame.shape


def high_scorers(frame):
    return frame[frame["score"] > 80]


def missing_scores(frame):
    return int(frame["score"].isnull().sum())


def avg_by_city(frame):
    return frame.groupby("city")["score"].mean()


if __name__ == "__main__":
    assert dimensions(df) == (200, 5)
    assert (high_scorers(df)["score"] > 80).all()
    assert missing_scores(df) == int(df["score"].isnull().sum())
    assert set(avg_by_city(df).index) == set(df["city"].dropna().unique())
    print("All solutions pass.")
