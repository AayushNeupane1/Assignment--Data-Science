"""Advanced - generators: lazy sequences with yield. Run: python generators_demo.py"""


def count_up_to(n):
    """Yield 1..n one at a time, without building a list."""
    i = 1
    while i <= n:
        yield i
        i += 1


def main():
    print("values:", list(count_up_to(5)))

    # generator expression - lazy, memory-friendly
    squares = (x * x for x in range(6))
    print("squares:", list(squares))

    # single-use: the generator above is now exhausted
    print("again  :", list(squares))   # []


if __name__ == "__main__":
    main()
