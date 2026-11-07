# 08 — Engineering (modules, project structure, logging)

The step from "a script" to "a project": splitting code into **modules**, laying
them out in a sensible **structure**, and using **logging** instead of scattered
`print()` calls. This is how the expense tracker from Module 06 would look in a
real codebase.

Files:
- `expenses/` — **the project**: the tracker, split into a proper package
  - `models.py` — the Expense data (a dataclass)
  - `storage.py` — load/save to JSON
  - `service.py` — the business logic (add, total), with logging
  - `__init__.py`
- `main.py` — the entry point that wires it together
- `exercises.py` / `solutions.py`

---

## 1. Modules — one job each

Instead of one 300-line file, split by responsibility:

```
expenses/
    models.py     # what an Expense IS
    storage.py    # how expenses are saved/loaded
    service.py    # what you can DO with expenses
```

Each module imports what it needs. This makes code easier to find, test, and change.

```python
from expenses.service import ExpenseService
```

## 2. Project structure — a common layout

```
project/
    main.py                 # entry point - run this
    requirements.txt        # dependencies
    README.md               # how to use it
    package_name/           # your code as a package
        __init__.py
        models.py
        storage.py
        service.py
    tests/                  # tests mirror the package
```

Keep the *runnable* entry point (`main.py`) separate from the *library* code
(`package_name/`). Entry point wires things together; the package holds the logic.

## 3. Logging — better than print

`print()` is fine for a demo, but real programs use the `logging` module: it has
severity **levels**, timestamps, and can write to a file — all switchable without
deleting lines.

```python
import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

log.debug("fine detail")      # hidden unless level=DEBUG
log.info("added expense")     # normal events
log.warning("low balance")    # something to watch
log.error("could not save")   # a failure
```

Levels in order: **DEBUG < INFO < WARNING < ERROR < CRITICAL**. Set the level once;
only messages at that level or above are shown.

> **Exam point:** the difference from `print` is control — you can silence
> `DEBUG`/`INFO` in production and keep only `WARNING`+ with one setting, and route
> logs to a file, without touching the code that logs.

---

## Recap

- Split code into **modules** by responsibility; keep `main.py` (entry) apart from the package (logic).
- A standard **structure** (entry point + package + tests) makes projects navigable.
- Use **logging** with levels instead of `print`; configure it once in the entry point.

**Run** `python main.py`, then do `exercises.py`.
