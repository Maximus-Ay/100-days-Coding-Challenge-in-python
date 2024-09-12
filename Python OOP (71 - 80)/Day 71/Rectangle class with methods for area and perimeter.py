'''
    Simple python OOP program that defines a class called Rectangle containing methods for the area and perimeter
'''

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.width + self.length)

myRectangle = Rectangle(12, 4)
print(myRectangle.area())
print(myRectangle.perimeter())