"""textkit.analysis - the actual text-analysis functions."""

from collections import Counter


def word_count(text):
    """Return the number of words in `text`."""
    return len(text.split())


def char_count(text, include_spaces=False):
    """Return the number of characters; spaces excluded unless asked for."""
    if include_spaces:
        return len(text)
    return len(text.replace(" ", ""))


def top_word(text):
    """Return the most common word (lowercased), or None for empty text."""
    words = text.lower().split()
    if not words:
        return None
    return Counter(words).most_common(1)[0][0]
