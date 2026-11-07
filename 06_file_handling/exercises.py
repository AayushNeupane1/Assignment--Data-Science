"""
06 File handling - EXERCISES.
Replace every ____, then run:  python exercises.py
Each function uses the data/ folder created for you.
"""

import csv
import json
import os

os.makedirs("data", exist_ok=True)


# Exercise 1 (text) -------------------------------------------------------
# Write `text` to a file, then read it back and return the content.
def write_then_read(path, text):
    with open(path, "____") as f:       # mode that writes
        f.write(text)
    with open(path, "____") as f:       # mode that reads
        return f.read()


# Exercise 2 (append) -----------------------------------------------------
# Append a line (with a trailing newline) without erasing the file.
def append_line(path, line):
    with open(path, "____") as f:       # mode that appends
        f.write(line + "\n")


# Exercise 3 (CSV) --------------------------------------------------------
# Return a list of the 'name' values from a CSV file.
def read_names(path):
    names = []
    with open(path, newline="") as f:
        for row in csv.____(f):         # reader that yields dicts keyed by header
            names.append(row["name"])
    return names


# Exercise 4 (JSON) -------------------------------------------------------
# Save a dict to JSON, then load it back and return it.
def round_trip(path, data):
    with open(path, "w") as f:
        json.____(data, f)              # object -> file
    with open(path) as f:
        return json.____(f)             # file -> object


# ---------------------------------------------------------------------------
def _check():
    r1 = write_then_read("data/ex1.txt", "hello")
    append_line("data/ex1.txt", "world")
    with open("data/ex1.txt") as f:
        appended = f.read()

    with open("data/ex3.csv", "w", newline="") as f:
        w = csv.writer(f); w.writerow(["name"]); w.writerow(["Ram"]); w.writerow(["Bob"])

    data = {"a": 1, "b": 2}
    r4 = round_trip("data/ex4.json", data)

    results = [
        ("ex1 write/read", r1 == "hello"),
        ("ex2 append",     appended == "helloworld\n"),
        ("ex3 read_names", read_names("data/ex3.csv") == ["Ram", "Bob"]),
        ("ex4 round_trip", r4 == data),
    ]
    passed = 0
    for name, ok in results:
        print(f"{'PASS' if ok else 'FAIL'}  {name}")
        passed += ok
    print(f"\n{passed}/{len(results)} passed")


if __name__ == "__main__":
    _check()
