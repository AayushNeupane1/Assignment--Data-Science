"""
Advanced - PROJECT: process a log stream lazily, timed by a decorator.

- a GENERATOR streams log lines one at a time (no giant list in memory)
- a DECORATOR times how long the processing takes
Run:  python log_processor.py
"""

import functools
import time


def timed(func):
    """Decorator: print how long the wrapped function took."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[timed] {func.__name__} took {elapsed * 1000:.2f} ms")
        return result
    return wrapper


def log_lines():
    """Generator: pretend to stream log lines from a file, one at a time."""
    sample = [
        "INFO  user logged in",
        "WARN  slow response",
        "ERROR database timeout",
        "INFO  user logged out",
        "ERROR disk full",
    ]
    for line in sample:
        yield line


@timed
def count_errors(lines):
    """Count ERROR lines in a stream of log lines."""
    errors = 0
    for line in lines:
        if line.startswith("ERROR"):
            errors += 1
    return errors


def main():
    errors = count_errors(log_lines())
    print(f"Found {errors} error lines")


if __name__ == "__main__":
    main()
