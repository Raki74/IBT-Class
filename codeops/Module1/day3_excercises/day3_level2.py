# Exercise 4: List Operations

numbers = [10, 25, 40, 15, 60, 30]

# Print only numbers greater than 30
print("Numbers greater than 30:")
for num in numbers:
    if num > 30:
        print(num, end=" ")

# Sort the list and print it
sorted_numbers = sorted(numbers)
print(f"\n\nSorted list: {sorted_numbers}")

# Find the sum and average
total = sum(numbers)
average = total / len(numbers)
print(f"Sum: {total}")
print(f"Average: {average:.2f}")




# Exercise 5: Dictionary Operations

products = {
    "Laptop": 25000,
    "Phone": 12000,
    "Headphones": 800,
    "Keyboard": 500,
    "Monitor": 7000
}

# Loop through and print each product with its price
print("\n--- Product Price List ---")
for product, price in products.items():
    print(f"{product}: {price} birr")

# Ask user for a product name and show its price
search_product = input("\nEnter a product name to check its price: ")
price = products.get(search_product, "Product not found.")
print(f"Price: {price}")


# Exercise 6: List Comprehension

# Numbers 1 to 20 using comprehension
numbers_1_to_20 = [n for n in range(1, 21)]
print(f"\nNumbers 1 to 20: {numbers_1_to_20}")

# Even numbers from 1 to 30 using comprehension
even_numbers = [n for n in range(1, 31) if n % 2 == 0]
print(f"Even numbers 1 to 30: {even_numbers}")

# Odd numbers from 1 to 10 using comprehension
odd_numbers = [n for n in range(1, 11) if n % 2 != 0]
print(f"Odd numbers 1 to 10: {odd_numbers}")