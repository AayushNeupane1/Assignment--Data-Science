# 11 — Statistics & Visualization

Describing data with numbers, seeing it with charts, and spotting the values that
don't belong. Core exploratory data analysis. Uses `data/students.csv` from Module 10.

> Needs `numpy`, `pandas`, `matplotlib`. `pip install numpy pandas matplotlib`.

Files:
- `descriptive_stats.py` — mean, median, mode, variance, std, quartiles
- `visualize.py` — histogram, box plot, scatter (saved to `figures/`)
- `outliers.py` — detecting & removing outliers with the IQR method
- `exercises.py` / `solutions.py`

---

## 1. Descriptive statistics

| Measure | Meaning | pandas |
|---------|---------|--------|
| **mean** | average | `s.mean()` |
| **median** | middle value (robust to outliers) | `s.median()` |
| **mode** | most frequent value | `s.mode()` |
| **variance** | average squared distance from the mean | `s.var()` |
| **std dev** | spread, in the data's own units | `s.std()` |
| **quartiles** | 25% / 50% / 75% cut points | `s.quantile([.25,.5,.75])` |

> **Exam point:** the **median** resists outliers; the **mean** gets dragged by
> them. For skewed data (income, house prices) the median is the better "typical".

## 2. Visualization — pick the chart for the question

| Chart | Answers | matplotlib |
|-------|---------|------------|
| **Histogram** | how is one variable distributed? | `plt.hist(x)` |
| **Box plot** | spread & outliers? | `plt.boxplot(x)` |
| **Scatter** | relationship between two variables? | `plt.scatter(x, y)` |

```python
import matplotlib
matplotlib.use("Agg")              # save to file without a screen
import matplotlib.pyplot as plt
plt.hist(df["score"], bins=15)
plt.xlabel("score"); plt.ylabel("count"); plt.title("Score distribution")
plt.savefig("figures/scores.png", dpi=120)
```

Always label axes and give the chart a title.

## 3. Outliers — the IQR method

An **outlier** is a value far from the rest. The standard rule uses the
**interquartile range** (IQR = Q3 − Q1): anything below `Q1 − 1.5·IQR` or above
`Q3 + 1.5·IQR` is an outlier.

```python
q1 = s.quantile(0.25)
q3 = s.quantile(0.75)
iqr = q3 - q1
lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
outliers = df[(s < lower) | (s > upper)]       # flag them
clean    = df[(s >= lower) & (s <= upper)]      # or drop them
```

> **Exam point:** the IQR rule is why a **box plot** draws points past its
> "whiskers" — those whiskers sit at the `1.5·IQR` fences.

---

## Recap

- **Centre** with mean/median/mode; **spread** with variance/std/quartiles; median beats mean for skewed data.
- **Histogram** = distribution, **box plot** = spread/outliers, **scatter** = relationship; always label.
- **Outliers** via IQR: outside `Q1 − 1.5·IQR` … `Q3 + 1.5·IQR`.

**Run** `python visualize.py` and `python outliers.py`, then do `exercises.py`.
