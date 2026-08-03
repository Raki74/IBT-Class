# Exercise 2: Rectangle Class

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        # Returns the area of the rectangle
        return self.length * self.width

    def perimeter(self):
        # Returns the perimeter of the rectangle
        return 2 * (self.length + self.width)

# Create 2 Rectangle objects and call area() & perimeter() on both
rect1 = Rectangle(5, 3)
rect2 = Rectangle(10, 7)

print(f"Rectangle 1 - Area: {rect1.area()}, Perimeter: {rect1.perimeter()}")
print(f"Rectangle 2 - Area: {rect2.area()}, Perimeter: {rect2.perimeter()}")
