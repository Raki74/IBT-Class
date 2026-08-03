# Exercise 2: Compare Complexities
# Ranking from fastest to slowest for large n (n = 1,000,000)

# Fastest to slowest:
# O(1)      - constant time, doesn't grow with n
# O(log n)  - grows very slowly (e.g. binary search)
# O(n)      - grows linearly with n
# O(n^2)    - grows quadratically, becomes very slow for large n

print("Ranking (fastest to slowest): O(1) < O(log n) < O(n) < O(n^2)")
print(f"For n = 1,000,000:")
import math
n = 1_000_000
print(f"O(1)      = 1 operation")
print(f"O(log n)  = {math.log2(n):.1f} operations")
print(f"O(n)      = {n} operations")
print(f"O(n^2)    = {n**2:,} operations")
