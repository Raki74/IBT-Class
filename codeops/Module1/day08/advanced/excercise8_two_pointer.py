# Exercise 8: Two Pointer Technique

def find_pair_with_sum(sorted_arr, target):
    # O(n) - much faster than checking every pair (which would be O(n^2))
    left = 0
    right = len(sorted_arr) - 1

    while left < right:
        current_sum = sorted_arr[left] + sorted_arr[right]
        if current_sum == target:
            return (sorted_arr[left], sorted_arr[right])
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None


numbers = [1, 2, 4, 6, 8, 9, 14, 15]
target = 15
result = find_pair_with_sum(numbers, target)
print(f"Pair that sums to {target}: {result}")