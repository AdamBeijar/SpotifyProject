import spotipy
from spotipy.oauth2 import *
import datetime
from Utility import connector

songFound = False
yearPlaylistId = ""
year = 2020
counter = 0
counter2 = 0
twoWeeksFromNow = datetime.datetime.now() + datetime.timedelta(weeks=2)
twoWeeksFromNow = twoWeeksFromNow.date()
scopeRead = "playlist-read-private"
scopeModify = "playlist-modify-public"
scopeModifyprivate = "playlist-modify-private"
spReadPlaylist = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='bccad02b357548da8135bc648ec477f4', client_secret='36920227d76e4f8c9925832acf638a9c', redirect_uri='http://localhost:1234/ForumTest/tabs/test.php', scope=scopeRead))
spCreatePlaylist = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='bccad02b357548da8135bc648ec477f4', client_secret='36920227d76e4f8c9925832acf638a9c', redirect_uri='http://localhost:1234/ForumTest/tabs/test.php', scope=scopeModify))
spCreatePlaylistPrivate = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='bccad02b357548da8135bc648ec477f4', client_secret='36920227d76e4f8c9925832acf638a9c', redirect_uri='http://localhost:1234/ForumTest/tabs/test.php', scope=scopeModifyprivate))
user = spReadPlaylist.me()['id']
playlists = spReadPlaylist.user_playlists(user)
for playlist in playlists['items']:
    if str(playlist['name']) == str(year):
        yearPlaylistId = playlist['id']
        break
sqlTime = "SELECT * FROM timeslistened"
connector.mycursor.execute(sqlTime)
timesListened = connector.mycursor.fetchall()
playlist = spReadPlaylist.user_playlist_tracks(user, yearPlaylistId)
for item in playlist['items']:
    print(item['track']['id'])