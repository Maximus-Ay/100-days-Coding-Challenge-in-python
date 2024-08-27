'''
    This is a program that finds the greatest common divisors between two numbers
'''

def GCD(number1, number2):
    divisors_of_first_number = []
    divisors_of_second_number = []
    for x in range(1, number1 + 1):
        if number1 % x == 0:
            divisors_of_first_number.append(x)
    for x in range(1, number2 + 1):
        if number2 % x == 0:
            divisors_of_second_number.append(x)
    common_divisors = []
    for element in divisors_of_first_number:
        if element in divisors_of_second_number:
            common_divisors.append(element)
    return f"The GCD between {number1} and {number2} is: {common_divisors[len(common_divisors) - 1]}"

print(GCD(10, 15))