# Mini Project: Personal Finance Tracker
# A menu-driven program to track income, expenses, and balance

balance = 0.0

def add_income():
    global balance
    try:
        amount = float(input("Enter income amount: "))
        balance += amount
        print(f"Income added. New balance: {balance:.2f}")
    except ValueError:
        print("Invalid input. Please enter a number.")

def add_expense():
    global balance
    try:
        amount = float(input("Enter expense amount: "))
        balance -= amount
        print(f"Expense recorded. New balance: {balance:.2f}")
    except ValueError:
        print("Invalid input. Please enter a number.")

def show_balance():
    print(f"Current balance: {balance:.2f}")

# Main menu loop
while True:
    print("\n--- Personal Finance Tracker ---")
    print("1. Add income")
    print("2. Add expense")
    print("3. Show balance")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_income()
    elif choice == "2":
        add_expense()
    elif choice == "3":
        show_balance()
    elif choice == "4":
        print(f"\nFinal balance: {balance:.2f}")
        print("Thank you for using the Personal Finance Tracker. Goodbye!")
        break
    else:
        print("Invalid option. Please choose between 1 and 4.")