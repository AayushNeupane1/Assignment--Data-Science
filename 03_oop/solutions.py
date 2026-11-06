"""03 OOP - reference solutions. Run: python solutions.py"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1


if __name__ == "__main__":
    r = Rectangle(3, 4)
    assert r.width == 3 and r.height == 4
    assert r.area() == 12
    sq = Square(5)
    assert isinstance(sq, Rectangle)
    assert sq.area() == 25
    c = Counter(); c.increment(); c.increment()
    assert c.count == 2
    print("All solutions pass.")
