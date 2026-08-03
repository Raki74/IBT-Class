# Intermediate Exercise 2: Factory Pattern
#
# THE PROBLEM: When code that creates objects (e.g. "if kind == 'savings'...")
# is scattered across the program, adding a new type means hunting down
# every place that creates accounts. A Factory centralizes that logic
# into ONE place.

class Account:
    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"{self.__class__.__name__} #{self.account_number} ({self.owner}): {self.balance}"


class SavingsAccount(Account):
    def __init__(self, account_number, owner, balance, interest_rate=0.05):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate


class CurrentAccount(Account):
    def __init__(self, account_number, owner, balance, overdraft_limit=500):
        super().__init__(account_number, owner, balance)
        self.overdraft_limit = overdraft_limit


class FixedDepositAccount(Account):
    def __init__(self, account_number, owner, balance, term_months=12):
        super().__init__(account_number, owner, balance)
        self.term_months = term_months


class AccountFactory:
    # Centralizes ALL account creation logic in one place.
    # Adding a new account type later means editing ONLY this method,
    # not code scattered throughout the program.
    @staticmethod
    def create(kind, owner, number, balance):
        if kind == "savings":
            return SavingsAccount(number, owner, balance)
        elif kind == "current":
            return CurrentAccount(number, owner, balance)
        elif kind == "fixed":
            return FixedDepositAccount(number, owner, balance)
        else:
            raise ValueError(f"Unknown account kind: {kind}")


# Test the factory
account1 = AccountFactory.create("savings", "Ribka", 1000, 500)
account2 = AccountFactory.create("current", "Dawit", 1001, 1000)
account3 = AccountFactory.create("fixed", "Sara", 1002, 5000)

print(account1)
print(account2)
print(account3)

# Test invalid kind
try:
    AccountFactory.create("crypto", "Test", 9999, 100)
except ValueError as e:
    print(f"Error: {e}")