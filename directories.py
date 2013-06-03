__author__ = 'Gustaf'

import datetime
import calendar

DASH_SYMBOL = '-'


class Directories:
    def __init__(self, start_date, end_date):
        self.sub_directories = []
        self.start_date = start_date
        self.end_date = end_date

    def generate_sub_directories(self):
        pass

    def short_name(self):
        pass

    def sub_directories(self):
        return self.sub_directories


class Year():
    def __init__(self, year_as_datetime):
        self.year_as_datetime = year_as_datetime

    def short_name(self):
        return str(self.year_as_datetime.year)


class Month():
    def __init__(self, month_as_datetime, photo_files=[]):
        self.month_as_datetime = month_as_datetime
        self.files = photo_files

    def short_name(self):
        month_number = self.month_as_datetime.month
        year = self.month_as_datetime.year
        return str(year) + DASH_SYMBOL + calendar.month_name[month_number]

    def addPhoto(self, photo_file):
        self.files.add(photo_file)

    def addAllPhotos(self, photo_files):
        self.files.extend(photo_files)

    def getFiles(self):
        return self.files


d = datetime.datetime
jan = datetime.date(2012, 1, 1)
now = datetime.date(2013,05,1)

day_count = (now - jan).days
months = [jan.month]
for day_number in range(day_count):
    days_diff = datetime.timedelta(days=day_number)
    new_date = jan + days_diff
    if new_date.month not in months:
        months.append(new_date.month)

mymonth = Month(d.today())
print mymonth.short_name()


