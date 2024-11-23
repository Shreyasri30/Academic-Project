class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.next_song = None
        self.prev_song = None

class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_song = None

    def insert_at_end(self, title, artist):
        new_song = Song(title, artist)
        if not self.head:
            self.head = new_song
            self.tail = new_song
            self.current_song = new_song
        else:
            new_song.prev_song = self.tail
            self.tail.next_song = new_song
            self.tail = new_song

    def insert_after_song(self, current_title, title, artist):
        current_song = self.find_song(current_title)
        if not current_song:
            print(f"Error: Song '{current_title}' not found.")
            return
        new_song = Song(title, artist)
        new_song.prev_song = current_song
        new_song.next_song = current_song.next_song
        if current_song.next_song:
            current_song.next_song.prev_song = new_song
        else:
            self.tail = new_song
        current_song.next_song = new_song

    def delete_song(self, title):
        song_to_delete = self.find_song(title)
        if not song_to_delete:
            print(f"Error: Song '{title}' not found.")
            return
        if song_to_delete.prev_song:
            song_to_delete.prev_song.next_song = song_to_delete.next_song
        else:
            self.head = song_to_delete.next_song
        if song_to_delete.next_song:
            song_to_delete.next_song.prev_song = song_to_delete.prev_song
        else:
            self.tail = song_to_delete.prev_song
        if song_to_delete == self.current_song:
            self.current_song = song_to_delete.next_song

    def play_next_song(self):
        if self.current_song and self.current_song.next_song:
            self.current_song = self.current_song.next_song
            print(f"Now playing: {self.current_song.title} by {self.current_song.artist}")
        else:
            print("Error: No next song in the playlist.")

    def play_previous_song(self):
        if self.current_song and self.current_song.prev_song:
            self.current_song = self.current_song.prev_song
            print(f"Now playing: {self.current_song.title} by {self.current_song.artist}")
        else:
            print("Error: No previous song in the playlist.")

    def find_song(self, title):
        current_song = self.head
        while current_song:
            if current_song.title == title:
                return current_song
            current_song = current_song.next_song
        return None

    def display_playlist(self):
        current_song = self.head
        while current_song:
            print(f"{current_song.title} by {current_song.artist}")
            current_song = current_song.next_song

playlist = Playlist()
playlist.insert_at_end("Song 1", "Artist 1")
playlist.insert_at_end("Song 2", "Artist 2")
playlist.insert_at_end("Song 3", "Artist 3")
print("Playlist:")
playlist.display_playlist()
print("\nPlay Next Song:")
playlist.play_next_song()
playlist.insert_after_song("Song 1", "Song 1.5", "Artist 1.5")
print("\nUpdated Playlist:")
playlist.display_playlist()
print("\nPlay Next Song:")
playlist.play_next_song()
print("\nPlay Previous Song:")
playlist.play_previous_song()
playlist.delete_song("Song 1.5")
print("\nUpdated Playlist after Deletion:")
playlist.display_playlist()
