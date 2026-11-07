"""File handling - CSV read/write with the csv module.
Reworked from FileHandling 4.py. Run: python csv_files.py
"""

import csv
import os

PATH = "data/people.csv"


def main():
    os.makedirs("data", exist_ok=True)

    rows = [("Aastha", 24, "Melbourne"),
            ("Bob", 30, "Sydney"),
            ("Smriti", 27, "Melbourne")]

    with open(PATH, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "age", "city"])   # header
        writer.writerows(rows)

    # read back as dictionaries
    print("People from the CSV:")
    with open(PATH, newline="") as f:
        for row in csv.DictReader(f):
            print(f"  {row['name']} ({row['age']}) - {row['city']}")


if __name__ == "__main__":
    main()
