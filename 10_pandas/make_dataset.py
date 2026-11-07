"""
Generate the small, reproducible dataset used across the pandas / stats / ML
modules: data/students.csv (200 rows). Run once:  python make_dataset.py
Some values are intentionally missing so the cleaning module has something to do.
"""

import csv

import numpy as np

CITIES = ["Melbourne", "Sydney", "Brisbane", "Perth"]


def main(path="data/students.csv", n=200, seed=42):
    rng = np.random.default_rng(seed)

    study_hours = rng.normal(5, 2, n).clip(0, 12).round(1)
    # score correlates with study hours + noise
    score = (35 + 5 * study_hours + rng.normal(0, 6, n)).clip(0, 100).round(1)
    age = rng.integers(18, 30, n)
    city = rng.choice(CITIES, n)

    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "age", "city", "study_hours", "score"])
        for i in range(n):
            # punch ~5% holes in study_hours and score to practise cleaning
            sh = "" if rng.random() < 0.05 else study_hours[i]
            sc = "" if rng.random() < 0.05 else score[i]
            w.writerow([i + 1, age[i], city[i], sh, sc])

    print(f"wrote {n} rows to {path}")


if __name__ == "__main__":
    main()
