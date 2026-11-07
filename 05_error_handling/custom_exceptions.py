"""Error handling - defining and raising your own exceptions. Run: python custom_exceptions.py"""


class InvalidAgeError(Exception):
    """Raised when an age is outside the allowed range."""
    pass


def set_age(age):
    if not isinstance(age, int):
        raise TypeError("age must be an integer")
    if age < 0 or age > 150:
        raise InvalidAgeError(f"age {age} is out of range")
    return age


def main():
    for value in [25, -3, 200]:
        try:
            print("set_age:", set_age(value))
        except InvalidAgeError as e:
            print("InvalidAgeError:", e)


if __name__ == "__main__":
    main()
