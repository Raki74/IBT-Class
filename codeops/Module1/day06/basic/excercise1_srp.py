# Exercise 1: Single Responsibility Principle (SRP)
#
# THE PROBLEM: A class should have only ONE reason to change.
# The "bad" version below mixes three unrelated responsibilities:
# calculating salary, saving data, and sending emails.
# If email logic changes, or the file format changes, this ONE class
# has to change for THREE different reasons - that's a violation of SRP.

# --- BAD VERSION (commented out, for reference only) ---
# class Employee:
#     def init(self, name, base_salary):
#         self.name = name
#         self.base_salary = base_salary
#
#     def calculate_salary(self):
#         return self.base_salary * 1.1
#
#     def save_to_file(self):
#         with open("employees.txt", "a") as f:
#             f.write(f"{self.name}: {self.calculate_salary()}\n")
#
#     def send_email(self):
#         print(f"Sending email to {self.name} about their salary.")


# --- REFACTORED VERSION: each class has ONE job ---

class Employee:
    # Responsible ONLY for holding employee data and calculating salary
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary * 1.1


class EmployeeFileSaver:
    # Responsible ONLY for saving employee data to a file
    def save(self, employee):
        with open("employees.txt", "a") as f:
            f.write(f"{employee.name}: {employee.calculate_salary()}\n")
        print(f"Saved {employee.name}'s record to file.")


class EmployeeEmailer:
    # Responsible ONLY for sending emails
    def send_salary_email(self, employee):
        print(f"Sending email to {employee.name} about their salary of {employee.calculate_salary()}.")


# Test the refactored design
employee = Employee("Ribka", 5000)
saver = EmployeeFileSaver()
emailer = EmployeeEmailer()

print(f"{employee.name}'s salary: {employee.calculate_salary()}")
saver.save(employee)
emailer.send_salary_email(employee)