"""expenses.service - the business logic: add expenses and total them."""

import logging

from .models import Expense

log = logging.getLogger(__name__)


class ExpenseService:
    def __init__(self):
        self._expenses = []

    def add(self, item, amount):
        if amount <= 0:
            log.error("rejected %s: amount %.2f not positive", item, amount)
            raise ValueError("amount must be positive")
        self._expenses.append(Expense(item, amount))
        log.info("added %s (%.2f)", item, amount)

    def total(self):
        return sum(e.amount for e in self._expenses)

    def all(self):
        return list(self._expenses)
