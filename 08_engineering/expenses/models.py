"""expenses.models - what an Expense is."""

from dataclasses import dataclass


@dataclass
class Expense:
    """A single expense. A dataclass auto-generates __init__, __repr__, __eq__."""
    item: str
    amount: float

    def to_dict(self):
        return {"item": self.item, "amount": self.amount}

    @staticmethod
    def from_dict(d):
        return Expense(d["item"], d["amount"])
