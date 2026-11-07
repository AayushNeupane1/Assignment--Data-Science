# 04 — Advanced Python

Three features that separate intermediate from beginner code: **iterators**,
**generators**, and **decorators**. In data science you meet them constantly —
streaming large files, lazy pipelines, and timing/caching wrappers.

Files:
- `iterators_demo.py`, `generators_demo.py`, `decorators_demo.py`
- `log_processor.py` — **the project**: stream a log file lazily + a timing decorator
- `exercises.py` / `solutions.py`

---

## 1. Iterators

An **iterable** is anything you can loop over (list, str, dict). Under the hood a
`for` loop calls `iter()` to get an **iterator**, then `next()` for each item.

```python
nums = [10, 20, 30]
it = iter(nums)
next(it)   # 10
next(it)   # 20
# ...next() again and again until StopIteration
```

You rarely call `next()` by hand — but knowing a `for` loop *is* this explains
generators below.

## 2. Generators — lazy sequences with `yield`

A generator produces values **one at a time, on demand**, instead of building a
whole list in memory. Use `yield` instead of `return`:

```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i        # pause here, hand back i, resume on the next next()
        i += 1

for x in count_up_to(3):
    print(x)           # 1 2 3
```

Why it matters: reading a 10 GB file line by line with a generator uses almost no
memory, because it never holds more than one line at a time.

```python
squares = (x * x for x in range(1000000))   # generator expression - nothing computed yet
```

> **Exam point:** a generator is single-use. Once you've looped over it, it's
> exhausted — loop again and you get nothing.

## 3. Decorators — wrap a function to add behaviour

A decorator is a function that takes a function and returns a new one with extra
behaviour (logging, timing, access checks) — without changing the original.

```python
import functools

def shout(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@shout                      # same as: greet = shout(greet)
def greet(name):
    return f"hi {name}"

greet("aastha")             # "HI AASTHA"
```

`*args, **kwargs` let the wrapper accept any arguments and pass them straight
through to the real function.

---

## Recap

- An **iterator** yields items one by one via `next()`; a `for` loop uses this.
- A **generator** (`yield`, or `(... for ...)`) produces values lazily — huge memory win for big data.
- A **decorator** wraps a function to add behaviour; apply it with `@name`.

**Run** `python log_processor.py`, then do `exercises.py`.
