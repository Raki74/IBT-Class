# Exercise 3: Linear Search

def linear_search(arr, target):
    # O(n) - checks each element one at a time
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


numbers = [5, 2, 9, 1, 7, 3]
print(f"Index of 9: {linear_search(numbers, 9)}")
print(f"Index of 100: {linear_search(numbers, 100)}")