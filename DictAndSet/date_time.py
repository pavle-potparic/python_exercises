import time
import datetime

# print(time.time())
# print(time.localtime())

format_time = time.strftime('%Y-%m-%d %HH:%M:%SS', time.localtime())
print(format_time)

print(datetime.date.today())

