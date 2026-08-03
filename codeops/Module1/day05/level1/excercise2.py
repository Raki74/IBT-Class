# Exercise 2: SavingsAccount Inheritance
# Using a base Account class (like from Day 4), then extending it

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


class SavingsAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        # Adds interest to the balance based on interest_rate
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"Interest of {interest:.2f} added.")


# Create a SavingsAccount object and test
savings = SavingsAccount("Ribka", 1000, 0.05)
print(f"Owner: {savings.owner}, Balance: {savings.balance}, Rate: {savings.interest_rate}")

savings.add_interest()
savings.deposit(200)