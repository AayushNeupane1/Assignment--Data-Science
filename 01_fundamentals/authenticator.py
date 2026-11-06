"""
Fundamentals - PROJECT: a mini authenticator app, built entirely from functions.

Shows variables, conditions, loops and functions working together. Passwords are
hashed, never stored in plain text. Run:  python authenticator.py
"""

import hashlib
import string


def validate_username(username):
    """Return True if username is 3-20 chars and only letters, digits, or '_'."""
    if len(username) < 3 or len(username) > 20:
        return False
    for char in username:
        if not (char.isalnum() or char == "_"):
            return False
    return True


def validate_password(password):
    """Return True if password is >= 8 chars, has a digit, and a special char."""
    if len(password) < 8:
        return False
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    return has_digit and has_special


def hash_password(password):
    """Return the SHA-256 hash of a password as a hex string."""
    return hashlib.sha256(password.encode()).hexdigest()


def register(users, username, password):
    """Add a new user to the `users` dict. Return a (success, message) pair."""
    if not validate_username(username):
        return False, "Invalid username (3-20 letters, digits or _)."
    if username in users:
        return False, "That username is already taken."
    if not validate_password(password):
        return False, "Weak password (need 8+ chars, a digit and a symbol)."
    users[username] = hash_password(password)
    return True, "Registered successfully."


def login(users, username, password):
    """Return True only if the username exists and the password matches."""
    if username not in users:
        return False
    return users[username] == hash_password(password)


def main():
    users = {}   # username -> hashed password

    print(register(users, "aastha", "Nepal@2026"))   # (True, 'Registered...')
    print(register(users, "aastha", "Another@1"))     # taken
    print(register(users, "bob", "weak"))             # weak password

    print("login ok   :", login(users, "aastha", "Nepal@2026"))  # True
    print("login wrong :", login(users, "aastha", "wrongpass"))  # False
    print("login ghost :", login(users, "nobody", "Nepal@2026")) # False


if __name__ == "__main__":
    main()
