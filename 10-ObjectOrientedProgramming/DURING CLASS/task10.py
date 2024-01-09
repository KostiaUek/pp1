def append_prefix(prefix: str):
    while len(prefix) < 12:
        prefix += " "
    return prefix


class Song:

    def __init__(self, author, name, album, year, duration, features):
        self.author = author
        self.name = name
        self.album = album
        self.year = year
        self.duration = duration
        self.features = features

    def __str__(self):
        return append_prefix("Performer:") + str(self.author) + "\n" \
            + append_prefix("Song:") + str(self.name) \
            + "\n" + append_prefix("Album:") + str(self.album) \
            + "\n" + append_prefix("Year:") + str(self.year) \
            + "\n" + append_prefix("Duration:") + str(self.duration) \
            + "\n" + append_prefix("Features:") + str(self.features) \
            + "\n"


song_1 = Song("Taylor Swift", "Blank Space", "1989", "2014", "3:51", "None")
song_2 = Song("Kendrick Lamar", "HUMBLE.", "DAMN.", "2017", "2:57", "None")
print(song_1)
print(song_2)
