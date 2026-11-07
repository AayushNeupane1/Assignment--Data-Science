# 02 — Data structures

Python's four core containers. Choosing the right one is half of writing good code.

| Structure | Syntax | Ordered? | Mutable? | Duplicates? | Use it for |
|-----------|--------|----------|----------|-------------|------------|
| **list**  | `[1, 2, 3]` | yes | yes | yes | an ordered, changeable sequence |
| **tuple** | `(1, 2, 3)` | yes | **no** | yes | fixed records that shouldn't change |
| **dict**  | `{"a": 1}`  | yes* | yes | keys unique | labelled key → value lookups |
| **set**   | `{1, 2, 3}` | no | yes | **no** | uniqueness & membership tests |

\*dicts keep insertion order in modern Python.

Files:
- `lists_demo.py`, `tuples_demo.py`, `dicts_demo.py`, `sets_demo.py`
- `contact_book.py` — **the project**, combining all four
- `exercises.py` / `solutions.py`

---

## 1. Lists — ordered and changeable

```python
marks = [85, 90, 78]
marks.append(92)        # add to the end  -> [85, 90, 78, 92]
marks[0] = 100          # change by index
marks.sort()            # sort in place
total = sum(marks)      # built-ins work on lists
```

## 2. Tuples — fixed records

```python
employee = ("Ram", 24, "Supervisor")   # (name, age, role)
name, age, role = employee                  # unpacking
# employee[0] = "Bob"  -> TypeError: tuples can't be changed
```

Use a tuple when the data shouldn't change — coordinates, a database row, a return
value with several parts.

## 3. Dictionaries — key → value

```python
student = {"name": "Ram", "mark": 90}
student["mark"]              # 90   (look up by key)
student["grade"] = "A"       # add / update a key
student.get("age", "n/a")    # safe lookup with a default
for key, value in student.items():
    print(key, value)
```

> **Exam point:** `student["age"]` on a missing key raises `KeyError`. Use
> `.get("age")` when the key might be absent.

## 4. Sets — unique items, fast membership

```python
a = {1, 2, 3}
b = {3, 4, 5}
unique = set([1, 1, 2, 3, 3])   # {1, 2, 3}  -> removes duplicates
a & b     # {3}        intersection (in both)
a | b     # {1,2,3,4,5} union (in either)
a - b     # {1, 2}     difference (in a, not b)
3 in a    # True       membership test (very fast)
```

---

## Recap

- **list** = ordered, mutable. **tuple** = ordered, immutable.
- **dict** = key→value lookups; use `.get()` to avoid `KeyError`.
- **set** = unique items + fast `in` tests + set algebra (`& | -`).

**Run** `python contact_book.py`, then do `exercises.py`.
