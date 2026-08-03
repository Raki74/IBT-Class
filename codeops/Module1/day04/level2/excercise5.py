# Exercise 5: Product Class

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def sell(self, quantity):
        # Reduces stock by quantity, prevents going negative
        if quantity > self.stock:
            print(f"Cannot sell {quantity} units. Only {self.stock} in stock.")
        else:
            self.stock -= quantity
            print(f"Sold {quantity} units of {self.name}. Remaining stock: {self.stock}")

    def restock(self, quantity):
        # Increases stock by quantity
        self.stock += quantity
        print(f"Restocked {quantity} units of {self.name}. New stock: {self.stock}")

# Create a product object and test sell and restock
product = Product("Laptop", 25000, 10)
print(f"Product: {product.name}, Price: {product.price}, Stock: {product.stock}")

product.sell(3)
product.sell(20)  # should fail, not enough stock
product.restock(5)

