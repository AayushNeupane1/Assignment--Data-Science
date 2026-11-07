"""File handling - JSON read/write with the json module. Run: python json_files.py"""

import json
import os

PATH = "data/profile.json"


def main():
    os.makedirs("data", exist_ok=True)

    profile = {
        "name": "Ram",
        "age": 24,
        "skills": ["python", "sql", "numpy"],
    }

    # Python object -> JSON file
    with open(PATH, "w") as f:
        json.dump(profile, f, indent=2)

    # JSON file -> Python object
    with open(PATH) as f:
        loaded = json.load(f)

    print("name  :", loaded["name"])
    print("skills:", ", ".join(loaded["skills"]))


if __name__ == "__main__":
    main()
