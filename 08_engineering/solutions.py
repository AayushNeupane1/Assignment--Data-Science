"""08 Engineering - reference solutions. Run: python solutions.py"""

import logging
from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float


def get_logger():
    return logging.getLogger(__name__)


def levels_in_order():
    return ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


if __name__ == "__main__":
    p = Product("Tea", 3.0)
    assert p.name == "Tea" and p.price == 3.0
    assert "Tea" in repr(p)
    assert isinstance(get_logger(), logging.Logger)
    assert levels_in_order() == ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    print("All solutions pass.")
