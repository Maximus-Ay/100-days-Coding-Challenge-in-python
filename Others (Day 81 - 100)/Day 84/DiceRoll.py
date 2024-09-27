'''
    - Write a Python program to create a class that simulates a dice roll and returns 
      a random number between 1 and 6.
'''

import random

class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

def main():
    dice = Dice()

    while True:
        print("\nDice Roll Simulator")
        print("1. Roll Dice")
        print("2. Change Number of sides")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            result = dice.roll()
            print(f"You rolled a {result}")
        elif choice == "2":
            sides = int(input("Enter new number of sides: "))
            dice = Dice(sides)
            print(f"Dice now has {sides} sides")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please Try again.")

if __name__ == "__main__":
    main()
  
