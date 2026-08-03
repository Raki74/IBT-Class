# Mini Project: Addis Bank Account System (Version 1)
# A menu-driven banking program with full encapsulation

class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
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

    def show_info(self):
        print(f"\nAccount Number: {self.account_number}")
        print(f"Owner: {self.owner}")
        print(f"Balance: {self.__balance}")


accounts = {}  # account_number -> BankAccount object
next_account_number = 1000


def create_account():
    global next_account_number
    owner = input("Enter account owner's name: ")
    try:
        initial_deposit = float(input("Enter initial deposit amount: "))
        if initial_deposit < 0:
            print("Initial deposit cannot be negative.")
            return
    except ValueError:
        print("Invalid amount. Account not created.")
        return

    account_number = next_account_number
    accounts[account_number] = BankAccount(account_number, owner, initial_deposit)
    next_account_number += 1
    print(f"Account created successfully! Account Number: {account_number}")


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


def check_balance():
    account = get_account()
    if account is None:
        return
    print(f"Balance: {account.balance}")


def view_account_info():
    account = get_account()
    if account is None:
        return
    account.show_info()


# Main menu loop
while True:
    print("\n--- Addis Bank Account System ---")
    print("1. Create new account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check balance")
    print("5. View account info")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit_money()
    elif choice == "3":
        withdraw_money()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        view_account_info()
    elif choice == "6":
        print("Thank you for using Addis Bank Account System. Goodbye!")
        break
    else:
        print("Invalid option. Please choose between 1 and 6.")