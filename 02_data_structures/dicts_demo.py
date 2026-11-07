"""Data structures - dictionaries. Reworked from dataTypes student marks. Run: python dicts_demo.py"""


def main():
    student_marks = {"Aayush": 85, "Ram": 90, "Smriti": 78, "Rohan": 69}

    # safe lookup
    print("Ram's mark:", student_marks.get("Ram"))
    print("Missing key  :", student_marks.get("Nobody", "n/a"))

    # iterate key/value pairs
    print("\nAll students:")
    for name, mark in student_marks.items():
        print(f"  {name}: {mark}")

    # top student (max by value)
    top = max(student_marks, key=student_marks.get)
    print(f"\nTop student: {top} ({student_marks[top]})")


if __name__ == "__main__":
    main()
