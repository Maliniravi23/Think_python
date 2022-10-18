start_time = 6 + 52 / 60.0
easy_pace = (8 + 15 / 60.0 ) / 60.0
tempo_pace = (7 + 12 / 60.0) / 60.0
running_time = 2 * easy_pace + 3 * tempo_pace
breakfast_hr = start_time + running_time
breakfast_min = (breakfast_hr-int(breakfast_hr))*60
breakfast_sec= (breakfast_min-int(breakfast_min))*60
print("breakfast",breakfast_hr) # 7.501666666666667
print("breakfast_min",breakfast_min) # 30.100000000000016
print("breakfast_sec",breakfast_sec) # 6.000000000000938

