'''
    - Write a Python program to create a class that represents a deck of cards. 
      Include methods to shuffle the deck and draw a card.
'''

import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"
    
class Deck:
    def __init__(self):
      self.cards = []
      self.suits = ['Hearts', 'Diamonds','Clubs','Spades']
      self.values = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']


      for suit in self.suits:
        for value in self.values:
          self.cards.append(Card(suit,value))

    def shuffle(self):
      random.shuffle(self.cards)
      print("Deck Shuffled.")

    def draw_card(self):
      if self.cards:
        drawn_card = self.cards.pop()
        print(f"Drew: {drawn_card}")
      else:
        print("No cards left in deck.") 

def main():
   deck = Deck()

   while True:
      print("\nDeck of Cards Menu:")
      print("1. Shuffle Deck")
      print("2. Draw Card")
      print("3. View Remaining Cards")
      print("4. Exit")

      choice = input("Enter your choice: ")

      if choice == "1":
        deck.shuffle()
      elif choice == "2":
        deck.draw_card()
      elif choice == "3":
        print(f"Remanining cards: {len(deck.cards)}")
        print("Top 5 cards.")
        for card in deck.cards[-5:]:
           print(card)
      elif choice == "4":
        break
      else:
        print("Invalid choice. Please Try again")

if __name__ == "__main__":
    main()