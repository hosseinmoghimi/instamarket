from persiantools.jdatetime import JalaliDateTime
from .settings import ON_SERVER
import datetime
class PersianCalendar:
    
    def __init__(self,date=None):
        if date is None:
            self.date=datetime.datetime.today()
            self.persian_date=self.from_gregorian(greg_date_time=self.date)
        if date is not None:
            self.date=date
            self.persian_date=self.from_gregorian(greg_date_time=self.date)
    
    def now(self):
        return JalaliDateTime.today()
    def parse(self,value):
        shamsi_date_time=value
        year_=int(shamsi_date_time[0:4])
        month_=int(shamsi_date_time[5:7])
        day_=int(shamsi_date_time[8:10])
        padding=shamsi_date_time.find(':')
        if not padding==-1:
            padding-=2;
            hour_=int(shamsi_date_time[padding:padding+2])
            
            padding+=3
            min_=int(shamsi_date_time[padding:padding+2])
            padding+=3
            sec_=int(shamsi_date_time[padding:padding+2])
           
        else:
            hour_=0
            padding+=3
            min_=0
            padding+=3
            sec_=0
        self.date=JalaliDateTime(year=year_,month=month_, day=day_,hour=hour_,minute=min_,second=sec_).to_gregorian()
        self.persian_date=self.from_gregorian(self.date)
        return self
    def from_gregorian(self,greg_date_time,add_time_zone=True):
        if not add_time_zone:
            return JalaliDateTime.to_jalali(greg_date_time).strftime("%Y/%m/%d %H:%M:%S") 
        if ON_SERVER:
            hours=0
            minutes=0
        else:
            hours=4
            minutes=30
        return JalaliDateTime.to_jalali(greg_date_time+datetime.timedelta(hours=hours,minutes=minutes)).strftime("%Y/%m/%d %H:%M:%S") 