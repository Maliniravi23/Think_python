import math

class Point:
    "......"

def distance_between_points(a, b):
    return math.sqrt((b.x - a.x)**2 + (b.y - a.y)**2)

a = Point()
a.x, a.y = 3, 1

b = Point()
b.x, b.y = 0, 0

print(distance_between_points(a, b))