from datetime import datetime, date, timedelta

today = date.today()
print(dir(today))
print(today.year, today.month, today.day)

jays_bd = date(2014, 8, 1)

diff = today - jays_bd

years, days = divmod(diff.days, 365)
print(f"Jay is {years} years and {days} days old")

random_moment = datetime(1982, 5, 17, 10, 43, 11)
print(random_moment)

# at command line:
# pip python-dateutil

# in script:
# import dateutil




