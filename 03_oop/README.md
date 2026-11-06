# 03 — Object-Oriented Programming (OOP)

A **class** is a blueprint; an **object** is a thing built from it. OOP bundles
data (attributes) and behaviour (methods) together, so related code lives in one
place instead of scattered functions and dicts.

Files:
- `classes_demo.py` — defining a class, `__init__`, attributes, methods
- `bank_account.py` — **the project**: accounts with inheritance
- `exercises.py` / `solutions.py`

---

## 1. Classes and objects

```python
class Dog:
    def __init__(self, name, breed):   # the constructor
        self.name = name               # attribute (data on each object)
        self.breed = breed

    def bark(self):                    # method (behaviour)
        return f"{self.name} says woof!"

rex = Dog("Rex", "Lab")   # create an object (an "instance")
print(rex.name)           # Rex
print(rex.bark())         # Rex says woof!
```

- `__init__` runs automatically when you create the object; it sets up its data.
- `self` is the object itself — every method takes it as the first parameter, and
  you use `self.x` to read or set that object's own data.

> **Exam point:** forgetting `self` is the most common OOP error. `def bark():`
> (without `self`) fails with *"takes 0 positional arguments but 1 was given"*.

---

## 2. Inheritance

A subclass reuses and extends a parent class. Say *"is-a"*: a savings account
**is a** kind of account.

```python
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

class SavingsAccount(Account):          # inherits everything from Account
    def __init__(self, owner, balance=0, rate=0.05):
        super().__init__(owner, balance)  # run the parent's constructor
        self.rate = rate                  # add something new

    def add_interest(self):               # a method only savings accounts have
        self.balance += self.balance * self.rate
```

- `SavingsAccount(Account)` — the parent goes in the parentheses.
- `super().__init__(...)` — reuse the parent's setup instead of repeating it.
- The subclass can **add** methods (`add_interest`) and **override** existing ones.

---

## Recap

- **Class** = blueprint, **object** = instance built from it.
- `__init__` sets up each object's attributes; `self` refers to that object.
- **Inheritance** (`class Child(Parent)`) reuses a parent; `super()` calls back into it.
- Subclasses can add new methods or override inherited ones.

**Run** `python bank_account.py`, then do `exercises.py`.
