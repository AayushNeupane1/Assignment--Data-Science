# 04 — Advanced Python

Features that separate intermediate from beginner code: **iterators**,
**generators**, **decorators**, **comprehensions**, **functional tools**
(lambda/map/filter/zip/reduce), and **regular expressions**. You meet all of
these constantly in real data work.

Files:
- `iterators_demo.py`, `generators_demo.py`, `decorators_demo.py`
- `comprehensions_demo.py` — comprehensions + lambda/map/filter/zip/reduce
- `regex_demo.py` — pattern matching with `re`
- `log_processor.py` — **the project**: stream a log file lazily + a timing decorator
- `exercises.py` / `solutions.py`

---

## 1. Iterators

An **iterable** is anything you can loop over (list, str, dict). A `for` loop
calls `iter()` to get an **iterator**, then `next()` for each item.

```python
it = iter([10, 20, 30])
next(it)   # 10
next(it)   # 20   ...until StopIteration
```

## 2. Generators — lazy sequences with `yield`

A generator produces values **one at a time, on demand**, instead of building a
whole list in memory. Use `yield` instead of `return`:

```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i        # pause, hand back i, resume on the next next()
        i += 1
```

Reading a 10 GB file line by line with a generator uses almost no memory.

> **Exam point:** a generator is single-use — loop over it once and it's exhausted.

## 3. Decorators — wrap a function to add behaviour

```python
import functools

def shout(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@shout
def greet(name):
    return f"hi {name}"
```

`*args, **kwargs` let the wrapper accept and pass through any arguments.

## 4. List comprehensions

A compact, readable way to build a list from a loop (and a filter):

```python
[i for i in range(1, 21) if i % 2 == 0]   # even numbers 1..20
[n * n for n in range(1, 6)]               # squares
```

Read it as "**expression** for **item** in **iterable** if **condition**".
Shorter and faster than appending in a `for` loop.

## 5. Lambda and functional tools

A **lambda** is a one-line anonymous function. It shines as an argument to
`map`, `filter`, `reduce`, or `sorted`:

```python
from functools import reduce

double = lambda x: x * 2
list(map(lambda x: x * 2, [1, 2, 3]))        # [2, 4, 6]
list(filter(lambda x: x % 2 == 0, [1, 2, 3])) # [2]
list(zip(["a", "b"], [1, 2]))                 # [('a', 1), ('b', 2)]
reduce(lambda a, b: a + b, [1, 2, 3, 4])      # 10  (folds to one value)
```

- `map` transforms every item, `filter` keeps some, `zip` pairs lists,
  `reduce` collapses a list to a single value.

> **Exam point:** keep lambdas tiny. If the logic needs more than one
> expression, use a normal `def`.

## 6. Regular expressions (regex)

Patterns for finding/extracting text, via the `re` module:

```python
import re
re.findall(r"[A-Z][a-z]+", text)   # every Capitalised word
re.findall(r"\d+", text)            # every run of digits
re.search(r"\d{4}-\d{3}-\d{3}", text)  # first phone-like match (or None)
```

Common pieces: `\d` digit, `\w` word char, `+` one-or-more, `*` zero-or-more,
`{n}` exactly n, `[A-Z]` a character set.

---

## Recap

- **Iterator**: items one by one via `next()`. **Generator** (`yield`): lazy, memory-cheap.
- **Decorator**: wraps a function to add behaviour; apply with `@name`.
- **Comprehension**: `[expr for x in it if cond]` builds a list concisely.
- **Lambda + map/filter/zip/reduce**: compact functional transformations.
- **Regex** (`re`): match and extract text patterns.

**Run** `python comprehensions_demo.py`, `python regex_demo.py`, `python log_processor.py`,
then do `exercises.py`.
