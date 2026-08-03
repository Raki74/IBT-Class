# Exercise 5: Grade Classifier
# Ask for a score and classify it using if/elif/else

score = float(input("Enter your score: "))

if score >= 90:
    print("Excellent")
elif score >= 80:
    print("Very Good")
elif score >= 70:
    print("Good")
elif score >= 50:
    print("Pass")
else:
    print("Fail")


    # Exercise 6: Number Patterns
# Print numbers 1-20, then only odd numbers, then only multiples of 5

print("\nNumbers 1 to 20:")
for i in range(1, 21):
    print(i, end=" ")

print("\n\nOdd numbers 1 to 20:")
for i in range(1, 21):
    if i % 2 != 0:
        print(i, end=" ")

print("\n\nNumbers divisible by 5 (1 to 20):")
for i in range(1, 21):
    if i % 5 == 0:
        print(i, end=" ")


        # Exercise 7: While Loop Practice
# Keep adding positive numbers until user enters 0

print("\nEnter positive numbers to add (enter 0 to stop):")
total = 0
while True:
    num = float(input("Enter a number: "))
    if num == 0:
        break
    total += num

print(f"Total sum: {total}")


# Exercise 8: Function Practice

def greet(name):
    # Prints a welcome message
    print(f"\nWelcome, {name}!")

def square(number):
    # Returns the square of a number
    return number * number

def is_even(number):
    # Returns True if number is even, False otherwise
    return number % 2 == 0

# Test the functions
greet("Ribka")
print(f"Square of 7: {square(7)}")
print(f"Is 10 even? {is_even(10)}")
print(f"Is 7 even? {is_even(7)}")

