def mainLog(reason, date, user, time):
    logs = open("./logs/" + date + ".log", "a+")
    logs.write(date + " " + time)
    logs.write("\nUser: " + user)
    logs.write("\n----------------------------------\n")
    logs.write("Reason: " + reason)
    logs.write("\n----------------------------------\n\n")
    logs.close()


def songLog(song, artist, album, type, user, date, time):
    logs = open("./logs/" + date + ".log", "a+")
    logs.write(date + " " + time)
    logs.write("\nUser: " + user + " is playing: ")
    logs.write("\n----------------------------------\n")
    logs.write("Song: " + song)
    logs.write("\nArtist: ")
    for item in artist:
        logs.write(str(item['name']) + " ")
    logs.write("\nAlbum: " + album)
    logs.write("\nType: " + type)
    logs.write("\n----------------------------------\n\n")
    logs.close()


def OfflineLog(user, date, time):
    logs = open("./logs/" + date + ".log", "a+")
    logs.write(date + " " + time)
    logs.write("\nUser: " + user + " is offline")
    logs.write("\n----------------------------------\n")
    logs.write("Song: Offline")
    logs.write("\nArtist: Offline")
    logs.write("\nAlbum: Offline")
    logs.write("\nType: Offline")
    logs.write("\n----------------------------------\n\n")
    logs.close()
