# Intermediate Exercise 1: Apply SRP + DIP
#
# We're fixing the Account class from Basic Exercise 4.
# Account should ONLY handle account logic (balance, deposit, withdraw).
# Notification and persistence become separate classes.
# We inject them into Account from OUTSIDE (dependency injection),
# so Account doesn't need to know WHICH notifier or database it's using.


class Notifier:
    # Base "interface" - any notifier must implement notify()
    def notify(self, message):
        raise NotImplementedError("Subclasses must implement notify()")


class EmailNotifier(Notifier):
    def notify(self, message):
        print(f"[EMAIL] {message}")


class SMSNotifier(Notifier):
    def notify(self, message):
        print(f"[SMS] {message}")


class AccountRepository:
    # Handles ONLY persistence (saving/loading data)
    def save(self, account):
        print(f"[DB] Saved account #{account.account_number}, balance: {account.balance}")


class Account:
    # Handles ONLY account logic - balance, deposit, withdraw
    # Notice: notifier and repository are passed IN (dependency injection),
    # not created inside this class. This means Account doesn't care
    # whether it's Email or SMS, or which database is used - it just
    # calls the methods on whatever it was given.
    def __init__(self, account_number, owner, balance, notifier, repository):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.notifier = notifier          # injected dependency
        self.repository = repository      # injected dependency

    def deposit(self, amount):
        self.balance += amount
        self.repository.save(self)
        self.notifier.notify(f"{self.owner} deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        self.repository.save(self)
        self.notifier.notify(f"{self.owner} withdrew {amount}. New balance: {self.balance}")


# Test - we can plug in ANY notifier without changing Account at all
email_notifier = EmailNotifier()
repository = AccountRepository()

account1 = Account(1000, "Ribka", 500, email_notifier, repository)
account1.deposit(200)
account1.withdraw(100)

print()

# Now let's use a DIFFERENT notifier - no changes needed to Account class
sms_notifier = SMSNotifier()
account2 = Account(1001, "Dawit", 1000, sms_notifier, repository)
account2.withdraw(300)