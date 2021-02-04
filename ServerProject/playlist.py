import spotipy
from spotipy.oauth2 import *
from Utility import connector, writeDebugLog


class playlists:
    def __init__(self, sp):
        self.sp = sp

