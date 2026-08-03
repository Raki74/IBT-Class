# Intermediate Exercise 4: Interface Segregation Principle (ISP)
#
# THE IDEA: Don't force a class to implement methods it doesn't need.
# CurrentAccount doesn't earn interest, so it shouldn't be forced to
# have interest-related methods just because it's an "Account."
# Instead, we create a SMALL, focused interface that ONLY accounts
# that actually need it will implement.

class Account:
    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance


class InterestBearing:
    # A small, focused "interface" - only classes that actually
    # earn interest need to implement this
    def calculate_interest(self):
        raise NotImplementedError("Subclasses must implement calculate_interest()")

    def apply_interest(self):
        interest = self.calculate_interest()
        self.balance += interest
        print(f"Interest of {interest:.2f} applied. New balance: {self.balance}")


class SavingsAccount(Account, InterestBearing):
    # SavingsAccount implements InterestBearing because it DOES earn interest
    # Note: because this uses multiple inheritance, we call Account's
    # init directly (with self passed explicitly) instead of using
    # super(), to avoid Python's multiple-inheritance super() chain issue.
    def __init__(self, account_number, owner, balance, interest_rate=0.05):
        Account.__init__(self, account_number, owner, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate


class CurrentAccount(Account):
    # CurrentAccount does NOT implement InterestBearing -
    # it's not forced to have calculate_interest() or apply_interest()
    # methods it would never use. This is single inheritance, so
    # super() works fine here.
    def __init__(self, account_number, owner, balance, overdraft_limit=500):
        super().__init__(account_number, owner, balance)
        self.overdraft_limit = overdraft_limit


# Test
savings = SavingsAccount(1000, "Ribka", 1000, 0.05)
current = CurrentAccount(1001, "Dawit", 500, 300)

savings.apply_interest()

# CurrentAccount has no interest methods at all - this would fail if uncommented:
# current.apply_interest()  # AttributeError: no such method

print(f"\nCurrentAccount has no interest methods, as expected.")
print(f"Does CurrentAccount have 'calculate_interest'? {hasattr(current, 'calculate_interest')}")
print(f"Does SavingsAccount have 'calculate_interest'? {hasattr(savings, 'calculate_interest')}")