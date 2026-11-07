# 06 — File handling

Programs that remember things read and write files. You'll cover plain **text**,
**CSV** (tabular data — the bread and butter of data science), and **JSON**
(structured data, APIs, config).

Files:
- `text_files.py` — read/write/append text, with error handling
- `csv_files.py` — read and write CSV with the `csv` module
- `json_files.py` — read and write JSON with the `json` module
- `expense_tracker.py` — **the project**: add expenses, save to disk, load back
- `exercises.py` / `solutions.py`
- `data/` — where the demos write their files

---

## 1. Text files — always use `with`

```python
with open("notes.txt", "w") as f:     # "w" = write (overwrites!)
    f.write("hello\n")

with open("notes.txt", "r") as f:     # "r" = read
    content = f.read()
```

`with` closes the file automatically, even if an error happens. Modes:

| Mode | Meaning |
|------|---------|
| `"r"` | read (error if missing) |
| `"w"` | write (creates / **overwrites**) |
| `"a"` | append (adds to the end) |

> **Exam point:** `"w"` wipes the file. Use `"a"` to add without losing what's there.

Always guard reads against a missing file:

```python
try:
    with open("missing.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("file not found")
```

## 2. CSV — tabular data

```python
import csv

# write
with open("data/people.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age"])     # header
    writer.writerow(["Aastha", 24])

# read as dictionaries (keyed by the header row)
with open("data/people.csv") as f:
    for row in csv.DictReader(f):
        print(row["name"], row["age"])
```

Use `newline=""` when writing CSV so you don't get blank lines on Windows.

## 3. JSON — structured data

```python
import json

data = {"name": "Aastha", "skills": ["python", "sql"]}

with open("data/profile.json", "w") as f:
    json.dump(data, f, indent=2)          # Python object -> JSON file

with open("data/profile.json") as f:
    loaded = json.load(f)                 # JSON file -> Python object
```

`json.dump`/`load` work with files; `json.dumps`/`loads` work with strings
(the `s` is for "string").

---

## Recap

- Always open files with `with` so they close safely.
- Modes: `r` read, `w` overwrite, `a` append. Guard reads with `FileNotFoundError`.
- `csv.writer` / `csv.DictReader` for tables; `newline=""` on write.
- `json.dump` / `json.load` convert between Python objects and JSON files.

**Run** `python expense_tracker.py`, then do `exercises.py`.
