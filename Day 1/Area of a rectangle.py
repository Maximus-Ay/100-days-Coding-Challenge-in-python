'''
    This is a simple program to be able to find the area of a rectangle.
    Things to know about a rectangle: 
    -> A rectangle is a shape that has 4 sides, two long sides and two short sides.
    -> The longest side is called the length and the shorter side is called the width.
    -> To find the area of the rectangle we have to take the length multiplied by the width.


'''

# Asking the user for the length and width of the rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

Area = length * width

print(f"The Area of the reactangle is: {Area} units^2")
