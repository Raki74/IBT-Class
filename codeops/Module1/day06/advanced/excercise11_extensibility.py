# Advanced Exercise 11: Refactoring Challenge
#
# THE TASK: Add a new account type, InvestmentAccount, to our system.
# THE POINT: because of OCP + Factory, this should be EASY - we add
# ONE new class and update the Factory's if-chain, WITHOUT touching
# any of SavingsAccount, CurrentAccount, or Account's existing code.

from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")

    @abstractmethod
    def calculate_interest(self):
        pass


class SavingsAccount(Account):
    def __init__(self, account_number, owner, balance, interest_rate=0.05):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate


class CurrentAccount(Account):
    def __init__(self, account_number, owner, balance, overdraft_limit=500):
        super().__init__(account_number, owner, balance)
        self.overdraft_limit = overdraft_limit

    def calculate_interest(self):
        return 0


# --- NEW: InvestmentAccount ---
# Notice: we did NOT touch Account, SavingsAccount, or CurrentAccount
# above to add this. That's OCP in action - "open for extension,
# closed for modification."
class InvestmentAccount(Account):
    def __init__(self, account_number, owner, balance, risk_level="medium"):
        super().__init__(account_number, owner, balance)
        self.risk_level = risk_level
        # Different risk levels earn different (simulated) returns
        self._return_rates = {"low": 0.03, "medium": 0.07, "high": 0.12}

    def calculate_interest(self):
        rate = self._return_rates.get(self.risk_level, 0.05)
        return self.balance * rate


# --- Factory: only ONE line needs to change to support the new type ---
class AccountFactory:
    @staticmethod
    def create(kind, account_number, owner, balance, **kwargs):
        if kind == "savings":
            return SavingsAccount(account_number, owner, balance, **kwargs)
        elif kind == "current":
            return CurrentAccount(account_number, owner, balance, **kwargs)
        elif kind == "investment":
            return InvestmentAccount(account_number, owner, balance, **kwargs)
        else:
            raise ValueError(f"Unknown account kind: {kind}")


# Test - the new account type works seamlessly alongside the old ones
accounts = [
    AccountFactory.create("savings", 1000, "Ribka", 1000, interest_rate=0.05),
    AccountFactory.create("current", 1001, "Dawit", 500, overdraft_limit=300),
    AccountFactory.create("investment", 1002, "Sara", 5000, risk_level="high"),
]

for account in accounts:
    print(f"{account.__class__.__name__} #{account.account_number} ({account.owner})")
    print(f"Balance: {account.balance}, Calculated return/interest: {account.calculate_interest():.2f}\n")