'''
    Simple python program to find the radius of a circle
'''
import math
def Area_Of_A_Circle(radius):
    return f"{math.pi * pow(radius, 2):.2f}cm^2"

print(Area_Of_A_Circle(10))