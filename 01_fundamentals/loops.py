"""Fundamentals - loops: for, while, range, break, continue.
Reworked from the class 'multiplication table' and 'dice' exercises.
Run: python loops.py
"""

import random


def multiplication_table(number, upto=10):
    """Print the multiplication table of `number` from 1 to `upto`."""
    for i in range(1, upto + 1):
        print(f"{number} x {i} = {number * i}")


def count_sixes(rolls=10, seed=42):
    """Roll a die `rolls` times (seeded, so it's reproducible). Return the number of 6s."""
    rng = random.Random(seed)
    sixes = 0
    for roll_number in range(1, rolls + 1):
        value = rng.randint(1, 6)
        if value == 6:
            sixes += 1
        print(f"roll {roll_number:>2}: {value}")
    return sixes


def main():
    print("Multiplication table of 7:")
    multiplication_table(7)

    print("\nRolling a die 10 times:")
    sixes = count_sixes()
    print(f"Number of 6s: {sixes}")


if __name__ == "__main__":
    main()
