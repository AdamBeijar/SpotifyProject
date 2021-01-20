import datetime


def date():
    currentDateTime = datetime.datetime.now()
    day = currentDateTime.day
    month = currentDateTime.month
    year = currentDateTime.year
    date = str(year) + "-" + str(month) + "-" + str(day)
    return date


def time():
    currentDateTime = datetime.datetime.now()
    hour = currentDateTime.hour
    minute = currentDateTime.minute
    second = currentDateTime.second
    time = str(hour) + ":" + str(minute) + ":" + str(second)
    return time


def second():
    currentDateTime = datetime.datetime.now()
    second = currentDateTime.second
    return second


def minute():
    currentDateTime = datetime.datetime.now()
    minute = currentDateTime.minute
    return minute


def hour():
    currentDateTime = datetime.datetime.now()
    hour = currentDateTime.hour
    return hour


def day():
    currentDateTime = datetime.datetime.now()
    day = currentDateTime.day
    return day


def month():
    currentDateTime = datetime.datetime.now()
    month = currentDateTime.month
    return month


def year():
    currentDateTime = datetime.datetime.now()
    year = currentDateTime.year
    return year
