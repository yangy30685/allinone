import time as tm
import datetime
import calendar


print(tm.time())
print(tm.localtime(tm.time()))

today = datetime.date.today()
print(today)
print(calendar.isleap(2020))