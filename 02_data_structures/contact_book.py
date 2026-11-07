"""
Data structures - PROJECT: a contact book that uses all four containers.

- dict   : stores contacts, name -> record
- tuple  : each record's phone+email is a fixed (phone, email) pair
- list   : search results
- set    : tracks the unique cities contacts live in

Run:  python contact_book.py
"""


def add_contact(book, name, phone, email, city):
    """Add or update a contact. The record stores a (phone, email) tuple + city."""
    book[name] = {"contact": (phone, email), "city": city}
    return book


def find_by_city(book, city):
    """Return a sorted list of names living in `city`."""
    matches = [name for name, rec in book.items() if rec["city"] == city]
    return sorted(matches)


def unique_cities(book):
    """Return the set of distinct cities across all contacts."""
    return {rec["city"] for rec in book.values()}


def main():
    book = {}
    add_contact(book, "Ram", "0401-111", "ram@example.com", "Melbourne")
    add_contact(book, "Bob", "0402-222", "ram@example.com", "Sydney")
    add_contact(book, "Smriti", "0403-333", "ram@example.com", "Melbourne")

    print("All contacts:")
    for name, rec in book.items():
        phone, email = rec["contact"]            # tuple unpacking
        print(f"  {name}: {phone}, {email} ({rec['city']})")

    print("\nIn Melbourne:", find_by_city(book, "Melbourne"))
    print("Unique cities:", sorted(unique_cities(book)))


if __name__ == "__main__":
    main()
