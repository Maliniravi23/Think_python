distance = 10
time = 43.30
# convert sec to min 1min = 0.0166 30min = 0.5
minutes = 43.5
hours = minutes/60 #0.725
# convert kilometers to miles
km_per_miles = 1.61
distance_miles = distance/1.61 # 6.2111801242
# the average time per mile
time_per_miles = minutes/distance_miles # 7.0035
print(time_per_miles)
# Average speed in miles per hour
avg_speed = distance_miles/ hours # 8.5671449989
print(avg_speed)