from abc import ABC, abstractmethod
from datetime import date

class Game(ABC):
    def __init__(self, title, genre, release_date):
        self.title = title
        self.genre = genre
        self.release_date = release_date

    @abstractmethod
    def play(self):
        pass

class ActionGame(Game):
    def __init__(self, title, release_date):
        super().__init__(title, "Action", release_date)

    def play(self):
        print(f"Playing {self.title} - Action")

class StrategyGame(Game):
    def __init__(self, title, release_date):
        super().__init__(title, "Strategy", release_date)

    def play(self):
        print(f"Playing {self.title} - Strategy")

class Developer:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info

    def create_game(self, title, genre, release_date):
        if genre.lower() == "action":
            return ActionGame(title, release_date)
        elif genre.lower() == "strategy":
            return StrategyGame(title, release_date)
        else:
            print("Invalid genre.")
            return None

class Publisher:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info

    def release_game(self, game):
        print(f"Publisher {self.name} is releasing {game.title} on {game.release_date}")

    def sell_game(self, game, copies_sold):
        print(f"Game {game.title} sold {copies_sold} copies.")

if __name__ == "__main__":
    game_developer = Developer("Ubisoft.", "ubisoft@gmail.com")

    action_game = game_developer.create_game("Assasin's Creed Mirage", "Action", date(2024, 1, 1))
    strategy_game = game_developer.create_game("Heroes of Might and Magic V", "Strategy", date(2024, 1, 15))

    game_publisher = Publisher("Ubisoft", "ubisoft@gmail.com")

    game_publisher.release_game(action_game)
    game_publisher.sell_game(action_game, 200000)

    game_publisher.release_game(strategy_game)
    game_publisher.sell_game(strategy_game, 40000)
