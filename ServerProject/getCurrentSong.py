import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


# from Utility import connector, writeDebugLog


# def main(date, time, path):
#    scopeCurrentSong = "user-read-currently-playing"
#    spGetCurrentSong = spotipy.Spotify(auth_manager=spotipy.SpotifyOAuth(client_id='bccad02b357548da8135bc648ec477f4',
#                                                                         client_secret='36920227d76e4f8c9925832acf638a9c',
#                                                                         redirect_uri='http://localhost:1234/ForumTest/tabs/test.php',
#                                                                         scope=scopeCurrentSong, open_browser=True))
#    user = spGetCurrentSong.me()['id']
#    x = spGetCurrentSong.currently_playing()
#    logs = open("./logs/" + date + ".log", "r")
#    loglines = logs.readlines()
#    if len(loglines) > 6:
#        lastSong = loglines[-6].replace("Song: ", "")
#        lastAlbum = loglines[-4].replace("Album: ", "")
#        lastAlbum = lastAlbum.replace("\n", "")
#        lastSong = lastSong.replace("\n", "")
#        logs.close()
#    else:
#        lastSong = ""
#        lastAlbum = ""
#    if x is None:
#        if lastSong == "Offline":
#            pass
#        else:
#            writeDebugLog.OfflineLog(user, date, time)
#            pass
#    else:
#        if x["currently_playing_type"] == "episode":
#            pass
#        elif x["currently_playing_type"] == "track":
#            currentSongName = str(x['item']['name'])
#            currentArtists = x['item']['artists']
#            currentAlbum = str(x['item']['album']['name'])
#            currentType = str(x['item']['type'])
#            sqlTrackID = str(x['item']['id'])
#            connector.mycursor.execute(
#                "SELECT * FROM timeslistened WHERE trackID = '" + sqlTrackID + "';"
#            )
#            row_count = connector.mycursor.rowcount
#            if row_count == 0 and currentType == "track":
#                sql = "INSERT INTO timeslistened (trackID, timesListened) VALUES ('" + sqlTrackID + "', 1)"
#                connector.mycursor.execute(sql)
#                connector.mydb.commit()
#                writeDebugLog.mainLog("Added " + currentSongName + " to Database", date, user, time)
#                if lastSong != str(currentSongName):
#                    writeDebugLog.songLog(currentSongName, currentArtists, currentAlbum, currentType, user, date, time)
#            else:
#                if lastSong != str(currentSongName) and currentType == "track":
#                    sqlTime = "SELECT timesListened FROM timeslistened WHERE trackID = '" + sqlTrackID + "';"
#                    connector.mycursor.execute(sqlTime)
#                    timesListened = connector.mycursor.fetchone()
#                    timesListened = int(timesListened['timesListened'])
#                    timesListened += 1
#                    sqlUpdateTime = "UPDATE timeslistened SET timesListened = '" + str(
#                        timesListened) + "' WHERE trackID = '" + sqlTrackID + "';"
#                    connector.mycursor.execute(sqlUpdateTime)
#                    connector.mydb.commit()
#                    writeDebugLog.mainLog(
#                        "Updated " + currentSongName + " to " + str(timesListened) + " times listened in Database",
#                        date, user, time)
#                    writeDebugLog.songLog(currentSongName, currentArtists, currentAlbum, currentType, user, date, time)
#                else:
#                    pass
#        else:
#            pass
class currentSong:
    def __init__(self, client_id, client_secret, redirect):
        self.scope_current_song = "user-read-currently-playing"
        self.sp = spotipy.Spotify(
            auth_manager=spotipy.SpotifyOAuth(client_id=client_id,
                                              client_secret=client_secret,
                                              redirect_uri=redirect,
                                              scope=self.scope_current_song))
        self.currently_playing = self.sp.currently_playing()
        if self.currently_playing:
            self.song = [self.currently_playing['item']['name'], self.currently_playing['item']['artists'],
                         self.currently_playing['item']['album']['name'],
                         self.currently_playing['item']['type'], self.currently_playing['item']['id']]
        else:
            self.song = None
        # self.song[0] is song name, [1] is artists, [2] is album name, [3] is type

    def printCurrent(self):
        if self.song:
            print(str(self.song[0]) + "\n" + str(self.song[2]))
        else:
            print("cannot")

    def addCurrentToDB


accountId = "bccad02b357548da8135bc648ec477f4"
accountSecret = "36920227d76e4f8c9925832acf638a9c"
URI = "http://localhost:1234/ForumTest/tabs/test.php"

currentSong = currentSong(accountId, accountSecret, URI)
currentSong.testMarket()
# currentSong.printCurrent()
