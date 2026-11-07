"""
File handling - PROJECT: an expense tracker that persists to disk as JSON.

Add expenses, save them, load them back next run. Shows the full cycle:
Python objects <-> JSON file, with a missing-file guard for the first run.
Run:  python expense_tracker.py
"""

import json
import os

PATH = "data/expenses.json"


def load_expenses():
    """Load the saved expenses, or start empty on the first run."""
    try:
        with open(PATH) as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_expenses(expenses):
    """Write the expenses list to disk as formatted JSON."""
    os.makedirs("data", exist_ok=True)
    with open(PATH, "w") as f:
        json.dump(expenses, f, indent=2)


def add_expense(expenses, item, amount):
    """Append a new expense record."""
    expenses.append({"item": item, "amount": amount})
    return expenses


def total(expenses):
    """Return the sum of all expense amounts."""
    return sum(e["amount"] for e in expenses)


def main():
    # fresh start each run so the demo is reproducible
    if os.path.exists(PATH):
        os.remove(PATH)

    expenses = load_expenses()          # [] on first run
    add_expense(expenses, "Groceries", 45.50)
    add_expense(expenses, "Bus fare", 3.20)
    add_expense(expenses, "Coffee", 4.00)
    save_expenses(expenses)

    # load it back from disk, proving it persisted
    reloaded = load_expenses()
    print("Saved and reloaded expenses:")
    for e in reloaded:
        print(f"  {e['item']}: ${e['amount']:.2f}")
    print(f"Total: ${total(reloaded):.2f}")


if __name__ == "__main__":
    main()
