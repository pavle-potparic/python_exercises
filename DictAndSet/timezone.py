import pytz
import datetime

country = 'Europe/Belgrade'
timezone = pytz.timezone(country)

print(datetime.datetime.now(tz=timezone))