# Hello, World!
print("Hello World!")

# Math Functions 
MF_A = 50 + 50 * 10
print(MF_A)
MF_B = 100 * 500 / 10
print(MF_B)
MF_C = 50 + 100 
print(MF_C)

# Functions
def my_function(value):
    return value + 5

print(my_function(6))
print(my_function(7 + 8))

# Strings - A Little Bit about me 
string1 = "Hello! "
string2 = "I'm Sushlok "
string3 = "and I'm Interested in Computer Science."
print(string1 + string2 + string3)

# Built-in-Functions - .format()
pi = 3.14159
formatted = format(pi, '.2f')
print(formatted)

# Built-in-Functions - .format() (But in my Code)
digits = 3.121810
formatted = format(pi, '.3f')
print(formatted)

# Classes - Birds
class Bird:
  # Class attribute
  is_hungry = True

parakeet = Bird()
parrot = Bird()

print("Bird are hungry!")
print("Feeding birds...")

parakeet.is_hungry = False
parrot.is_hungry = False

print("Birds fed!")

# Classes - Code Ninja
class House:
    name = "Code Ninja"
    rooms = 4
    stories = 2

    @staticmethod
    def is_on_market(home):
        if home.name == "":
            return True
        else:
            return False

    @classmethod
    def paint_wall(cls, color):
        return f"Painting wall with the color {color}."

# Example usage:
my_home = House()
print(House.is_on_market(my_home))
print(House.paint_wall("blue"))