'''
    This is a simple python program that solves quadratic equations.
    It will also consider the fact that the equation might be complex.

'''
import math
import time # Just to play with output and make it sound cool
from printEquation import printEquation # This is used for my printEquation method I created.
import os  # to clear the screen while solving

a = float(input("Enter the coefficient of x^2 in the equation:  "))
b = float(input("Enter the coefficient of x in the equation: "))
c = float(input("Enter the constant term in the equation: "))

# Printing the equation:
printEquation(a,b,c)

Determinant = pow(b,2) - (4*a*c)
def FunDisplay():
    time.sleep(0.9)
    print("Solving...")
    time.sleep(0.9)
    print("Processing...")
    time.sleep(0.9)
    print("Almost done...")
    time.sleep(0.9)

if Determinant > 0:
    os.system("cls")
    printEquation(a,b,c)
    FunDisplay()
    print("The equation has distinct real roots")
    x1  = (-b + math.sqrt(Determinant))/ (2*a)
    x2 = (-b - math.sqrt(Determinant))/ (2*a)
    print(f"The roots of the quadratic equations are: x = {x1} or x = {x2}")
elif Determinant == 0:
    os.system("cls")
    printEquation(a,b,c)
    FunDisplay()
    print("Equation has equal roots hence answer only one value")
    x = (-b)/(2*a)
    print(f"The root of the quadratic equation is: x = {x}")
else:
    os.system("cls")
    printEquation(a,b,c)
    FunDisplay()
    complexpart = math.sqrt(-(Determinant))/(2*a)
    realtpart = (-b)/(2*a)
    print("Equation has complex roots hence answer only one value")
    print(f"The roots of the quadratic equations are: x = ({realtpart} + i{complexpart:.2f}) Or x = ({realtpart} - i{complexpart:.2f})")



    


