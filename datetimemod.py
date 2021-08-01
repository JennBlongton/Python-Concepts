import datetime
import pytz

tday = datetime.date.today()
# gives year, month, days
print(tday)
print(tday.year)
print(tday.day)
print(tday.weekday()) 
# for weekday Monday = 0 and Sunday = 6
print(tday.isoweekday())
# for isoweekday Monday = 1 and Sunday = 7

# Timedeltas
tdelta = datetime.timedelta(days=7)
print(tday + tdelta)

#date2 = date1 + timedelta
# if timedelta is added/sub to date then it gives us date
# timedelta = date1 + date2
# if 2 dates are added/sub then it gives timedelta

# *********************TIME*************************
t = datetime.time(9, 30, 45, 5000)
# gives hour, minutes, seconds, microseconds
print(t)
print(t.hour)

# *********************DATETIME*********************
# Gives access to everything both date and time together
dt = datetime.datetime(2021, 7, 31, 23, 52, 45, 100000)
print(dt)
dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print("*********")
print(dt_now)
print("*********")
print(dt_utcnow)
print("*********")

dtNow = datetime.datetime.now(tz=pytz.UTC)
print(dtNow)