from project.song import Song


class Album:

    def __init__(self, name):
        self.name = name
        self.published = False
        self.songs = []

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return f"Cannot add songs. Album is published."
        for current_song in self.songs:
            if current_song.name == song.name:
                return f"Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return f"Cannot remove songs. Album is published."
        for current_song in self.songs:
            if current_song.name == song_name:
                self.songs.remove(current_song)
                return f"Removed song {song_name} from album {self.name}."
        return f"Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = ''
        result += 'Album ' + self.name + '\n'
        for current_song in self.songs:
            result += '== ' + current_song.get_info() + '\n'
        return result
