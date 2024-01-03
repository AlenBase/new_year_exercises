from abc import ABC,abstractmethod
from datetime import datetime, timedelta


class Movies(ABC):
    def __init__(self,title,genre,rating):
        self.title = title
        self.genre = genre
        self.rating = rating
    
    @abstractmethod
    def display_details(self):
        pass
    
    
    
class Comedy(Movies):
    def __init__(self, title, rating):
        super().__init__(title, "Comedy", rating)

    def display_details(self):
        print(f"Title: {self.title}, Genre: {self.genre}, Rating: {self.rating}")

class Drama(Movies):
    def __init__(self, title, rating):
        super().__init__(title, "Drama", rating)

    def display_details(self):
        print(f"Title: {self.title}, Genre: {self.genre}, Rating: {self.rating}")
    
class Customers:
    def __init__(self,name,contact_info):
        self.name = name
        self.contact_info = contact_info
        self.rental_history = []
    
    
    def rent_movie(self, movie, duration_days):
        rental = Rentals(self, movie, duration_days)
        self.rental_history.append(rental)
        print(f"{self.name} rented '{movie.title}' for {duration_days} days.")

    def view_rental_history(self):
        print(f"{self.name}'s Rental History:")
        for rental in self.rental_history:
            print(f"{rental.movie.title} - {rental.duration} days")
            
    def return_movie(self, rental):
        rental.return_movie()
        self.rental_history.remove(rental)
        print(f"{self.name} returned '{rental.movie.title}'.")


class Rentals:
    def __init__(self,customer,movie, duration_days):
        self.customer = customer
        self.duration = duration_days
        self.movie = movie
        self.rental_date = datetime.now()
        self.return_date = None

    def return_movie(self):
        self.return_date = datetime.now()

    def get_rental_cost(self):
        return self.duration * 2 
    
if __name__=="__main__":
    comedy_movie = Comedy('Scary Movie','NC-17')
    drama_movie = Drama('My Fault','R')

    customer = Customers('Kolumb','456-1238')
    customer.rent_movie(comedy_movie,3)
    customer.rent_movie(drama_movie,5)

    customer.view_rental_history()

    rental_return = customer.rental_history[0]
    customer.return_movie(rental_return)
    customer.view_rental_history()
            
        