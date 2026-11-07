# 09 — NumPy

The foundation of data science in Python. NumPy gives you the **array**: a fast,
vectorized container for numbers that pandas, scikit-learn and everything else is
built on.

> Needs `numpy`. Install with `pip install numpy`.

Files:
- `creation.py` — making arrays (array, zeros, arange, linspace, random)
- `attributes_indexing.py` — ndim/shape/size/dtype, slicing, 2D & 3D
- `operations.py` — vectorized math, boolean masking, np.where, axis aggregations
- `exercises.py` / `solutions.py`

---

## 1. Why arrays — vectorization

```python
import numpy as np
arr = np.array([1, 2, 3, 4])
arr * 2            # [2 4 6 8]  - one operation on the whole array
arr + arr          # [2 4 6 8]  - element-wise
```

A loop in C under the hood: far faster than a Python `for` loop, and shorter to write.

## 2. Creating arrays

| Want | Use | Example |
|------|-----|---------|
| from data | `np.array` | `np.array([1,2,3])` |
| zeros/ones | `np.zeros` / `np.ones` | `np.zeros((2,3))` |
| a range by **step** | `np.arange` | `np.arange(0,10,2)` → `[0 2 4 6 8]` |
| N points by **count** | `np.linspace` | `np.linspace(0,1,5)` |
| random (reproducible) | `default_rng` | `np.random.default_rng(42).integers(1,100,5)` |

> **Exam point:** `arange` stop is *excluded* and you give the step; `linspace`
> stop is *included* and you give the number of points.

## 3. Attributes, indexing, slicing

```python
m = np.array([[1,2,3],[4,5,6]])
m.shape      # (2, 3)   <- check this constantly
m.ndim       # 2
m[0, 2]      # 3        [row, column]
m[:, 0]      # [1 4]    whole column 0
```

> **Pitfall:** a slice is a **view**, not a copy — editing it changes the original.
> Use `.copy()` for an independent one.

## 4. Operations that matter for data

```python
a = np.array([1, -2, 3, -4])

a[a > 0]                  # [1 3]        boolean mask - keep positives
np.where(a < 0, 0, a)     # [1 0 3 0]    replace negatives with 0

m = np.array([[1,2],[3,4]])
m.sum(axis=0)             # [4 6]  down the columns
m.sum(axis=1)             # [3 7]  across the rows
m.mean()                  # 2.5    everything
```

`axis=0` = collapse rows (per-column), `axis=1` = collapse columns (per-row).
This is the single most useful idea when you move to pandas.

---

## Recap

- Arrays give **vectorized**, fast, element-wise math.
- Create with `array/zeros/arange/linspace` and a seeded `default_rng`.
- Index 2D with `[row, col]`; a slice is a view — `.copy()` to detach.
- **Boolean masks** filter, `np.where` replaces, and `axis=` aggregates per column/row.

**Run** the demos, then do `exercises.py`.
