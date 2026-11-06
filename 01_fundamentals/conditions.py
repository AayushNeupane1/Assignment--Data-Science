"""Fundamentals - conditions: if/elif/else, comparison & logical operators.
Reworked from the class 'grade' and 'largest' exercises. Run: python conditions.py
"""


def grade(average):
    """Return a letter grade for a numeric average (bug-free version)."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    return "F"


def largest(a, b, c):
    """Return the largest of three numbers using comparisons."""
    biggest = a
    if b > biggest:
        biggest = b
    if c > biggest:
        biggest = c
    return biggest


def main():
    for avg in (95, 83, 50, 40):
        print(f"average {avg:>3} -> grade {grade(avg)}")

    print("\nlargest(3, 9, 5) =", largest(3, 9, 5))   # 9

    # logical operators
    age = 20
    if age >= 18 and age < 65:
        print(f"age {age}: adult")


if __name__ == "__main__":
    main()
