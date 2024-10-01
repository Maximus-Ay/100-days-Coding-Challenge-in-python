'''
    - Write a Python program to create a simple text-based game using classes and functions.
'''

import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []


    def is_alive(self):
        return self.health > 0
    

class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def is_alive(self):
        return self.health > 0
    
class Game:
    def __init__(self):
        self.player = None

    def start_game(self):
        name = input("Enter player name: ")
        self.player = Player(name)
        print(f"Welcome, {self.player.name}!")

        while True:
            print("\nGame Menu")
            print("1. Explore")
            print("2. Inventory")
            print("3. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.explore()
            elif choice == "2":
                self.show_inventory()
            elif choice == "3":
                print(f"Thanks for playing")
                break
            else:
                print("Invalid choice. Please Try again")

    def explore(self):
        print("\nExploring....")
        encounter_chance = random.randint(1, 10)

        if encounter_chance <= 5:
            enemy_name = random.choice(["Goblin", "Troll", "Orc"])
            enemy_health = random.randint(20, 50)
            enemy = Enemy(enemy_name, enemy_health)
            print(f"Encountered {enemy_name}!")

            while enemy.is_alive() and self.player.is_alive():
                print("\nCombat Menu")
                print("1. Attack")
                print("2. Run")

                choice = input("Enter your choice: ")

                if choice == "1":
                    damage = random.randint(10, 20)
                    enemy.health -= damage
                    print(f" You dealt {damage} to {enemy.name} damage to you!")

                    if enemy.is_alive():
                        damage = random.randint(5, 15)
                        self.player.health -= damage
                        print(f"{enemy.name} dealt {damage} damage to you")
                
                elif choice == "2":
                    print("Ran away!")
                    break
                else:
                    print("Invalid choice. Please Try again!")
                    
            if not enemy.is_alive():
                print(f"You defeated {enemy.name}!")
                loot_chance = random.randint(1, 10)
                if loot_chance <= 7:
                    loot = random.choice(["Sword", "Shield", "Potion"])
                    self.player.inventory.append(loot)
                    print(f"You found {loot}!")
            elif not self.player.is_alive():
                print("You died! Game over.")
                exit()
            else:
                print("Nothing Found!")

    def show_inventory(self):
        print("\nInventory")
        for item in self.player.inventory:
            print(item)


game = Game()
game.start_game()

            