# Intermediate Exercise 3: Observer Pattern
#
# THE IDEA: The Account doesn't need to know WHAT should happen when
# a big withdrawal occurs - it just needs to "announce" the event,
# and any interested "observers" (SMSAlert, AuditLog, etc.) react to it.
# This keeps Account decoupled from the specific reactions.

class Observer:
    # Base "interface" - any observer must implement update()
    def update(self, message):
        raise NotImplementedError("Subclasses must implement update()")


class SMSAlert(Observer):
    def update(self, message):
        print(f"[SMS ALERT] {message}")


class AuditLog(Observer):
    def update(self, message):
        print(f"[AUDIT LOG] {message}")


class Account:
    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self._observers = []  # list of observers watching this account

    def add_observer(self, observer):
        # Registers a new observer to be notified of events
        self._observers.append(observer)

    def _notify_all(self, message):
        # Announces an event to every registered observer
        for observer in self._observers:
            observer.update(message)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")

        # If the withdrawal is large, notify all observers
        if amount > 3000:
            self._notify_all(
                f"Large withdrawal alert: {self.owner} withdrew {amount} from account #{self.account_number}."
            )


# Test the observer pattern
account = Account(1000, "Ribka", 10000)
account.add_observer(SMSAlert())
account.add_observer(AuditLog())

account.withdraw(500)     # small withdrawal - no notification
print()
account.withdraw(5000)    # large withdrawal - triggers both observers