# Exercise 3: CurrentAccount Inheritance

class Account:
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


class CurrentAccount(Account):
    def __init__(self, owner, balance=0, overdraft_limit=500):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        # Overridden to allow withdrawing into overdraft, up to the limit
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance + self.overdraft_limit:
            print(f"Withdrawal exceeds overdraft limit. Max available: {self.balance + self.overdraft_limit}")
            return
        # Access the parent's private balance through its deposit/withdraw logic
        # Since balance is private in Account, we simulate overdraft by allowing negative via direct manipulation
        new_balance = self.balance - amount
        # Use the parent's internal mechanism via deposit of a negative isn't allowed, so we bypass with a workaround
        self._Account__balance = new_balance
        print(f"Withdrew {amount}. New balance: {self._Account__balance}")


# Create a CurrentAccount object and test
current = CurrentAccount("Dawit", 500, 300)
print(f"Owner: {current.owner}, Balance: {current.balance}, Overdraft limit: {current.overdraft_limit}")

current.withdraw(700)   # goes into overdraft, should succeed
current.withdraw(200)   # exceeds overdraft limit, should fail