"""05 Error handling - reference solutions. Run: python solutions.py"""


def to_int(text):
    try:
        return int(text)
    except ValueError:
        return -1


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "undefined"


class EmptyInputError(Exception):
    pass


def shout(text):
    if text == "":
        raise EmptyInputError("text was empty")
    return text.upper()


if __name__ == "__main__":
    assert to_int("42") == 42 and to_int("abc") == -1
    assert divide(10, 2) == 5 and divide(10, 0) == "undefined"
    assert issubclass(EmptyInputError, Exception)
    try:
        shout(""); raised = False
    except EmptyInputError:
        raised = True
    assert raised
    assert shout("hi") == "HI"
    print("All solutions pass.")
