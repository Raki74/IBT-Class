# main.py
# Imports and uses the add_tax function from utils.py

from utils import add_tax

price = float(input("Enter a price: "))
price_with_tax = add_tax(price)
print(f"Price including tax: {price_with_tax:.2f}")

# Test with a custom tax rate too
price_custom_tax = add_tax(price, rate=0.10)
print(f"Price with 10% tax: {price_custom_tax:.2f}")

