# Advanced Exercise 9: Full SOLID Refactoring
#
# Starting point: a "god class" Account that does EVERYTHING -
# balance logic, notifications, persistence, and interest calculation
# all mixed into one class. We refactor it using SRP, OCP, DIP, and ISP
# together, combining ideas from all the earlier exercises.

# --- BAD VERSION (commented out, for reference) ---
# class Account:
#     def init(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Email sent to {self.owner}")
#         print(f"Saved to database")
#
#     def withdraw(self, amount):
#         self.balance -= amount
#         print(f"Email sent to {self.owner}")
#         print(f"Saved to database")
#         if amount > 3000:
#             print("SMS sent for large withdrawal")
#
#     def calculate_interest(self):
#         return self.balance * 0.05  # hardcoded, only makes sense for savings


# --- FULLY REFACTORED VERSION ---

from abc import ABC, abstractmethod


# SRP: notifications are their own responsibility
class Notifier(ABC):
    @abstractmethod
    def notify(self, message):
        pass


class EmailNotifier(Notifier):
    def notify(self, message):
        print(f"[EMAIL] {message}")


class SMSNotifier(Notifier):
    def notify(self, message):
        print(f"[SMS] {message}")


# SRP: persistence is its own responsibility
class AccountRepository:
    def save(self, account):
        print(f"[DB] Saved account #{account.account_number}")


# ISP: only accounts that earn interest implement this
class InterestBearing(ABC):
    @abstractmethod
    def calculate_interest(self):
        pass


# SRP + DIP: Account only handles account logic,
# and depends on injected notifier/repository (abstractions),
# not concrete classes it creates itself
class Account(ABC):
    def __init__(self, account_number, owner, balance, notifier, repository):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.notifier = notifier
        self.repository = repository

    def deposit(self, amount):
        self.balance += amount
        self.repository.save(self)
        self.notifier.notify(f"{self.owner} deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        self.repository.save(self)
        self.notifier.notify(f"{self.owner} withdrew {amount}. New balance: {self.balance}")
        if amount > 3000:
            self.notifier.notify(f"ALERT: Large withdrawal of {amount} on account #{self.account_number}")


# OCP: new account types can be ADDED without modifying Account
class SavingsAccount(Account, InterestBearing):
    def __init__(self, account_number, owner, balance, notifier, repository, interest_rate=0.05):
        Account.__init__(self, account_number, owner, balance, notifier, repository)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate


class CurrentAccount(Account):
    def __init__(self, account_number, owner, balance, notifier, repository, overdraft_limit=500):
        super().__init__(account_number, owner, balance, notifier, repository)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print(f"Withdrawal exceeds overdraft limit. Max available: {self.balance + self.overdraft_limit}")
            return
        self.balance -= amount
        self.repository.save(self)
        self.notifier.notify(f"{self.owner} withdrew {amount}. New balance: {self.balance}")
        if amount > 3000:
            self.notifier.notify(f"ALERT: Large withdrawal of {amount} on account #{self.account_number}")


# Test the fully refactored system
email = EmailNotifier()
repo = AccountRepository()
savings = SavingsAccount(1000, "Ribka", 1000, email, repo, 0.05)
current = CurrentAccount(1001, "Dawit", 500, SMSNotifier(), repo, 300)

savings.deposit(200)
print(f"Interest: {savings.calculate_interest():.2f}\n")

current.withdraw(4000)  # triggers large withdrawal alert AND uses overdraft