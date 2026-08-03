# Exercise 4: Binary Search
#
# WHY IT NEEDS A SORTED ARRAY:
# Binary search works by repeatedly checking the middle element and
# deciding whether to search the left half or right half, based on
# whether the target is smaller or larger. This "eliminate half the
# remaining elements each time" logic ONLY works if the array is
# sorted - otherwise, we have no guarantee the target isn't hiding
# in the half we just threw away.

def binary_search(arr, target):
    # O(log n) - cuts the search space in half each time
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


sorted_numbers = [1, 3, 5, 7, 9, 11, 13, 15]
print(f"Index of 9: {binary_search(sorted_numbers, 9)}")
print(f"Index of 100: {binary_search(sorted_numbers, 100)}")