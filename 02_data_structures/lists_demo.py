"""Data structures - lists. Reworked from dataTypes sorting/duplicates. Run: python lists_demo.py"""


def main():
    names = ["Rohan", "Aastha", "Bob", "Smriti"]
    print("original :", names)

    names.append("Max")
    print("appended :", names)

    names.sort()
    print("sorted   :", names)

    marks = [85, 90, 78, 92]
    print("\nmarks    :", marks)
    print("total    :", sum(marks))
    print("highest  :", max(marks))
    print("average  :", sum(marks) / len(marks))


if __name__ == "__main__":
    main()
