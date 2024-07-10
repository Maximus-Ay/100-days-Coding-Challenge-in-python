'''
    Below is the fibonacci series upto to the nth term entered by the user.
    The fibonacci series is a recursive mathematical concept in which the next term in 
    the series is gotten from the addition of the two previous terms.
    I will write this program, using recursion
'''

def fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number-1) + fibonacci(number-2)
    
nthTerm = int(input("Enter the nth term of the series: "))

for values in range(1, nthTerm+1):
    print(fibonacci(values), end=" ")