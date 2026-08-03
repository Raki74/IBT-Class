# Exercise 2: Recursion with Lists

def sum_list(numbers):
    # Base case: empty list sums to 0
    if len(numbers) == 0:
        return 0
    # Recursive case: first element + sum of the rest
    return numbers[0] + sum_list(numbers[1:])


test_numbers = [4, 8, 15, 16, 23, 42]
print(f"Sum of {test_numbers}: {sum_list(test_numbers)}")