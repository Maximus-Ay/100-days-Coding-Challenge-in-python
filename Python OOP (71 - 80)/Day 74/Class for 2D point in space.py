'''
    This is a simple program that defines a 2D point in Space and method to calculate the distance between.
'''
import math
class Point2D:
    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

def distance(Point1, Point2):
    return math.sqrt(pow(Point2.y_coordinate - Point1.y_coordinate, 2) + pow(Point2.x_coordinate - Point1.x_coordinate, 2))
    

point1 = Point2D(3, 4)
point2 = Point2D(0, 0)
print(distance(point1, point2))
