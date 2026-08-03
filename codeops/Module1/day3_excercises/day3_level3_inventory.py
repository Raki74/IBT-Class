# Exercise 10: Inventory Manager
# A menu-driven program to manage product inventory

inventory = {}

def add_product():
    name = input("Enter product name: ")
    try:
        quantity = int(input("Enter quantity: "))
        inventory[name] = quantity
        print(f"Added '{name}' with quantity {quantity}.")
    except ValueError:
        print("Invalid quantity. Please enter a number.")

def update_quantity():
    name = input("Enter product name to update: ")
    if name in inventory:
        try:
            quantity = int(input("Enter new quantity: "))
            inventory[name] = quantity
            print(f"Updated '{name}' to quantity {quantity}.")
        except ValueError:
            print("Invalid quantity. Please enter a number.")
    else:
        print(f"Product '{name}' not found in inventory.")

def view_products():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("\n--- Current Inventory ---")
        for name, quantity in inventory.items():
            print(f"{name}: {quantity}")

def save_to_file():
    with open("inventory.txt", "w") as file:
        for name, quantity in inventory.items():
            file.write(f"{name},{quantity}\n")
    print("Inventory saved to inventory.txt")

def load_from_file():
    global inventory
    try:
        with open("inventory.txt", "r") as file:
            lines = file.readlines()
        inventory = {}
        for line in lines:
            name, quantity = line.strip().split(",")
            inventory[name] = int(quantity)
        print("Inventory loaded from inventory.txt")
    except FileNotFoundError:
        print("Error: inventory.txt not found.")

# Main menu loop
while True:
    print("\n--- Inventory Manager ---")
    print("1. Add new product")
    print("2. Update quantity")
    print("3. View all products")
    print("4. Save to file")
    print("5. Load from file")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        add_product()
    elif choice == "2":
        update_quantity()
    elif choice == "3":
        view_products()
    elif choice == "4":
        save_to_file()
    elif choice == "5":
        load_from_file()
    elif choice == "6":
        print("Exiting Inventory Manager. Goodbye!")
        break
    else:
        print("Invalid option. Please choose between 1 and 6.")

        