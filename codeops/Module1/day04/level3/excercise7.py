# Exercise 7: Full Bank Account with Properties

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self):
        # Getter for balance
        return self.__balance

    @balance.setter
    def balance(self, value):
        # Setter with validation - balance cannot be set negative directly
        if value < 0:
            print("Balance cannot be negative.")
        else:
            self.__balance = value

    def deposit(self, amount):
        # Validates positive amount only
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        # Checks sufficient funds
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.__balance:
            print(f"Insufficient funds. Current balance: {self.__balance}")
            return
        self.__balance -= amount
        print(f"Withdrew {amount}. New balance: {self.__balance}")

    def transfer(self, to_account, amount):
        # Transfers amount to another BankAccount object
        if amount <= 0:
            print("Transfer amount must be positive.")
            return
        if amount > self.__balance:
            print(f"Insufficient funds to transfer. Current balance: {self.__balance}")
            return
        self.__balance -= amount
        to_account.deposit(amount)
        print(f"Transferred {amount} to {to_account.owner}. New balance: {self.__balance}")

# Create BankAccount objects and test
account1 = BankAccount("Ribka", 1000)
account2 = BankAccount("Dawit", 500)

print(f"{account1.owner}'s balance: {account1.balance}")
print(f"{account2.owner}'s balance: {account2.balance}")

account1.deposit(200)
account1.withdraw(150)
account1.transfer(account2, 300)

print(f"\nFinal balances:")
print(f"{account1.owner}: {account1.balance}")
print(f"{account2.owner}: {account2.balance}")