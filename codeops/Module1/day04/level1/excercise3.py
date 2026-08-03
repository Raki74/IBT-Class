# Exercise 3: Bank Account (Basic)

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        # Adds amount to the balance
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        # Subtracts amount from the balance
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")

# Create an object and test deposits and withdrawals
account = Account("Ribka", 1000)
print(f"Account owner: {account.owner}, Initial balance: {account.balance}")

account.deposit(500)
account.withdraw(300)
