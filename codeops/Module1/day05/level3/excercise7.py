# Exercise 7: Full Account Hierarchy
# Improved abstract Account class with proper super() usage and @property

from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance   # protected, not private, so subclasses can adjust it safely

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self._balance += amount
        print(f"Deposited {amount}. New balance: {self._balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self._balance:
            print(f"Insufficient funds. Current balance: {self._balance}")
            return
        self._balance -= amount
        print(f"Withdrew {amount}. New balance: {self._balance}")

    @abstractmethod
    def calculate_interest(self):
        pass

    def statement(self):
        print(f"\n--- Statement for {self.owner} ---")
        print(f"Balance: {self.balance}")


class SavingsAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.__interest_rate = interest_rate  # private, since only this class manages it

    @property
    def interest_rate(self):
        return self.__interest_rate

    def calculate_interest(self):
        return self.balance * self.__interest_rate

    def add_interest(self):
        interest = self.calculate_interest()
        self.deposit(interest)

    def statement(self):
        print(f"\n--- Savings Statement for {self.owner} ---")
        print(f"Balance: {self.balance}")
        print(f"Interest Rate: {self.__interest_rate * 100}%")


class CurrentAccount(Account):
    def __init__(self, owner, balance=0, overdraft_limit=500):
        super().__init__(owner, balance)
        self.__overdraft_limit = overdraft_limit

    @property
    def overdraft_limit(self):
        return self.__overdraft_limit

    def withdraw(self, amount):
        # Overridden to allow overdraft, using the protected _balance directly
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance + self.__overdraft_limit:
            print(f"Withdrawal exceeds overdraft limit. Max available: {self.balance + self.__overdraft_limit}")
            return
        self._balance -= amount
        print(f"Withdrew {amount}. New balance: {self._balance}")

    def calculate_interest(self):
        # Current accounts earn no interest
        return 0

    def statement(self):
        print(f"\n--- Current Account Statement for {self.owner} ---")
        print(f"Balance: {self.balance}")
        print(f"Overdraft Limit: {self.__overdraft_limit}")


# Test the improved hierarchy
savings = SavingsAccount("Ribka", 1000, 0.05)
current = CurrentAccount("Dawit", 500, 300)

savings.statement()
savings.add_interest()

current.statement()
current.withdraw(700)
current.withdraw(200)
