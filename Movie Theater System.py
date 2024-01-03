from abc import ABC, abstractmethod
from datetime import datetime

class Movie:
    def __init__(self, title, genre, length):
        self.title = title
        self.genre = genre
        self.length = length

class Theater:
    def __init__(self, location, seating_capacity):
        self.location = location
        self.seating_capacity = seating_capacity
        self.seats_available = [[True] * 10 for _ in range(seating_capacity // 10)]

    def display_seating(self):
        for row in self.seats_available:
            print(" ".join(["X" if seat else "O" for seat in row]))

class Showtime:
    def __init__(self, movie, theater, datetime):
        self.movie = movie
        self.theater = theater
        self.datetime = datetime

class Ticket:
    def __init__(self, showtime, seat):
        self.showtime = showtime
        self.seat = seat

class MovieTheaterOperations(ABC):
    @abstractmethod
    def browse_movies(self):
        pass

    @abstractmethod
    def browse_showtimes(self):
        pass

    @abstractmethod
    def reserve_seat(self, showtime, seat):
        pass

    @abstractmethod
    def purchase_ticket(self, ticket):
        pass

class StandardTheater(Theater):
    def __init__(self, location, seating_capacity):
        super().__init__(location, seating_capacity)

class IMAXTheater(Theater):
    def __init__(self, location, seating_capacity):
        super().__init__(location, seating_capacity)

class MovieTheaterSystem(MovieTheaterOperations):
    def __init__(self):
        self.movies = []
        self.theaters = []
        self.showtimes = []
        self.tickets = []

    def browse_movies(self):
        for movie in self.movies:
            print(f"{movie.title} - {movie.genre} - {movie.length} minutes")

    def browse_showtimes(self):
        for showtime in self.showtimes:
            print(f"{showtime.movie.title} - {showtime.theater.location} - {showtime.datetime}")

    def reserve_seat(self, showtime, seat):
        if showtime.theater.seats_available[seat[0]][seat[1]]:
            showtime.theater.seats_available[seat[0]][seat[1]] = False
            print(f"Seat {seat} reserved for {showtime.movie.title} at {showtime.datetime}")
        else:
            print(f"Seat {seat} is already taken.")

    def purchase_ticket(self, ticket):
        self.tickets.append(ticket)
        print(f"Ticket purchased for {ticket.showtime.movie.title} at {ticket.showtime.datetime}. Seat: {ticket.seat}")


if __name__ == "__main__":
    system = MovieTheaterSystem()

    movie1 = Movie("Inception", "Sci-Fi", 133)
    movie2 = Movie("The Dark Knight", "Action", 154)

    theater1 = StandardTheater("City Center", 200)
    theater2 = IMAXTheater("Mega Mall", 100)

    showtime1 = Showtime(movie1, theater1, datetime(2024, 1, 3, 18, 30))
    showtime2 = Showtime(movie2, theater2, datetime(2024, 1, 3, 20, 0))

    system.movies.extend([movie1, movie2])
    system.theaters.extend([theater1, theater2])
    system.showtimes.extend([showtime1, showtime2])

    system.browse_movies()
    print("\n")
    system.browse_showtimes()
    print("\n")

    system.reserve_seat(showtime1, (1, 5))
    system.reserve_seat(showtime1, (1, 5))
    system.reserve_seat(showtime2, (2, 8))

    ticket = Ticket(showtime1, (1, 5))
    system.purchase_ticket(ticket)
