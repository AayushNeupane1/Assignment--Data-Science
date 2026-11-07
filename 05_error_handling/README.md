# 05 — Error handling

Real programs meet bad input, missing files, and wrong types. **Exceptions** let
you handle those cleanly instead of crashing. In data science this is daily work:
messy CSVs, missing values, bad API responses.

Files:
- `exceptions_demo.py` — try/except/else/finally, catching specific errors
- `custom_exceptions.py` — defining your own exception types
- `data_parser.py` — **the project**: a resilient parser that survives bad rows
- `exercises.py` / `solutions.py`

---

## 1. try / except

```python
try:
    value = int("abc")          # raises ValueError
except ValueError:
    print("not a number")        # handle it, don't crash
```

Catch **specific** exceptions, not a bare `except:` — otherwise you hide real bugs.

| Exception | Raised when |
|-----------|-------------|
| `ValueError` | right type, wrong value (`int("abc")`) |
| `TypeError`  | wrong type (`"a" + 1`) |
| `KeyError`   | missing dict key |
| `IndexError` | list index out of range |
| `FileNotFoundError` | opening a file that doesn't exist |
| `ZeroDivisionError` | dividing by zero |

## 2. else and finally

```python
try:
    f = open("data.txt")
except FileNotFoundError:
    print("no file")
else:
    print("opened fine")   # runs only if NO exception happened
    f.close()
finally:
    print("always runs")    # cleanup - runs whether or not it failed
```

## 3. Raising exceptions

Stop early when something is wrong:

```python
def set_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age
```

## 4. Custom exceptions

Define your own for your program's specific failures — clearer than a generic
`ValueError`:

```python
class InvalidRowError(Exception):
    """Raised when a data row can't be parsed."""
    pass

raise InvalidRowError("row 4 has no price")
```

A custom exception is just a class that inherits from `Exception`.

> **Exam point:** `except A as e:` binds the exception object to `e`, so you can
> read `str(e)` for its message or log it.

---

## Recap

- Wrap risky code in `try`; handle named exceptions in `except`.
- `else` runs on success, `finally` always runs (cleanup).
- `raise` throws an exception; define custom ones by subclassing `Exception`.
- Catch **specific** exceptions, never a bare `except`.

**Run** `python data_parser.py`, then do `exercises.py`.
