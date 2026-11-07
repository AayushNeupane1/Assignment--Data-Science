# 01 — Fundamentals

The four building blocks every other module relies on: **variables**,
**conditions**, **loops**, and **functions**.

Files:
- `variables.py` — data types, conversion, f-strings
- `conditions.py` — if / elif / else, comparison & logical operators
- `loops.py` — for / while, range, break & continue
- `authenticator.py` — **the project**: a password authenticator built from functions
- `exercises.py` / `solutions.py` — practice

---

## 1. Variables & data types

A variable is a name bound to a value. Python figures out the type for you.

```python
name = "Ram"      # str
age = 24             # int
height = 1.63        # float
is_student = True    # bool
```

Check a type with `type(x)`. Convert with `int()`, `float()`, `str()`, `bool()`:

```python
int("42") + 1        # 43   (str -> int)
str(42) + "!"        # "42!" (int -> str)
```

**f-strings** are the modern way to build text from values:

```python
print(f"{name} is {age} years old")   # Ram is 24 years old
print(f"{height:.1f} m")               # 1.6 m  (formatted to 1 decimal)
```

> **Exam point:** `"3" + 3` raises `TypeError` — you can't add a str and an int.
> Convert first.

---

## 2. Conditions

Run code only when something is true.

```python
score = 72
if score >= 80:
    grade = "A"
elif score >= 60:
    grade = "B"
else:
    grade = "C"
```

- **Comparison:** `==  !=  <  <=  >  >=`
- **Logical:** `and  or  not`

```python
age = 20
if age >= 18 and age < 65:
    print("adult")
```

> **Exam point:** `=` assigns, `==` compares. Using `=` in an `if` is a syntax error.

---

## 3. Loops

Repeat work without copy-pasting.

```python
# for: when you know what you're iterating over
for i in range(1, 4):      # 1, 2, 3  (stop is excluded)
    print(i)

# while: when you loop until a condition changes
count = 3
while count > 0:
    print(count)
    count -= 1
```

- `break` — leave the loop early.
- `continue` — skip to the next iteration.

```python
for n in range(10):
    if n == 5:
        break          # stops entirely at 5
    if n % 2 == 0:
        continue       # skips even numbers
    print(n)           # 1 3
```

---

## 4. Functions

Covered in depth by the project. In short: `def name(params):` groups reusable
logic and `return` hands a value back. See `authenticator.py`.

> **Exam point:** `return` gives a value back to your program; `print` only shows
> it on screen. A function that computes something should `return`.

---

## Recap

- Variables hold typed values; convert with `int()/str()/float()`; format with f-strings.
- `if/elif/else` picks a branch; combine tests with `and/or/not`.
- `for` iterates a sequence, `while` loops on a condition; `break`/`continue` control flow.
- Functions package logic and `return` results.

**Run** `python authenticator.py`, then do `exercises.py`.
