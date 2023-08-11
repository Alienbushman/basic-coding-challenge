class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song

    def is_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
        songs = set()
        current_song = self
        while current_song:
            song_name = current_song.name
            if song_name in songs:
                return True
            else:
                if current_song.next is not None:
                    songs.add(song_name)
                    current_song = current_song.next
                    continue
                else:
                    break

        return False


def populate_songs(song_names):
    playlist = None
    prev_song = None
    for name in song_names:
        song = Song(name)
        if playlist:
            prev_song.next_song(song)
        else:
            playlist = song
        prev_song = song

    return playlist


if __name__ == '__main__':
    non_repeating_song_names = [f'song_{i}' for i in range(0, 100)]
    repeating_song_names = [f'song_{i}' for i in range(0, 3)]
    repeating_song_names.extend(['song_0'])

    non_repeating_playlist = populate_songs(non_repeating_song_names)
    repeating_playlist = populate_songs(repeating_song_names)

    print(non_repeating_playlist.is_repeating_playlist())
    print(repeating_playlist.is_repeating_playlist())
