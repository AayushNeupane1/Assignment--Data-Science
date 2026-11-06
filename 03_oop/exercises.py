"""
03 OOP - EXERCISES.
Replace every ____, then run:  python exercises.py
"""


# Exercise 1 -------------------------------------------------------------
# Complete the constructor so each Rectangle stores width and height.
class Rectangle:
    def __init__(self, width, height):
        ____.width = width          # store width on the object
        self.height = ____          # store height on the object

    # Exercise 2: return width * height
    def area(self):
        return self.____ * self.____


# Exercise 3 -------------------------------------------------------------
# Make Square inherit from Rectangle. A square's width and height are equal.
class Square(____):
    def __init__(self, side):
        super().____(side, side)    # call Rectangle's constructor


# Exercise 4 -------------------------------------------------------------
# Give Counter a method that increases its count by 1.
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count ____ 1


# ---------------------------------------------------------------------------
def _check():
    r = Rectangle(3, 4)
    sq = Square(5)
    c = Counter()
    c.increment()
    c.increment()
    results = [
        ("ex1 attributes", r.width == 3 and r.height == 4),
        ("ex2 area",       r.area() == 12),
        ("ex3 inherits",   isinstance(sq, Rectangle)),
        ("ex3 square area", sq.area() == 25),
        ("ex4 increment",  c.count == 2),
    ]
    passed = 0
    for name, ok in results:
        print(f"{'PASS' if ok else 'FAIL'}  {name}")
        passed += ok
    print(f"\n{passed}/{len(results)} passed")


if __name__ == "__main__":
    _check()
