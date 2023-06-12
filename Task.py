from datetime import date
from datetime import datetime


class TaskIn:
    def __init__(self, Day, Year, Month, Hour, Min, Points, Name):
        self.Day = Day
        self.Year = Year
        self.Month = Month
        self.Hour = Hour
        self.Min = (Hour * 60) + Min
        self.Points = Points
        self.Name = Name


    def convert_Time(self):
        Today = (str(date.today()))
        today_list = [(int(x)) for x in Today.split("-")]
        yeardiff = today_list[0] - self.Year
        monthdiff = today_list[1] - self.Month
        daydiff = today_list[2] - self.Day
        yeardiff *= 525600
        monthdiff *= 43800
        daydiff *= 1440
        current_time = datetime.now().time()
        minutes = current_time.hour * 60 + current_time.minute
        mindiff = minutes - self.Min
        totaldiff = yeardiff+daydiff+monthdiff+mindiff
        if(totaldiff >= 0):
            return totaldiff
        else:
            return 0

    def getPoints(self):
        return self.Points * 100

    def get_weight(self):
        weight = self.convert_Time() - self.getPoints()
        return weight
    def getName(self):
        return self.Name

