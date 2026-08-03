# Exercise 1: Recursion Basics

def factorial_recursive(n):
    # Base case: factorial of 0 or 1 is 1
    if n <= 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    return n * factorial_recursive(n - 1)


def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


print(f"Recursive factorial(5): {factorial_recursive(5)}")
print(f"Iterative factorial(5): {factorial_iterative(5)}")