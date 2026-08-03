# Exercise 4: Hashmaps (Dictionaries)

student_grades = {
    "Ribka": "A",
    "Dawit": "B",
    "Sara": "A",
    "Kebede": "C",
    "Almaz": "B"
}

# Add a new student - O(1) average
student_grades["Yonas"] = "A"
print(f"After adding Yonas: {student_grades}")

# Update a grade - O(1) average
student_grades["Dawit"] = "A"
print(f"After updating Dawit's grade: {student_grades}")

# Check if a student exists - O(1) average, much faster than list search
print(f"Is Sara in grades? {'Sara' in student_grades}")
print(f"Is Betty in grades? {'Betty' in student_grades}")