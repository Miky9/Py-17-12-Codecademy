from datetime import datetime

now = datetime.now()  # current date and time
print(now)
print(now.year)
print(now.month)
print(now.day)

# current date in the form of mm/dd/yyyy hh:mm:ss
print('%s/%s/%s %s:%s:%s ' % (now.month, now.day, now.year, now.hour, now.minute, now.second))




