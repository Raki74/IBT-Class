# Exercise 6: Abstract Base Class
# Make Account abstract with an abstract method calculate_interest()

from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.__balance:
            print(f"Insufficient funds. Current balance: {self.__balance}")
            return
        self.__balance -= amount
        print(f"Withdrew {amount}. New balance: {self.__balance}")

    @abstractmethod
    def calculate_interest(self):
        # Must be implemented by subclasses
        pass


class SavingsAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        # Implements the abstract method
        return self.balance * self.interest_rate


class CurrentAccount(Account):
    def __init__(self, owner, balance=0, overdraft_limit=500):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def calculate_interest(self):
        # Current accounts don't earn interest
        return 0


# Test - Account cannot be instantiated directly (it's abstract)
try:
    account = Account("Test", 100)
except TypeError as e:
    print(f"Error: {e}")

savings = SavingsAccount("Ribka", 1000, 0.05)
current = CurrentAccount("Dawit", 500, 300)

print(f"\nSavings interest: {savings.calculate_interest():.2f}")
print(f"Current account interest: {current.calculate_interest()}")