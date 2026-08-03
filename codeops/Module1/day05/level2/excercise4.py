# Exercise 4: Method Overriding
# Override statement() in CurrentAccount and SavingsAccount

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

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)

    def statement(self):
        # Overridden to show interest rate
        print(f"\n--- Savings Statement for {self.owner} ---")
        print(f"Balance: {self.balance}")
        print(f"Interest Rate: {self.interest_rate * 100}%")


class CurrentAccount(Account):
    def __init__(self, owner, balance=0, overdraft_limit=500):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance + self.overdraft_limit:
            print(f"Withdrawal exceeds overdraft limit. Max available: {self.balance + self.overdraft_limit}")
            return
        self._Account__balance = self.balance - amount
        print(f"Withdrew {amount}. New balance: {self._Account__balance}")

    def statement(self):
        # Overridden to show overdraft info
        print(f"\n--- Current Account Statement for {self.owner} ---")
        print(f"Balance: {self.balance}")
        print(f"Overdraft Limit: {self.overdraft_limit}")


# Test method overriding
savings = SavingsAccount("Ribka", 1000, 0.05)
current = CurrentAccount("Dawit", 500, 300)

savings.statement()
current.statement()