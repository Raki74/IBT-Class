# Exercise 4: Student Class

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        # Adds a grade to the student's grade list
        self.grades.append(grade)

    def average_grade(self):
        # Returns the average of all grades
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

# Create a student object, add several grades, and print the average
student = Student("Ribka", "STU001")
student.add_grade(85)
student.add_grade(90)
student.add_grade(78)
student.add_grade(92)

print(f"Student: {student.name} (ID: {student.student_id})")
print(f"Grades: {student.grades}")
print(f"Average grade: {student.average_grade():.2f}")

