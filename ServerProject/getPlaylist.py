import spotipy
from spotipy.oauth2 import *
from Utility import writeDebugLog


def main(date, time, year, path):
    playlistFound = False
    yearPlaylist = 0
    scopeRead = "playlist-read-private"
    scopeModify = "playlist-modify-private"
    scopeGetUser = "user-read-private"
    spReadPlaylist = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='bccad02b357548da8135bc648ec477f4',
                                                               client_secret='36920227d76e4f8c9925832acf638a9c',
                                                               redirect_uri='http://localhost:1234/ForumTest/tabs/test.php',
                                                               scope=scopeRead, open_browser=False))
    spCreatePlaylist = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='bccad02b357548da8135bc648ec477f4',
                                                                 client_secret='36920227d76e4f8c9925832acf638a9c',
                                                                 redirect_uri='http://localhost:1234/ForumTest/tabs/test.php',
                                                                 scope=scopeModify, open_browser=False))
    spGetUser = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='bccad02b357548da8135bc648ec477f4',
                                                          client_secret='36920227d76e4f8c9925832acf638a9c',
                                                          redirect_uri='http://localhost:1234/ForumTest/tabs/test.php',
                                                          scope=scopeGetUser, open_browser=False))
    user = spGetUser.me()['id']
    writeDebugLog.mainLog("New Day " + date, date, user, time)
    playlists = spReadPlaylist.current_user_playlists()
    for playlist in playlists['items']:
        if str(playlist['name']) == str(year):
            playlistFound = True
            yearPlaylist = playlist['name']
            break
        else:
            playlistFound = False
    if playlistFound:
        writeDebugLog.mainLog("Found playlist: " + yearPlaylist, date, user, time)
    else:
        spCreatePlaylist.user_playlist_create(user, str(year), False, False,
                                              "Playlist created for " + user + " most listened songs of " + str(year))
        writeDebugLog.mainLog("Created playlist: " + yearPlaylist, date, user, time)
