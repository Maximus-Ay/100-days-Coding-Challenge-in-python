'''
     Write a class to represent a Matrix with methods to add, subtract, and multiply matrices.
'''


class Matrix:
     def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])

     def __str__(self):
       return '\n'.join([''.join(map(str, row)) for row in self.matrix])
    
     def add(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrices must have the same dimensions for addition")
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.columns)] for i in range(self.rows)]
        return Matrix(result)
 
     def subtract(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrices must have the same dimensions for subtraction")
        result = [[self.matrix[i][j] - other.matrix[i][j] for j in range(self.columns)] for i in range(self.rows)]
        return Matrix(result)

     def Multiply(self, other):
        if self.columns!= other.rows:
          raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix for multiplication!")
        result = [[sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.columns)) for j in range(other.columns)] for i in range(self.rows)]
        return Matrix(result)
     
     def print_matrix(self):
          for row in self.matrix:
             print('|', end = "")
             for elem in row:
                print(f"{elem:^4}", end='|')
             print()
             

# Using the Class
matrix1 = Matrix([[1,2], [3,4]])
matrix2 = Matrix([[5,6], [7,8]])

print("Matrix 1: ")
matrix1.print_matrix()

print("\nMatrix 2: ")
matrix2.print_matrix()

print("\n Matrix 1 + Matrix 2: ")
(matrix1.add(matrix2)).print_matrix()

print("\n Matrix 1 - Matrix 2: ")
(matrix1.subtract(matrix2)).print_matrix()

print("\n Matrix 1 x Matrix 2: ")
(matrix1.Multiply(matrix2)).print_matrix()






