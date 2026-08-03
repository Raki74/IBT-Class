# Exercise 6: Recursive Problems

def reverse_string(s):
    # Base case: empty or single character is already "reversed"
    if len(s) <= 1:
        return s
    # Recursive case: reverse everything after the first char, then append first char at the end
    return reverse_string(s[1:]) + s[0]


def count_occurrences(arr, target):
    # Base case: empty list has 0 occurrences
    if len(arr) == 0:
        return 0
    # Recursive case: check first element, then recurse on the rest
    count = 1 if arr[0] == target else 0
    return count + count_occurrences(arr[1:], target)


print(f"Reverse of 'Addis Ababa': {reverse_string('Addis Ababa')}")

numbers = [3, 7, 3, 1, 3, 9, 3]
print(f"Occurrences of 3 in {numbers}: {count_occurrences(numbers, 3)}")