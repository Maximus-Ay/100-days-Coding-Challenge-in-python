'''
    - Write a Python program to create a class that represents a basic hotel reservation system 
      with methods to add, remove, and reserve rooms.
'''
class HotelReservation:
    def __init__(self, total_rooms):
        """Initialize the hotel reservation system."""
        self.total_rooms = total_rooms
        self.available_rooms = {room_number: "Available" for room_number in range(1, total_rooms + 1)}

    def display_rooms(self):
        """Display the status of all rooms."""
        print("\nRoom Status:")
        for room, status in self.available_rooms.items():
            print(f"Room {room}: {status}")
        print()

    def add_room(self, room_number):
        """Add a new room to the system."""
        if room_number in self.available_rooms:
            print(f"Room {room_number} already exists.")
        else:
            self.available_rooms[room_number] = "Available"
            print(f"Room {room_number} has been added.")

    def remove_room(self, room_number):
        """Remove a room from the system."""
        if room_number in self.available_rooms:
            del self.available_rooms[room_number]
            print(f"Room {room_number} has been removed.")
        else:
            print(f"Room {room_number} does not exist.")

    def reserve_room(self, room_number):
        """Reserve a room."""
        if room_number not in self.available_rooms:
            print(f"Room {room_number} does not exist.")
        elif self.available_rooms[room_number] == "Reserved":
            print(f"Room {room_number} is already reserved.")
        else:
            self.available_rooms[room_number] = "Reserved"
            print(f"Room {room_number} has been reserved.")

    def cancel_reservation(self, room_number):
        """Cancel a reservation."""
        if room_number not in self.available_rooms:
            print(f"Room {room_number} does not exist.")
        elif self.available_rooms[room_number] == "Available":
            print(f"Room {room_number} is not reserved.")
        else:
            self.available_rooms[room_number] = "Available"
            print(f"Reservation for room {room_number} has been canceled.")


# Example Usage
if __name__ == "__main__":
    hotel = HotelReservation(total_rooms=5)
    
    # Display initial room status
    hotel.display_rooms()

    # Reserve a room
    hotel.reserve_room(2)
    hotel.reserve_room(3)

    # Display updated room status
    hotel.display_rooms()

    # Add a new room
    hotel.add_room(6)

    # Remove an existing room
    hotel.remove_room(4)

    # Cancel a reservation
    hotel.cancel_reservation(2)

    # Try to cancel a non-reserved room
    hotel.cancel_reservation(4)

    # Display final room status
    hotel.display_rooms()
