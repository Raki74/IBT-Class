# Mini Project: Addis Bank System - Version 2
# Menu-driven banking system using inheritance, abstraction, and polymorphism

from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self._balance = balance

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
        print(f"\n--- Statement: Account #{self.account_number} ({self.owner}) ---")
        print(f"Balance: {self._balance}")


class SavingsAccount(Account):
    def __init__(self, account_number, owner, balance=0, interest_rate=0.05):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self._balance * self.interest_rate

    def apply_interest(self):
        interest = self.calculate_interest()
        self.deposit(interest)
        print(f"Interest of {interest:.2f} applied.")

    def statement(self):
        print(f"\n--- Savings Statement: Account #{self.account_number} ({self.owner}) ---")
        print(f"Balance: {self._balance}")
        print(f"Interest Rate: {self.interest_rate * 100}%")


class CurrentAccount(Account):
    def __init__(self, account_number, owner, balance=0, overdraft_limit=500):
        super().__init__(account_number, owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self._balance + self.overdraft_limit:
            print(f"Withdrawal exceeds overdraft limit. Max available: {self._balance + self.overdraft_limit}")
            return
        self._balance -= amount
        print(f"Withdrew {amount}. New balance: {self._balance}")

    def calculate_interest(self):
        return 0

    def statement(self):
        print(f"\n--- Current Account Statement: Account #{self.account_number} ({self.owner}) ---")
        print(f"Balance: {self._balance}")
        print(f"Overdraft Limit: {self.overdraft_limit}")


accounts = {}
next_account_number = 1000


def create_savings_account():
    global next_account_number
    owner = input("Enter owner's name: ")
    try:
        balance = float(input("Enter initial deposit: "))
        rate = float(input("Enter interest rate (e.g. 0.05 for 5%): "))
    except ValueError:
        print("Invalid input. Account not created.")
        return
    acc_num = next_account_number
    accounts[acc_num] = SavingsAccount(acc_num, owner, balance, rate)
    next_account_number += 1
    print(f"Savings Account created! Account Number: {acc_num}")


def create_current_account():
    global next_account_number
    owner = input("Enter owner's name: ")
    try:
        balance = float(input("Enter initial deposit: "))
        overdraft = float(input("Enter overdraft limit: "))
    except ValueError:
        print("Invalid input. Account not created.")
        return
    acc_num = next_account_number
    accounts[acc_num] = CurrentAccount(acc_num, owner, balance, overdraft)
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
    # Applies interest to every SavingsAccount using polymorphism-friendly type check
    count = 0
    for account in accounts.values():
        if isinstance(account, SavingsAccount):
            account.apply_interest()
            count += 1
    if count == 0:
        print("No savings accounts found.")


def show_all_accounts():
    # Demonstrates polymorphism - same method call, different behavior per type
    if not accounts:
        print("No accounts to show.")
        return
    for account in accounts.values():
        account.statement()


# Main menu loop
while True:
    print("\n--- Addis Bank System (v2) ---")
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