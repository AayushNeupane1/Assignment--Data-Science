# 11 — Statistics & Visualization

Describing data with numbers, and seeing it with charts. Both are the core of
exploratory data analysis. Uses `data/students.csv` from Module 10.

> Needs `numpy`, `pandas`, `matplotlib`. `pip install numpy pandas matplotlib`.

Files:
- `descriptive_stats.py` — mean, median, mode, variance, std, quartiles
- `visualize.py` — **the analysis**: histogram, box plot, scatter (saved to `figures/`)
- `exercises.py` / `solutions.py`

---

## 1. Descriptive statistics

| Measure | Meaning | pandas / numpy |
|---------|---------|----------------|
| **mean** | average | `s.mean()` |
| **median** | middle value (robust to outliers) | `s.median()` |
| **mode** | most frequent value | `s.mode()` |
| **variance** | average squared distance from the mean | `s.var()` |
| **std dev** | spread, in the data's own units | `s.std()` |
| **quartiles** | 25% / 50% / 75% cut points | `s.quantile([.25,.5,.75])` |

```python
scores.mean()      # the centre
scores.std()       # the spread
scores.median()    # middle - use when there are outliers, since the mean gets dragged
```

> **Exam point:** the **median** resists outliers; the **mean** does not. For
> skewed data (income, house prices) prefer the median as "typical".

## 2. Visualization — pick the chart for the question

| Chart | Answers | matplotlib |
|-------|---------|------------|
| **Histogram** | how is one variable distributed? | `plt.hist(x)` |
| **Box plot** | spread & outliers? | `plt.boxplot(x)` |
| **Scatter** | relationship between two variables? | `plt.scatter(x, y)` |

```python
import matplotlib
matplotlib.use("Agg")              # save to file without a screen (headless)
import matplotlib.pyplot as plt

plt.hist(df["score"], bins=15)
plt.xlabel("score"); plt.ylabel("count"); plt.title("Score distribution")
plt.savefig("figures/scores.png", dpi=120)
plt.close()
```

> **Tip:** always label axes and give the chart a title. An unlabelled chart is
> unreadable to anyone but you.

---

## Recap

- **Centre** with mean/median/mode; **spread** with variance/std/quartiles.
- The **median** beats the mean for skewed data with outliers.
- **Histogram** = distribution, **box plot** = spread/outliers, **scatter** = relationship.
- Always label axes and title your charts.

**Run** `python visualize.py` (writes PNGs to `figures/`), then do `exercises.py`.
