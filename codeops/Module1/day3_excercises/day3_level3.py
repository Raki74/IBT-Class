# Exercise 8: File Reading & Writing

# Write 5 student names and scores to a file
students = {
    "Ribka": 85,
    "Almaz": 92,
    "Dawit": 78,
    "Sara": 88,
    "Kebede": 95
}

with open("students.txt", "w") as file:
    for name, score in students.items():
        file.write(f"{name},{score}\n")

print("Student data written to students.txt")

# Read the file back and calculate the average score
try:
    with open("students.txt", "r") as file:
        lines = file.readlines()

    total_score = 0
    count = 0

    print("\n--- Students in file ---")
    for line in lines:
        name, score = line.strip().split(",")
        score = int(score)
        print(f"{name}: {score}")
        total_score += score
        count += 1

    average_score = total_score / count
    print(f"\nAverage score: {average_score:.2f}")

except FileNotFoundError:
    print("Error: students.txt file not found.")





    

    # Exercise 9: Error Handling

print("\n--- Division Calculator ---")

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
    print(f"Result: {result}")

except ValueError:
    print("Error: Please enter valid numbers only.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

finally:
    print("Calculation attempt completed.")