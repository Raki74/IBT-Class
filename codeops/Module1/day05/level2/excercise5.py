# Exercise 5: Polymorphism Practice

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

    def statement(self):
        print(f"\n--- Statement for {self.owner} ---")
        print(f"Balance: {self.balance}")


class SavingsAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def statement(self):
        print(f"\n--- Savings Statement for {self.owner} ---")
        print(f"Balance: {self.balance}")
        print(f"Interest Rate: {self.interest_rate * 100}%")


class CurrentAccount(Account):
    def __init__(self, owner, balance=0, overdraft_limit=500):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def statement(self):
        print(f"\n--- Current Account Statement for {self.owner} ---")
        print(f"Balance: {self.balance}")
        print(f"Overdraft Limit: {self.overdraft_limit}")


# Create a list of different account types and demonstrate polymorphism
accounts = [
    Account("Sara", 800),
    SavingsAccount("Ribka", 1000, 0.05),
    CurrentAccount("Dawit", 500, 300)
]

# Loop through and call statement() and deposit() on each
# Even though each object is a different type, the same method calls work correctly
for account in accounts:
    account.statement()
    account.deposit(100)