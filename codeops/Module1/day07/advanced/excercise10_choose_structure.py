# Exercise 10: Choose the Right Structure

# 1. Checking if a username is already taken
#    -> Use a SET or DICTIONARY (hash-based)
#    Justification: O(1) average lookup time, much faster than
#    scanning a list (O(n)) especially as the user base grows.

# 2. Processing tasks in the order they arrive (customer support)
#    -> Use a QUEUE
#    Justification: FIFO (First In, First Out) matches the requirement
#    exactly - tasks are handled in arrival order. enqueue/dequeue
#    are O(1) with a proper deque-based queue.

# 3. Implementing "Undo" feature in a text editor
#    -> Use a STACK
#    Justification: LIFO (Last In, First Out) matches "undo" perfectly -
#    the most recent action is the first one to be undone.
#    push/pop are O(1).

# 4. Storing student IDs for fast lookup
#    -> Use a SET or DICTIONARY
#    Justification: O(1) average lookup by ID, versus O(n) for
#    searching through a list.

print("See comments above for structure recommendations and justifications.")