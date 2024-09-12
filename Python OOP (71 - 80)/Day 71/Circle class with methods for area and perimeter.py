'''
    This simple python program defines a circle class with methods for the area and circumference
'''
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    # Area of a circle
    def area(self):
        return f"{math.pi * pow(self.radius, 2):.2f}cm^2"
    
    # Circumference of a circle
    def circumference(self):
        return f"{2 * math.pi * self.radius:.2f}cm"

# Instantiating the Circle class
myCircle = Circle(10)
print(myCircle.area())
print(myCircle.circumference())
