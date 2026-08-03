# Exercise 8: Queue (FIFO)

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)     # O(1)

    def dequeue(self):
        return self.items.pop(0)    # O(n) - list, not ideal for real use

    def is_empty(self):
        return len(self.items) == 0


bank_queue = Queue()
bank_queue.enqueue("Ribka")
bank_queue.enqueue("Dawit")
bank_queue.enqueue("Sara")

print("Serving customers in order:")
while not bank_queue.is_empty():
    print(f"Now serving: {bank_queue.dequeue()}")