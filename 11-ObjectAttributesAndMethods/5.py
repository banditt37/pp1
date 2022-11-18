class music:
    def __init__(self, performer, song, album, year):
        self.performer = performer
        self.song = song
        self.album = album
        self.year = year

    def __str__(self):
        return "Performer: " + self.performer + "\nSong: " + self.song + "\nAlbum: " + self.album + "\nYear: " + self.year



m1 = music("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", "2017")
m2 = music("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", "2017")
m3 = music("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", "2017")

print(m1, "\n")
print(m2, "\n")
print(m3, "\n")