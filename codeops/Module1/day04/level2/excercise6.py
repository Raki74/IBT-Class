# Exercise 6: Encapsulation Practice
# Modified Account class with private balance and a read-only property

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private attribute

    @property
    def balance(self):
        # Read-only getter for balance
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        # Improved withdraw with validation
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.__balance:
            print(f"Insufficient funds. Current balance: {self.__balance}")
            return
        self.__balance -= amount
        print(f"Withdrew {amount}. New balance: {self.__balance}")

# Create an object and test the encapsulated account
account = Account("Ribka", 1000)
print(f"Account owner: {account.owner}, Balance: {account.balance}")

account.deposit(500)
account.withdraw(300)
account.withdraw(5000)   # should fail, insufficient funds
account.deposit(-100)    # should fail, invalid amount

# Try accessing the private attribute directly (this would raise an error)
# print(account.__balance)  # AttributeError if uncommented
