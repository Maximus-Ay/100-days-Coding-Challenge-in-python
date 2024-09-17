'''
    This is a python program that creates a class shape and defines methods to calculate the area and perimeter
    It also includes subclasses like Triangle, Circle and Rectangle
'''
import math

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def area(self):
        return "The area is lol"

    def perimeter(self):
        return "The perimeter is lol"

class Rectangle(Shape):
    def __init__(self, color, is_filled, length, width):
        super().__init__(color, is_filled)
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
    
    def area(self):
        return math.pi * pow(self.radius, 2)
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, color, is_filled, base, height):
        super().__init__(color, is_filled)
        self.base = base
        self.height = height
    
    def area(self):
        return (self.base * self.height) / 2
    
    def perimeter(self):
        return "Don't know how to calculate!"

    
myShape = Shape("Red", True)
myCircle = Circle("Red", False, 7)
myRectangle = Rectangle("Blue", True, 10, 5)
myTriangle = Triangle("Violet", True, 12, 20)
print(myShape.area())
print(myShape.perimeter())
print(myCircle.area())
print(myCircle.perimeter())
print(myTriangle.area())
print(myTriangle.perimeter())
print(myRectangle.area())
print(myRectangle.perimeter())

