'''
    This python program represents a class called Library with methods to add, remove and search for books
'''

class Library:
    def __init__(self):
        self.books = {}
    
    def add_books(self, title, author):
        self.books[title] = author
        print(f"Book {title} by {author} has been added!")

    def remove_books(self, title):
        if title in self.books:
            del self.books[title]
            print(f"Book {title} removed!")
        else:
            print(f"Book {title} not found!")

    def search_books(self, title):
        if title in self.books:
            print(f"Book {title} found. Author : {self.books[title]}")
        else:
            print(f"Book {title} not found!")
    

myLibrary = Library()
myLibrary.add_books("Atomic Habits", "James Clear")
myLibrary.add_books("The Art of War", "San Tzu")
myLibrary.add_books("Wisdom from Monroe", "Myles Munroe")
myLibrary.search_books("Atomic Habits")
myLibrary.search_books("Maximus")
myLibrary.remove_books("The Art of War")
myLibrary.search_books("The Art of War")
