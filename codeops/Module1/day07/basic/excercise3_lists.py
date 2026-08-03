# Exercise 3: Arrays / Lists

students = ["Ribka", "Dawit", "Sara", "Kebede", "Almaz",
            "Yonas", "Meron", "Abel", "Tigist", "Solomon"]

# Access by index - O(1)
print(f"Student at index 0: {students[0]}")
print(f"Student at index 5: {students[5]}")

# Add at the end - O(1) amortized
students.append("Betty")
print(f"After append: {students}")

# Insert at position 0 - O(n), since everything shifts
students.insert(0, "Abebe")
print(f"After insert at 0: {students}")