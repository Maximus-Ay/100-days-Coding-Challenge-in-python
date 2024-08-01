'''
    This is a program that uses the notion and concept of loops to be able to print the fibonacci
    series up to the nth term entered by the users
'''

def isFibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return isFibonacci(number-1) + isFibonacci(number-2)
    
nth_term = int(input("Enter the nth term: "))
print(f"Fibonacci series upto the {nth_term} is: ")
for x in range(1, nth_term+1):
    print(isFibonacci(x), end=" ")

    