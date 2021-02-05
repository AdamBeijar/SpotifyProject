import spotipy
from spotipy.oauth2 import *
from Utility import connector, writeDebugLog, getDate


class playlists:
    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='bccad02b357548da8135bc648ec477f4',
                                                            client_secret='36920227d76e4f8c9925832acf638a9c',
                                                            redirect_uri='http://localhost:1234/ForumTest/tabs'
                                                                         '/test.php',
                                                            scope="playlist-modify-private", open_browser=False))
        self.user = self.sp.me()['id']
        self.playlists = self.sp.current_user_playlists()
        getDates = getDate.getDate()
        self.name = "per e homosex"# str(getDates.year)

    def findYearPlaylist(self):
        for playlist in self.playlists['items']:
            if playlist['name'] == self.name:
                return True
        return False

    def isYearPlaylist(self):
        if not self.findYearPlaylist():
            self.createPlaylist(self.name)
        else:
            print("there is")

    def createPlaylist(self, name):
        self.sp.user_playlist_create(self.user, name, False, False, f"Playlist created for {self.user}  most listened "
                                                                    f"songs of {name}")


currentPlaylist = playlists()
currentPlaylist.isYearPlaylist()
