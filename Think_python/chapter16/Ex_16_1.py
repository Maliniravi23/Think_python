class Time(object):
        "time object"

time = Time()
time.hour = 11
time.minute = 59
time.second = 30

def print_time(time):
    print("{:02.0f}:{:02.0f}:{:02.0f}".format(time.hour, time.minute, time.second))
    
print_time(time)
