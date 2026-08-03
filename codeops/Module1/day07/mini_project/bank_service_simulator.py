# Mini Project: Bank Customer Service Simulator
# Uses a Stack for transaction history and a Dictionary for customer lookup

class BankServiceSimulator:
    def __init__(self):
        self.customers = {}          # account_number -> customer name, O(1) lookup
        self.transaction_history = []  # acts as a stack, O(1) push/pop

    def add_customer(self, account_number, name):
        self.customers[account_number] = name  # O(1) average
        print(f"Customer '{name}' added with account #{account_number}.")

    def make_transaction(self, account_number, description):
        # O(1) - dictionary lookup + list append (stack push)
        if account_number not in self.customers:
            print("Account not found.")
            return
        self.transaction_history.append((account_number, description))
        print(f"Transaction recorded: {description} (Account #{account_number})")

    def undo_last_transaction(self):
        # O(1) - stack pop
        if not self.transaction_history:
            print("No transactions to undo.")
            return
        account_number, description = self.transaction_history.pop()
        print(f"Undone: {description} (Account #{account_number})")

    def search_customer(self, account_number):
        # O(1) average - dictionary lookup
        name = self.customers.get(account_number)
        if name:
            print(f"Found: Account #{account_number} belongs to {name}.")
        else:
            print("Customer not found.")


# Menu-driven program
bank = BankServiceSimulator()

# Pre-load a couple of customers for testing
bank.add_customer(1000, "Ribka")
bank.add_customer(1001, "Dawit")

while True:
    print("\n--- Addis Bank Customer Service Simulator ---")
    print("1. Make a transaction")
    print("2. Undo last transaction")
    print("3. Search customer by account number")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        try:
            acc_num = int(input("Enter account number: "))
            desc = input("Enter transaction description: ")
            bank.make_transaction(acc_num, desc)
        except ValueError:
            print("Invalid account number.")
    elif choice == "2":
        bank.undo_last_transaction()
    elif choice == "3":
        try:
            acc_num = int(input("Enter account number: "))
            bank.search_customer(acc_num)
        except ValueError:
            print("Invalid account number.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please choose between 1 and 4.")