# Exercise 9: Performance Comparison

import time
from collections import deque

# List search vs dictionary search
size = 100000
my_list = list(range(size))
my_dict = {i: True for i in range(size)}
target = size - 1

start = time.time()
found = target in my_list
list_time = time.time() - start

start = time.time()
found = target in my_dict
dict_time = time.time() - start

print(f"List search time: {list_time:.6f}s")
print(f"Dict search time: {dict_time:.6f}s")
print(f"Dictionary is much faster because it's O(1) vs list's O(n)\n")

# Insert at beginning: list vs deque
n = 10000

start = time.time()
my_list2 = []
for i in range(n):
    my_list2.insert(0, i)
list_insert_time = time.time() - start

start = time.time()
my_deque = deque()
for i in range(n):
    my_deque.appendleft(i)
deque_insert_time = time.time() - start

print(f"List insert-at-start time: {list_insert_time:.6f}s")
print(f"Deque appendleft time: {deque_insert_time:.6f}s")
print(f"Deque is much faster for this because it's optimized for O(1) operations at both ends")