# Exercise 9: Car Class with Encapsulation

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.__speed = 0      # private attribute
        self.__fuel = 100     # private attribute, starts full

    @property
    def speed(self):
        return self.__speed

    @property
    def fuel(self):
        return self.__fuel

    def accelerate(self, amount):
        # Increases speed if there's enough fuel
        if self.__fuel <= 0:
            print("Cannot accelerate. Out of fuel!")
            return
        self.__speed += amount
        self.__fuel -= amount * 0.5  # consumes fuel based on acceleration
        if self.__fuel < 0:
            self.__fuel = 0
        print(f"Accelerated to {self.speed} km/h. Fuel remaining: {self.fuel:.1f}%")

    def brake(self, amount):
        # Decreases speed, doesn't go below 0
        self.__speed -= amount
        if self.__speed < 0:
            self.__speed = 0
        print(f"Braked to {self.__speed} km/h.")

    def refuel(self, amount):
        # Increases fuel, doesn't exceed 100
        self.__fuel += amount
        if self.__fuel > 100:
            self.__fuel = 100
        print(f"Refueled. Fuel level: {self.__fuel:.1f}%")

# Create a Car object and test accelerate, brake, refuel
car = Car("Toyota", "Corolla")
print(f"Car: {car.make} {car.model}")

car.accelerate(40)
car.brake(15)
car.refuel(20)
car.accelerate(100)  # test fuel depletion