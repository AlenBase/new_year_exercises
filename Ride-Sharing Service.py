from abc import ABC, abstractmethod
from random import randint

class Vehicle(ABC):
    def __init__(self, model, plate_number):
        self.model = model
        self.plate_number = plate_number

    @abstractmethod
    def get_vehicle_type(self):
        pass

class Car(Vehicle):
    def __init__(self, model, plate_number):
        super().__init__(model, plate_number)

    def get_vehicle_type(self):
        return "Car"

class Motorcycle(Vehicle):
    def __init__(self, model, plate_number):
        super().__init__(model, plate_number)

    def get_vehicle_type(self):
        return "Motorcycle"

class Person:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info

class Driver(Person):
    def __init__(self, name, contact_info, vehicle):
        super().__init__(name, contact_info)
        self.vehicle = vehicle
        self.rating = 5.0

    def accept_ride(self, passenger, destination):
        ride_fare = randint(5, 20)  # Random fare for simplicity
        ride = Ride(self, passenger, destination, ride_fare)
        return ride

    def complete_ride(self, ride):
        ride.complete()
        self.rate_passenger(ride.passenger)

    def rate_passenger(self, passenger):
        rating = float(input(f"Rate {passenger.name} (1-5): "))
        passenger.rating = (passenger.rating + rating) / 2

class Passenger(Person):
    def __init__(self, name, contact_info):
        super().__init__(name, contact_info)
        self.rating = 5.0

    def request_ride(self, driver, destination):
        return driver.accept_ride(self, destination)

    def rate_driver(self, driver):
        rating = float(input(f"Rate {driver.name} (1-5): "))
        driver.rating = (driver.rating + rating) / 2

class Ride:
    def __init__(self, driver, passenger, destination, fare):
        self.driver = driver
        self.passenger = passenger
        self.destination = destination
        self.fare = fare
        self.completed = False

    def complete(self):
        self.completed = True
        print(f"Ride from {self.driver.name} to {self.passenger.name} completed.")
        print(f"Fare: ${self.fare}")
        self.passenger.rate_driver(self.driver)

car = Car("Toyota", "Camry")
motorcycle = Motorcycle("Honda", "XYZ")

driver1 = Driver("Pique", "469-861-9364", car)
driver2 = Driver("Hacob", "234-751-9356", motorcycle)

passenger1 = Passenger("Marin", "138-462-1647")
passenger2 = Passenger("Johan", "267-567-1963")

ride1 = passenger1.request_ride(driver1, "Airport")
driver1.complete_ride(ride1)

ride2 = passenger2.request_ride(driver2, "Downtown")
driver2.complete_ride(ride2)
