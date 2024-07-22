'''
    This is simple program that prints the first n fibonacci series number
    n is entered by the user.
'''
def fibo(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibo(number-1) + fibo(number-2)


n = int(input("Enter the value of n: "))
print(f"The first {n} numbers of the fibonacci series are: ")
for num in range(1, n+1):
    print(fibo(num), end=" ")

