# 10 — pandas

pandas is how you work with **tables** in Python. The `DataFrame` (rows and
columns, like a spreadsheet) is the workhorse of data analysis. Everything here
uses `data/students.csv` (200 rows), built by `make_dataset.py`.

> Needs `pandas`. Install with `pip install pandas`.

Files:
- `make_dataset.py` — regenerates the dataset (already run for you)
- `basics.py` — Series/DataFrame, loading CSV, selecting, filtering
- `cleaning.py` — missing values, dtypes, duplicates
- `eda.py` — **the analysis**: describe, groupby, correlation
- `exercises.py` / `solutions.py`

---

## 1. Series and DataFrame

- A **Series** is one column (a labelled 1D array).
- A **DataFrame** is a whole table (a dict of Series sharing an index).

```python
import pandas as pd
df = pd.read_csv("data/students.csv")

df.head()          # first 5 rows
df.shape           # (200, 5)  -> (rows, columns)
df.columns         # the column names
df["score"]        # one column (a Series)
df[["city","score"]]  # several columns (a DataFrame)
```

## 2. Selecting and filtering

```python
df.loc[0, "score"]              # label-based: row 0, column 'score'
df.iloc[0, 4]                   # position-based: row 0, column 4

# boolean filtering - the pandas equivalent of a NumPy mask
df[df["score"] > 80]            # rows where score > 80
df[(df["city"] == "Sydney") & (df["age"] < 25)]   # combine with & and |
```

> **Exam point:** use `&` / `|` (not `and`/`or`) for pandas conditions, and wrap
> each condition in parentheses.

## 3. Cleaning — missing data

Real data has gaps (`NaN`). You either drop or fill them.

```python
df.isnull().sum()         # count NaN per column
df.dropna()               # drop any row with a NaN
df["score"].fillna(df["score"].mean())   # fill NaN with the column mean
df.drop_duplicates()      # remove duplicate rows
df["age"].astype(int)     # fix a column's dtype
```

## 4. EDA — understanding the data

```python
df.describe()                        # count, mean, std, min, quartiles, max
df["city"].value_counts()            # how many of each category
df.groupby("city")["score"].mean()   # average score per city
df[["study_hours","score"]].corr()   # correlation between two columns
```

`groupby` is the most important analysis tool: **split** by a category,
**apply** a calculation, **combine** the results.

---

## Recap

- `read_csv` loads a table; `.head()`, `.shape`, `.describe()` get you oriented.
- Select columns with `df["col"]`; filter rows with boolean masks using `&`/`|`.
- Clean with `isnull().sum()`, `dropna`/`fillna`, `drop_duplicates`, `astype`.
- Analyse with `value_counts`, `groupby`, and `corr`.

**Run** `python eda.py`, then do `exercises.py`.
