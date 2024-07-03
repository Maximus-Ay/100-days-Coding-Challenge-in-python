'''
    This is a simple program to find the area of a triangle.
    -> Here, we will ask the 3 sides from the user and calculate the area of the traingle using
       a mathematical concept known as Heron's Formula
'''

import math
a = float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))
c = float(input("Enter the length of the third side: "))

s = a + b + c

Area = math.sqrt(s*(s-a)*(s-b)*(s-c))
decimal_places = int(input("Enter the number of decimal places: "))
print(f"Area of triangle with sides a = {a}, b = {b}, and c = {c} is: {Area:.{decimal_places}f} units\u00B2")

'''
    NOTE : This area of a triangle is calculated based on the mathematical concept of Heron's formula. 
    Note that it is not applied for Right Angled triangles
    
'''