"""Error handling - try/except/else/finally, specific exceptions. Run: python exceptions_demo.py"""


def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "cannot divide by zero"
    else:
        return result            # only if no exception
    finally:
        pass                     # would hold cleanup in a real program


def main():
    print("10 / 2 =", safe_divide(10, 2))     # 5.0
    print("10 / 0 =", safe_divide(10, 0))     # cannot divide by zero

    for text in ["42", "abc"]:
        try:
            print(f"int('{text}') =", int(text))
        except ValueError as e:
            print(f"int('{text}') failed: {e}")


if __name__ == "__main__":
    main()
