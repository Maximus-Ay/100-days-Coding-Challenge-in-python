'''
    Write a Python class to represent a Polynomial with methods to add, subtract, and multiply polynomials.
'''

class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __str__(self):
        terms = []
        for i, coeff in enumerate(self.coefficients):
            if coeff != 0:
                term = ""
                if coeff != 1 or i == 0:
                    term += str(coeff)
                if i>0:
                    term += "x"
                if i>1:
                    term += "^" + str(i)
                terms.append(term)
        return " + ".join(terms).replace("+-", "-")
    
    def add(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))
        result = [0] * max_len
        for i in range(max_len):
            if i<len(self.coefficients):
                result[i] += self.coefficients[i]
            if i<len(other.coefficients):
                result[i] += other.coefficients[i]
        return Polynomial(result)

    def subtract(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))
        result = [0] * max_len
        for i in range(max_len):
            if i<len(self.coefficients):
                result[i] += self.coefficients[i]
            if i<len(other.coefficients):
                result[i] -= other.coefficients[i]
        return Polynomial(result)
    
    def multiply(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))
        result = [0] * (len(self.coefficients) + len(other.coefficients) - 1)
        for i in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                result[i + j] += self.coefficients[i] * other.coefficients[j]
        return Polynomial(result)
    

p1 = Polynomial([1,2,3]) # 1 + 2x + 3x^2
p2 = Polynomial([4,5]) # 4 + 5x

print("Polynomial 1:", p1)
print("Polynomial 2:", p2)

print("\nPolynomial 1 + Polynomial 2:", p1.add(p2))
print("\nPolynomial 1 - Polynomial 2:", p1.subtract(p2))
print("\nPolynomial 1 * Polynomial 2:", p1.multiply(p2))

