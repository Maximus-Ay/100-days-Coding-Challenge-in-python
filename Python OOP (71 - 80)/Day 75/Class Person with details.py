'''
    This is a class called Person with attributes Name and Age and method to display the details
'''

class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def display_details(self):
        print(f"My name is {self.name} and I am {self.age} years old!")

me = Person("Maximus", 20)
me.display_details()
