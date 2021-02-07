import datetime


class getDate:
    def __init__(self):
        self.currentDateTime = datetime.datetime.now()
        self.day = self.currentDateTime.day
        self.month = self.currentDateTime.month
        self.year = self.currentDateTime.year
        self.hour = self.currentDateTime.hour
        self.minute = self.currentDateTime.minute
        self.second = self.currentDateTime.second

    def date(self):
        date = str(self.year) + "-" + str(self.month) + "-" + str(self.day)
        return date

    def time(self):
        time = str(self.hour) + ":" + str(self.minute) + ":" + str(self.second)
        return time

    def second(self):
        return self.second

    def minute(self):
        return self.minute

    def hour(self):
        return self.hour

    def day(self):
        return self.day

    def month(self):
        return self.month

    def year(self):
        return self.year

    def twoWeeksFromNow(self):
        twoWeeksFromNow = self.currentDateTime.now() + datetime.timedelta(weeks=2)
        return twoWeeksFromNow.date()
