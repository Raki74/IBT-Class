# Exercise 5: Bubble Sort

def bubble_sort(arr):
    n = len(arr)
    for pass_num in range(n - 1):
        swapped = False
        for i in range(n - 1 - pass_num):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        print(f"After pass {pass_num + 1}: {arr}")
        if not swapped:
            break  # already sorted, no need to continue
    return arr


numbers = [5, 2, 9, 1, 7, 3]
print(f"Original: {numbers}")
bubble_sort(numbers)
print(f"Sorted: {numbers}")