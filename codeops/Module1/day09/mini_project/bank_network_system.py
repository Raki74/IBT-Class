# Mini Project: Addis Bank Network & Priority System
# Combines Trees, Graphs, and Heaps into one menu-driven program

import heapq


# --- TREE: branch hierarchy ---
class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)  # O(1)


def print_tree(node, depth=0):
    # O(n) - visits every node once
    print("  " * depth + node.name)
    for child in node.children:
        print_tree(child, depth + 1)


def find_node(node, name):
    # O(n) - may need to check every node in the worst case
    if node.name == name:
        return node
    for child in node.children:
        found = find_node(child, name)
        if found:
            return found
    return None


# --- BST: customer account search ---
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        # O(log n) average
        if self.root is None:
            self.root = BSTNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = BSTNode(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = BSTNode(value)
            else:
                self._insert(node.right, value)

    def search(self, value):
        # O(log n) average
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)


# --- GRAPH: customer transfer network ---
class Graph:
    def __init__(self):
        self.connections = {}

    def add_customer(self, name):
        if name not in self.connections:
            self.connections[name] = []

    def add_transfer(self, person1, person2):
        # O(1)
        self.add_customer(person1)
        self.add_customer(person2)
        self.connections[person1].append(person2)
        self.connections[person2].append(person1)

    def bfs(self, start):
        # O(V + E) - visits every vertex and edge once
        if start not in self.connections:
            return []
        visited = set()
        queue = [start]
        order = []
        while queue:
            current = queue.pop(0)
            if current not in visited:
                visited.add(current)
                order.append(current)
                for neighbor in self.connections[current]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return order


# --- Application state ---
branch_tree = TreeNode("Head Office")
customer_graph = Graph()
account_bst = BST()
urgent_transactions = []  # heap


def add_branch_or_employee():
    parent_name = input("Enter parent name (e.g. 'Head Office' or branch name): ")
    new_name = input("Enter new branch/employee name: ")
    parent = find_node(branch_tree, parent_name)
    if parent:
        parent.add_child(TreeNode(new_name))
        print(f"Added '{new_name}' under '{parent_name}'.")
    else:
        print("Parent not found.")


def add_transfer_connection():
    person1 = input("Enter first customer name: ")
    person2 = input("Enter second customer name: ")
    customer_graph.add_transfer(person1, person2)
    print(f"Connection added between {person1} and {person2}.")


def show_connected_customers():
    start = input("Enter customer name to start BFS from: ")
    result = customer_graph.bfs(start)
    if result:
        print(f"Connected customers (BFS order): {result}")
    else:
        print("Customer not found in the network.")
 
def add_urgent_transaction():
    try:
        amount = float(input("Enter transaction amount: "))
        description = input("Enter description: ")
        heapq.heappush(urgent_transactions, (-amount, description))
        print(f"Urgent transaction added: {description} ({amount})")
    except ValueError:
        print("Invalid amount.")


def process_highest_priority():
    if not urgent_transactions:
        print("No urgent transactions to process.")
        return
    priority, description = heapq.heappop(urgent_transactions)
    print(f"Processing highest priority: {description} (amount: {-priority})")


def search_account():
    try:
        account_number = int(input("Enter account number to search: "))
        found = account_bst.search(account_number)
        print(f"Account #{account_number} found: {found}")
    except ValueError:
        print("Invalid account number.")


def add_account():
    try:
        account_number = int(input("Enter new account number to add to BST: "))
        account_bst.insert(account_number)
        print(f"Account #{account_number} added to BST.")
    except ValueError:
        print("Invalid account number.")


# Pre-load some sample data
bole = TreeNode("Bole Branch")
bole.add_child(TreeNode("Teller"))
bole.add_child(TreeNode("Loan Officer"))
branch_tree.add_child(bole)
branch_tree.add_child(TreeNode("Piassa Branch"))

for acc in [50, 30, 70, 20, 40, 60]:
    account_bst.insert(acc)

customer_graph.add_transfer("Almaz", "Dawit")
customer_graph.add_transfer("Dawit", "Tigist")


# --- Main menu loop ---
while True:
    print("\n--- Addis Bank Network & Priority System ---")
    print("1. Add new branch/employee (Tree)")
    print("2. Add money transfer connection (Graph)")
    print("3. Show connected customers (BFS)")
    print("4. Add urgent transaction (Heap)")
    print("5. Process highest priority transaction")
    print("6. Search for account (BST)")
    print("7. Add account to BST")
    print("8. Show branch tree")
    print("9. Exit")

    choice = input("Choose an option (1-9): ")

    if choice == "1":
        add_branch_or_employee()
    elif choice == "2":
        add_transfer_connection()
    elif choice == "3":
        show_connected_customers()
    elif choice == "4":
        add_urgent_transaction()
    elif choice == "5":
        process_highest_priority()
    elif choice == "6":
        search_account()
    elif choice == "7":
        add_account()
    elif choice == "8":
        print_tree(branch_tree)
    elif choice == "9":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please choose between 1 and 9.")