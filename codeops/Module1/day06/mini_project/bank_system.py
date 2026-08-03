# Mini Project: Clean Addis Bank System
# Demonstrates SOLID principles + Factory, Singleton, and Observer patterns

from abc import ABC, abstractmethod


# --- SINGLETON: bank-wide configuration ---
class BankConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.interest_rate = 0.05
            cls._instance.overdraft_limit = 500
        return cls._instance


# --- OBSERVER: notification system ---
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


# --- Account hierarchy (SRP, OCP, DIP, ISP all applied) ---
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
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print(f"Insufficient funds. Current balance: {self.balance}")
            return
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")
        if amount > 3000:
            self._notify_all(f"Large withdrawal: {self.owner} withdrew {amount} from account #{self.account_number}.")

    @abstractmethod
    def calculate_interest(self):
        pass

    def statement(self):
        print(f"\n--- Statement: Account #{self.account_number} ({self.owner}) ---")
        print(f"Type: {self.__class__.__name__}")
        print(f"Balance: {self.balance}")


class SavingsAccount(Account):
    def __init__(self, account_number, owner, balance):
        super().__init__(account_number, owner, balance)
        self.interest_rate = BankConfig().interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate

    def apply_interest(self):
        interest = self.calculate_interest()
        self.deposit(interest)
        print(f"Interest of {interest:.2f} applied.")

    def statement(self):
        super().statement()
        print(f"Interest Rate: {self.interest_rate * 100}%")


class CurrentAccount(Account):
    def __init__(self, account_number, owner, balance):
        super().__init__(account_number, owner, balance)
        self.overdraft_limit = BankConfig().overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance + self.overdraft_limit:
            print(f"Withdrawal exceeds overdraft limit. Max available: {self.balance + self.overdraft_limit}")
            return
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")
        if amount > 3000:
            self._notify_all(f"Large withdrawal: {self.owner} withdrew {amount} from account #{self.account_number}.")

    def calculate_interest(self):
        return 0

    def statement(self):
        super().statement()
        print(f"Overdraft Limit: {self.overdraft_limit}")


# --- FACTORY: centralizes account creation ---
class AccountFactory:
    @staticmethod
    def create(kind, account_number, owner, balance):
        if kind == "savings":
            account = SavingsAccount(account_number, owner, balance)
        elif kind == "current":
            account = CurrentAccount(account_number, owner, balance)
        else:
            raise ValueError(f"Unknown account kind: {kind}")

        # Every new account automatically gets standard observers
        account.add_observer(SMSAlert())
        account.add_observer(AuditLog())
        return account


# --- Application state ---
accounts = {}
next_account_number = 1000


def create_savings_account():
    global next_account_number
    owner = input("Enter owner's name: ")
    try:
        balance = float(input("Enter initial deposit: "))
    except ValueError:
        print("Invalid amount. Account not created.")
        return
    acc_num = next_account_number
    accounts[acc_num] = AccountFactory.create("savings", acc_num, owner, balance)
    next_account_number += 1
    print(f"Savings Account created! Account Number: {acc_num}")


def create_current_account():
    global next_account_number
    owner = input("Enter owner's name: ")
    try:
        balance = float(input("Enter initial deposit: "))
    except ValueError:
        print("Invalid amount. Account not created.")
        return
    acc_num = next_account_number
    accounts[acc_num] = AccountFactory.create("current", acc_num, owner, balance)
    next_account_number += 1
    print(f"Current Account created! Account Number: {acc_num}")


def get_account():
    try:
        acc_num = int(input("Enter account number: "))
    except ValueError:
        print("Invalid account number.")
        return None
    account = accounts.get(acc_num)
    if account is None:
        print("Account not found.")
    return account


def deposit_money():
    account = get_account()
    if account is None:
        return
    try:
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)
    except ValueError:
        print("Invalid amount.")


def withdraw_money():
    account = get_account()
    if account is None:
        return
    try:
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)
    except ValueError:
        print("Invalid amount.")


def show_statement():
    account = get_account()
    if account is None:
        return
    account.statement()


def apply_interest_to_all_savings():
    # New feature - added without breaking any existing code (OCP in action)
    count = 0
    for account in accounts.values():
        if isinstance(account, SavingsAccount):
            account.apply_interest()
            count += 1
    if count == 0:
        print("No savings accounts found.")


def show_all_accounts():
    if not accounts:
        print("No accounts to show.")
        return
    for account in accounts.values():
        account.statement()


# --- Main menu loop ---
while True:
    print("\n--- Addis Bank System (Clean Architecture) ---")
    print("1. Create Savings Account")
    print("2. Create Current Account")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Show statement")
    print("6. Apply interest to all savings accounts")
    print("7. Show all accounts")
    print("8. Exit")

    choice = input("Choose an option (1-8): ")

    if choice == "1":
        create_savings_account()
    elif choice == "2":
        create_current_account()
    elif choice == "3":
        deposit_money()
    elif choice == "4":
        withdraw_money()
    elif choice == "5":
        show_statement()
    elif choice == "6":
        apply_interest_to_all_savings()
    elif choice == "7":
        show_all_accounts()
    elif choice == "8":
        print("Thank you for using Addis Bank System. Goodbye!")
        break
    else:
        print("Invalid option. Please choose between 1 and 8.")