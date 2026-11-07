"""
08 Engineering - EXERCISES.
Replace every ____, then run:  python exercises.py
"""

import logging
from dataclasses import dataclass


# Exercise 1 --------------------------------------------------------------
# Make Product a dataclass so Product("Tea", 3.0) works automatically.
@____                          # the decorator that auto-writes __init__ etc.
class Product:
    name: str
    price: float


# Exercise 2 --------------------------------------------------------------
# Return a logger for the current module (the standard pattern).
def get_logger():
    return logging.____(__name__)   # function that returns a named logger


# Exercise 3 --------------------------------------------------------------
# Return the log levels in order from least to most severe.
def levels_in_order():
    return ["DEBUG", "INFO", "____", "ERROR", "CRITICAL"]   # the missing level


# ---------------------------------------------------------------------------
def _check():
    p = Product("Tea", 3.0)
    results = [
        ("ex1 dataclass fields", p.name == "Tea" and p.price == 3.0),
        ("ex1 auto repr",        "Tea" in repr(p)),
        ("ex2 logger",           isinstance(get_logger(), logging.Logger)),
        ("ex3 levels",           levels_in_order() ==
                                 ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]),
    ]
    passed = 0
    for name, ok in results:
        print(f"{'PASS' if ok else 'FAIL'}  {name}")
        passed += ok
    print(f"\n{passed}/{len(results)} passed")


if __name__ == "__main__":
    _check()
