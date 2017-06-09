import datetime

from dateutil import rrule

d1 = datetime.date(2017, 2, 28)
d2 = datetime.date(2017, 5, 27)

months = rrule.rrule(rrule.MONTHLY, dtstart=d1, until=d2).count()

print(f"months={months}")
