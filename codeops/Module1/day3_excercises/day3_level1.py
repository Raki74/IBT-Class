# Exercise 1: Lists & Tuples

# Create a list of 6 favorite foods
favorite_foods = ["Injera", "Pizza", "Pasta", "Doro Wat", "Sushi", "Tacos"]

# Print the first and last item
print(f"First food: {favorite_foods[0]}")
print(f"Last food: {favorite_foods[-1]}")

# Add a new food using .append()
favorite_foods.append("Kitfo")
print(f"After adding Kitfo: {favorite_foods}")

# Remove the second food using .pop()
removed_food = favorite_foods.pop(1)
print(f"Removed: {removed_food}")
print(f"After removing: {favorite_foods}")

# Create a tuple of coordinates for Ethiopia and unpack it
ethiopia_coordinates = (9.1450, 40.4897)  # (latitude, longitude)
latitude, longitude = ethiopia_coordinates
print(f"\nEthiopia's coordinates -> Latitude: {latitude}, Longitude: {longitude}")




# Exercise 2: Dictionaries

# Create a student dictionary
student = {
    "name": "Ribka Dawit",
    "age": 26,
    "grade": "A",
    "city": "Addis Ababa",
    "department": "Computer Science"
}

# Print name, department, and grade
print(f"\nStudent Name: {student['name']}")
print(f"Department: {student['department']}")
print(f"Grade: {student['grade']}")

# Add a new key: phone
student["phone"] = "0987654321"
print(f"After adding phone: {student}")

# Update the grade
student["grade"] = "A+"
print(f"After updating grade: {student}")


# Exercise 3: Sets

# Create a list with duplicate names
names_list = ["Ribka", "Almaz", "Ribka", "Dawit", "Almaz", "Sara"]
print(f"\nOriginal list with duplicates: {names_list}")

# Convert it to a set to remove duplicates
names_set = set(names_list)
print(f"Set with duplicates removed: {names_set}")

# Add a new name to the set
names_set.add("Kebede")
print(f"After adding a new name: {names_set}")

