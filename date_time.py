# from datetime import datetime
# # custom_date=datetime(year,month,date,hour,minutes,seconds)
# custom_date=datetime(2026,11,5,11,17,46)
# print(custom_date)
# custom_date=datetime(2026,11,5)
# print(custom_date)
#
# todays_date=datetime.now()
# todays_date=datetime.today()
# print(todays_date)
# print(todays_date.year)
# print(todays_date.month)
# print(todays_date.day)
# print(todays_date.hour)
# print(todays_date.minute)
# print(todays_date.second)
# print(todays_date.microsecond)
#
# print(todays_date.time())
# print(todays_date.date())




from datetime import time

# custom_time=time(hour,minute,seconds,microseconds)

# time=time(12,50,00,0)
# print(time) #12:50pm

# run this separately otherwise shows error

# time=time(0,50,0,0)
# print(time) #12:50am

# 9am
from datetime import timedelta,datetime
time =time(9,0,0)
print(time)

# add 15 minutes
# time=time+timedelta(minutes=15)
# print(time)

# we can only add timedelta while using time and date , cannot use in time only
todays_date=datetime.now()
print(todays_date)

# Adding 15 minutes
print("addding 15 minutes",todays_date+timedelta(minutes=15))
print("adding 2 hours",todays_date+timedelta(hours=2))
print("adding 7 days",todays_date+timedelta(days=7))

# Adding 7 days to date 2026-11-05
date=datetime(2026,11,5,0,0,0)+timedelta(days=7)
print(date)

# Adding 15 minutes
date=datetime(2026,11,5,9,0,0)+timedelta(minutes=9)
print(date)
