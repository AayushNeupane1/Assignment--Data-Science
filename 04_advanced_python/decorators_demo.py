"""Advanced - decorators: wrap a function to add behaviour. Run: python decorators_demo.py"""

import functools


def shout(func):
    @functools.wraps(func)         # keeps the original name/docstring
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper


@shout
def greet(name):
    return f"hi {name}"


def main():
    print(greet("aastha"))    # HI AASTHA
    print(greet.__name__)     # greet  (thanks to functools.wraps)


if __name__ == "__main__":
    main()
