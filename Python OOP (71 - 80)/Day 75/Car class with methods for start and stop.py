'''
    Simple car class with methods for the start and stop 
'''

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        return f"The {self.model} {self.year} has been started!"
    
    def stop(self):
        return f"The {self.model} {self.year} has been stopped!"
    
myCar = Car("Yo", "BMW", "2021")
print(myCar.start())
print(myCar.stop())