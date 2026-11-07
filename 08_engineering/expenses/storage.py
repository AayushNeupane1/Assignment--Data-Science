"""expenses.storage - saving and loading expenses as JSON."""

import json
import logging
import os

from .models import Expense

log = logging.getLogger(__name__)


def save(expenses, path):
    """Write a list of Expense objects to a JSON file."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w") as f:
        json.dump([e.to_dict() for e in expenses], f, indent=2)
    log.info("saved %d expenses to %s", len(expenses), path)


def load(path):
    """Load expenses from JSON; return [] if the file doesn't exist yet."""
    try:
        with open(path) as f:
            data = json.load(f)
    except FileNotFoundError:
        log.warning("no file at %s, starting empty", path)
        return []
    return [Expense.from_dict(d) for d in data]
