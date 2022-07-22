
#! Arrow: Better dates & times for Python

"""Arrow is a Python library that offers a sensible and human-friendly approach to creating, manipulating, formatting and 
converting dates, times and timestamps. It implements and updates the datetime type, plugging gaps in functionality and 
providing an intelligent module API that supports many common creation scenarios. Simply put, it helps you work with dates and 
times with fewer imports and a lot less code."""



import arrow
from datetime import datetime

utc = arrow.utcnow()
print(utc)

local = utc.to('Asia/Kathmandu')
print(local)
print(local.timestamp())

datetime_now=arrow.get(datetime.utcnow())
print(datetime_now)

from dateutil import tz
datetime_tz=arrow.get(datetime(2013, 5, 5), tz.gettz('Asia/Kathmandu'))
print(datetime_tz)

datetime=arrow.get("2022-07-21 10:04:26.102404+05:45").timestamp()
print(datetime)