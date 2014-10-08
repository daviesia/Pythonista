import datetime

today = datetime.date.today()
SomeDate = datetime.date(2018, 11, 11)
diff = SomeDate - today
print 'Somedate is', diff.days, 'day(s) away'
