"""OOP - defining a class, __init__, attributes, methods. Run: python classes_demo.py"""


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks              # a list of marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 80:
            return "A"
        elif avg >= 60:
            return "B"
        return "C"


def main():
    s1 = Student("Ram", [90, 85, 95])
    s2 = Student("Bob", [55, 60, 65])

    for s in (s1, s2):
        print(f"{s.name}: avg {s.average():.1f} -> grade {s.grade()}")


if __name__ == "__main__":
    main()
