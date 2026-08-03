# Exercise 3: Liskov Substitution Principle (LSP)
#
# THE PROBLEM: If class B is a subclass of class A, you should be
# able to use a B object anywhere an A object is expected, WITHOUT
# breaking anything.
#
# The classic broken example: Penguin inherits from Bird, but penguins
# can't fly. If Bird has a fly() method, and make_bird_fly() calls it
# blindly, Penguin will break the function - violating LSP.

# --- BAD VERSION (commented out, for reference) ---
# class Bird:
#     def fly(self):
#         print("Flying high!")
#
# class Penguin(Bird):
#     def fly(self):
#         raise Exception("Penguins can't fly!")  # breaks the substitution
#
# def make_bird_fly(bird):
#     bird.fly()  # crashes if bird is a Penguin


# --- FIXED VERSION: separate flying ability from being a bird ---

class Bird:
    # Base class - only things ALL birds can do belong here
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")


class FlyingBird(Bird):
    # Only birds that CAN fly inherit this
    def fly(self):
        print(f"{self.name} is flying high!")


class Penguin(Bird):
    # Penguin inherits from Bird (not FlyingBird), since it can't fly
    def swim(self):
        print(f"{self.name} is swimming.")


class Eagle(FlyingBird):
    pass


def make_bird_fly(bird):
    # Now this function only accepts birds that CAN actually fly
    if isinstance(bird, FlyingBird):
        bird.fly()
    else:
        print(f"{bird.name} cannot fly.")


# Test - both Eagle and Penguin work with make_bird_fly() without crashing
eagle = Eagle("Eagle")
penguin = Penguin("Penguin")

make_bird_fly(eagle)     # flies successfully
make_bird_fly(penguin)   # gracefully handled, no crash

penguin.swim()
eagle.eat()