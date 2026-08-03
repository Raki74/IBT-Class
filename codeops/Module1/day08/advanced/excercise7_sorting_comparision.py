# Exercise 7: Sorting Comparison

def selection_sort(arr):
    arr = arr.copy()
    comparisons = 0
    swaps = 0
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1
    return arr, comparisons, swaps


def insertion_sort(arr):
    arr = arr.copy()
    comparisons = 0
    swaps = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                swaps += 1
                j -= 1
            else:
                break
        arr[j + 1] = key
    return arr, comparisons, swaps


test_list = [5, 2, 9, 1, 7, 3, 8, 4]

sorted1, comp1, swap1 = selection_sort(test_list)
print(f"Selection Sort: {sorted1}")
print(f"Comparisons: {comp1}, Swaps: {swap1}\n")

sorted2, comp2, swap2 = insertion_sort(test_list)
print(f"Insertion Sort: {sorted2}")
print(f"Comparisons: {comp2}, Swaps: {swap2}")