"""Data structures - tuples. Reworked from dataTypes employee info. Run: python tuples_demo.py"""


def main():
    # a tuple is a fixed record: (name, age, position, salary)
    employee = ("Aastha", 24, "Supervisor", 55000)

    # unpacking into named variables
    name, age, position, salary = employee
    print(f"{name}, {age}, {position}, ${salary}")

    # tuples are immutable
    try:
        employee[0] = "Bob"
    except TypeError as e:
        print("Can't change a tuple:", e)


if __name__ == "__main__":
    main()
