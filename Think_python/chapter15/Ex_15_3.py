class Point:
    "...."

class Rectangle:
    "...."

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

def print_point(p):
    print('(%g, %g)' % (p.x, p.y))
    
def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width / 2
    p.y = rect.corner.y + rect.height / 2
    return p

def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy
    return rect

move_rectangle(box, 100, 200)
center = find_center(box)
print_point(center)

# print(Point())

import copy

def move_new_rectangle(rect, dx, dy):
    
    new_rect = copy.deepcopy(rect)
    new_rect.corner.x += dx
    new_rect.corner.y += dy
    return new_rect

nmr = move_new_rectangle(box, 100, 200)
print(nmr)