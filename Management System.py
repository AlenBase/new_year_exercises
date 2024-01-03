from abc import ABC, abstractmethod
from datetime import datetime


class AbstractRoom(ABC):
    def __init__(self, room_number, price, amenities=[]):
        self.room_number = room_number
        self.price = price
        self.amenities = amenities

    @abstractmethod
    def display_info(self):
        pass

class AbstractReservation(ABC):
    def __init__(self, guest, room, start_date, end_date):
        self.guest = guest
        self.room = room
        self.start_date = start_date
        self.end_date = end_date

    @abstractmethod
    def display_info(self):
        pass

class Room(AbstractRoom):
    def display_info(self):
        print(f"Room Number: {self.room_number}")
        print(f"Price: ${self.price} per night")
        print(f"Amenities: {', '.join(self.amenities)}")

class Reservation(AbstractReservation):
    def display_info(self):
        print("Reservation Details:")
        self.guest.display_info()
        self.room.display_info()
        print(f"Reservation Dates: {self.start_date} to {self.end_date}")

class StandardRoom(Room):
    def __init__(self, room_number):
        super().__init__(room_number, price=100, amenities=["TV", "Wi-Fi"])

class DeluxeRoom(Room):
    def __init__(self, room_number):
        super().__init__(room_number, price=200, amenities=["TV", "Wi-Fi", "Mini Bar"])

class Guest:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info

    def display_info(self):
        print(f"Guest Name: {self.name}")
        print(f"Contact Information: {self.contact_info}")

class HotelBookingSystem:
    def __init__(self):
        self.rooms = []
        self.reservations = []

    def add_room(self, room):
        self.rooms.append(room)

    def search_available_rooms(self, start_date, end_date):
        available_rooms = []
        for room in self.rooms:
            if all(self.is_room_available(room, start_date, end_date) for reservation in self.reservations):
                available_rooms.append(room)
        return available_rooms

    def is_room_available(self, room, start_date, end_date):
        for reservation in self.reservations:
            if reservation.room == room and self.is_overlapping(reservation.start_date, reservation.end_date, start_date, end_date):
                return False
        return True

    def is_overlapping(self, start1, end1, start2, end2):
        return start1 < end2 and end1 > start2

    def book_room(self, guest, room, start_date, end_date):
        if self.is_room_available(room, start_date, end_date):
            reservation = Reservation(guest, room, start_date, end_date)
            self.reservations.append(reservation)
            print("Reservation successful!")
            reservation.display_info()
        else:
            print("Sorry, the room is not available for the specified dates.")

    def view_reservation_history(self, guest):
        guest_reservations = [reservation for reservation in self.reservations if reservation.guest == guest]
        if guest_reservations:
            for reservation in guest_reservations:
                reservation.display_info()
        else:
            print("No reservation history found for this guest.")

hotel = HotelBookingSystem()

standard_room1 = StandardRoom(101)
deluxe_room1 = DeluxeRoom(201)

hotel.add_room(standard_room1)
hotel.add_room(deluxe_room1)

guest1 = Guest("Vazgen", "vazgen@gmail.com")

hotel.book_room(guest1, standard_room1, datetime(2024, 1, 10), datetime(2024, 1, 15))

# hotel.view_reservation_history(guest1)
