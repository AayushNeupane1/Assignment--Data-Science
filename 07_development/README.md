# 07 — Development (environments, pip, packages)

How real Python projects are set up and shared. This is less about syntax and more
about *workflow* — the habits that stop "it works on my machine" problems.

Files:
- `textkit/` — **the project**: a small installable package
- `requirements.txt` — the project's dependencies
- `use_textkit.py` — a script that imports and uses the package
- `exercises.py` / `solutions.py`

---

## 1. Virtual environments — why

A virtual environment is an isolated Python just for one project, so project A's
library versions don't clash with project B's.

```bash
python -m venv venv          # create an env in a folder called venv/
# activate it:
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows

deactivate                    # leave the env when done
```

Your terminal prompt shows `(venv)` when it's active. Install packages *inside*
the activated env, and they stay local to the project.

> Your own `DS_Assignment` repo already has a `venv/` folder — that's this idea in
> action.

## 2. pip — installing packages

```bash
pip install numpy             # install one package
pip install numpy==2.2.0      # a specific version
pip list                      # what's installed
pip freeze > requirements.txt # record exact versions
pip install -r requirements.txt   # recreate the env from the file
```

`requirements.txt` is how someone else reproduces your setup exactly.

## 3. Packages and modules

- A **module** is a single `.py` file.
- A **package** is a folder of modules with an `__init__.py` file (it marks the
  folder as importable and can expose the package's public names).

```
textkit/
    __init__.py       <- makes 'textkit' a package
    analysis.py       <- a module inside it
```

```python
from textkit import word_count      # thanks to __init__.py re-exporting it
```

## 4. Installing your own package (editable)

```bash
pip install -e .      # install THIS project so edits take effect immediately
```

The `-e` ("editable") flag links the package instead of copying it, so you can
keep editing the source and your changes apply right away.

---

## Recap

- A **venv** isolates a project's dependencies; activate it before installing.
- **pip** installs packages; `requirements.txt` (from `pip freeze`) reproduces them.
- A **module** is a `.py` file; a **package** is a folder with `__init__.py`.
- `pip install -e .` installs your own package for development.

**Run** `python use_textkit.py`, then do `exercises.py`.
