'''
    - Write a program to create a class that represents a movie rental system with methods to add, remove, and rent movies.
'''
class Movie:
    def __init__(self, title, genre, rating, availability=True):
        self.title = title
        self.genre = genre
        self.rating = rating
        self.availability = availability

    def __str__(self):
        return f"{self.title} ({self.genre}, {self.rating}) - Available: {self.availability}"
    
class MovieRentalSystem:
    def __init__(self):
        self.movies = []

    def add_movie(self, title, genre, rating):
        movie = Movie(title, genre, rating)
        self.movies.append(movie)
        print(f"Added movie: {movie}")

    def remove_movie(self, title):
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                self.movies.remove(movie)
                print(f"Removed movie: {title}")
                return
            print(f"Movie '{title}' not found.")

    def rent_movie(self, title):
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                if movie.availability:
                    movie.availability = False
                    print(f"Rented movie: {title}")
                else:
                    print(f"Movie '{title}' is currently unavailable.")
                return
            print(f"Movie '{title}' not found")
    
    def return_movie(self, title):
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                if not movie.availability:
                    movie.availability = True
                    print(f"Returned movie: {title}")
                else:
                    print(f"Movie '{title}' is already available.")
                return 
            print(f"Movie '{title}' not found")
        
    def display_movies(self):
        print("\nAvailable Movies:")
        for movie in self.movies:
            if movie.availability:
                print(movie)
        print("\nRented Movies:")
        for movie in self.movies:
            if not movie.availability:
                print(movie)

rental_system = MovieRentalSystem()

while True:
    print("\nMovie Rental System")
    print("1. Add movie")
    print("2. Remove movie")
    print("3. Rent movie")
    print("4. Return movie")
    print("5. Display movies")
    print("6. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        title = input("Enter movie title: ")
        genre = input("Enter movie genre: ")
        rating = input("Enter movie rating: ")
        rental_system.add_movie(title,genre,rating)
    elif choice == "2":
        title = input("Enter movie title: ")
        rental_system.remove_movie(title)
    elif choice == "3":
        title = input("Enter movie title: ")
        rental_system.rent_movie(title)
    elif choice == "4":
        title = input("Enter movie title: ")
        rental_system.return_movie(title)
    elif choice == "5":
        rental_system.display_movies()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please Try Again.")
    

