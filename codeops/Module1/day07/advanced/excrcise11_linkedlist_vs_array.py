# Exercise 11: Linked List vs Array - removing the middle element

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove_middle(self):
        # O(n) - must traverse to find the middle (slow/fast pointer technique)
        if self.head is None or self.head.next is None:
            return
        slow = self.head
        fast = self.head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if prev:
            prev.next = slow.next

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result


def remove_middle_from_list(arr):
    # O(n) - Python must shift all elements after the removed index
    middle_index = len(arr) // 2
    arr.pop(middle_index)
    return arr


# Test array removal
array = [1, 2, 3, 4, 5]
print(f"Array before: {array}")
print(f"Array after removing middle: {remove_middle_from_list(array)}")

# Test linked list removal
ll = LinkedList()
for val in [1, 2, 3, 4, 5]:
    ll.append(val)
print(f"\nLinked list before: {ll.to_list()}")
ll.remove_middle()
print(f"Linked list after removing middle: {ll.to_list()}")

# DISCUSSION:
# - Array: removing the middle element is O(n) because all elements
#   after that index must shift left by one to fill the gap.
# - Linked List: removing the middle element ALSO takes O(n) just to
#   FIND the middle (no direct indexing), but once found, the actual
#   removal is O(1) - just re-pointing one link.
# - Trade-off: arrays have fast random access (O(1)) but slow insertion/
#   deletion in the middle (O(n)). Linked lists have slow access (O(n))
#   but the deletion itself, once located, is faster (O(1)).