# Exercise 1: Simple Class - Person

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        # Prints a greeting using the person's name and age
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

# Create 2 Person objects and call introduce() on both
person1 = Person("Ribka", 26)
person2 = Person("Dawit", 30)

person1.introduce()
person2.introduce()





