"""06 File handling - reference solutions. Run: python solutions.py"""

import csv
import json
import os

os.makedirs("data", exist_ok=True)


def write_then_read(path, text):
    with open(path, "w") as f:
        f.write(text)
    with open(path, "r") as f:
        return f.read()


def append_line(path, line):
    with open(path, "a") as f:
        f.write(line + "\n")


def read_names(path):
    names = []
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            names.append(row["name"])
    return names


def round_trip(path, data):
    with open(path, "w") as f:
        json.dump(data, f)
    with open(path) as f:
        return json.load(f)


if __name__ == "__main__":
    assert write_then_read("data/sol1.txt", "hello") == "hello"
    append_line("data/sol1.txt", "world")
    with open("data/sol1.txt") as f:
        assert f.read() == "helloworld\n"
    with open("data/sol3.csv", "w", newline="") as f:
        w = csv.writer(f); w.writerow(["name"]); w.writerow(["Ram"]); w.writerow(["Bob"])
    assert read_names("data/sol3.csv") == ["Ram", "Bob"]
    assert round_trip("data/sol4.json", {"a": 1}) == {"a": 1}
    print("All solutions pass.")
