"""Statistics - visualization: histogram, box plot, scatter (saved to figures/).
Reworked from stats_assignment. Run: python visualize.py
"""

import os

import matplotlib
matplotlib.use("Agg")          # headless: save PNGs, no screen needed
import matplotlib.pyplot as plt
import pandas as pd


def main():
    os.makedirs("figures", exist_ok=True)
    df = pd.read_csv("data/students.csv")
    df = df.dropna(subset=["study_hours", "score"])

    # 1. Histogram - distribution of scores
    plt.figure()
    plt.hist(df["score"], bins=15, color="#4C78A8", edgecolor="white")
    plt.xlabel("score"); plt.ylabel("count"); plt.title("Score distribution")
    plt.savefig("figures/score_histogram.png", dpi=120, bbox_inches="tight")
    plt.close()

    # 2. Box plot - spread of study hours
    plt.figure()
    plt.boxplot(df["study_hours"], vert=True, tick_labels=["study_hours"])
    plt.ylabel("hours"); plt.title("Study hours spread")
    plt.savefig("figures/study_hours_box.png", dpi=120, bbox_inches="tight")
    plt.close()

    # 3. Scatter - study hours vs score (the relationship)
    plt.figure()
    plt.scatter(df["study_hours"], df["score"], alpha=0.5, color="#F58518")
    plt.xlabel("study hours"); plt.ylabel("score")
    plt.title("Study hours vs score")
    plt.savefig("figures/hours_vs_score.png", dpi=120, bbox_inches="tight")
    plt.close()

    print("Saved 3 charts to figures/:")
    for name in sorted(os.listdir("figures")):
        print("  -", name)


if __name__ == "__main__":
    main()
