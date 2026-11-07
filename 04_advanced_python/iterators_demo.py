"""Advanced - iterators: iter() and next() behind every for loop. Run: python iterators_demo.py"""


def main():
    nums = [10, 20, 30]
    it = iter(nums)
    print("next:", next(it))   # 10
    print("next:", next(it))   # 20
    print("next:", next(it))   # 30
    try:
        next(it)
    except StopIteration:
        print("StopIteration: the iterator is exhausted")


if __name__ == "__main__":
    main()
