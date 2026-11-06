"""
02 Data structures - EXERCISES.
Replace every ____, then run:  python exercises.py
"""


# Exercise 1 (list) -------------------------------------------------------
# Return the list sorted, with the highest value first (descending).
def top_scores(scores):
    return sorted(scores, reverse=____)


# Exercise 2 (tuple) ------------------------------------------------------
# A point is a (x, y) tuple. Return x + y by unpacking it.
def point_sum(point):
    x, y = ____
    return x + y


# Exercise 3 (dict) -------------------------------------------------------
# Safely return the price of `item`, or 0 if it isn't in the menu.
def price_of(menu, item):
    return menu.____(item, 0)


# Exercise 4 (set) --------------------------------------------------------
# Return the number of UNIQUE words in a list (case matters).
def unique_word_count(words):
    return len(____(words))


# Exercise 5 (combine) ----------------------------------------------------
# Return a set of names that appear in BOTH class lists.
def in_both_classes(class_a, class_b):
    return set(class_a) ____ set(class_b)    # operator for "in both"


# ---------------------------------------------------------------------------
def _check():
    results = [
        ("ex1 top_scores",  top_scores([3, 9, 5]) == [9, 5, 3]),
        ("ex2 point_sum",   point_sum((2, 5)) == 7),
        ("ex3 price found", price_of({"tea": 3}, "tea") == 3),
        ("ex3 price miss",  price_of({"tea": 3}, "coffee") == 0),
        ("ex4 unique",      unique_word_count(["a", "b", "a", "c"]) == 3),
        ("ex5 both",        in_both_classes(["a", "b"], ["b", "c"]) == {"b"}),
    ]
    passed = 0
    for name, ok in results:
        print(f"{'PASS' if ok else 'FAIL'}  {name}")
        passed += ok
    print(f"\n{passed}/{len(results)} passed")


if __name__ == "__main__":
    _check()
