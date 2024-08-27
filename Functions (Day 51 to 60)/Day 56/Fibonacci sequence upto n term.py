'''
    This python program uses functions to generate the fibonacci series upto the nth term demanded by the user
'''

def fibonacci(nth_term):
    a,b = 0,1
    for i in range(nth_term):
        print(a, end=' ')
        a,b = b, a+b

n = int(input("Enter the number of terms: "))
fibonacci(n)
