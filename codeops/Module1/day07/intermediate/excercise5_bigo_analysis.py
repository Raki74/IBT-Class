# Exercise 5: Big-O Analysis

def find_max(numbers):
    # Single loop through the list once -> O(n)
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value


def nested_loop_example(numbers):
    # Two nested loops, each running n times -> O(n^2)
    pairs = []
    for i in numbers:
        for j in numbers:
            pairs.append((i, j))
    return pairs


test_list = [3, 7, 1, 9, 4]
print(f"Max value: {find_max(test_list)}  (O(n))")
print(f"Number of pairs from nested loop: {len(nested_loop_example(test_list))}  (O(n^2))")