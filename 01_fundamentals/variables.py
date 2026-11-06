"""Fundamentals - variables, data types, conversion, f-strings. Run: python variables.py"""


def main():
    # --- types ---
    name = "Aastha"
    age = 24
    height = 1.63
    is_student = True

    print("name     :", name, "->", type(name).__name__)
    print("age      :", age, "->", type(age).__name__)
    print("height   :", height, "->", type(height).__name__)
    print("is_student:", is_student, "->", type(is_student).__name__)

    # --- conversion ---
    print("\nint('42') + 1 =", int("42") + 1)       # 43
    print("str(42) + '!' =", str(42) + "!")          # 42!
    print("float('3.5') * 2 =", float("3.5") * 2)    # 7.0

    # --- f-strings ---
    print(f"\n{name} is {age} years old and {height:.1f} m tall")


if __name__ == "__main__":
    main()
