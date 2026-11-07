"""
07 Development - EXERCISES.
Replace every ____, then run:  python exercises.py
This module tests that you can import from the textkit package correctly.
"""

# Exercise 1 --------------------------------------------------------------
# Import word_count and top_word from the textkit package.
from ____ import word_count, top_word


# Exercise 2 --------------------------------------------------------------
# A requirements line pins a package to an exact version with '=='.
# Return the correct requirements string for numpy version 2.2.6.
def numpy_requirement():
    return "numpy____2.2.6"          # the operator that pins an exact version


# Exercise 3 --------------------------------------------------------------
# Which filename, placed in a folder, turns that folder into a package?
def package_marker_filename():
    return "____.py"                 # the special module name


# ---------------------------------------------------------------------------
def _check():
    results = [
        ("ex1 word_count",   word_count("a b c") == 3),
        ("ex1 top_word",     top_word("hi hi bye") == "hi"),
        ("ex2 requirement",  numpy_requirement() == "numpy==2.2.6"),
        ("ex3 marker",       package_marker_filename() == "__init__.py"),
    ]
    passed = 0
    for name, ok in results:
        print(f"{'PASS' if ok else 'FAIL'}  {name}")
        passed += ok
    print(f"\n{passed}/{len(results)} passed")


if __name__ == "__main__":
    _check()
