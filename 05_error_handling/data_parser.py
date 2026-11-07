"""
Error handling - PROJECT: a resilient parser for messy 'name,price' rows.

Bad rows don't crash the program - they're caught, logged, and skipped, while
good rows are parsed. This is exactly how you clean real-world data files.
Run:  python data_parser.py
"""


class InvalidRowError(Exception):
    """Raised when a row can't be parsed into (name, price)."""
    pass


def parse_row(row):
    """Parse 'name,price' into (name, float(price)). Raise InvalidRowError if bad."""
    parts = row.split(",")
    if len(parts) != 2:
        raise InvalidRowError(f"expected 2 fields, got {len(parts)}")
    name, price_text = parts[0].strip(), parts[1].strip()
    if not name:
        raise InvalidRowError("missing name")
    try:
        price = float(price_text)
    except ValueError:
        raise InvalidRowError(f"price '{price_text}' is not a number")
    return name, price


def parse_all(rows):
    """Return (good_records, errors). Never crashes on a bad row."""
    good = []
    errors = []
    for i, row in enumerate(rows, start=1):
        try:
            good.append(parse_row(row))
        except InvalidRowError as e:
            errors.append(f"row {i}: {e}")
    return good, errors


def main():
    rows = [
        "Tea, 3.50",
        "Coffee, 4.00",
        "Cake",                 # too few fields
        ", 2.00",               # missing name
        "Juice, free",          # bad price
        "Water, 1.25",
    ]
    good, errors = parse_all(rows)

    print("Parsed records:")
    for name, price in good:
        print(f"  {name}: ${price:.2f}")

    print("\nSkipped rows:")
    for err in errors:
        print(f"  {err}")

    print(f"\n{len(good)} ok, {len(errors)} skipped")


if __name__ == "__main__":
    main()
