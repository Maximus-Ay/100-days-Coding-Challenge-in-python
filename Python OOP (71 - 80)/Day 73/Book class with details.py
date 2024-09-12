'''
    This python program defines a class called book which displays the details of a book
'''

class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
    
    def Display_book_details(self):
        return f"BOOK DETAILS:\nTitle: {self.title}\nAuthor: By {self.author}\nISBN: {self.ISBN}"

book1 = Book("Holy Spirit My Senior Partner", "David Yonggi Cho", 7827963718687)
book2 = Book("Atomic Habits", "James Clear", 737637531367)
print(book1.Display_book_details())
print(book2.Display_book_details())
