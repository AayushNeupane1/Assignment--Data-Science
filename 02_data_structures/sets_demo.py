"""Data structures - sets. Reworked from dataTypes remove-duplicates. Run: python sets_demo.py"""


def main():
    numbers = [1, 2, 2, 3, 3, 3, 4]
    unique = set(numbers)
    print("list     :", numbers)
    print("unique   :", sorted(unique))

    a = {1, 2, 3}
    b = {3, 4, 5}
    print("\na        :", a)
    print("b        :", b)
    print("union    :", a | b)
    print("intersect:", a & b)
    print("a - b    :", a - b)
    print("3 in a?  :", 3 in a)


if __name__ == "__main__":
    main()
