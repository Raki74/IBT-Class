# Exercise 1: Simple Inheritance

class Vehicle:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def info(self):
        # Prints basic vehicle information
        print(f"{self.year} {self.name} {self.model}")


class Car(Vehicle):
    def __init__(self, name, model, year, num_doors):
        super().__init__(name, model, year)
        self.num_doors = num_doors  # unique attribute

    def honk(self):
        # Unique method for cars
        print(f"{self.name} {self.model} goes Beep Beep!")


class Motorcycle(Vehicle):
    def __init__(self, name, model, year, has_sidecar):
        super().__init__(name, model, year)
        self.has_sidecar = has_sidecar  # unique attribute

    def wheelie(self):
        # Unique method for motorcycles
        print(f"{self.name} {self.model} pops a wheelie!")


# Create objects and test
car = Car("Toyota", "Corolla", 2023, 4)
motorcycle = Motorcycle("Honda", "CBR", 2022, False)

car.info()
print(f"Number of doors: {car.num_doors}")
car.honk()

print()

motorcycle.info()
print(f"Has sidecar: {motorcycle.has_sidecar}")
motorcycle.wheelie()