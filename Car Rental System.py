from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class Car(ABC):
    def __init__(self, make, model, rental_price):
        self.make = make
        self.model = model
        self.rental_price = rental_price
        self.is_available = True

    @abstractmethod
    def display_info(self):
        pass

class LuxuryCar(Car):
    def display_info(self):
        return f"Luxury Car: {self.make} {self.model}, Rental Price: ${self.rental_price} per day"

class EconomyCar(Car):
    def display_info(self):
        return f"Economy Car: {self.make} {self.model}, Rental Price: ${self.rental_price} per day"

class Customer:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.rental_history = []

    def rent_car(self, car, duration):
        if car.is_available:
            rental_cost = car.rental_price * duration
            rental = Rental(self, car, duration, rental_cost)
            car.is_available = False
            self.rental_history.append(rental)
            return rental
        else:
            print("Sorry, the selected car is not available for rent.")
            return None

    def return_car(self, rental):
        rental.return_car()
        rental.car.is_available = True

class Rental:
    def __init__(self, customer, car, duration, cost):
        self.customer = customer
        self.car = car
        self.duration = duration
        self.cost = cost
        self.start_date = datetime.now()
        self.end_date = self.start_date + timedelta(days=duration)

    def return_car(self):
        print(f"Car returned by {self.customer.name}. Duration: {self.duration} days. Total cost: ${self.cost}")

if __name__ == "__main__":
    luxury_car = LuxuryCar("BMW", "X5", 100)
    economy_car = EconomyCar("Toyota", "Camry", 50)

    customer = Customer("John", "John@gmail.com")

    rental = customer.rent_car(luxury_car, 3)
    if rental:
        print(rental.car.display_info())

    rental1 = customer.rent_car(economy_car, 5)
    if rental1:
        print(rental1.car.display_info())

    print("\nRental History:")
    for rental in customer.rental_history:
        print(f"{rental.car.make} {rental.car.model}, Duration: {rental.duration} days, Cost: ${rental.cost}")

    customer.return_car(rental)
