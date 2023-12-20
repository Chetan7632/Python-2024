from datetime import date
import datetime
cd=date.today()
print("Current Date=",cd)
print("Day of week=",cd.weekday())
print("Month=",cd.month())
print("Year=",cd.year())
print("Date=",cd.day())

t=datetime.datetime.now()
print("Date & Time=",t)
t=datetime.datetime.now().time()
print("Time=",t)
print("Hours=",t.hour)
print("Minute=",t.minute)
print("Second=",t.second)
