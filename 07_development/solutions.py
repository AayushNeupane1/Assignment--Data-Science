"""07 Development - reference solutions. Run: python solutions.py"""

from textkit import word_count, top_word


def numpy_requirement():
    return "numpy==2.2.6"


def package_marker_filename():
    return "__init__.py"


if __name__ == "__main__":
    assert word_count("a b c") == 3
    assert top_word("hi hi bye") == "hi"
    assert numpy_requirement() == "numpy==2.2.6"
    assert package_marker_filename() == "__init__.py"
    print("All solutions pass.")
