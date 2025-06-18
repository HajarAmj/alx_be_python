class BankAccount:
    """A simple bank account class."""

    def __init__(self, initial_balance=0.0):
        self.__account_balance = float(initial_balance)

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")

    def display_balance(self):
        """Display the current balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")


