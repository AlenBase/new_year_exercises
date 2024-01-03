
from abc import ABC, abstractmethod
from datetime import datetime

class MusicOperation(ABC):
    @abstractmethod
    def play(self):
        pass


class Rock(MusicOperation):
    def get_genre(self):
        return "Rock"

class Pop(MusicOperation):
    def get_genre(self):
        return "Pop"

class Classic(MusicOperation):
    def get_genre(self):
        return "Classic"

class Song(Rock, Pop, Classic):
    def __init__(self, title, artist, length):
        self.title = title
        self.artist = artist
        self.length = length

    def play(self):
        print(f"Now playing: {self.title} by {self.artist} ({self.length} seconds)")

class Album(Rock, Pop, Classic):
    def __init__(self, title, artist, release_date):
        self.title = title
        self.artist = artist
        self.release_date = release_date
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def play(self):
        print(f"Now playing album: {self.title} by {self.artist} ({self.release_date})")
        for song in self.songs:
            song.play()

class Playlist(Rock,Pop,Classic):
    def __init__(self, name, songs):
        self.name = name
        self.songs = songs

    def play(self):
        print(f"Now playing playlist: {self.name}")
        for song in self.songs:
            song.play()
            
class User:
    def __init__(self,username):
        self.username = username
        self.playlists = []
        self.listening_history = []
        
    
    def create_playlist(self,name,songs):
        playlist = Playlist(name,songs)
        self.playlists.append(playlist)
        return playlist
    
    
    def add_song_to_playlist(self,playlist,song):
        if playlist in self.playlists:
            playlist.songs.append(song)
            print('hello')
        else:
            print('Playlist not found.')
            
    def listen_to_song(self,song):
        song.play()
        self.listening_history.append(song)
        
    def view_history(self):
        print('Listening history:')
        for song in self.listening_history:
            print(f' - {song.title} by {song.artist} ({song.get_genre()})')
            

if __name__ == "__main__":
    rock_song = Song("The Boys Are Back in Town", "Thin Lizzy", 143)
    pop_song = Song("Michael Jackson", "Smooth Criminal", 240)
    classic_song = Song("Mocart", "Moon Sonata", 364)
    rock_song2 = Song("Just Because","Elvis Presli",154)

    rock_album = Album("Rock Album", "Rock Band", datetime.now().strftime("%Y-%m-%d"))
    rock_album.add_song(rock_song)
    rock_album.add_song(rock_song2)

    pop_playlist = Playlist("Pop Playlist", [pop_song])
    classic_playlist = Playlist("Classic Playlist", [classic_song])
    
    user = User('Alen')
    user.create_playlist('Favorite songs',[rock_song,pop_song])
    user.add_song_to_playlist('Favorite songs',classic_song)
    
    user.listen_to_song(rock_song)
    user.listen_to_song(rock_song2)
    user.listen_to_song(pop_song)
    user.listen_to_song(classic_song)
    
    user.view_history()