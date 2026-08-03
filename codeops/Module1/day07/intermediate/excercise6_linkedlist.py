# Exercise 6: Linked List Basics

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        # O(n) - must traverse to the end since we don't track a tail
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        # O(n) - visits every node once
        current = self.head
        values = []
        while current:
            values.append(str(current.value))
            current = current.next
        print(" -> ".join(values))


ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.print_list()