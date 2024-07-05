'''
    This is a simple program that converts a temperature from celcius to Fahrenheit

'''

temp_in_celcius = float(input("Enter the temperature in Celcius: "))
temp_in_fahrenheit = ((9 * temp_in_celcius)/5) + 32
print(f"{temp_in_celcius} C = {temp_in_fahrenheit} F")

