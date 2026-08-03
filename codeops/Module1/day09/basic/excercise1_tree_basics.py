# Exercise 1: Tree Basics

class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


def print_tree(node, depth=0):
    # O(n) - visits every node once (n = total number of nodes)
    print("  " * depth + node.name)
    for child in node.children:
        print_tree(child, depth + 1)


# Build the bank hierarchy
head_office = TreeNode("Head Office")

bole_branch = TreeNode("Bole Branch")
teller = TreeNode("Teller")
loan_officer = TreeNode("Loan Officer")
bole_branch.add_child(teller)
bole_branch.add_child(loan_officer)

piassa_branch = TreeNode("Piassa Branch")

head_office.add_child(bole_branch)
head_office.add_child(piassa_branch)

print_tree(head_office)