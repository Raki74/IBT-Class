# Exercise 7: Stack (LIFO)

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)  # O(1)

    def pop(self):
        return self.items.pop()  # O(1)

    def peek(self):
        return self.items[-1]    # O(1)

    def is_empty(self):
        return len(self.items) == 0


def reverse_string(text):
    stack = Stack()
    for char in text:
        stack.push(char)
    reversed_text = ""
    while not stack.is_empty():
        reversed_text += stack.pop()
    return reversed_text


result = reverse_string("Addis Ababa")
print(f"Reversed: {result}")