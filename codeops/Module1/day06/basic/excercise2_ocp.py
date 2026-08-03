# Exercise 2: Open/Closed Principle (OCP)
#
# THE PROBLEM: A class/function should be OPEN for extension,
# but CLOSED for modification. Meaning: you should be able to add
# new behavior WITHOUT editing existing, already-tested code.
#
# The "bad" version below uses if-elif. Every time we add a new
# employee type, we have to go back and EDIT this function,
# risking breaking what already works.

# --- BAD VERSION (commented out, for reference) ---
# def calculate_bonus(employee_type):
#     if employee_type == "manager":
#         return 1000
#     elif employee_type == "developer":
#         return 800
#     elif employee_type == "intern":
#         return 200
#     # Adding a new type means editing this function again


# --- REFACTORED VERSION: uses classes and polymorphism instead ---

class Employee:
    def calculate_bonus(self):
        # Base class default - subclasses override this
        raise NotImplementedError("Subclasses must implement calculate_bonus()")


class Manager(Employee):
    def calculate_bonus(self):
        return 1000


class Developer(Employee):
    def calculate_bonus(self):
        return 800


class Intern(Employee):
    def calculate_bonus(self):
        return 200


# Adding a NEW employee type requires NO changes to existing classes -
# we just add a new class. This is what "open for extension" means.
class SeniorDeveloper(Employee):
    def calculate_bonus(self):
        return 1200


# Test - the calling code doesn't need to know which type it's dealing with
employees = [Manager(), Developer(), Intern(), SeniorDeveloper()]

for emp in employees:
    print(f"{emp.__class__.__name__} bonus: {emp.calculate_bonus()}")
    