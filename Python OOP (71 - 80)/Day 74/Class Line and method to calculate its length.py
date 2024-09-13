'''
    This is a class Line and a method to calculate its length
'''
import math

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def length(self):
        x1,y1 = self.point1
        x2,y2 = self.point2
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)

myline = Line((1,2), (4,6))
print("Length of the line is: ",myline.length())