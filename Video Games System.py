from abc import ABC, abstractmethod

class Game(ABC):
    def __init__(self, title, genre, release_date):
        self.title = title
        self.genre = genre
        self.release_date = release_date

    @abstractmethod
    def play(self):
        pass

class SportsGame(Game):
    def __init__(self, title, release_date, sport_type):
        super().__init__(title, "Sports", release_date)
        self.sport_type = sport_type

    def play(self):
        print(f"Playing {self.title} - {self.sport_type} game")

class AdventureGame(Game):
    def __init__(self, title, release_date, theme):
        super().__init__(title, "Adventure", release_date)
        self.theme = theme

    def play(self):
        print(f"Playing {self.title} - Adventure game")

class Player:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info

    def save_progress(self, game):
        print(f"Saving progress for {game.title}")

    def compete_with(self, opponent):
        print(f"Competing with {opponent.name}")

class Console:
    def __init__(self, console_type):
        self.console_type = console_type
        self.installed_games = []

    def install_game(self, game):
        self.installed_games.append(game)
        print(f"Installed {game.title} on {self.console_type}")

    def play_game(self, game, player):
        print(f"{player.name} is playing {game.title} on {self.console_type}")
        game.play()

if __name__=="__main__":
    
    sports_game = SportsGame("FIFA 22", "2022-09-10", "Soccer")
    adventure_game = AdventureGame("The Legend of Zelda: Breath of the Wild", "2017-03-03", "Fantasy")

    player1 = Player("Alex", "alex@gmail.com")
    player2 = Player("Alen", "alen@gmail.com")

    ps4_console = Console("Xbox Series X")

    ps4_console.install_game(sports_game)
    ps4_console.install_game(adventure_game)

    ps4_console.play_game(sports_game, player1)
    ps4_console.play_game(adventure_game, player2)

    player1.save_progress(sports_game)
    player2.save_progress(adventure_game)

    player1.compete_with(player2)
