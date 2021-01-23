import spotipy
from spotipy.oauth2 import *
import datetime
from Utility import connector, writeDebugLog


def main(date, time, path, year):
    counter = 0
    songFound = False
    yearPlaylistId = ""
    twoWeeksFromNow = datetime.datetime.now() + datetime.timedelta(weeks=2)
    twoWeeksFromNow = twoWeeksFromNow.date()
    scopeRead = "playlist-read-private"
    scopeModifyPublic = "playlist-modify-public"
    scopeModifyPrivate = "playlist-modify-private"
    spReadPlaylist = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='bccad02b357548da8135bc648ec477f4',
                                                               client_secret='36920227d76e4f8c9925832acf638a9c',
                                                               redirect_uri='http://localhost:1234/ForumTest/tabs/test.php',
                                                               scope=scopeRead, open_browser=False))
    spCreatePlaylist = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='bccad02b357548da8135bc648ec477f4',
                                                                 client_secret='36920227d76e4f8c9925832acf638a9c',
                                                                 redirect_uri='http://localhost:1234/ForumTest/tabs/test.php',
                                                                 scope=scopeModifyPublic, open_browser=False))
    spCreatePlaylistPrivate = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='bccad02b357548da8135bc648ec477f4',
                                                                        client_secret='36920227d76e4f8c9925832acf638a9c',
                                                                        redirect_uri='http://localhost:1234/ForumTest/tabs/test.php',
                                                                        scope=scopeModifyPrivate, open_browser=False))
    user = spReadPlaylist.me()['id']
    playlists = spReadPlaylist.user_playlists(user)
    for playlist in playlists['items']:
        if str(playlist['name']) == str(year):
            yearPlaylistId = playlist['id']
            break
    sqlTime = "SELECT * FROM timeslistened"
    connector.mycursor.execute(sqlTime)
    timesListened = connector.mycursor.fetchall()
    playlist = spReadPlaylist.playlist_items(yearPlaylistId)
    for item in playlist['items']:
        counter += 1
    if counter == 100:
        playlist2 = spReadPlaylist.playlist_items(yearPlaylistId, None, 100, 100)
        for item in playlist2['items']:
            counter += 1
        if counter == 200:
            playlist3 = spReadPlaylist.playlist_items(yearPlaylistId, None, 100, 200)
            for item in playlist3['items']:
                counter += 1
            if counter == 300:
                playlist4 = spReadPlaylist.playlist_items(yearPlaylistId, None, 100, 300)
                for item in playlist4['items']:
                    counter += 1
    for x in timesListened:
        if x['dates'] < twoWeeksFromNow:
            if x['timesListened'] > 8:
                for item in playlist['items']:
                    if x['trackID'] == item['track']['id']:
                        songFound = True
                        break
                    else:
                        songFound = False
                        if 100 < counter < 200:
                            for item in playlist2['items']:
                                if x['trackID'] == item['track']['id']:
                                    songFound = True
                                    break
                                else:
                                    songFound = False
                                    if 200 < counter < 300:
                                        for item in playlist3['items']:
                                            if x['trackID'] == item['track']['id']:
                                                songFound = True
                                                break
                                            else:
                                                songFound = False
                                                if 300 < counter < 400:
                                                    for item in playlist4['items']:
                                                        if x['trackID'] == item['track']['id']:
                                                            songFound = True
                                                            break
                                                        else:
                                                            songFound = False
                if not songFound:
                    try:
                        trackID = [x['trackID']]
                        spCreatePlaylist.user_playlist_add_tracks(user, yearPlaylistId, trackID, None)
                        writeDebugLog.mainLog("Added " + str(x['id']) + " to playlist", date, user, time)
                    except:
                        try:
                            trackID = [x['trackID']]
                            spCreatePlaylistPrivate.user_playlist_add_tracks(user, yearPlaylistId, trackID, None)
                            writeDebugLog.mainLog("Added " + str(x['id']) + " to playlist", date, user, time)
                        except:
                            writeDebugLog.mainLog(
                                "Error has occurred during adding song " + str(x['id']) + " to a playlist", date,
                                "user", time)
                            pass
        else:
            sqlTime = "DELETE FROM timeslistened WHERE id='" + str(x['id']) + "';"
            connector.mycursor.execute(sqlTime)
            connector.mydb.commit()
            writeDebugLog.mainLog("Deleted " + str(x['trackID']) + " from database cause it was over two weeks old",
                                  date, user, time)
