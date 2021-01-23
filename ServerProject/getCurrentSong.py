import time
import spotipy
from Utility import connector, writeDebugLog


class songs:
    def __init__(self, client_id, client_secret, redirect):
        scope_current_song = "user-read-currently-playing"
        sp = spotipy.Spotify(
            auth_manager=spotipy.SpotifyOAuth(client_id=client_id,
                                              client_secret=client_secret,
                                              redirect_uri=redirect,
                                              scope=scope_current_song))
        self.currently_playing = sp.currently_playing()
        if self.currently_playing:
            self.song = [self.currently_playing['item']['name'], self.currently_playing['item']['artists'],
                         self.currently_playing['item']['album']['name'],
                         self.currently_playing['item']['type'], self.currently_playing['item']['id']]
            # self.song[0] is song name, [1] is artists, [2] is album name, [3] is type, [4] is id
        else:
            self.song = None
        self.user = sp.me()['id']

    def fixArtists(self):
        fixed_artists = []
        for artist in self.song[1]:
            fixed_artists.append(artist['name'])
        return fixed_artists

    def main(self):
        if self.song:
            if self.checkSongState():
                writeDebugLog.logs.songLog(self.song[0], self.song[1], self.song[2], self.song[3])
                connector.mycursor.execute("SELECT * FROM timeslistened WHERE trackID = '" + self.song[4] + "';")
                row_count = connector.mycursor.rowcount
                if row_count == 0:
                    self.addCurrentToDB()
                else:
                    self.addOneToCurrentDB()
        else:
            writeDebugLog.logs.OfflineLog(self.user)

    def addCurrentToDB(self):
        sql = "INSERT INTO timeslistened (trackID, timesListened) VALUES ('" + self.song[4] + "', 1)"
        connector.mycursor.execute(sql)
        connector.mydb.commit()
        writeDebugLog.logs.mainLog(f"Added {self.song[1]} to the database")

    def addOneToCurrentDB(self):
        current_times = "SELECT timesListened FROM timeslistened WHERE trackID = '" + self.song[4] + "';"
        connector.mycursor.execute(current_times)
        current_listen_times = connector.mycursor.fetchone()
        current_listen_times = int(current_listen_times['timesListened'])
        current_listen_times += 1
        sqlUpdateTime = "UPDATE timeslistened SET timesListened = '" + str(
            current_listen_times) + "' WHERE trackID = '" + self.song[4] + "';"
        connector.mycursor.execute(sqlUpdateTime)
        connector.mydb.commit()
        writeDebugLog.logs.mainLog(f"Updated {self.song[0]}'s times listened to {current_listen_times}")

    def checkSongState(self):
        try:
            if self.getSong() == lastSong.getSong():
                return False  # Is same song as last, wont update anything
            else:
                return True  # Is not same song as last
        except NameError:  # First song playing with bot
            return True

    def getSong(self):
        real_artists = self.fixArtists()
        return self.song, real_artists


accountId = "bccad02b357548da8135bc648ec477f4"
accountSecret = "36920227d76e4f8c9925832acf638a9c"
URI = "http://localhost:1234/ForumTest/tabs/test.php"

while True:
    currentSong = songs(accountId, accountSecret, URI)
    currentSong.main()
    lastSong = songs(accountId, accountSecret, URI)
    time.sleep(20)
