import getCurrentSong
import getPlaylist
import addToPlaylist
import getDate
import getPath


def main():
    path = getPath.main()
    getPath.createLog()
    playlistCount = 0
    songCount = 0
    while True:
        date = getDate.date()
        time = getDate.time()
        second = getDate.second()
        hour = getDate.hour()
        if second == 20 and songCount == 0:
            logs = open("./logs/" + date + ".log", "a+")
            logs.close()
            getCurrentSong.main(date, time, path)
            songCount = 1
            pass
        if second == 21 and songCount == 1:
            songCount = 0
        if hour == 1 and playlistCount == 1:
            playlistCount = 0


if __name__ == "__main__":
    main()
