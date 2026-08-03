# Exercise 4: Heap Basics

import heapq

# heapq is a MIN-heap by default. Since we want the HIGHEST priority
# (largest amount) popped first, we store amounts as NEGATIVE numbers,
# so the "smallest" negative number corresponds to the largest real amount.

priority_queue = []

heapq.heappush(priority_queue, (-5000, "Big Loan"))
heapq.heappush(priority_queue, (-200, "Small Deposit"))
heapq.heappush(priority_queue, (-10000, "Fraud Alert"))

# Pop the highest priority item - O(log n)
priority, description = heapq.heappop(priority_queue)
print(f"Highest priority item: {description} (amount: {-priority})")