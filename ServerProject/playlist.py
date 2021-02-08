import spotipy
from spotipy.oauth2 import *
import time
from Utility import connector, writeDebugLog, getDate


class playlists:
    def __init__(self, sp):
        self.sp = sp
        self.user = self.sp.me()['id']
        self.playlists = self.sp.current_user_playlists()
        self.getDates = getDate.getDate()
        self.name = str(self.getDates.year)
        self.currentID = ""
        self.dataBase = None
        self.addedSongs = []
        self.yearPlaylist = []

    def main(self):
        self.currentID = self.isYearPlaylist()
        self.getDatabase()
        self.getPlaylistSong()
        for item in self.dataBase:
            self.updateAddedSongs(item)
        self.addToPlaylist()

    def printTwoWeeks(self):
        print(self.getDates.twoWeeksFromNow())

    def isYearPlaylist(self):
        if not self.getPlaylistId():
            self.createPlaylist(self.name)
        return self.getPlaylistId()

    def getPlaylistId(self):
        for playlist in self.playlists['items']:
            if playlist['name'] == self.name:
                return playlist['id']
        return False

    def createPlaylist(self, name):
        self.sp.user_playlist_create(self.user, name, False, False, f"Playlist created for {self.user}  most listened "
                                                                    f"songs of {name}")
        self.playlists = self.sp.current_user_playlists()
        return self.getPlaylistId()

    def getDatabase(self):
        sql = "SELECT * FROM timeslistened"
        connector.mycursor.execute(sql)
        self.dataBase = connector.mycursor.fetchall()

    def getPlaylistSong(self):
        counter = 0
        timesCounted = 0
        playlist = self.sp.playlist_items(self.currentID)
        for item in playlist['items']:
            self.yearPlaylist.append(item)
            counter += 1
        if counter == 100:
            counterIsMax = True
            while counterIsMax:
                timesCounted += 1
                playlistCount = self.sp.playlist_items(self.currentID, None, 100, counter)
                for song in playlistCount['items']:
                    self.yearPlaylist.append(song)
                    counter += 1
                if counter == 100 * timesCounted:
                    counterIsMax = True
                else:
                    counterIsMax = False

    def updateAddedSongs(self, song):
        if song['dates'] < self.getDates.twoWeeksFromNow():
            if song['timesListened'] > 7:
                self.addedSongs.append((song['trackID']))

    def addToPlaylist(self):
        removedSongs = []
        for addedSong in self.addedSongs:
            for playlistSong in self.yearPlaylist:
                if addedSong == playlistSong['track']['id']:
                    print(addedSong)
                    removedSongs.append(addedSong)
                    print("same song")
        for song in removedSongs:
            self.addedSongs.remove(song)
        if len(self.addedSongs) > 0:
            self.sp.playlist_add_items(self.currentID, self.addedSongs)
            writeDebugLog.logs.mainLog("Added songs to playlist")


Spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='bccad02b357548da8135bc648ec477f4',
                                                    client_secret='36920227d76e4f8c9925832acf638a9c',
                                                    redirect_uri='http://localhost:1234/ForumTest/tabs'
                                                                 '/test.php',
                                                    scope="playlist-modify-public", open_browser=False))
while True:
    try:
        currentPlaylist = playlists(Spotify)
        currentPlaylist.main()
    except Exception as Error:
        errorLog = writeDebugLog.ErrorLogs()
        errorLog.MainError(Error)
        pass
    time.sleep(7200)
