# Exercise 1: Variables & Data Types
# Storing basic info about a person using different data types

full_name = "Ribka Dawit"        # string
age = 26                          # integer
height = 1.50                     # float (in meters)
is_student = True                 # boolean
favorite_food = "Injera"          # string

# Print everything using an f-string in a nice readable sentence
print(f"Hi, my name is {full_name}. I am {age} years old and {height}m tall. "
      f"Am I a student? {is_student}. My favorite food is {favorite_food}.")

# Exercise 2: Arithmetic Operations
# Take two numbers from the user and perform basic arithmetic

num1 = float(input("\nEnter the first number: "))
num2 = float(input("Enter the second number: "))

print(f"\nSum: {num1} + {num2} = {num1 + num2}")
print(f"Difference: {num1} - {num2} = {num1 - num2}")
print(f"Product: {num1} * {num2} = {num1 * num2}")
print(f"Division: {num1} / {num2} = {num1 / num2}")
print(f"Floor Division: {num1} // {num2} = {num1 // num2}")
print(f"Remainder: {num1} % {num2} = {num1 % num2}")

# Exercise 3: Type Conversion
# Ask for birth year and calculate age

current_year = 2026
birth_year = int(input("\nEnter your birth year: "))
calculated_age = current_year - birth_year
print(f"You are {calculated_age} years old.")

# Exercise 4: Simple Decision (if/else)
# Ask for a score and print Pass or Fail

score = float(input("\nEnter your score (0-100): "))
if score >= 50:
    print("Pass")
else:
    print("Fail")
    