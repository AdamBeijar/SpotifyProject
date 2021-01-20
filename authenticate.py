import spotipy
from spotipy.oauth2 import *
import writeDebugLog as Log
import getDate as Date
scopeCurrentSong = "user-read-currently-playing"
scopeRead = "playlist-read-private"
scopeModify = "playlist-modify-private"
scopeGetUser = "user-read-private"
scopeRead = "playlist-read-private"
scopeModify = "playlist-modify-public"
scopeModifyprivate = "playlist-modify-private"
spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='bccad02b357548da8135bc648ec477f4', client_secret='36920227d76e4f8c9925832acf638a9c', redirect_uri='http://localhost:1234/ForumTest/tabs/test.php', scope=scopeCurrentSong, open_browser=False))
spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='bccad02b357548da8135bc648ec477f4', client_secret='36920227d76e4f8c9925832acf638a9c', redirect_uri='http://localhost:1234/ForumTest/tabs/test.php', scope=scopeRead, open_browser=False))
spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='bccad02b357548da8135bc648ec477f4', client_secret='36920227d76e4f8c9925832acf638a9c', redirect_uri='http://localhost:1234/ForumTest/tabs/test.php', scope=scopeModify, open_browser=False))
spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='bccad02b357548da8135bc648ec477f4', client_secret='36920227d76e4f8c9925832acf638a9c', redirect_uri='http://localhost:1234/ForumTest/tabs/test.php', scope=scopeGetUser, open_browser=False))
spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='bccad02b357548da8135bc648ec477f4', client_secret='36920227d76e4f8c9925832acf638a9c',redirect_uri='http://localhost:1234/ForumTest/tabs/test.php', scope=scopeRead, open_browser=False))
spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='bccad02b357548da8135bc648ec477f4', client_secret='36920227d76e4f8c9925832acf638a9c',redirect_uri='http://localhost:1234/ForumTest/tabs/test.php', scope=scopeModify, open_browser=False))
spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='bccad02b357548da8135bc648ec477f4', client_secret='36920227d76e4f8c9925832acf638a9c',redirect_uri='http://localhost:1234/ForumTest/tabs/test.php', scope=scopeModifyprivate, open_browser=False))
Log.mainLog("authentication completed", Date.date(), "user", Date.time())