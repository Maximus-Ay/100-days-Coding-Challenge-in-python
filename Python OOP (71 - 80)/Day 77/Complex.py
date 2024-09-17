'''
This program creates a class called Complex Number with methods to perform 
addition, subtraction, multiplication, and division. 
'''

class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def Addition(self, complex1, complex2):
        return f"{complex1.real + complex2.real} + {complex1.imaginary + complex2.imaginary}i"
    
    def Subtraction(self, complex1, complex2):
        return f"{complex1.real - complex2.real} + {complex1.imaginary - complex2.imaginary}i"
    
    def Multiplication(self, complex1, complex2):
        return f"{(complex1.real * complex2.real) + ((-1) * complex1.imaginary * complex2.imaginary)} + {(complex1.real * complex2.imaginary) + (complex2.real * complex1.imaginary)}i"
    
    def Division(self, complex1, complex2):
        return "Coming soon..."
    
complex1 = Complex(2,4)
complex2 = Complex(3,5)

print(complex1.Addition(complex1, complex2))
print(complex1.Subtraction(complex1, complex2))
print(complex1.Multiplication(complex1, complex2))
print(complex1.Division(complex1, complex2))


