"""
Engineering - PROJECT entry point: wire the expenses package together with logging.
Run:  python main.py
"""

import logging

from expenses import ExpenseService
from expenses import storage

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)-7s %(name)s: %(message)s",
)

PATH = "data/expenses.json"


def main():
    service = ExpenseService()
    service.add("Groceries", 45.50)
    service.add("Bus fare", 3.20)

    try:
        service.add("Refund", -5)      # rejected + logged as ERROR
    except ValueError:
        pass

    storage.save(service.all(), PATH)
    reloaded = storage.load(PATH)

    print("\nExpenses on file:")
    for e in reloaded:
        print(f"  {e.item}: ${e.amount:.2f}")
    print(f"Total: ${sum(e.amount for e in reloaded):.2f}")


if __name__ == "__main__":
    main()
