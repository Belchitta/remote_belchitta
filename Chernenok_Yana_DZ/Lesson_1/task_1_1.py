minutes = 60
hours = int(minutes ** 2)
days = int(hours * 24)
duration = int(input("how much seconds? "))
duration = abs(duration)
if duration in range(0, 61):
    print(duration, "sec")
elif duration in range(61, 3600):
    seconds = duration % minutes
    minute = duration // minutes
    if seconds != 0:
        print(minute, "min", seconds, "sec")
    else:
        print(minute, "min, 0 sec")
elif duration in range(3600, 86400):
    hour = duration // hours
    minute = duration % hours
    seconds = (duration % hours) % minutes
    if duration % hours == 0:
        print(hour, "hours, 0 min, 0 sec")
    else:
        print(hour, "hours", minute, "min", seconds, 'sec')
elif duration in range(86400, 31622400):
    day = duration // days
    hour = (duration % days) // hours
    minute = ((duration % days) % hours) // minutes
    seconds = ((duration % days) % hours) % minutes
    if duration % days == 0:
        print(day, "days, 0 hours, 0 min, 0 sec", )
    elif duration % days == 0 and duration % hours == 0:
        print(day, "days", hour, "hours, 0 min, 0 sec")
    elif duration % days == 0 and duration % hours == 0 and duration % minutes:
        print(day, "days", hour, "hours", minute, "min, 0 sec")
    else:
        print(day, "days", hour, "hours", minute, "min", seconds, 'sec')
