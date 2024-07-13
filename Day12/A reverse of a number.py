'''
    This is a simple program to find the reverse of a number

'''
def reverse(number):
    number = str(number)
    return int(number[::-1])

    # or we could go the normal way with some mathematics
    # reversed_number = 0
    # while number > 0:
    #   last digit = number % 10
    #   reversed_number = reversed_number * 10 + last_digit
    #   number = number // 10

    # return reversed_number

number = int(input("Enter the number: "))

print(f"The reverse of a {number} is {reverse(number)}")