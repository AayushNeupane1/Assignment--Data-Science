# Fundamentals ▸ Functions

> **Project in this folder:** a small **authenticator app** — `authenticator.py` —
> built entirely out of functions. You'll read it, then complete `exercises.py`.

A **function** is a named, reusable block of code. You define it once and call it
as many times as you need. Functions are how you stop copy-pasting logic and
start building real programs.

---

## 1. Defining and calling

```python
def greet(name):          # `def`, a name, parameters in ()
    return f"Hello, {name}!"   # `return` sends a value back

message = greet("Aastha")      # call it; store what it returns
print(message)                 # Hello, Aastha!
```

- **Parameters** are the names in the definition (`name`).
- **Arguments** are the real values you pass in (`"Aastha"`).

---

## 2. `return` vs `print` — the #1 exam trap

```python
def add_print(a, b):
    print(a + b)        # shows it on screen, gives back None

def add_return(a, b):
    return a + b        # hands the value back to be used

x = add_print(2, 3)     # prints 5, but x is None
y = add_return(2, 3)    # prints nothing, but y is 5 — usable later
```

Rule: **`print` is for humans, `return` is for your program.** A function that
computes something should `return` it.

---

## 3. Arguments: positional, keyword, default

```python
def make_user(name, role="user", active=True):
    return {"name": name, "role": role, "active": active}

make_user("Bob")                      # role defaults to "user"
make_user("Eve", role="admin")        # keyword argument
make_user("Max", "guest", False)      # positional, in order
```

Default values make a parameter optional. Put parameters *with* defaults
**after** parameters without them, or Python raises an error.

---

## 4. Scope — where a variable lives

```python
total = 0                 # global

def spend(amount):
    tax = amount * 0.1    # local: exists only inside spend()
    return amount + tax

print(spend(100))         # 110.0
# print(tax)              # NameError — tax doesn't exist out here
```

A variable created inside a function is **local** and disappears when the
function ends. Reach for `return` to get values out — not global variables.

> **Pitfall — the mutable default argument.** Never use a list/dict as a
> default value; it is created **once** and shared across calls:
> ```python
> def bad(item, bucket=[]):   # DON'T
>     bucket.append(item)
>     return bucket
> bad("a"); bad("b")          # -> ['a', 'b']  (surprise!)
> ```
> Use `bucket=None` and create a fresh list inside instead.

---

## 5. Docstrings

The first string inside a function documents it. Good functions have one.

```python
def validate_password(password):
    """Return True if password is at least 8 chars and has a special char."""
    ...
```

---

## Recap

- `def name(params):` … `return value`.
- `return` gives a value back; `print` only displays — don't confuse them.
- Arguments can be positional, keyword, or have defaults.
- Variables inside a function are local; never use a mutable default argument.

**Now:** read `authenticator.py`, run it, then open `exercises.py`.
