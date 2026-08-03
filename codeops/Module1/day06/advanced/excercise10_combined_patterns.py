# Advanced Exercise 10: Combine Factory + Observer + Singleton

from abc import ABC, abstractmethod


# --- SINGLETON: BankConfig ---
# A Singleton ensures only ONE instance of a class ever exists.
# Perfect for something like bank-wide settings (interest rates),
# since it wouldn't make sense to have multiple conflicting "configs."
class BankConfig:
    _instance = None  # holds the single shared instance

    def __new__(cls):
        # new controls object CREATION (before init runs).
        # If an instance already exists, return that one instead of
        # creating a new one.
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.interest_rate = 0.05
            cls._instance.overdraft_limit = 500
        return cls._instance


# --- OBSERVER: notify on big transactions ---
class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass


class SMSAlert(Observer):
    def update(self, message):
        print(f"[SMS ALERT] {message}")


class AuditLog(Observer):
    def update(self, message):
        print(f"[AUDIT LOG] {message}")


# --- Account classes using the Observer pattern ---
class Account(ABC):
    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def _notify_all(self, message):
        for observer in self._observers:
            observer.update(message)

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")
        if amount > 3000:
            self._notify_all(f"Large withdrawal: {self.owner} withdrew {amount}.")

    @abstractmethod
    def calculate_interest(self):
        pass


class SavingsAccount(Account):
    def __init__(self, account_number, owner, balance):
        super().__init__(account_number, owner, balance)
        config = BankConfig()  # uses the shared Singleton config
        self.interest_rate = config.interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate


class CurrentAccount(Account):
    def __init__(self, account_number, owner, balance):
        super().__init__(account_number, owner, balance)
        config = BankConfig()
        self.overdraft_limit = config.overdraft_limit

    def calculate_interest(self):
        return 0


# --- FACTORY: create accounts ---
class AccountFactory:
    @staticmethod
    def create(kind, account_number, owner, balance):
        if kind == "savings":
            return SavingsAccount(account_number, owner, balance)
        elif kind == "current":
            return CurrentAccount(account_number, owner, balance)
        else:
            raise ValueError(f"Unknown account kind: {kind}")


# --- Test everything together ---

# Prove the Singleton works - both references are the SAME object
config1 = BankConfig()
config2 = BankConfig()
print(f"Same config instance? {config1 is config2}")
print(f"Interest rate: {config1.interest_rate}, Overdraft limit: {config1.overdraft_limit}\n")

# Use the Factory to create accounts
savings = AccountFactory.create("savings", 1000, "Ribka", 1000)
current = AccountFactory.create("current", 1001, "Dawit", 500)

# Attach observers
savings.add_observer(SMSAlert())
savings.add_observer(AuditLog())

# Test a large withdrawal to trigger observers
savings.deposit(200)
savings.withdraw(5000)
print(f"Interest: {savings.calculate_interest():.2f}")