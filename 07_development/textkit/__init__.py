"""textkit - a tiny text-analysis package.

__init__.py marks this folder as a package and re-exports the public functions,
so users can write `from textkit import word_count`.
"""

from .analysis import word_count, char_count, top_word

__all__ = ["word_count", "char_count", "top_word"]
__version__ = "0.1.0"
