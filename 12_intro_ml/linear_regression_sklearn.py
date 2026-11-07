"""
Intro ML - the same linear regression with scikit-learn, incl. a train/test split.
Run:  python linear_regression_sklearn.py
If scikit-learn isn't installed, it tells you how and exits cleanly.
"""

import pandas as pd

try:
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error, r2_score
except ImportError:
    print("scikit-learn isn't installed. Run:  pip install scikit-learn")
    raise SystemExit(0)


def main():
    df = pd.read_csv("data/students.csv").dropna(subset=["study_hours", "score"])
    X = df[["study_hours"]]      # 2D: features must be a table
    y = df["score"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    model = LinearRegression().fit(X_train, y_train)
    preds = model.predict(X_test)

    print(f"slope     : {model.coef_[0]:.3f}")
    print(f"intercept : {model.intercept_:.3f}")
    print(f"test MSE  : {mean_squared_error(y_test, preds):.2f}")
    print(f"test R^2  : {r2_score(y_test, preds):.3f}")
    print(f"predict 6h -> score {model.predict([[6]])[0]:.1f}")


if __name__ == "__main__":
    main()
