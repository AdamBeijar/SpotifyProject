from Utility import getDate


class logs:
    def __init__(self, user):
        date = getDate.getDate()
        self.date = date.date()
        self.user = user
        self.time = date.time()
        self.logs = open("./logs/" + self.date + ".log", "a")
        self.logs.write(f"{self.date} {self.time}")

    def mainLog(self, reason):
        self.logs.write(f"\nUser: {self.user}")
        self.logs.write("\n----------------------------------\n")
        self.logs.write(f"Reason: {reason}")
        self.logs.write("\n----------------------------------\n\n")
        self.logs.close()

    def songLog(self, song, artist, album):
        artists = ", ".join(artist)
        self.logs.write(f"\nUser: {self.user} is playing: ")
        self.logs.write("\n----------------------------------\n")
        self.logs.write(f"Song: {song}")
        self.logs.write(f"\nArtist: {artists}")
        self.logs.write(f"\nAlbum: {album}")
        self.logs.write("\n----------------------------------\n\n")
        self.logs.close()

    def OfflineLog(self):
        self.logs.write(f"\nUser: {self.user} is offline")
        self.logs.write("\n----------------------------------\n")
        self.logs.write("Song: Offline")
        self.logs.write("\nArtist: Offline")
        self.logs.write("\nAlbum: Offline")
        self.logs.write("\nType: Offline")
        self.logs.write("\n----------------------------------\n\n")
        self.logs.close()
