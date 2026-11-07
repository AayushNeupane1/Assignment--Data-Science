# 12 — Intro to Machine Learning: Linear Regression

Your first ML model. **Linear regression** fits a straight line `y = m·x + c`
through data so you can **predict** `y` from `x`. We predict a student's `score`
from their `study_hours` (the two had a 0.78 correlation in Module 10).

You'll do it **twice**: once from scratch with NumPy to see the maths, then with
scikit-learn to see how it's done in practice.

> `linear_regression_scratch.py` needs only `numpy`/`pandas`.
> `linear_regression_sklearn.py` also needs `scikit-learn` (`pip install scikit-learn`);
> it prints a friendly note and skips if scikit-learn isn't installed.

Files:
- `linear_regression_scratch.py` — the maths, by hand (from your class notebook)
- `linear_regression_sklearn.py` — the same model with scikit-learn
- `exercises.py` / `solutions.py`

---

## 1. The idea

A line is `y = m·x + c`:
- **m** (slope) — how much `y` rises when `x` goes up by 1.
- **c** (intercept) — `y` when `x` is 0.

"Fitting" means finding the `m` and `c` that make the line pass as close as
possible to all the points — minimising the **errors** (actual − predicted).

## 2. From scratch — the least-squares formulas

```
m = covariance(x, y) / variance(x)
c = mean(y) − m · mean(x)
```

```python
x_mean, y_mean = x.mean(), y.mean()
m = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean) ** 2)
c = y_mean - m * x_mean
y_pred = m * x + c
```

This is exactly what your `LinearRegression.ipynb` did — now on real data.

## 3. Measuring fit

- **MSE** (mean squared error) — average squared error; smaller is better.
- **R²** — fraction of the variation the line explains (1.0 = perfect, 0 = useless).

```python
mse = np.mean((y - y_pred) ** 2)
ss_res = np.sum((y - y_pred) ** 2)
ss_tot = np.sum((y - y_mean) ** 2)
r2 = 1 - ss_res / ss_tot
```

## 4. With scikit-learn

The real-world workflow — the same model in a few lines, plus the train/test
split that keeps you honest (you test on data the model didn't learn from):

```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

X = df[["study_hours"]]      # features are a 2D table (note double brackets)
y = df["score"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression().fit(X_train, y_train)
model.predict(X_test)        # predictions
model.score(X_test, y_test)  # R² on unseen data
```

> **Exam point:** always evaluate on a **held-out test set**, never on the data the
> model trained on — otherwise you measure memorisation, not prediction.

---

## Recap

- Linear regression fits `y = m·x + c` by minimising squared error.
- From scratch: `m = cov(x,y)/var(x)`, `c = ȳ − m·x̄`.
- Judge fit with **MSE** (lower = better) and **R²** (higher = better).
- With scikit-learn: `LinearRegression().fit()`, and always test on a held-out split.

**Run** `python linear_regression_scratch.py`, then do `exercises.py`.
