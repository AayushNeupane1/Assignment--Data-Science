"""02 Data structures - reference solutions. Run: python solutions.py"""


def top_scores(scores):
    return sorted(scores, reverse=True)


def point_sum(point):
    x, y = point
    return x + y


def price_of(menu, item):
    return menu.get(item, 0)


def unique_word_count(words):
    return len(set(words))


def in_both_classes(class_a, class_b):
    return set(class_a) & set(class_b)


if __name__ == "__main__":
    assert top_scores([3, 9, 5]) == [9, 5, 3]
    assert point_sum((2, 5)) == 7
    assert price_of({"tea": 3}, "tea") == 3
    assert price_of({"tea": 3}, "coffee") == 0
    assert unique_word_count(["a", "b", "a", "c"]) == 3
    assert in_both_classes(["a", "b"], ["b", "c"]) == {"b"}
    print("All solutions pass.")
