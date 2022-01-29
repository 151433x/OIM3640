#The time module provides a function, also named time, that returns the current Greenwich Mean Time in “the epoch”, which is an arbitrary time used as a reference point. On UNIX systems, the epoch is 1 January 1970.
from inspect import currentframe
import time
print(time.time())
time_seconds=time.time()
time_minutes=time_seconds/60 # time since jan 1 1970 in minutes
time_hours=time_minutes/60 # time since jan 1970 in hours
print(time_hours) # number of hours since epoch
time_days=time_hours/24 # time since jan 1 1970 in days
print(time_days) # number of days that have passed since 19021
hours_left=time_hours%24
print(hours_left) # hours of the day in military time with reimender, 13.1229 or 13 which is 1 pm
minutes_left=time_minutes%60
print(minutes_left) # minutes left after hours 
seconds_left=time_seconds%60
print(seconds_left) #seconds after minutes
final_time=hours_left
print(f'Here is the time: {hours_left:.0f}:{minutes_left:.0f}:{seconds_left:.0f} and the number of days that has passed since the epoch is: {time_days:.0f}')