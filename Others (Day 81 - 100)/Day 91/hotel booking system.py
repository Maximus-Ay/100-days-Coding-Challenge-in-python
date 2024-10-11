'''
    - Write a Python program to create a class that represents a hotel booking system 
      with methods to add, remove, and book rooms.
'''
class Room:
    def __init__(self, room_number, room_type, price, availability=True):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.availability = availability

    def __str__(self):
        return f"Room {self.room_number} ({self.room_type}, ${self.price}) - Available: {self.availability}"

class HotelBookingSystem:
    def __init__(self):
        self.rooms = []

    def add_room(self, room_number, room_type, price):
        room = Room(room_number, room_type, price)
        self.rooms.append(room)
        print(f"Room added: {room}")

    def remove_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                self.rooms.remove(room)
                print(f"Room {room_number} removed")
                return
        print(f"Room {room_number} not found")

    def book_room(self, room_number, guest_name, duration):
        for room in self.rooms:
            if room.room_number == room_number:
                if room.availability:
                    room.availability = False
                    print(f"Room {room_number} booked by {guest_name} for {duration} nights")
                    print(f"Total cost: ${room.price * duration}")
                else:
                    print(f"Room {room_number} is already booked")
                return
        print(f"Room {room_number} not found")

    def check_out(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                if not room.availability:
                    room.availability = True
                    print(f"Room {room_number} checked out")
                else:
                    print(f"Room {room_number} is already available")
                return
        print(f"Room {room_number} not found")

    def display_rooms(self):
        print("\nAvailable Rooms:")
        for room in self.rooms:
            if room.availability:
                print(room)
        print("\nBooked Rooms:")
        for room in self.rooms:
            if not room.availability:
                print(room)

# Example usage
hotel_system = HotelBookingSystem()

while True:
    print("\nHotel Booking System")
    print("1. Add room")
    print("2. Remove room")
    print("3. Book room")
    print("4. Check out")
    print("5. Display rooms")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        room_number = input("Enter room number: ")
        room_type = input("Enter room type: ")
        price = float(input("Enter room price: "))
        hotel_system.add_room(room_number, room_type, price)
    elif choice == "2":
        room_number = input("Enter room number: ")
        hotel_system.remove_room(room_number)
    elif choice == "3":
        room_number = input("Enter room number: ")
        guest_name = input("Enter guest name: ")
        duration = int(input("Enter duration (nights): "))
        hotel_system.book_room(room_number, guest_name, duration)
    elif choice == "4":
        room_number = input("Enter room number: ")
        hotel_system.check_out(room_number)
    elif choice == "5":
        hotel_system.display_rooms()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")
