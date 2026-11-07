"""
OOP - PROJECT: a bank account system showing classes, objects and inheritance.

Account        : base class (deposit, withdraw)
SavingsAccount : subclass that adds interest
Run:  python bank_account.py
"""


class Account:
    """A basic bank account."""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return False, "Deposit must be positive."
        self.balance += amount
        return True, f"Deposited {amount}. Balance: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return False, "Insufficient funds."
        self.balance -= amount
        return True, f"Withdrew {amount}. Balance: {self.balance}"

    def __str__(self):
        return f"{self.owner}'s account: {self.balance}"


class SavingsAccount(Account):
    """An account that also earns interest."""

    def __init__(self, owner, balance=0, rate=0.05):
        super().__init__(owner, balance)   # reuse Account's setup
        self.rate = rate

    def add_interest(self):
        interest = self.balance * self.rate
        self.balance += interest
        return f"Added {interest:.2f} interest. Balance: {self.balance:.2f}"


def main():
    acc = Account("Ram", 100)
    print(acc.deposit(50)[1])      # Deposited 50. Balance: 150
    print(acc.withdraw(200)[1])    # Insufficient funds.
    print(acc)                     # Ram's account: 150

    savings = SavingsAccount("Bob", 1000, rate=0.10)
    print(savings.deposit(500)[1]) # inherited method -> Balance: 1500
    print(savings.add_interest())  # own method -> Added 150.00 interest...
    print(savings)                 # inherited __str__ -> Bob's account: 1650.0


if __name__ == "__main__":
    main()
