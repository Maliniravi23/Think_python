class Time(object):
    "time object"

time1 = Time()
time1.hour = 11
time1.minute = 59
time1.second = 2

time2 = Time()
time2.hour = 11
time2.minute = 19
time2.second = 1

def is_after(t1, t2):
    "function is_after"

    ns1 = number(t1)
    ns2 = number(t2)
    print(ns1,ns2)
    return ns1 > ns2

def number(time):
    "adding all"

    number_seconds = time.hour 
    number_seconds += time.minute 
    number_seconds += time.second
    
    return number_seconds

print(is_after(time1, time2))
