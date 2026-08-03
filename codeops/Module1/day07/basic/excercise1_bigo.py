# Exercise 1: Big-O Notation
#
# What is the time complexity of the following operations?

# 1. Accessing an element in a Python list by index -> O(1)
#    Lists in Python are stored as contiguous arrays in memory,
#    so Python can jump straight to the memory address of index i
#    using simple math, regardless of list size.

# 2. Searching for an element in a list using 'in' -> O(n)
#    Python has to check each element one by one (in the worst case)
#    until it finds a match or reaches the end.

# 3. Inserting at the beginning of a list -> O(n)
#    Since lists are stored contiguously, inserting at index 0 means
#    every other element must shift over by one position - that's
#    proportional to the list's length.

# 4. Dictionary lookup by key -> O(1) on average
#    Dictionaries use a hash table internally. The key is hashed to
#    find its "slot" directly, so lookup doesn't depend on how many
#    items are in the dictionary (on average - worst case can be O(n)
#    if there are many hash collisions, but that's rare in practice).

print("Answers documented in comments above.")
print("1. List index access: O(1)")
print("2. List search with 'in': O(n)")
print("3. Insert at beginning of list: O(n)")
print("4. Dictionary lookup by key: O(1) average")