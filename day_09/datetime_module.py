import datetime

my_time = datetime.time(20, 30)
print(type(my_time))
# <class 'datetime.time'>
print(my_time)

my_datetime = datetime.datetime(2024, 7, 14, 8, 30, 50)
print(type(my_datetime))
print(my_datetime)
my_datetime = my_datetime.replace(month=10)
print(my_datetime)

birthday = datetime.date(1980, 3, 22)
die = datetime.date(2060, 2, 28)

life_time = die - birthday
print(life_time, f'years = {round(life_time.days / 365, 2)}')
# 29197 days, 0:00:00 years = 79.99

wake_up = datetime.datetime(2023, 12, 24, 9, 30, 39)
sleep = datetime.datetime(2023, 12, 25, 4, 30, 50)

wake_up_time = sleep - wake_up
print(wake_up_time.seconds)

# today
print(datetime.date.today())
# minutes from actual datetime
print(datetime.datetime.today().minute)

