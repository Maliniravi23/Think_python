def increment(time, seconds):
    time.second += seconds
    
    if time.second >= 60:
        time.second -= 60
        time.minute += 1
        
    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1

class Time(object):
    "time object"


def print_time(time):
    print("{:02.0f}:{:02.0f}:{:02.0f}".format(time.hour, time.minute, time.second))
    
time = Time()
time.hour = 1
time.minute = 59
time.second = 30

increment(time, 60)

print_time(time)