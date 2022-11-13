class Time(object):
    "..."

def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def add_time(t1, t2):
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

time = Time()
time.hour = 1
time.minute = 59
time.second = 30

start = Time()
start.hour = 9
start.minute = 45
start.second = 0

def print_time(time):
    print("{:02.0f}:{:02.0f}:{:02.0f}".format(time.hour, time.minute, time.second))

time_to_int(time)
time_adds = add_time(time,start)
print_time(time_adds)