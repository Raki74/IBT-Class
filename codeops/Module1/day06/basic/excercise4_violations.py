# Exercise 4: Identify SOLID Violations
#
# Given code:
#
# class Account:
#     def init(self):
#         self.notifier = EmailNotifier()
#         ...
#     def withdraw(self, amount):
#         ...
#         self.notifier.send_email(...)
#         self.save_to_db(...)

# ANALYSIS:

# 1. Single Responsibility Principle (SRP) - VIOLATED
#    The Account class is doing THREE separate jobs:
#    - Managing account balance/withdrawal logic
#    - Sending email notifications
#    - Saving data to the database
#    Each of these is a separate reason for the class to change,
#    which breaks SRP. If the notification method changes (e.g. SMS
#    instead of email), or the database changes, this class has to
#    change too - even though its "core job" is just account logic.

# 2. Dependency Inversion Principle (DIP) - VIOLATED
#    Account creates its own EmailNotifier directly inside init:
#        self.notifier = EmailNotifier()
#    This means Account is tightly coupled to one specific notifier
#    class. If we wanted to switch to SMS or push notifications,
#    we'd have to edit the Account class itself.
#    DIP says: high-level modules (like Account) should depend on
#    abstractions (like a generic "Notifier" interface), not on
#    concrete implementations (like EmailNotifier directly).
#    The fix is dependency injection - passing the notifier IN from
#    outside, rather than Account creating it itself.

# 3. Open/Closed Principle (OCP) - Partially violated
#    Because the notifier is hardcoded, extending this class to
#    support a new notification type means MODIFYING the Account
#    class rather than just adding a new notifier class - which
#    goes against "open for extension, closed for modification."

# SUMMARY: This code violates SRP, DIP, and (partially) OCP.
# The Intermediate exercises fix exactly this problem using
# dependency injection - see exercise1_srp_dip.py.

print("See comments above for the SOLID violation analysis.")
print("This code sample violates: SRP, DIP, and partially OCP.")