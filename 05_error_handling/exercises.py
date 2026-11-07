"""
05 Error handling - EXERCISES.
Replace every ____, then run:  python exercises.py
"""


# Exercise 1 --------------------------------------------------------------
# Return int(text), or -1 if text isn't a valid number.
def to_int(text):
    try:
        return int(text)
    ____ ValueError:            # keyword that catches the error
        return -1


# Exercise 2 --------------------------------------------------------------
# Return a / b, or the string "undefined" if b is zero.
def divide(a, b):
    try:
        return a / b
    except ____:                # which exception for dividing by zero?
        return "undefined"


# Exercise 3 --------------------------------------------------------------
# Define a custom exception named EmptyInputError.
class EmptyInputError(____):    # what should a custom exception inherit from?
    pass


# Exercise 4 --------------------------------------------------------------
# Raise EmptyInputError if text is empty; otherwise return it uppercased.
def shout(text):
    if text == "":
        ____ EmptyInputError("text was empty")   # keyword to throw it
    return text.upper()


# ---------------------------------------------------------------------------
def _check():
    results = []
    results.append(("ex1 valid",   to_int("42") == 42))
    results.append(("ex1 invalid", to_int("abc") == -1))
    results.append(("ex2 ok",      divide(10, 2) == 5))
    results.append(("ex2 zero",    divide(10, 0) == "undefined"))
    results.append(("ex3 subclass", issubclass(EmptyInputError, Exception)))
    try:
        shout("")
        raised = False
    except EmptyInputError:
        raised = True
    results.append(("ex4 raises",  raised))
    results.append(("ex4 shout",   shout("hi") == "HI"))

    passed = 0
    for name, ok in results:
        print(f"{'PASS' if ok else 'FAIL'}  {name}")
        passed += ok
    print(f"\n{passed}/{len(results)} passed")


if __name__ == "__main__":
    _check()
