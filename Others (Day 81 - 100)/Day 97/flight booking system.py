'''
    Write a program to create a class that represents a basic flight booking system 
    with methods to add, remove, and book flights.
'''

class Flight:
    def __init__(self, flight_number, departure, arrival, departure_time, arrival_time, seats):
        self.flight_number = flight_number
        self.departure = departure
        self.arrival = arrival
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.seats = seats
        self.booked_seats = 0

    def __str__(self):
        return f"Flight Number: {self.flight_number}\nDeparture: {self.departure}\nArrival: {self.arrival}\nDeparture Time: {self.departure_time}\nArrival Time: {self.arrival_time}\nAvailable Seats: {self.seats - self.booked_seats}"

class FlightBookingSystem:
    def __init__(self):
        self.flights = {}
        self.bookings = {}

    def add_flight(self, flight_number, departure, arrival, departure_time, arrival_time, seats):
        if flight_number not in self.flights:
            flight = Flight(flight_number, departure, arrival, departure_time, arrival_time, seats)
            self.flights[flight_number] = flight
            print(f"Flight {flight_number} added successfully.")
        else:
            print(f"Flight {flight_number} already exists.")

    def remove_flight(self, flight_number):
        if flight_number in self.flights:
            del self.flights[flight_number]
            print(f"Flight {flight_number} removed successfully.")
        else:
            print(f"Flight {flight_number} not found.")

    def book_flight(self, flight_number, passenger_name):
        if flight_number in self.flights:
            flight = self.flights[flight_number]
            if flight.booked_seats < flight.seats:
                flight.booked_seats += 1
                self.bookings[passenger_name] = flight_number
                print(f"Flight {flight_number} booked successfully for {passenger_name}.")
            else:
                print(f"Flight {flight_number} fully booked.")
        else:
            print(f"Flight {flight_number} not found.")

    def cancel_booking(self, passenger_name):
        if passenger_name in self.bookings:
            flight_number = self.bookings[passenger_name]
            flight = self.flights[flight_number]
            flight.booked_seats -= 1
            del self.bookings[passenger_name]
            print(f"Booking cancelled for {passenger_name}.")
        else:
            print(f"Booking for {passenger_name} not found.")

    def display_flights(self):
        print("\nAvailable Flights:")
        for flight in self.flights.values():
            print(flight)
            print("--------------------")

    def display_bookings(self):
        print("\nBookings:")
        for passenger_name, flight_number in self.bookings.items():
            print(f"{passenger_name}: {flight_number}")

# Example usage
flight_system = FlightBookingSystem()

while True:
    print("\nFlight Booking System")
    print("1. Add flight")
    print("2. Remove flight")
    print("3. Book flight")
    print("4. Cancel booking")
    print("5. Display flights")
    print("6. Display bookings")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        flight_number = input("Enter flight number: ")
        departure = input("Enter departure: ")
        arrival = input("Enter arrival: ")
        departure_time = input("Enter departure time: ")
        arrival_time = input("Enter arrival time: ")
        seats = int(input("Enter number of seats: "))
        flight_system.add_flight(flight_number, departure, arrival, departure_time, arrival_time, seats)
    elif choice == "2":
        flight_number = input("Enter flight number: ")
        flight_system.remove_flight(flight_number)
    elif choice == "3":
        flight_number = input("Enter flight number: ")
        passenger_name = input("Enter passenger name: ")
        flight_system.book_flight(flight_number, passenger_name)
    elif choice == "4":
        passenger_name = input("Enter passenger name: ")
        flight_system.cancel_booking(passenger_name)
    elif choice == "5":
        flight_system.display_flights()
    elif choice == "6":
        flight_system.display_bookings()
    elif choice == "7":
        break
    else:
        print("Invalid choice. Please try again.")
